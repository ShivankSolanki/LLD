from models.Order import Order


class OrderManager:

    _instance = None

    def __init__(self):

        if OrderManager._instance is not None:
            raise Exception(
                "OrderManager is a singleton. Use get_instance()."
            )

        self.orders = []

    @staticmethod
    def get_instance():

        if OrderManager._instance is None:
            OrderManager._instance = OrderManager()

        return OrderManager._instance

    def add_order(self, order: Order):
        self.orders.append(order)

    def list_orders(self):

        print("\n--- All Orders ---")

        for order in self.orders:

            print(
                f"{order.get_type()} order for "
                f"{order.get_user().get_name()} "
                f"| Total: ₹{order.get_total()} "
                f"| At: {order.get_scheduled()}"
            )