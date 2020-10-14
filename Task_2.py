def info_func(**kwargs):
    info_dict = kwargs
    for i in info_dict:
        print(f'{i}: {kwargs.get(i)}', end=', ')


info_func(Name='Alex', year_of_the_birth='1999', age=21, city='Tyumen',)
