rate_list = [12, 7, 5, 5, 3, 2]
print(f'Перед вами рейтинг: \n{rate_list}')

user_number = None
while user_number != 'q':
    user_number = input('Введите целое положительное число для рейтинга \n(Если хотите закончить, введите "q"): ')
    if user_number.isdecimal():
        user_number = int(user_number)
        for ind, item in enumerate(rate_list):
            if user_number > item:
                rate_list.insert(ind, user_number)
                print(rate_list)
                break
            elif user_number <= rate_list[-1]:
                rate_list.append(user_number)
                print(rate_list)
                break

