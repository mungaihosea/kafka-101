from confluent_kafka import Consumer, KafkaError

# Kafka bootstrap servers
bootstrap_servers = 'localhost:9092'

# Kafka topic to consume messages from
topic = 'your_topic'

# Create a Kafka consumer configuration
conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': 'my_consumer_group1',  # Choose a unique consumer group ID
    'auto.offset.reset': 'earliest',  # Start consuming from the beginning of the topic if no offset is stored
}

# Create a Kafka consumer instance
consumer = Consumer(conf)

# Subscribe to the Kafka topic
consumer.subscribe([topic])

# Poll for messages
try:
    while True:
        msg = consumer.poll(1.0)  # Adjust the timeout as needed

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                print("Reached end of partition, resetting offset")
                consumer.seek(msg.partition(), msg.offset())
            else:
                print("Error: {}".format(msg.error()))
        else:
            # Print the received message key and value
            print('Received message: key={}, value={}'.format(msg.key(), msg.value()))

except KeyboardInterrupt:
    pass
finally:
    # Close the consumer
    consumer.close()
