from collections import deque
import threading

class LoadBalancer:

    def __init__(self):
        self.servers = deque()
        self.lock = threading.Lock()

    def add_server(self, server):
        with self.lock:
            self.servers.append(server)

    def remove_server(self, server):
        with self.lock:
            if not self.servers:
                raise Exception("No servers available!")
            return self.servers.remove(server)

    def get_server(self) -> str:
        with self.lock:
            server = self.servers.popleft()
            self.servers.append(server)
            return server


