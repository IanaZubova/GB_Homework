class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())


data = Position('Max', 'Coleman', 'Master', 15000, 5000)
print(f"Employe name: {data.get_full_name()}")
print(f"Employee total income: {data.get_total_income()}")