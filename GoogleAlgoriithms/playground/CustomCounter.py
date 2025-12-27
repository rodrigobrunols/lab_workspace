from threading import Lock, Thread


class Counter:

    def __init__(self):
        self.count = 0
        self.lock = Lock()

    def increment(self):
        with self.lock:
            self.count += 1



counter = Counter()
threads = []


def worker():
    for _ in range(1000):
        counter.increment()


def main():
    for i in range(10):
        t = Thread(target=worker)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Final counter value: {counter.count}")  # Should be 10000


if __name__ == "__main__":
    main()



