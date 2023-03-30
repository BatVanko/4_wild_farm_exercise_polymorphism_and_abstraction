from project.animals.animal import Mammal
from project.food import Food


class Mouse(Mammal):
    INCREMENTAL_COEF = 0.1
    ALLOWED_FOODS = ["Vegetable", "Fruit"]

    @staticmethod
    def make_sound():
        return "Squeak"

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def feed(self, food: Food):
        incremental_coeff = self.INCREMENTAL_COEF
        food_type = food.__class__.__name__
        if food_type not in self.ALLOWED_FOODS:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * incremental_coeff


class Dog(Mammal):
    INCREMENTAL_COEF = 0.4
    ALLOWED_FOODS = ['Meat']

    @staticmethod
    def make_sound():
        return "Woof!"

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def feed(self, food: Food):
        incremental_coeff = self.INCREMENTAL_COEF
        food_type = food.__class__.__name__
        if food_type not in self.ALLOWED_FOODS:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * incremental_coeff


class Cat(Mammal):
    INCREMENTAL_COEF = 0.3
    ALLOWED_FOODS = ['Meat', 'Vegetables']

    @staticmethod
    def make_sound():
        return "Meow"

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def feed(self, food: Food):
        incremental_coeff = self.INCREMENTAL_COEF
        food_type = food.__class__.__name__
        if food_type not in self.ALLOWED_FOODS:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * incremental_coeff


class Tiger(Mammal):
    INCREMENTAL_COEF = 1.0
    ALLOWED_FOODS = ['Meat']

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def feed(self, food: Food):
        incremental_coeff = self.INCREMENTAL_COEF
        food_type = food.__class__.__name__
        if food_type not in self.ALLOWED_FOODS:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * incremental_coeff
