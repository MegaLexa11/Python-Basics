class MyTypeError(Exception):
    def __init__(self, txt):
        self.txt = txt


number_list = []

while True:
    user_numbers = input('Input some numbers separated by space to add them to the list '
                         '(if you want to stop, input "q"): ')
    add_list = []
    for i in user_numbers.split():
        n = 0
        for el in i:
            if el.isalpha():
                n += 1
        try:
            if (i[0] == '-' and n == 0) or i.isdecimal():
                add_list.append(int(i))
            elif '.' in i and n == 0:
                add_list.append(float(i))
            elif i == 'q':
                pass
            else:
                raise MyTypeError('There are only numbers to input!')
        except MyTypeError as err:
            print(err)
    number_list.extend(add_list)
    if 'q' in user_numbers.split():
        break

print(number_list)
