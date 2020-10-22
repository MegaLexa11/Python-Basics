# Обработка имеющегося файла
read_file = open('task_4_text.txt', 'r', encoding='utf-8')
number_list = read_file.readlines()
number_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
new_list = []

for i in number_list:
    i = i.split()
    if i[0] in number_dict:
        i.insert(0, number_dict.get(i[0]))
        i.remove(i[1])
        new_list.append(i)

read_file.close()

# Создание файла
file_name = 'task_4_new.txt'
try:
    create_file = open(file_name, 'x', encoding='utf-8')
    write_file = open(file_name, 'a', encoding='utf-8')

    for i in new_list:
        for word in i:
            write_file.write(f'{word} ')
        write_file.write('\n')

    write_file.close()

except FileExistsError:
    print('This file already exists! \nPlease, change the name in program code and repeat')
except FileNotFoundError:
    print('Wrong file name! \nPlease, change the name in program code and repeat')
