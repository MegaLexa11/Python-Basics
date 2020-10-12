my_list = input('Введите элементы списка через пробел: ').split()

print(my_list)

for ind, item in enumerate(my_list):
    if item != my_list[-1]:
        if ind % 2 == 0:
            my_list[ind + 1], my_list[ind] = item, my_list[ind + 1]

print(my_list)
