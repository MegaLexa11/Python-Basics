def fact(fact_num):
    answer_num = 1
    for i in range(1, fact_num + 1, 1):
        answer_num *= i
        yield answer_num


for ind, el in enumerate(fact(9), 1):
    print(f'{ind}! = {el}')
