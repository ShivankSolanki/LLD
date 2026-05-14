from models.Restaurant import Restaurant


class RestaurantManager:

    _instance = None

    def __init__(self):

        if RestaurantManager._instance is not None:
            raise Exception(
                "RestaurantManager is a singleton. Use get_instance()."
            )

        self.restaurants = []

    @staticmethod
    def get_instance():

        if RestaurantManager._instance is None:
            RestaurantManager._instance = RestaurantManager()

        return RestaurantManager._instance

    def add_restaurant(self, restaurant: Restaurant):
        self.restaurants.append(restaurant)

    def search_by_location(self, location: str):

        result = []

        location = location.lower()

        for restaurant in self.restaurants:

            restaurant_location = (
                restaurant.get_location().lower()
            )

            if restaurant_location == location:
                result.append(restaurant)

        return result