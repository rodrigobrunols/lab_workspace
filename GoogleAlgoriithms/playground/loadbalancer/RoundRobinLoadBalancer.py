import itertools, threading


class RoundRobinLoadBalancer:

    def __init__(self):
        self.servers = []
        self.server_cycle = itertools.cycle([])

    def add_server(self, server):
        self.servers.append(server)
        self.server_cycle = itertools.cycle(self.servers)

    def remove_server(self, server):
        if not self.servers:
            raise Exception("No servers available!")

        if server not in self.servers:
            raise ValueError(f"Server {server} not in servers list!")

        self.servers.remove(server)
        self.server_cycle = itertools.cycle(self.servers)

    def get_server(self):
        if not self.servers:
            raise Exception("No servers available!")
        return next(self.server_cycle)


if __name__ == "__main__":

    lb = RoundRobinLoadBalancer()
    lb.add_server("Server1")
    lb.add_server("Server2")
    lb.add_server("Server3")

    for i in range(1, 11):
        s = lb.get_server()
        print(f"Request {i} routed to {s}")

    print("\nRemoving Server2...")
    lb.remove_server("Server2")

    for i in range(11, 16):
        server = lb.get_server()
        print(f"Request {i} routed to {server}")
