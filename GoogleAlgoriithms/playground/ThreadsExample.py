import random
import threading
import time


def worker():
    name = threading.current_thread().name
    print(f"Thread {name} starting")
    time.sleep(random.uniform(1, 3))
    print(f"Thread {name} completed")


threads = []
for i in range(3):
    t = threading.Thread(target=worker, name=f"Worker-{i}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()
