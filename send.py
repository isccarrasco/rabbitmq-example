import uuid

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


exist = channel.queue_declare(queue='isccarrasco')

for i in range(100):
    data = f'Hello world! key: {uuid.uuid1()}'
    channel.basic_publish(exchange='', routing_key='isccarrasco', body=data)
    print(f" [x] Sent '{data}'")

connection.close()
