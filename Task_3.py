class Worker:

    # Конструктор
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_info(self):
        print(f"Worker's name: {self.name} {self.surname} \nWorkers position: {self.position}")

    def get_total_income(self):
        print(f'Total income: {sum(self._income.values())}')


# Не совсем понял, что имеется в виду под 'ссылаться на словарь', поэтому сделал так
income = {
    'Wage': 100000,
    'Bonus': 20000
}
smith = Position('Jack', 'Smith', 'Designer', income)
smith.get_full_info()
smith.get_total_income()
