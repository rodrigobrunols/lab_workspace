from threading import Semaphore


class APIClient:
    def __init__(self):
        self.http_client = None
        self.semaphore = Semaphore(5)

    def make_request(self, method, url, **kwargs):
        with self.semaphore:
            return self.http_client .request(method, url, **kwargs)