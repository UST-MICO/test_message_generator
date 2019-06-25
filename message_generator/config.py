from os import environ
import uuid

"""
Reads all the relevant environment variables of the OS and stores them in a variable with the same name.
Every script with `from config import *` can access these variables.  
"""
LOG_FILE_PATH = environ.get('LOG_FILE_PATH', 'test_message_generator.log')
LOG_FORMAT = environ.get('LOG_FORMAT', '%(asctime)-15s %(message)s')
LOG_LEVEL = environ.get('LOG_LEVEL', 'INFO')
MESSAGE_SOURCE = environ.get('MESSAGE_SOURCE', 'test_message_generator_' + uuid.uuid4().hex)
MESSAGE_SEND_INTERVAL = environ.get('MESSAGE_SEND_INTERVAL', 5)
KAFKA_TARGET_TOPIC = environ.get('KAFKA_TARGET_TOPIC', 'test-message-generator')
KAFKA_TARGET_TOPIC_REPLICATION_FACTOR = environ.get('KAFKA_TARGET_TOPIC_REPLICATION_FACTOR ', 1)
KAFKA_TARGET_TOPIC_NUM_PARTITIONS = environ.get('KAFKA_TARGET_TOPIC_NUM_PARTITIONS', 1)
KAFKA_BROKER_HOST = environ.get('KAFKA_BROKER_HOST', 'localhost')
KAFKA_BROKER_PORT = environ.get('KAFKA_BROKER_PORT', 9092)

