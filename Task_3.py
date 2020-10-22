from math import fsum

employee = open('task_3_text.txt', 'r', encoding='utf-8')
employee_list = employee.readlines()
employee_dict = {}
salary_list = []

for i in employee_list:
    i = i.split()
    if float(i[1]) < 20000:
        add_employee = {i[0]: float(i[1])}
        employee_dict.update(add_employee)
        salary_list.append(float(i[1]))

mid_salary = round(fsum(salary_list) / len(salary_list), 2)
print(f'Сотрудники, имеющие оклад менее 20000: \n{employee_dict} \nИх средняя зработная плата: {mid_salary}')

employee.close()