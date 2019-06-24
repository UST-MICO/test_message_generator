#!/usr/bin/env bash

# Please execute this file with the project root as working directory

export TEST_MESSAGE_GENERATOR_PATH=$(pwd)
export PATH=$(pwd)/bin:$PATH
export PYTHONPATH=$(pwd)/message_generator:${PYTHONPATH}

# application variables
# export LOG_FILE_PATH='test_message_generator.log'
# export LOG_FORMAT='%(asctime)-15s %(message)s'
# export LOG_LEVEL='DEBUG'
# export MESSAGE_SOURCE='message generator'
# export MESSAGE_SEND_INTERVAL=5
# export KAFKA_TARGET_TOPIC='test-message-generator'
# export KAFKA_BROKER_HOST='localhost'
# export KAFKA_BROKER_PORT=9092
