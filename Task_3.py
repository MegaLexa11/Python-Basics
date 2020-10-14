def my_func(arg_1, arg_2, arg_3):
    num_list = [arg_1, arg_2, arg_3]
    num_list.remove(min(num_list))
    return sum(num_list)


print(my_func(34, 22, 89))
