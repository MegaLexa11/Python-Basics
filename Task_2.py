class MyZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


user_numbers = input('Введите делимое и делитель через "/": ')
try:
    user_numbers = list(map(int, user_numbers.split('/')))
    if user_numbers[1] == 0:
        raise MyZeroDivision('На ноль делить нельзя!')
    print(f'{user_numbers[0]}/{user_numbers[1]} = {round(user_numbers[0]/user_numbers[1], 2)}')
except ValueError:
    print('Неверный ввод!')
except MyZeroDivision as err:
    print(err)
