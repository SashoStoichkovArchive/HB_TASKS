class Worker:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def salary(self):
        return self._salary

class Tailor(Worker):
    def __init__(self, name, address, salary):
        super().__init__(name, salary)
        self.tailor_address = address

    @classmethod
    def calc_hours(cls, hours_per_day):
        return hours_per_day * 3

    @classmethod
    def birthday_hours(cls, has_birthday=True):
        if has_birthday:
            return cls.calc_hours(16)

        return 0

    @staticmethod
    def min_salary():
        return 580

t = Tailor("Pesho", "Pernik", 8)

print(Tailor.calc_hours(13))