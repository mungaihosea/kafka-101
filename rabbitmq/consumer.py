import pika

# Connection parameters
credentials = pika.PlainCredentials(username='user', password='password')
connection_params = pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials )

# Establish a connection
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare a queue
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

# Set prefetch count (1 in this example)
channel.basic_qos(prefetch_count=1)


def callback(ch, method, properties, body):
    # Callback function to process the received message
    print(f" [x] Received {body}")
    # Acknowledge the message
    print(method.delivery_tag)
    # ch.basic_ack(delivery_tag=method.delivery_tag)
    # ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)



# Set up a consumer and start consuming messages
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
