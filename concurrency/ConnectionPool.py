import dataclasses
import random

from queue import Queue


@dataclasses.dataclass
class Connection:
    name: str


class ConnectionPool:

    def __init__(self, max_size: int = 5):
        self.connection_pool = Queue()
        for _ in range(max_size):
            self.connection_pool.put(self._create_connection())

    @staticmethod
    def _create_connection():
        return Connection(random.choice("abcdefg"))

    def get_connection(self):
        return self.connection_pool.get(timeout=10)

    def release_connection(self, connection):
        self.connection_pool.put(connection)

    def execute_query(self, query):
        conn = self.get_connection()

        try:
            return conn.execute(query)
        except Exception as e:
            print(e)
        finally:
            self.release_connection(conn)
