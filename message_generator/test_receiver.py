from kafka import KafkaConsumer
from os import environ
from config import *

if __name__ == '__main__':
    bootstrap_servers = ['{}:{}'.format(KAFKA_BROKER_HOST, KAFKA_BROKER_PORT)]
    consumer = KafkaConsumer(KAFKA_TARGET_TOPIC, bootstrap_servers=bootstrap_servers)
    for msg in consumer:
        print(msg)

