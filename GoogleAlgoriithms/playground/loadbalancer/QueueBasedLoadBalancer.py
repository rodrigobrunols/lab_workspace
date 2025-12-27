from collections import deque
import threading


class QueueBasedLoadBalancer:

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

            if server not in self.servers:
                raise ValueError(f"Server {server} not in servers list!")

            self.servers.remove(server)

    def get_server(self):
        if not self.servers:
            raise Exception("No servers available!")

        with self.lock:
            server = self.servers.popleft()
            self.servers.append(server)
            return server


if __name__ == "__main__":

    lb = QueueBasedLoadBalancer()
    lb.add_server("Server1")
    lb.add_server("Server2")
    lb.add_server("Server3")

    def make_requests():
        for _ in range(10):
            server = lb.get_server()
            print(server)

    # Start 10 threads making requests
    threads = []
    for _ in range(10):
        t = threading.Thread(target=make_requests)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
