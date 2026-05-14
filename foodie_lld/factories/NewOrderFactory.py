from factories import OrderFactory
from models import DeliveryOrder, PickupOrder

class NowOrderFactory(OrderFactory):

    def create_order(self,
        user,
        cart,
        restaurant,
        order_items,
        payment_strategy,
        total_cost,
        order_type
    ):
        order = None
        
        if order_type == "Delivery":
            order = DeliveryOrder()
            order.set_user_address(user.get_address())
        else:
            order = PickupOrder()
            order.get_restaurant_address(restaurant.get_location())

        order.set_user(user)
        order.set_restaurant(restaurant)
        order.set_items(order_items)
        order.set_payment_strategy(payment_strategy)
        order.set_total(total_cost)

        return order