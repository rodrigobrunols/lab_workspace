import itertools, threading


class RoundRobinLoadBalancer:

    def __init__(self):
        self.servers = []
        self.server_cycle = itertools.cycle([])
        self.lock = threading.Lock()

    def add_server(self, server):
        with self.lock:
            self.servers.append(server)
            self.server_cycle = itertools.cycle(self.servers)

    def remove_server(self, server):
        with self.lock:
            if not self.servers:
                raise Exception("No servers available!")

            if server not in self.servers:
                raise ValueError(f"Server {server} not in servers list!")

            self.servers.remove(server)
            self.server_cycle = itertools.cycle(self.servers)

    def get_server(self):
        with self.lock:
            if not self.servers:
                raise Exception("No servers available!")
            return next(self.server_cycle)


if __name__ == "__main__":
    lb = RoundRobinLoadBalancer()
    lb.add_server("Server1")
    lb.add_server("Server2")

    def make_requests():
        for _ in range(100):
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
