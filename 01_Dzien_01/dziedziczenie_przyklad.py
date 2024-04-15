from math import sqrt


class Shape:
    def __init__(self, x, y, color):
        print("init class shape")
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


class Circle(Shape):  # circle jest dzieckiem Shape, dziedziczy jego metody i atrybuty
    def __init__(self, x, y, color, radius):
        print("init class circle")
        super().__init__(x, y, color)  # wywoła __init__ z klasy shape super() sięga do rodzica
        self.radius = radius

    def __str__(self):
        return f'{self.describe()} its circle'


# a = Shape(5, 8, 'red')
# b = Shape(5, 5, 'blue')
c = Circle(5, 8, 'green', 6)
# a.distance(b)
# print(a)
print(c)
