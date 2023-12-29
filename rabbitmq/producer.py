import pika
import time

# Connection parameters
credentials = pika.PlainCredentials(username='user', password='password')
connection_params = pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials )

# Establish a connection
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare a queue
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

# Publish a message to the queue

for i in range(10):
    message = f'Hello, RabbitMQ! {i}'
    channel.basic_publish(exchange='', routing_key=queue_name, body=message)
    print(f" [x] Sent '{message}'")
    time.sleep(1)

# message = 'Hello, RabbitMQ!'
# channel.basic_publish(exchange='', routing_key=queue_name, body=message)
# print(f" [x] Sent '{message}'")


# Close the connection
connection.close()
