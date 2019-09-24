from os import environ, path
import uuid
from pathlib import Path

"""
Reads all the relevant environment variables of the OS and stores them in a variable with the same name.
Every script with `from config import *` can access these variables.  
"""
LOG_FILE_PATH = environ.get('LOG_FILE_PATH', 'test_message_generator.log')
LOG_FORMAT = environ.get('LOG_FORMAT', '%(asctime)-15s %(message)s')
LOG_LEVEL = environ.get('LOG_LEVEL', 'INFO')
MESSAGE_SOURCE = environ.get('MESSAGE_SOURCE', 'test_message_generator_' + uuid.uuid4().hex)
MESSAGE_SEND_INTERVAL = environ.get('MESSAGE_SEND_INTERVAL', 5)
KAFKA_TOPIC_OUTPUT = environ.get('KAFKA_TOPIC_OUTPUT', 'test-message-generator')
KAFKA_TOPIC_OUTPUT_REPLICATION_FACTOR = environ.get('KAFKA_TOPIC_OUTPUT_REPLICATION_FACTOR ', 1)
KAFKA_TOPIC_OUTPUT_NUM_PARTITIONS = environ.get('KAFKA_TOPIC_OUTPUT_NUM_PARTITIONS', 1)
KAFKA_BOOTSTRAP_SERVERS = environ.get('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
PROJECT_PATH = Path(path.dirname(path.abspath(__file__)))

