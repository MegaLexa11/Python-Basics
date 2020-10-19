from sys import argv

try:
    directory, time, rate, premium = argv
    try:
        salary = (int(time) * int(rate)) + int(premium)
        print(f'Зарплата сотрудника составит {salary}')
    except ValueError:
        print('You have to input an integer!')
except ValueError:
    print('You have to input 3 values: time worked, rate and premium')
