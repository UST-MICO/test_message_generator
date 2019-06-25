from message_generator import MessageGenerator
from kafka import KafkaProducer, KafkaConsumer, KafkaAdminClient
from kafka.admin import NewTopic
from threading import Event
from time import sleep
from logging import info, debug, error
import json


class MessagingController:
    """
    Handles the process of sending random messages.
    """

    def __init__(self,
                 generator: MessageGenerator,
                 producer: KafkaProducer,
                 target_topic: str,
                 num_partitions: int,
                 replication_factor: int,
                 send_interval: int):
        """
        :param generator: MessageGenerator for generating CloudEvent messages
        :param producer: KafkaProducer for sending messages
        :param target_topic: str, the topic, to which each message is sent
        :param num_partitions: int, the number of partitions that are used for target_topic
        :param replication_factor: int, the replication factor of the target topic
        :param send_interval: int, the number of seconds between each message
        """
        self.generator = generator
        self.producer = producer
        self.target_topic = target_topic
        self.num_partitions = num_partitions
        self.replication_factor = replication_factor
        self.send_interval = send_interval
        self.stopped = Event()
        #self._prepare_topic()
        info('MessagingController was created')

    def _send_message(self):
        """
        Generates a message with the MessageGenerator, creates a log (level: debug) of the message, and sends
        it to the kafka broker.
        :return: -
        """
        msg = self.generator.get_random_message()
        debug(msg)
        self.producer.send(
            topic=self.target_topic,
            value=json.dumps(self.generator.get_random_message()).encode('utf-8'))

    def _prepare_topic(self):
        """
        If the target topic is not available yet, it is created. This is only required, if autocreate topic is set
        to off at the Kafka Broker.
        :return: -
        """
        consumer = KafkaConsumer(bootstrap_servers=self.producer.config.get('bootstrap_servers'))
        topics = consumer.topics()
        if self.target_topic not in topics:
            client = KafkaAdminClient(bootstrap_servers=self.producer.config.get('bootstrap_servers'))
            topics = [NewTopic(self.target_topic, num_partitions=self.num_partitions,
                               replication_factor=self.replication_factor)]
            client.create_topics(new_topics=topics)

    def start_producing(self):
        """
        An endless loop with the following steps:
        * send a random CloudEvent message
        * wait until the send_interval is over
        * repeat
        :return: -
        """
        info('start producing messages')
        try:
            while not self.stopped.is_set():
                self._send_message()
                sleep(self.send_interval)
        except KeyboardInterrupt:
            pass
        except Exception as e:
            error(e)
            raise e

