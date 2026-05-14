# models/Restaurant.py
from .MenuItem import MenuItem

class Restaurant:

    _restaurant_id = 0

    def __init__(self, name, location):
        self.name = name
        self.location = location

        Restaurant._restaurant_id += 1
        self.restaurant_id = Restaurant._restaurant_id

        self.menu = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def add_menu_item(self, item):
        self.menu.append(item)

    def get_menu(self):
        return self.menu