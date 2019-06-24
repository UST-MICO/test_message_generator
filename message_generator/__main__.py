from commons import *
from message_generator import MessageGenerator
from messaging_controller import MessagingController
from kafka import KafkaProducer
from logging import info
from config import *


if __name__ == '__main__':
    # Read in the environment variables

    prepare_logging(LOG_FILE_PATH, LOG_FORMAT, LOG_LEVEL)
    info('Start logging with the following setting: \n ' + get_env_variable_str(locals()))

    # prepare the controller
    generator = MessageGenerator(MESSAGE_SOURCE)
    producer = KafkaProducer(bootstrap_servers=["{}:{}".format(KAFKA_BROKER_HOST, KAFKA_BROKER_PORT)])
    controller = MessagingController(generator, producer, KAFKA_TARGET_TOPIC, MESSAGE_SEND_INTERVAL,
                                     KAFKA_TARGET_TOPIC_NUM_PARTITIONS, KAFKA_TARGET_TOPIC_REPLICATION_FACTOR)

    # start execution
    controller.start_producing()

