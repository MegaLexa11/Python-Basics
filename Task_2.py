my_list = [300, 2, 93, 12, 22, 1, 92, 44, 44, 44, 1, 1, 4, 10, 7, 1, 78, 123, 196]

new_list = [my_list[el] for el in range(1, len(my_list), 1) if my_list[el] > my_list[el - 1]]
print(new_list)
