class Burger():
    def __init__(self):
        self.buns = None
        self.patties = None
        self.cheese = None
        self.veggies = None
    
    def setBuns(self, buns_type):
        self.buns = buns_type
    
    def setPatties(self, patties_type):
        self.patties = patties_type
    
    def setCheese(self, cheese_type):
        self.cheese = cheese_type
    
    def setVeggies(self, veggies_type):
        self.veggies = veggies_type
    
    def __str__(self) -> str:
        return f"{self.buns}, {self.patties}, {self.cheese}, {self.veggies}"


class BurgerBuilder():
    def __init__(self):
        self.burger = Burger()
    
    def addBuns(self, buns_type):
        self.burger.setBuns(buns_type)
        return self
    def addPatties(self, patties_type):
        self.burger.setPatties(patties_type)
        return self
    def addCheese(self, cheese_type):
        self.burger.setCheese(cheese_type)
        return self
    def addVeggies(self, veggies_type):
        self.burger.setVeggies(veggies_type)
        return self
    def build(self):
        return self.burger


burger = BurgerBuilder().addBuns('sesame').addPatties('chicken').addCheese('cheddar').addVeggies('lettuce').build()
print(burger)