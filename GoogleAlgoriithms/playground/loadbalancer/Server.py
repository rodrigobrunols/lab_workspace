class Server:

    def __init__(self, name, weight: int = 1):
        self.name = name
        self.weight = weight
        self.original_weight = weight
        self.healthy = True

    def __repr__(self):
        return f"Server({self.name}, weight={self.weight})"
