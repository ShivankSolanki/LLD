from .PaymentStrategy import PaymentStrategy


class UPIPaymentStrategy(PaymentStrategy):

    def __init__(self, phone_number):
        self.phone_number = phone_number

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI ({self.phone_number})")