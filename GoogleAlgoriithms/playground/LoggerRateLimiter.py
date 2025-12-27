import time, threading

class Logger:
    def __init__(self, interval:int):
        self.interval = interval
        self.message_time = {}

    def should_print_message(self, message):
        return message not in self.message_time or time.monotonic() - self.message_time[message] > self.interval


    def log(self, message):
        if self.should_print_message(message):
            now = time.time()
            print(f"[{time.strftime('%X')}]  {message}")
            self.message_time[message] = now


class ThreadSafeLogger:

    def __init__(self, interval:int):
        self.interval = interval
        self.message_time = {}
        self.lock = threading.Lock()


    def should_print_message(self, message):
        return message not in self.message_time or time.monotonic() - self.message_time[message] > self.interval


    def log(self, message):
        now = time.time()
        with self.lock:
            if self.should_print_message(message):
                print(f"[{time.strftime('%X')}]  {message}")
                self.message_time[message] = now
