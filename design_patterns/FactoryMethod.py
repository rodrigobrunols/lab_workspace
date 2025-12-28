from abc import ABC, abstractmethod
from enum import Enum


class Notification(ABC):

    @abstractmethod
    def send(self, message: str):
        pass

    def type(self):
        pass


class EmailNotification(Notification):
    def send(self, message: str):
        print(f"Email: {message}")

    def type(self):
        return NotificationType.Email


class SMSNotification(Notification):
    def send(self, message: str):
        print(f"SMS: {message}")

    def type(self):
        return NotificationType.SMS


class NotificationType(Enum):
    EMAIL = EmailNotification
    SMS = SMSNotification


class NotificationFactory:
    @staticmethod
    def crete(notification_type: NotificationType):
        if notification_type == NotificationType.EMAIL:
            return EmailNotification()
        elif notification_type == NotificationType.SMS:
            return SMSNotification()
        raise ValueError("Invalid notification type")


notification = NotificationFactory.crete(NotificationType.Email)
notification.send('Hello')
