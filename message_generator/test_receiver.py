from commons import *
from kafka import KafkaConsumer
from config import *
from logging import info


"""
Simple application that continuously receives the messages for KAFKA_TOPIC_OUTPUT and 
logs them to a file, as well as to stdout. 
"""
if __name__ == '__main__':
    prepare_logging(LOG_FILE_PATH, LOG_FORMAT, LOG_LEVEL)
    info('Setting: \n ' + get_env_variable_str(locals()))

    bootstrap_servers = KAFKA_BOOTSTRAP_SERVERS.split(',')
    consumer = KafkaConsumer(KAFKA_TOPIC_OUTPUT, bootstrap_servers=bootstrap_servers)
    info('\nStart receiving......')
    for msg in consumer:
        info(msg)

