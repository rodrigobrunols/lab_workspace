import collections
from threading import Thread
import time


class MessageStream2:

    def __init__(self):
        self.messageQueue = collections.deque()
        self.running = True
        self.listenerThread = None
        self.recentMessages = {}


    def startListening(self):
        def listen():
            while self.running:
                if self.messageQueue:

                    messageTime, message = self.messageQueue.popleft()

                    currentTime = int(time.time())
                    # self.recentMessages[message] = currentTime

                    self.recentMessages = {
                        message : ts for message, ts in self.recentMessages.items()
                        if currentTime - ts < 10
                    }


                    if message not in self.recentMessages:
                        print(f"{messageTime} - Message Received: {message}")
                        self.recentMessages[message] = currentTime


                    # time.sleep(0.1)

        self.listenerThread = Thread(target=listen, daemon=True)
        self.listenerThread.start()

    def sendMessage(self, messageTime, message):
        self.messageQueue.append((messageTime, message))

    def stopListen(self):
        self.running = False
        self.messageQueue.append((None,None))
        if self.listenerThread:
            self.listenerThread.join()


# Test the implementation
stream = MessageStream2()
stream.startListening()

# Get the current time as an integer timestamp
current_time = int(time.time())

stream.sendMessage(current_time, "Hello")
time.sleep(3)
stream.sendMessage(int(time.time()), "Hello")  # Should not be printed (within 10 sec)
time.sleep(7)
stream.sendMessage(int(time.time()), "Hello")  # Should be printed (after 10 sec)
time.sleep(5)
stream.sendMessage(int(time.time()), "Hello")  # Should not be printed (within 10 sec)

time.sleep(3)
stream.sendMessage(int(time.time()), "New Message")  # Should be printed

time.sleep(5)
stream.stopListen()
print("Listener stopped successfully.")
