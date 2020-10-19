from functools import reduce

my_list = [el for el in range(100, 10001, 2)]

print(reduce(lambda a_1, a_2: a_1 * a_2, my_list))
