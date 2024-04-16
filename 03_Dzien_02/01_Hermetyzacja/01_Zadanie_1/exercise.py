class Square:
    def __init__(self, side):
        self._side = side
        self._perimeter = 4 * side
        self._area = side * side
        self._diagonal = side * (2 ** 0.5)

    def get_side(self):
        return self._side

    def get_area(self):
        return self._area

    def get_diagonal(self):
        return self._diagonal

    def get_perimeter(self):
        return self._perimeter

    def set_side(self, new_side):
        self.__init__(new_side)

    def set_area(self, new_area):
        self.__init__(new_area ** 0.5)

    def set_perimeter(self, new_perimeter):
        self.__init__(new_perimeter / 4)

    def set_diagonal(self, new_diagonal):
        self.__init__(new_diagonal / (2 ** 0.5))


s1 = Square(4)
print(s1.get_diagonal())
s1.set_diagonal(7.2)
print(s1.get_area())
