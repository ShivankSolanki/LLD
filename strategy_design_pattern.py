from abc import ABC, abstractmethod


# --- Generic Behavior Interface ---
class Behavior(ABC):

    @abstractmethod
    def execute(self):
        pass


# =========================================================
# WALK STRATEGIES
# =========================================================

class NormalWalk(Behavior):

    def execute(self):
        print("Walking normally...")


class HeavyWalk(Behavior):

    def execute(self):
        print("Walking with heavy robotic steps...")


class FastWalk(Behavior):

    def execute(self):
        print("Walking very fast...")


# =========================================================
# FLY STRATEGIES
# =========================================================

class JetFly(Behavior):

    def execute(self):
        print("Flying using jet boosters...")


class HoverFly(Behavior):

    def execute(self):
        print("Hovering smoothly in air...")


class RocketFly(Behavior):

    def execute(self):
        print("Flying with rocket propulsion...")


# =========================================================
# TALK STRATEGIES
# =========================================================

class FriendlyTalk(Behavior):

    def execute(self):
        print("Talking in a friendly way...")


class AIProfessionalTalk(Behavior):

    def execute(self):
        print("Talking professionally with AI voice...")


# =========================================================
# ROBOT BASE CLASS
# =========================================================

class Robot(ABC):

    def __init__(self):
        self.behaviors = {}

    # Dynamically attach behavior
    def add_behavior(self, name, behavior):
        self.behaviors[name] = behavior

    # Dynamically run behavior
    def perform(self, name):

        behavior = self.behaviors.get(name)

        if behavior:
            behavior.execute()

        else:
            print(f"This robot does not support '{name}' behavior.")

    @abstractmethod
    def projection(self):
        pass


# =========================================================
# ROBOT TYPES
# =========================================================

class CompanionRobot(Robot):

    def projection(self):
        print("Displaying companion robot UI...")


class WorkerRobot(Robot):

    def projection(self):
        print("Displaying worker robot stats...")


class MilitaryRobot(Robot):

    def projection(self):
        print("Displaying military combat systems...")


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":

    # ---------------------------------
    # Companion Robot
    # ---------------------------------

    robot1 = CompanionRobot()

    robot1.add_behavior("walk", NormalWalk())
    robot1.add_behavior("talk", FriendlyTalk())

    robot1.perform("walk")
    robot1.perform("talk")
    robot1.perform("fly")   # not supported

    robot1.projection()

    print("\n-------------------------\n")


    # ---------------------------------
    # Worker Robot
    # ---------------------------------

    robot2 = WorkerRobot()

    robot2.add_behavior("walk", HeavyWalk())
    robot2.add_behavior("talk", AIProfessionalTalk())
    robot2.add_behavior("fly", HoverFly())

    robot2.perform("walk")
    robot2.perform("talk")
    robot2.perform("fly")

    robot2.projection()

    print("\n-------------------------\n")


    # ---------------------------------
    # Military Robot
    # ---------------------------------

    robot3 = MilitaryRobot()

    robot3.add_behavior("walk", FastWalk())
    robot3.add_behavior("fly", RocketFly())

    robot3.perform("walk")
    robot3.perform("fly")
    robot3.perform("talk")  # not supported

    robot3.projection()