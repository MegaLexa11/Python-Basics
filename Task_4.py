def deg_func(arg_1, arg_2):
    deg_num = 1
    # Обычное возведение в степень (чтоб было)
    if arg_2 == abs(arg_2):
        for i in range(arg_2):
            deg_num = deg_num * arg_1
    # Возведение в отрицательную степень
    else:
        for i in range(abs(arg_2)):
            deg_num = deg_num / arg_1
    return deg_num


print(deg_func(2.44, -4))
