class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def sub(self, a, b):
        return a - b


class LoggingCalculator(Calculator):
    def __init__(self):
        self.history = []

    def add(self, a, b):
        self.history.append(f'{a} + {b} = {a + b}')
        return super().add(a, b)

    def sub(self, a, b):
        self.history.append(f'{a} - {b} = {a - b}')
        return super().sub(a, b)

    def mul(self, a, b):
        self.history.append(f'{a} * {b} = {a * b}')
        return super().mul(a, b)

    def div(self, a, b):
        self.history.append(f'{a} / {b} = {a / b}')
        return super().div(a, b)


kalk = LoggingCalculator()

print(kalk.add(1, 2))
print(kalk.mul(2, 2))
print(kalk.sub(2, 2))
print(kalk.div(2, 2))


print(kalk.history)
