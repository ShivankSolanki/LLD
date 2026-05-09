# robot_factory.py

from abc import ABC, abstractmethod

from strategy_design_pattern import (
    CompanionRobot,
    WorkerRobot,
    MilitaryRobot
)

from strategy_design_pattern import (
    NormalWalk,
    HeavyWalk,
    FastWalk,
    FriendlyTalk,
    AIProfessionalTalk,
    HoverFly,
    RocketFly
)


# =========================================================
# CREATOR INTERFACE
# =========================================================

class RobotCreator(ABC):

    @abstractmethod
    def create(self):
        pass


# =========================================================
# CONCRETE CREATOR CLASSES
# =========================================================

class CompanionRobotCreator(RobotCreator):

    def create(self):

        robot = CompanionRobot()

        robot.add_behavior("walk", NormalWalk())
        robot.add_behavior("talk", FriendlyTalk())

        return robot


class WorkerRobotCreator(RobotCreator):

    def create(self):

        robot = WorkerRobot()

        robot.add_behavior("walk", HeavyWalk())
        robot.add_behavior("talk", AIProfessionalTalk())
        robot.add_behavior("fly", HoverFly())

        return robot


class MilitaryRobotCreator(RobotCreator):

    def create(self):

        robot = MilitaryRobot()

        robot.add_behavior("walk", FastWalk())
        robot.add_behavior("fly", RocketFly())

        return robot


# =========================================================
# FACTORY CLASS
# =========================================================

class RobotFactory:

    _registry = {}

    @classmethod
    def register_robot(cls, robot_type, creator):
        cls._registry[robot_type] = creator

    @classmethod
    def create_robot(cls, robot_type):

        creator = cls._registry.get(robot_type)

        if not creator:
            raise ValueError(
                f"Robot type '{robot_type}' not registered."
            )

        return creator.create()


# =========================================================
# REGISTER CREATORS
# =========================================================

RobotFactory.register_robot(
    "companion",
    CompanionRobotCreator()
)

RobotFactory.register_robot(
    "worker",
    WorkerRobotCreator()
)

RobotFactory.register_robot(
    "military",
    MilitaryRobotCreator()
)


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":

    robot1 = RobotFactory.create_robot("worker")

    robot1.perform("walk")
    robot1.perform("talk")
    robot1.perform("fly")

    print("\n----------------------\n")

    robot2 = RobotFactory.create_robot("military")

    robot2.perform("walk")
    robot2.perform("fly")
    robot2.perform("talk")