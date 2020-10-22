from random import randint
from math import fsum

file_name = 'task_5_text.txt'
try:
    create_file = open(file_name, 'x', encoding='utf-8')
    write_file = open(file_name, 'a+', encoding='utf-8')
    sum_list = []

    try:
        number_amount = int(input('Input an amount of numbers to add them in file: '))
        for i in range(1, number_amount + 1):
            random_number = randint(1, 100)
            sum_list.append(random_number)
            write_file.write(f'{random_number} ')
        write_file.seek(0)
        print(f'Numbers: \n{write_file.readline()} \nSum: {fsum(sum_list)}')
        print(f'Also you should check file "{file_name}" to make sure, that numbers are in it')
    except ValueError:
        print('Incorrect Value!')

    write_file.close()

except FileExistsError:
    print('This file already exists! \nPlease, change the name in program code and repeat')
except FileNotFoundError:
    print('Wrong file name! \nPlease, change the name in program code and repeat')
