"""
Problem 3: Producer-Consumer Pattern
Implement a producer-consumer system where:
2 producer threads generate random numbers every 0.5s
3 consumer threads process numbers from queue
"""
import random
import threading
import time
from queue import Queue


def produces(queue: Queue, producer_id: str):
    while True:
        num = random.randint(1, 10000)
        queue.put(num)
        print(f"Producer {producer_id} generated {num}")
        time.sleep(0.5)


def consumes(queue: Queue, consumer_id=str):
    thread_name = threading.current_thread().name
    num = queue.get()
    print(f"Consumer {consumer_id} processed {num}")
    queue.task_done()


main_queue = Queue()

producers = []
for i in range(2):
    thread = threading.Thread(target=produces, args=(main_queue, i))
    producers.append(thread)
    thread.start()


consumers = []
for i in range(3):
    thread = threading.Thread(target=consumes, args=(main_queue,i))
    consumers.append(thread)
    thread.start()
