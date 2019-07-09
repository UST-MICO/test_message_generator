# test_message_generator

A message producer, that generates messages randomly for testing purposes.

## Commands

### Start generator with test environment

This will start up the generator together with Kafka and ZooKeeper

```bash
docker-compose up -d
```

### Start generator with test environment and additional message logger

Additionally to the previous command, it will start the app `message_generator/test_receiver.py`. (This is useful for checking if the Kafka setting actually works).

```bash
docker-compose -f docker-compose-with-testreceiver.yaml up -d
```

You can read the logs as follows:

```bash
docker logs -ft test-receiver
```

### Start only the generator

Here you have to provide the environment variables and install the dependencies manually.

```bash
pip3 install -r requirements.txt
source environ.sh
python3 message_generator/__main__.py
```

### Execute the tests

This will start up a testing environment (Kafka and ZooKeeper) and run all tests. Afterwards the test environment is stopped

```bash
./bin/test.sh
```

### Running in Kubernetes cluster

We assume that the test_message_generator is deployed with [MICO](https://github.com/UST-MICO/mico/), therefore it is running in namespace `mico-workspace`.

Get logs:

```bash
kubectl -n mico-workspace logs -f $(kubectl get pods -n mico-workspace -l ust.mico/name=test-message-generator --output=jsonpath={.items..metadata.name})
```

Get environment variables:

```bash
kubectl -n mico-workspace exec -it $(kubectl get pods -n mico-workspace -l ust.mico/name=test-message-generator --output=jsonpath={.items..metadata.name}) env
```

Restart:

```bash
kubectl -n mico-workspace delete pod $(kubectl get pods -n mico-workspace -l ust.mico/name=test-message-generator --output=jsonpath={.items..metadata.name})
```

Manually change the deployment image:

```bash
kubectl set image deployment/$(kubectl get deployments -n mico-workspace -l ust.mico/name=test-message-generator --output=jsonpath={.items..metadata.name}) test-message-generator=ustmico/message-generator:local -n mico-workspace
```

## Environment Variables

Variable                              | Implementation Strategy                                                                                                            | default
------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------
LOG_FILE_PATH                         | Path to the file, in which the logs are stored                                                                                     | `<workdir>/test_message_generator.log</workdir>`
LOG_FORMAT                            | The format of the logs. Format variables are described [here](https://docs.python.org/3/library/logging.html#logrecord-attributes) | %(asctime)-15s %(message)s
LOG_LEVEL                             | The log level. Supported values (INFO, DEBUG)                                                                                      | INFO
MESSAGE_SOURCE                        | The value that is used in every message for the CloudEvent field 'source'                                                          | test_message_generator_ + `<random uuid>`
MESSAGE_SEND_INTERVAL                 | The number of seconds between each message                                                                                         | 5
KAFKA_TOPIC_OUTPUT                    | The topic, to which each message is published                                                                                      | test-message-generator
KAFKA_TOPIC_OUTPUT_REPLICATION_FACTOR | The replication factor of the target topic. Only applied, when the message generator has to create the topic manually              | 1
KAFKA_TOPIC_OUTPUT_NUM_PARTITIONS     | The number of partitions of the target topic. Only applied, when the message generator has to create the topic manually            | 1
KAFKA_BOOTSTRAP_SERVERS               | The domain and port of the Kafka broker                                                                                            | localhost:9092
