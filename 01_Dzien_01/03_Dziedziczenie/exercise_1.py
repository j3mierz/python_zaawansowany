class Cart:
    def __init__(self):
        self.products = []

    def add(self, price, product_name):
        self.products.append((price, product_name))

    def summary(self):
        return self.products


class Discount20Percent(Cart):
    def summary(self):
        return [(i[0] * 0.8, i[1]) for i in super().summary()]


class Above3Products(Cart):
    def summary(self):
        user_cart = super().summary()
        user_cart = sorted(user_cart)
        if len(user_cart) > 3:
            user_cart[0] = (0, user_cart[0][1])
        return user_cart


a = Discount20Percent()
a.add(10, "siekiera")
a.add(100, "kostka")
a.add(30, "pomidor")
a.add(50, "towel")
print(a.summary())

b = Above3Products()
b.add(10, "siekiera")
b.add(100, "kostka")
b.add(30, "pomidor")
b.add(50, "towel")
print(b.summary())
