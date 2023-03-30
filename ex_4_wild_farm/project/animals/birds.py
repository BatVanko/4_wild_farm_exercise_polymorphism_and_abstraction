from project.animals.animal import Bird
from project.food import Meat, Food


class Owl(Bird):
    OWL_INCREMENTAL_COEFF = 0.25
    ALLOWED_FOODS = ['Meat']

    def feed(self, food: Food):
        incremental_coeff = self.OWL_INCREMENTAL_COEFF
        food_type = food.__class__.__name__
        if food_type not in self.ALLOWED_FOODS:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * incremental_coeff

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    HEN_INCREMENTAL_COEFF = 0.35
    HEN_ALLOWED_FOODS = ["Vegetable", "Fruit", "Meat", "Seed "]

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food: Food):
        food_type = food.__class__.__name__
        if food_type not in self.HEN_ALLOWED_FOODS:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * self.HEN_INCREMENTAL_COEFF
