from abc import ABC, abstractmethod

class PaymentStrategy():

    @abstractmethod
    def pay(self, amount):
        pass