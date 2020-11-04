class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_int(cls, date):
        date_list = list(map(int, date.split('-')))
        return Date(date_list)

    @staticmethod
    def check_date():

        def check_validation(p_1, num, p_2, attr):
            if p_1 <= num <= p_2:
                pass
            else:
                print(f'Введен некорректный {attr}')

        for ind, el in enumerate(date_1.date):
            if ind == 0:
                check_validation(1, el, 31, 'день')
            if ind == 1:
                check_validation(1, el, 12, 'месяц')
            if ind == 2:
                check_validation(1, el, 2020, 'год')


date_1 = Date.date_to_int('41-15-2011')
print(f'Преобразование даты в числа: {date_1.date}')
Date.check_date()

