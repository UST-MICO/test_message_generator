from message_generator import MessageGenerator
from kafka import KafkaProducer, KafkaConsumer, KafkaAdminClient
from kafka.admin import NewTopic
from threading import Event
from time import sleep
from logging import info, debug, error
import json


class MessagingController:

    def __init__(self,
                 generator: MessageGenerator,
                 producer: KafkaProducer,
                 target_topic: str,
                 num_partitions: int,
                 replication_factor: int,
                 send_interval: int):
        self.generator = generator
        self.producer = producer
        self.target_topic = target_topic
        self.num_partitions = num_partitions
        self.replication_factor = replication_factor
        self.send_interval = send_interval
        self.stopped = Event()
        self._prepare_topic()
        info('MessagingController was created')

    def _send_message(self):
        msg = self.generator.get_random_message()
        debug(msg)
        self.producer.send(
            topic=self.target_topic,
            value=json.dumps(self.generator.get_random_message()).encode('utf-8'))

    def _prepare_topic(self):
        consumer = KafkaConsumer(bootstrap_servers=self.producer.config.get('bootstrap_servers'))
        topics = consumer.topics()
        if self.target_topic not in topics:
            client = KafkaAdminClient(bootstrap_servers=self.producer.config.get('bootstrap_servers'))
            topics = [NewTopic(self.target_topic, num_partitions=self.num_partitions,
                               replication_factor=self.replication_factor)]
            client.create_topics(new_topics=topics)

    def start_producing(self):
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

