class Employee:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self._salary = 0

    def set_salary(self, salary):
        if isinstance(salary, int) and salary >= 0:
            self._salary = salary


a = Employee(100, 'Marian', 'Judasz')
a.set_salary(130)
print(a._salary)
