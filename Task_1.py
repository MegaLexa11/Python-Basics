def div_func():
    arg_1 = input('Введите делимое: ')
    arg_2 = input('Введите делитель: ')
    try:
        return round(int(arg_1) / int(arg_2), 3)
    except (ValueError, ZeroDivisionError):
        return 'Операция не может быть завершена, так как вы ввели некорректные данные'


print(div_func())
