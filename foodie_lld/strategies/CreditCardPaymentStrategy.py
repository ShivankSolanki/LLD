from strategies.PaymentStrategy import PaymentStrategy


class CreditCardPaymentStrategy(PaymentStrategy):

    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card ({self.card_number})")