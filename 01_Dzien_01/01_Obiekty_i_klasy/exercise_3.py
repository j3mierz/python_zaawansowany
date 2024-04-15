class Bank_Account:
    def __init__(self, number):
        self.number = number
        self.cash = float(0)

    def deposit(self, amount):
        if amount > 0:
            self.cash += amount

    def withdraw(self, amount):
        if self.cash >= amount:
            self.cash -= amount
            print(amount)

    def info(self):
        print(f"on account:{self.number}, is  {self.cash}$")


a = Bank_Account(23)
a.deposit(1566)
a.withdraw(10550)
a.info()
