import math

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
def sum_of_odd(list_of_numbers):
    sum = 0
    for number in list_of_numbers:
        if number % 2 != 1:
            sum += number
    print(sum)
    print("_____________________________________")


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
def sum_of_pair(_list):
    list_of_sum = list()
    half_len = math.ceil(len(_list) / 2)
    for i in range(half_len):
        list_of_sum.append(_list[i]*_list[len(_list)-1-i])
    print(list_of_sum)
    print("_____________________________________")


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
def diff_of_mod(_list):
    _list = list(map(lambda x: round(x % 1, 2), _list))
    _list = list(filter(lambda x: x != 0, _list))
    print(max(_list) - min(_list))
    print("_____________________________________")
#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
def binary(number):
    binary = ''
    while number > 0:
        binary += str(number % 2)
        number = number // 2
    print(binary)
    print("_____________________________________")

#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def negafibonacci(_n):
    fib_list = [0,1]
    nega_fib_list = list()
    for i in range(_n-1):
        fib_list.append(fib_list[-1] + fib_list[-2])
    for idx, num in enumerate(fib_list):
        if idx %2 == 0:
            nega_fib_list.append(-num)
        else:
            nega_fib_list.append(num)
    nega_fib_list = nega_fib_list[1::]
    nega_fib_list.reverse()
    nega_fib_list+= fib_list
    print(nega_fib_list)
    print("_____________________________________")

sum_of_odd([2, 3, 5, 9, 3])
sum_of_pair([2, 3, 4, 5, 6])
diff_of_mod([1.1, 1.2, 3.1, 5, 10.01])
binary(45)
negafibonacci(8)



