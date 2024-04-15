class Car:
    def __init__(self, year, rejestracja, engine):
        self.year = year / 10
        self.rejestracja = rejestracja
        self.engine = engine

    def deposit(self, amount):
        self.state = amount


class Account:

    def __init__(self, numer, stan):
        self.numer = numer
        self.stan = stan

    def deposit(self, amount):
        self.stan += amount

    def withdraw(self, amount):
        if amount > 0:
            self.stan -= amount


a = car(1999, 199, 4.5)
a = car(1999, 199, 4.5, )
print(a.year)
a.deposit(2)
print(a.state)
