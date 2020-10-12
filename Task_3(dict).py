month_dict = {
    'Зимы': [12, 1, 2],
    'Весны': [3, 4, 5],
    'Лета': [6, 7, 8],
    'Осени': [9, 10, 11]
}

month = input("Введите номер месяца: ")
while not month.isdecimal() or int(month) < 1 or int(month) > 12:
    month = input("Вы что, не знаете, что в году 12 месяцев? Попробуйте еще раз: ")

month = int(month)
for season in month_dict:
    for i in month_dict.get(season):
        if month == i:
            print(f'Это месяц {season}')
