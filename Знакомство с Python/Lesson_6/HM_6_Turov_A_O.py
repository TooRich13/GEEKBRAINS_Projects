import numexpr as ne
# Напишите программу  вычисления арифметического  выражения заданного строкой.
# Используйте операции +,-,/,*. Приоритет операций стандартный.

# Улучшение кода
input_str = "2+(3+6/2)/3"
res = ne.evaluate(input_str)
print(res)

# ИЛИ

operators = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}


def parse(input_string):
    res_list = []
    number = ''
    prior = 0
    for s in input_string:
        if s.isdigit():  # если символ - цифра, то собираем число
            number += s
        elif number:  # если символ не цифра, то выдаём собранное число и начинаем собирать заново
            res_list.append(float(number))
            number = ''
        if s == "(":
            prior += 2
        if s == ")":
            prior -= 2
        if s in operators:  # если символ - оператор или скобка, то выдаём как есть
            res_list.append((operators[s][0]+prior, operators[s][1]))

    if number:  # если в конце строки есть число, выдаём его
        res_list.append(float(number))
    return res_list


def calc(parse_list):
    while len(parse_list)>2:
        list_prior = []
        for idx, elem in enumerate(parse_list):
            if type(elem) == tuple:
                list_prior.append((idx, elem[0])) # здесь elem[0] - это приоритет функции
        if len(list_prior) !=0:
            oper_idx = max(list_prior, key= lambda i: i[1] )[0] # индекс операции с максимальным приоритетом

            oper = parse_list[oper_idx][1] 
            res = oper(parse_list[oper_idx-1], parse_list[oper_idx+1])

            parse_list.insert(oper_idx+2, res)
            del parse_list[oper_idx-1: oper_idx+2]
    return parse_list[0]




print(calc(parse(input_str)))



# Дана последовательностиь чисел.
# Получить список уникальных элементов последовательности
# Улучшение кода
input_list = [1,2,3,5,1,5,3,10]
res = list(set(input_list))
print(res)
