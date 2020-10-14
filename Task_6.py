def int_func(word_str):
    latin_list = list(range(97, 123, 1))
    word_list = word_str.split()
    error_list = []
    for i in word_list:
        for j in i:
            if ord(j) not in latin_list:
                error_list.append(i)
                break
    for i in error_list:
        if i in word_list:
            word_list.remove(i)
    for i in word_list:
        print(i.title(), end=' ')


int_func('nice авп ъghj helicopter jапро hjjпаро вапрghgh cool')
