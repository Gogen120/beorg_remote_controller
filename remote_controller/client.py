import ast
import os

import pika

from rabbit_connection import RabbitConnection


class Client(RabbitConnection):
    def callback(self, ch, method, properties, body):
        os.system('clear')
        self._print_folder_structure(body.decode())

    def consume(self):
        channel = self.configure_rabbit()

        channel.basic_consume(
            queue=self._queue_name, on_message_callback=self.callback, auto_ack=True
        )

        channel.start_consuming()

    @staticmethod
    def _print_folder_structure(body):
        dir_structure = ast.literal_eval(body)
        for root, subdirs, files in dir_structure:
            print(f'{root}/:')
            all_root_files = subdirs + files
            print(' '.join(all_root_files))
            print()


if __name__ == '__main__':
    try:
        Client(os.getenv('BROKER_HOST', 'localhost')).consume()
    except KeyboardInterrupt:
        print('Stopping the client')
