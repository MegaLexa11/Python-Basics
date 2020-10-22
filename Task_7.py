from math import fsum
import json


firm_file = open('task_7_text.txt', 'r', encoding='utf-8')
firm_list = []
all_profit = []

for i in firm_file:
    i = i.split()
    firm_profit = int(i[-2]) - int(i[-1])
    if firm_profit > 0:
        all_profit.append(firm_profit)
    firm_list.append({i[0]: firm_profit})

mid_profit = round(fsum(all_profit) / len(all_profit), 2)
firm_list.append({'Средняя прибыль': mid_profit})

firm_file.close()

with open('task_7.json', 'w', encoding='utf-8') as write_file:
    json.dump(firm_list, write_file)
