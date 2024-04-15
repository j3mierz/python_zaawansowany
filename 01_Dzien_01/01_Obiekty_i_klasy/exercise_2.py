from math import sqrt


class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def describe(self):
        return f'x:{self.x}, y:{self.y}, color:{self.color}'

    def distance(self, other):
        print(
            f"distance from ({self.describe()}) to ({other.describe()}) is {sqrt(abs(self.x - other.x) ** 2 + abs(self.y - other.y) ** 2)}")

    def __str__(self):
        return f'{self.describe()}'


a = Shape(5, 8, 'red')
b = Shape(5, 5, 'blue')

a.distance(b)
print(a)
