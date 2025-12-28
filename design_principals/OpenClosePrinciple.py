from abc import ABC, abstractmethod

"""
Classes should be open for extension but closed for modification. You should be able to add new behavior without 
changing existing code. This usually means using interfaces or abstract classes so you can add new implementations 
without touching the original code.
"""


class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount: float):
        pass


class CreditCardPaymentMethod(PaymentMethod):
    def process(self, amount: float):
        print(f"Credit card payment: {amount}")


class CryptoPaymentMethod(PaymentMethod):
    def process(self, amount: float):
        print(f"Crypto payment: {amount}")


class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process(self, amount: float):
        self.payment_method.process(amount)
