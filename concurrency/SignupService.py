from dataclasses import dataclass
from queue import Queue
from threading import Thread


@dataclass
class EmailTask:
    user: str
    email: str
    subject: str
    body: str


@dataclass
class User:
    name: str
    email: str


class SignupService:

    def __init__(self):
        self.users = []
        self.email_queue = Queue(maxsize=100)

    def signup(self, user):
        self.add_user(user)
        self.add_welcome_email_task(user)
        return True

    def add_user(self, user):
        return self.users.append(user)

    def add_welcome_email_task(self, user):
        self.email_queue.put(EmailTask(user.name, user.email, f"Welcome E-mail", f"Welcome user {user.name}"))

    def start_work(self):
        print("Starting work")
        print()
        while True:
            task = self.email_queue.get()
            print(f"Task processed: {task}")


if __name__ == "__main__":
    service = SignupService()
    worker_thread = Thread(target=service.start_work)
    worker_thread.start()

    service.signup(User("rodrigo", "rodrigo@email.com"))
    service.signup(User("leoncio", "leoncio@email.com"))
