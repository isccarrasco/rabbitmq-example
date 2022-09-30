import uuid

import pika

# Establishing the connection with the RabbitMQ server by
# providing the URL or location of the server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


# Creating the Queue and assigning a name to it
channel.queue_declare(queue='isccarrasco')

# Sending the messages to the queue by providing the name
# of the queue in the routing_key parameter
data = f'Hello world! key: {uuid.uuid1()}'
channel.basic_publish(exchange='',
                      routing_key='isccarrasco',
                      body=data)
print(f" [x] Sent '{data}'")

connection.close()
