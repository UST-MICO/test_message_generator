from commons import *
from kafka import KafkaConsumer
from config import *
from logging import info

if __name__ == '__main__':
    prepare_logging(LOG_FILE_PATH, LOG_FORMAT, LOG_LEVEL)
    info('Setting: \n ' + get_env_variable_str(locals()))

    bootstrap_servers = ['{}:{}'.format(KAFKA_BROKER_HOST, KAFKA_BROKER_PORT)]
    consumer = KafkaConsumer(KAFKA_TARGET_TOPIC, bootstrap_servers=bootstrap_servers)
    info('\nStart receiving......')
    for msg in consumer:
        info(msg)

