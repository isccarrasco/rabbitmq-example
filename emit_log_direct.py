import sys

import pika

# Establishing the connection with the RabbitMQ server by
# providing the URL or location of the server
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Creating the Exchange and assigning a name and a type to it
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(
    exchange='direct_logs',
    routing_key=severity,
    body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()
