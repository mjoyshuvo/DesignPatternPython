# Creational Pattern
class Burger:
    def __init__(self, ingredients) -> None:
        self.ingredients = ingredients
    
    def print(self):
        print(self.ingredients)

    def __str__(self) -> str:
        return f"{self.ingredients}"
    

# Create different types of burgers with factory pattern
class BurgerFactory:

    def createCheeseBurger(self):
        return Burger(['cheese', 'latuse', 'tomato', 'bread'])

    def createVegBurger(self):
        return Burger(['tomato', 'latuse', 'bread'])
    
    def createChickenBurger(self):
        return Burger(['chicken', 'latuse', 'bread'])
    

burger_factory = BurgerFactory()
cheese_burger = burger_factory.createCheeseBurger()
cheese_burger.print()
veg_burger = burger_factory.createVegBurger()
veg_burger.print()
chicken_burger = burger_factory.createChickenBurger()
chicken_burger.print()