import sys

import pika

# Establishing the connection with the RabbitMQ server by
# providing the URL or location of the server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Creating the Queue and assigning a name to it
channel.queue_declare(queue='isccarrasco-v2', durable=True)


message = ' '.join(sys.argv[1:]) or "Hello world!"
channel.basic_publish(exchange='',
                      routing_key='isccarrasco-v2',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                      ))

print(" [x] Sent %r" % message)

connection.close()
