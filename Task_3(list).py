month_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
season_list = ["Зимы", "Весны", "Лета", "Осени"]

month = input("Введите номер месяца: ")
while not month.isdecimal() or int(month) < 1 or int(month) > 12:
    month = input("Вы что, не знаете, что в году 12 месяцев? Попробуйте еще раз: ")

month = int(month)
for season in month_list:
    for i in season:
        if month == i:
            for j in season_list:
                season_number_1 = month_list.index(season)
                season_number_2 = season_list.index(j)
                if season_number_1 == season_number_2:
                    print(f'Это месяц {season_list[season_number_2]}')
