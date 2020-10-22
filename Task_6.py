from math import fsum

read_file = open('task_6_text.txt', 'r', encoding='utf-8')
file_list = read_file.readlines()
lesson_dict = {}

for el in file_list:
    el = el.split()
    num_list = []
    for word in el:
        num = ''
        for char in word:
            if char.isdecimal():
                num += char
            elif num != '':
                num_list.append(int(num))
                num = ''
    lesson_dict.update({el[0]: int(fsum(num_list))})
print(lesson_dict)

read_file.close()

