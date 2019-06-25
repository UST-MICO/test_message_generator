# test_message_generator
A message producer, that generates messages randomly for testing purposes. 

## Commands
#### Start generator with test environment
This will start up the generator together with kafka and zookeeper
```bash
docker-compose up -d
```

#### Start generator with test environment and additional message logger
Additionally to the previous command, it will start the app `message_generator/test_receiver.py`. (This is useful for checking if the kafka setting actually works). 
```bash
docker-compose -f docker-compose-with-testreceiver.yaml up -d
```
You can read the logs as follows:
```bash
docker logs -ft test-receiver
```

#### Start only the generator
Here you have to provide the environment variables and install the dependencies manually. 
```bash
pip3 install -r requirements.txt
source environ.sh
python3 message_generator/__main__.py
```
#### Execute the tests
This will start up a testing environment (kafka and zookeeper) and run all tests. Afterwards the test environment is stopped
```bash
./bin/test.sh
```

## Environment Variables
| Variable                              | Implementation Strategy                                                                                                            | default                                 |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| LOG_FILE_PATH                         | Path to the file, in which the logs are stored                                                                                     | <WORKDIR>/test_message_generator.log    |
| LOG_FORMAT                            | The format of the logs. Format variables are described [here](https://docs.python.org/3/library/logging.html#logrecord-attributes) | %(asctime)-15s %(message)s              |
| LOG_LEVEL                             | The log level. Supported values (INFO, DEBUG)                                                                                      | INFO                                    |
| MESSAGE_SOURCE                        | The value that is used in every message for the CloudEvent field 'source'                                                          | test_message_generator_ + <random uuid> |
| MESSAGE_SEND_INTERVAL                 | The number of seconds between each message                                                                                         | 5                                       |
| KAFKA_TARGET_TOPIC                    | The topic, to which each message is published                                                                                      | test-message-generator                  |
| KAFKA_TARGET_TOPIC_REPLICATION_FACTOR | The replication factor of the target topic. Only applied, when the message generator has to create the topic manually              | 1                                       |
| KAFKA_TARGET_TOPIC_NUM_PARTITIONS     | The number of partitions of the target topic. Only applied, when the message generator has to create the topic manually            | 1                                       |
| KAFKA_BROKER_HOST                     | The domain of the kafka broker                                                                                                     | localhost                               |
| KAFKA_BROKER_PORT                     | The port of the kafka broker                                                                                                       | 9092                                    |

