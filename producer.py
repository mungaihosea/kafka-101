from confluent_kafka import Producer
import time

# Kafka bootstrap servers
bootstrap_servers = 'localhost:9092'

# Kafka topic to produce messages to
# topic = 'your_topic'
topic = 'something'

# Create a Kafka producer configuration
conf = {'bootstrap.servers': bootstrap_servers}

# Create a Kafka producer instance
producer = Producer(conf)

# Define a callback function to handle delivery reports
def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

# Produce messages to the Kafka topic
for i in range(10):
    message = 'Message {}'.format(i)
    producer.produce(topic, key=str(i), value=message, callback=delivery_report)
    producer.flush()

    time.sleep(1)  # Add a delay for demonstration purposes

# Close the producer
producer.flush()
# producer.close()
