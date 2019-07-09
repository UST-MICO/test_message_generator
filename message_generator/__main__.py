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

    # prepare the message generator and controller
    generator = MessageGenerator(MESSAGE_SOURCE)
    producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS.split(','))
    controller = MessagingController(generator, producer, KAFKA_TOPIC_OUTPUT,
                                     MESSAGE_SEND_INTERVAL, KAFKA_TOPIC_OUTPUT_NUM_PARTITIONS,
                                     KAFKA_TOPIC_OUTPUT_REPLICATION_FACTOR)

    # start execution
    controller.start_producing()


