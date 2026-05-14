from abc import ABC, abstractmethod


class OrderFactory(ABC):

    @abstractmethod
    def create_order(
        self,
        user,
        cart,
        restaurant,
        order_items,
        payment_strategy,
        total_cost,
        order_type
    ):
        pass