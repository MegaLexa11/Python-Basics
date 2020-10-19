my_list = [9, 2, 2, 2, 7, 23, 1, 44, 13, 44, 9, 3, 2, 10, 7, 4, 11]

my_set = [el for el in my_list if my_list.count(el) == 1]
print(my_set)
