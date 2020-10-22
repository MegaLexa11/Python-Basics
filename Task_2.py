def counter(file_name):
    count_text = open(f'{file_name}.txt', 'r', encoding='utf-8')
    count_str = count_text.readlines()
    # Список добавляем для подсчета слов
    word_count = 0

    for i in count_str:
        i = i.split()
        for word in i:
            # Здесь мы проверяем, действительно ли слово это слово, а не набор символов
            letter_count = 0
            for letter in word:
                if letter.isalpha():
                    letter_count += 1
                if letter_count == len(word):
                    word_count += 1

    print(f'Количество строк: {len(count_str)} \nКоличество слов: {word_count}')
    count_text.close()
