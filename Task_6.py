from itertools import count, cycle

try:
    user_number = int(input('Input a number to begin a sequence: '))
    user_end = int(input('Input a number, which will be the ending of a sequence: '))

    counting = count(user_number)
    for i in range(user_number, user_end + 1, 1):
        print(next(counting))

except ValueError:
    print('Incorrect values!')

try:
    user_text = input('Input some text to make a cycle: ')
    user_limit = int(input('Input a limit to the cycle: '))
    limit_count = 1

    repeating = cycle(user_text)
    for i in range(1, user_limit + 1, 1):
        print(next(repeating))

except ValueError:
    print('Incorrect value!')
