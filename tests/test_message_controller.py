from messaging_controller import MessagingController
from message_generator import MessageGenerator
from kafka import KafkaProducer, KafkaConsumer, KafkaAdminClient, errors, TopicPartition
from threading import Thread, Event
from json import loads
from time import sleep

topic = 'test_topic'
topic_partition = TopicPartition(topic=topic, partition=0)
broker = ['localhost:9092']


class TestMessageController:
    """
    Test for the class MessageController. The test environment can be started with tests/resources docker-compose.yml
    """

    @staticmethod
    def _clear_topic():
        client = KafkaAdminClient(bootstrap_servers=broker)
        try:
            client.delete_topics([topic])
        except errors.UnknownTopicOrPartitionError:
            pass

    @staticmethod
    def _consume(consumer: KafkaConsumer, messages: list, stopped: Event):
        for msg in consumer:
            messages.append(msg)
            if stopped.is_set():
                break

    @staticmethod
    def _controller_factory():
        return MessagingController(generator=MessageGenerator('test_source'),
                                   producer=KafkaProducer(bootstrap_servers=broker),
                                   target_topic=topic,
                                   send_interval=1,
                                   replication_factor=1,
                                   num_partitions=1)

    def test_send_message(self):
        """
        Tests if the MessageController sends messages in the given time interval.
        It will run the MessageController for a couple of seconds, and then poll all the messages.
        It is successful if the Messages are actually CloudEvents
        :return:
        """
        self._clear_topic()
        controller = self._controller_factory()
        consumer = KafkaConsumer(topic, bootstrap_servers=broker, auto_offset_reset='earliest')
        stopped = Event()
        messages = []

        controller_thread = Thread(target=controller.start_producing, daemon=True)
        controller_thread.start()
        consumer_thread = Thread(target=self._consume, args=[consumer, messages, stopped], daemon=True)
        consumer_thread.start()
        sleep(5)
        controller.stopped.set()
        stopped.set()

        # with a send interval of 1 second and a timespan of 5 seconds,
        # the amount of received messages should be at least between 4 and 6
        assert 4 <= len(messages) <= 6

        # the duration between the events should be about 1 second
        for i in range(len(messages) - 1):
            duration = messages[i + 1].timestamp - messages[i].timestamp
            assert 900 < duration < 1100

        # Check if the messages are actually CloudEvents
        for msg in messages:
            msg = loads(msg.value)
            for k in ['id', 'time', 'data', 'specversion', 'type', 'source', 'contenttype']:
                assert k in msg.keys()


