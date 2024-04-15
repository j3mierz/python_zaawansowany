class Calculator:
    def __init__(self):
        self.operations = []

    def add(self, num1, num2):
        self.operations.append(f"added {num1} to {num2} got {num1 + num2}")

    def multiply(self, num1, num2):
        self.operations.append(f"multiplied {num1} by {num2} got {num1 * num2}")

    def operations_show(self):
        print(self.operations)


calculator_1 = Calculator()
calculator_1.add(1, 2)
calculator_1.multiply(4, 6)
calculator_1.operations_show()
