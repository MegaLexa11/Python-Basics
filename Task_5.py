def str_sum():
    num_list = []
    while True:
        num_str = input('Введите строку целых чисел через пробел (Если хотите прекратить, введите "q"): ').split()
        # Вводим счетчик для красивого оформления
        n = 0
        current_num_list = []
        for i in num_str:
            if i.isdecimal():
                num_list.append(int(i))
                current_num_list.append(int(i))
            elif i == 'q':
                pass
            else:
                n += 1
        # Красивое (наверно) оформление
        if n > 0:
            print('Один или неколько введенных вами элементов не был просуммирован, так как не являлся целым числом')
        print(f'Сумма введенных чисел: {sum(current_num_list)} \nОбщая сумма: {sum(num_list)}')
        if 'q' in num_str:
            break


str_sum()
