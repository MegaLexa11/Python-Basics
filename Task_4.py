user_str = input("Введите строку из нескольких слов, разделив их пробелами: ").split()

for ind, item in enumerate(user_str, 1):
    print(ind, item[:10])
