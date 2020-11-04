class ComplexNums:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

    # Преобразователь в список выглядит не очень, но работает
    @staticmethod
    def comp_to_list(number):
        comp_list = []
        num = ''
        for i in number:
            if i.isdecimal():
                num += i
            elif i == '+':
                comp_list.append(num)
                num = ''
            elif i == '-':
                comp_list.append(num)
                num = f'{i}'
        comp_list.append(num)
        if '' in comp_list:
            comp_list.remove('')
        return comp_list

    def __add__(self, other):
        self_comp = list(map(int, self.comp_to_list(self.number)))
        other_comp = list(map(int, other.comp_to_list(other.number)))
        result_list = [el + other_comp[ind] for ind, el in enumerate(self_comp)]
        return f'{result_list[0]}{"+" if "-" not in str(result_list[1]) else ""}{result_list[1]}i'

    def __mul__(self, other):
        self_comp = list(map(int, self.comp_to_list(self.number)))
        other_comp = list(map(int, other.comp_to_list(other.number)))
        part_1 = self_comp[0] * other_comp[0] - self_comp[1] * other_comp[1]
        part_2 = self_comp[0] * other_comp[1] + other_comp[0] * self_comp[1]
        return f'{part_1}{"+" if "-" not in str(part_2) else ""}{part_2}i'


c_1 = ComplexNums('9-10i')
c_2 = ComplexNums('-4+7i')
print(c_1)
print(c_2)
print(c_1 + c_2)
print(c_1 * c_2)
