"""

High-level modules shouldn't depend on low-level modules. Both should depend on abstractions. This means your business
logic shouldn't directly instantiate concrete classes - it should depend on interfaces.

"""

from abc import ABC, abstractmethod


class MessageSender(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailSender(MessageSender):
    def send(self, message):
        print(f"Sending message: {message}")


class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def notify(self, message):
        self.sender.send(message)
