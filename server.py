import os
import time

import pika

from rabbit_connection import RabbitConnection


class Server(RabbitConnection):
    def __init__(self, broker_host, dir_path, queue_name='remote_dir_controller'):
        super().__init__(broker_host, queue_name)
        self._dir_path = dir_path

    def listen(self):
        channel = self.configure_rabbit()

        dir_structure = [(root, subdirs, files) for root, subdirs, files in os.walk(self._dir_path)]
        while True:
            time.sleep(1)
            channel.basic_publish(
                exchange='', routing_key=self._queue_name, body=str(dir_structure)
            )
            updated_dir_structure = [(root, subdirs, files) for root, subdirs, files in os.walk(self._dir_path)]
            if updated_dir_structure != dir_structure:
                channel.basic_publish(
                    exchange='', routing_key=self._queue_name, body=str(updated_dir_structure)
                )
            dir_structure = updated_dir_structure


if __name__ == '__main__':
    try:
        Server(os.getenv('BROKER_HOST', 'localhost'), os.getenv('DIR_PATH', '.')).listen()
    except KeyboardInterrupt:
        print('Stopping the server')
