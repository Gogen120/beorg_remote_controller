import os

import pika


class RabbitConnection:
    def __init__(self, broker_host, queue_name='remote_dir_controller'):
        self._broker_host = broker_host
        self._queue_name = queue_name

        self._broker_user = os.getenv('RABBITMQ_DEFAULT_USER')
        self._broker_pass = os.getenv('RABBITMQ_DEFAULT_PASS')

    def configure_rabbit(self):
        credentials = self._create_credentials()
        connection = self._create_connection(credentials)
        channel = self._create_channel(connection)

        self._declare_queue(channel)

        return channel

    def _create_credentials(self):
        return pika.PlainCredentials(self._broker_user, self._broker_pass)

    def _create_connection(self, credentials):
        return pika.BlockingConnection(
            pika.ConnectionParameters(host=self._broker_host, credentials=credentials)
        )

    def _create_channel(self, connection):
        return connection.channel()

    def _declare_queue(self, channel):
        channel.queue_declare(queue=self._queue_name)
