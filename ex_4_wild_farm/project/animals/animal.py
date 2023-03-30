from abc import ABC, abstractmethod

from project.food import Food


class Animal(ABC):
    ALLOWED_FOODS = None
    INCREMENTAL_COEF = None

    def __init__(self, name: str, weight: float, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten


    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    @abstractmethod
    def feed(self, food: Food):
        pass
        # incremental_coeff = self.INCREMENTAL_COEF
        # food_type = food.__class__.__name__
        # if food_type not in self.ALLOWED_FOODS:
        #     return f"{self.__class__.__name__} does not eat {food_type}!"
        # self.food_eaten += food.quantity
        # self.weight += food.quantity * incremental_coeff


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float, food_eaten=0):
        super().__init__(name, weight, food_eaten)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
