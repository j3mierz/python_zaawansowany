class Ingridient:
    def __init__(self, name, protein, carbons, fats):
        self.name = name
        self.protein = protein
        self.carbons = carbons
        self.fats = fats


class Meal:
    def __init__(self, meal):
        self.meal = meal
        self.ingridients = []

    def add(self, name, how_much):
        self.ingridients.append((name, how_much))

    def info(self):
        for i in self.ingridients:
            print(f'name :{i[0].name}, protein : {i[0].protein // 100 * i[1]},carbons: {i[0].carbons // 100 * i[1]},fats: {i[0].fats // 100 * i[1]}')
                  # sumowanie składników trzbea zrobi

egg = Ingridient("egg", 13, 11, 32)
tomato = Ingridient("tomato", 8, 8, 8)
bread = Ingridient("bread", 2, 4, 6)
day1 = Meal("Steak")

day1.add(egg, 95)
day1.add(tomato, 90)
day1.add(bread, 123)

day1.info()
