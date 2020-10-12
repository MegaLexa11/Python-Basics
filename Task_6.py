from typing import Dict, List, Any

catalogue = []
item_number = 1
choice = None
attribute_number = 1

while choice != 'q':
    choice = input('Введите "+", чтобы добавить товар в каталог \n(Если вы введете "q", то завершите процесс): ')
    if choice == '+':
        name = input('Введите название товара: ')
        catalogue.append((item_number, {'Название': name}))
        # Добавление стоимости
        price = input('Введите стоимость товара (в рублях): ')
        while not price.isdecimal():
            price = input('Для того, чтобы ввести стоимость, нужно использовать целые числа: ')
        add_dict = {'Стоимость': int(price)}
        catalogue[item_number - 1][attribute_number].update(add_dict)
        # Добавление количества
        amount = input('Введите количество товара: ')
        while not amount.isdecimal():
            amount = input('Для того, чтобы ввести количество, нужно использовать целые числа: ')
        add_dict = {'Количество': int(amount)}
        catalogue[item_number - 1][attribute_number].update(add_dict)
        # Добавление единиц измерения
        measure = input('Введите единицы измерения количества товара: ')
        add_dict = {'Ед.Изм.': measure}
        catalogue[item_number - 1][attribute_number].update(add_dict)
        # Добавление большего числа характеристик
        """choice_2 = None
        while choice_2 != 'y' and choice_2 != 'n':
            choice_2 = input('Желаете ли добавить еще характеристик к товару (y/n): ')
            if choice_2 == 'y':
                new_attribute_amount = input('Введите число характеристик, которое вы хотите добавить: ')
                while not new_attribute_amount.isdecimal():
                    new_attribute_amount = input('Нужно ввести целое число: ')
                for attribute in range(int(new_attribute_amount)):
                     new_attribute = None
                     while type(new_attribute) is not list:
                         new_attribute = input('Введите характеристику и ее значение через "/": ')
                         for i in new_attribute:
                            if i == '/':
                                new_attribute = new_attribute.split('/')
                                break
                     if new_attribute[1].isdecimal():
                        new_attribute[1] = int(new_attribute[1])
                     add_dict = {new_attribute[0]: new_attribute[1]}
                     catalogue[item_number - 1][attribute_number].update(add_dict)"""

        item_number += 1
print(f'Получившийся каталог: {catalogue}')

# Сбор аналитики
print('Анализ товаров по их характеристикам:')
key_list = []
attribute_tuple = catalogue[0][1].items()
for el in attribute_tuple:
    key_list.append((el[0], []))

for item in catalogue:
    item_dict = item[1]
    for ind, el in enumerate(item_dict):
        if key_list[ind][0] == el:
            key_list[ind][1].append(item_dict.get(el))
analysis_dict = dict(key_list)
set_dict = {'Ед.Изм.': list(set(analysis_dict.get('Ед.Изм.')))}
analysis_dict.update(set_dict)
print(analysis_dict)



