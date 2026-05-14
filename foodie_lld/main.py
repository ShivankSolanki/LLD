from models import *
from FoodieApp import *
from strategies import *

if __name__ == "__main__":

    # Simulating a happy flow

    # Create FoodieApp Object
    Foodie = FoodieApp()

    # Simulate a user coming in
    user = User(101, "Aditya", "Delhi")

    print(f"User: {user.get_name()} is active.")

    # User searches for restaurants by location
    restaurant_list = Foodie.search_restaurants("Delhi")

    if not restaurant_list:
        print("No restaurants found!")
        exit()

    print("Found Restaurants:")

    for restaurant in restaurant_list:
        print(f" - {restaurant.get_name()}")

    # User selects a restaurant
    Foodie.select_restaurant(user, restaurant_list[0])

    print(f"Selected restaurant: {restaurant_list[0].get_name()}")

    # User adds items to cart
    Foodie.add_to_cart(user, "P1")
    Foodie.add_to_cart(user, "P2")

    Foodie.print_user_cart(user)

    # User checkout the cart
    order = Foodie.checkout_now(
        user,
        "Delivery",
        UPIPaymentStrategy("1234567890")
    )

    # User pays for the order
    Foodie.pay_for_order(user, order)