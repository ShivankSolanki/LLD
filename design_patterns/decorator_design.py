# Component Interface: defines a common interface for Mario and all power-up decorators.
from abc import ABC, abstractmethod


class Character(ABC):

    @abstractmethod
    def get_abilities(self):
        pass


# Concrete Component: Basic Mario character with no power-ups.
class Mario(Character):

    def get_abilities(self):
        return "Mario"


# Abstract Decorator: CharacterDecorator "is-a" Character and "has-a" Character.
class CharacterDecorator(Character):

    def __init__(self, character):
        self.character = character  # Wrapped component


# Concrete Decorator: Height-Increasing Power-Up.
class HeightUp(CharacterDecorator):

    def get_abilities(self):
        return self.character.get_abilities() + " with HeightUp"


# Concrete Decorator: Gun Shooting Power-Up.
class GunPowerUp(CharacterDecorator):

    def get_abilities(self):
        return self.character.get_abilities() + " with Gun"


# Concrete Decorator: Star Power-Up (temporary ability).
class StarPowerUp(CharacterDecorator):

    def get_abilities(self):
        return self.character.get_abilities() + " with Star Power (Limited Time)"


# Driver code
if __name__ == "__main__":

    # Create a basic Mario character.
    mario = Mario()
    print("Basic Character:", mario.get_abilities())

    # Decorate Mario with a HeightUp power-up.
    mario = HeightUp(mario)
    print("After HeightUp:", mario.get_abilities())

    # Decorate Mario further with a GunPowerUp.
    mario = GunPowerUp(mario)
    print("After GunPowerUp:", mario.get_abilities())

    # Finally, add a StarPowerUp decoration.
    mario = StarPowerUp(mario)
    print("After StarPowerUp:", mario.get_abilities())