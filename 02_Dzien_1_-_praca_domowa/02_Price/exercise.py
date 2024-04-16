class Price:
    def __init__(self, price):
        self.value = round(float(price), 2)

    def from_usd(self, usd):
        self.value = round(float(usd) * 3.8, 2)

    def from_eur(self, eur):
        self.value = round(float(eur) * 4.5, 2)

    def __str__(self):
        return f'{self.value} PLN'

a = Price(100)
b = Price(200)
b.from_eur(100)

print(a)
print(b)
