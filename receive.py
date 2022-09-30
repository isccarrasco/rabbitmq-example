import os
import sys

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
        """
        print(" [x] Received %r" % body)

    # Connecting the consumer with the queue
    channel.basic_consume(queue='isccarrasco',
                          auto_ack=True,
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
