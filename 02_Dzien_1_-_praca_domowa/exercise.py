class Ingridients:
    def __init__(self, name, protein, carbons, fats):
        self.name = name
        self.protein = protein
        self.carbons = carbons
        self.fats = fats


class Meal(Ingridients):
    def __init__(self, meal):
        self.meal = meal

    def add(self, name_i, protein, carbons, fats):
        super().__init__(name_i, protein, carbons, fats)


day1 = Meal("Steak")

day1.add("egg", protein=100, carbons=100, fats=100)
print(day1.ing)
