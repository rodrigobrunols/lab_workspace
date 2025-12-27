import threading
from random import random
from Server import Server


class WeightedRoundRobinLoadBalancer:

    def __init__(self):
        self.servers = []
        self.lock = threading.Lock()
        self.current_index = 0
        self.current_weight = 0
        self.max_weight = 0
        self.gcd_weight = 1  # Greatest common divisor of all weights

    def add_server(self, server: Server):
        with self.lock:
            self.servers.append(server)
            self._update_weights()

    def remove_server(self, server_name):
        with self.lock:
            if not self.servers:
                raise Exception("No servers available!")

            self.servers = [s for s in self.servers if s.name != server_name]
            self._update_weights()

    def _update_weights(self):
        if not self.servers:
            return
        weights = [s.weight for s in self.servers if s.healthy]
        self.max_weight = max(weights) if weights else 0
        self.gcd_weight = self._gcd_of_list(weights)
        self.current_index = -1
        self.current_weight = 0

    def _gcd_of_list(self, weights):
        """Calculate GCD of all weights"""
        from math import gcd
        from functools import reduce

        if not weights:
            return 1

        return reduce(gcd, weights)

    def health_check(self):
        """Simulate health checks"""
        with self.lock:
            for server in self.servers:
                # Simulate random health status (90% healthy)
                server.healthy = random.random() < 0.9
            self._update_weights()

    def get_server(self):
        """Get next server using weighted round-robin algorithm"""
        with self.lock:
            if not self.servers:
                raise RuntimeError("No servers available")

            healthy_servers = [s for s in self.servers if s.healthy]
            if not healthy_servers:
                raise RuntimeError("No healthy servers available")

            while True:
                self.current_index = (self.current_index + 1) % len(healthy_servers)
                if self.current_index == 0:
                    self._reinit_values()

                server = healthy_servers[self.current_index]
                if server.weight >= self.current_weight:
                    return server

    def _reinit_values(self):
        self.current_weight = self.current_weight - self.gcd_weight
        if self.current_weight <= 0:
            self.current_weight = self.max_weight
            if self.current_weight == 0:
                return None
