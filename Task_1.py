# Из задания 2 импортируем функцию для подсчета
from Task_2 import counter

# Ввод названия файла
file_name = input('Input a name of the file, which you would like to create (without extension): ')

# Задание 1 (формирование текста в файле)
try:
    new_file = open(f'{file_name}.txt', 'x', encoding='utf-8')
    count_file = open(f'{file_name}.txt', 'a', encoding='utf-8')

    while True:
        user_text = input('Input any text to add it to the new file (if you want to stop, do not enter anything): ')
        if user_text == '':
            break
        count_file.write(f'{user_text}\n')
    count_file.close()
# Функция из задания 2
    counter(file_name)

except (FileExistsError, FileNotFoundError):
    print('Wrong file name!')





