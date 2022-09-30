import os
import sys
import time

import pika


def main() -> None:
    """
    Method that connect to RabbitMQ server and consume the messages
    :return: None
    """
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Connecting to the queue with the provided name
    # if the queue does not exist, will be created
    channel.queue_declare(queue='isccarrasco')

    def callback(ch, method, properties, body):
        """
        Method that will be used for the consumer once
        it receives the message from the RabbitMQ server
        and will simulate a time taken for processing the
        operation
        """
        print(" [x] Received %r" % body.decode())
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # Connecting the consumer with the queue
    channel.basic_consume(queue='isccarrasco',
                          on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
