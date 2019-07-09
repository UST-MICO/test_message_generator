#!/usr/bin/env bash

set -e

echo -e "\nPlease ensure to execute 'source environ.sh'\n"
docker-compose -f ${TEST_MESSAGE_GENERATOR_PATH}/tests/resources/docker-compose.yml up -d
sleep 8
py.test --capture no tests
docker-compose -f ${TEST_MESSAGE_GENERATOR_PATH}/tests/resources/docker-compose.yml down