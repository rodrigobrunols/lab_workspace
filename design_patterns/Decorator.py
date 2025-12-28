"""

A decorator adds behavior to an object without changing its class. Use it when you need to layer on extra functionality
at runtime.


Decorator is powerful but comes up less often than Strategy or Observer. You might need this when the requirements say
things like "add logging to specific operations" or "encrypt certain messages." Instead of creating subclasses for every
combination (LoggedEmailNotification, EncryptedEmailNotification, LoggedEncryptedEmailNotification), you wrap the base
object with decorators. If you see words like "optional features," "stack behaviors," or "combine multiple enhancements,
" think Decorator.

"""

from abc import ABC, abstractmethod


class Datasource(ABC):

    @abstractmethod
    def write_data(self, data: str) -> None:
        pass

    @abstractmethod
    def read_data(self) -> str:
        pass


class FileDataSource(Datasource):
    def write_data(self, data: str) -> None:
        print(f"writing data to file: {data}")

    def read_data(self) -> str:
        print("reading data")


class EncryptionDecorator(Datasource):
    def __init__(self, data_source: Datasource):
        self.wrapped = data_source

    def write_data(self, data: str) -> None:
        encrypted_data = self._encrypt_data(data)
        self.wrapped.write_data(encrypted_data)

    def read_data(self) -> str:
        data = self.wrapped.read_data()
        return self._decrypt_data(data)

    def _encrypt_data(self, data: str) -> str:
        return f"encrypted:{data}"

    def _decrypt_data(self, data: str) -> str:
        return data.replace("encrypted:", "")
