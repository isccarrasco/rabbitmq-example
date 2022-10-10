import sys

import pika

# Establishing the connection with the RabbitMQ server by
# providing the URL or location of the server
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Creating the Exchange and assigning a name and a type to it
channel.exchange_declare(exchange='logs', exchange_type='fanout')


message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(
    exchange='logs',
    routing_key='',
    body=message)
print(" [x] Sent %r" % message)
connection.close()
