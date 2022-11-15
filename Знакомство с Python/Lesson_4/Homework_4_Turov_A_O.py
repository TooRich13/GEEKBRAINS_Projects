import math
import random
import re


def my_round(x, d=0.01):  # Вычислить число c заданной точностью d
    if 10e-1 >= d >= 10e-10:
        d = int(abs(math.log10(d)))
        print(round(x, d))
    else:
        print("d введён некорректно")


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def prime_factors(n):
    primfac = list()
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            primfac.append(int(i))
            n /= i
    if n != 1:
        primfac.append(int(n))
    print(primfac)


# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
def non_repeat(numbers):
    non_repeat_list = list()
    for i in numbers:
        if i not in non_repeat_list:
            non_repeat_list.append(i)
        else:
            non_repeat_list.remove(i)
    print(non_repeat_list)


# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
def polynomial(k):
    var = "x"
    out = ""
    coefficient = [random.randint(0, 100) for i in range(k+1)]
    for idx, item in enumerate(coefficient):
        if idx == k:
            out += str(item) + " = " + "0"
        elif k - idx == 1:
            out += str(item)+"*"+var + " + "
        else:
            out += str(item)+"*"+var+"^" + str(k-idx) + " + "
    with open("polynomial_1.txt", "w") as file:
        file.write(out)


# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
def sum_polynom(polynom_file_1="polynomial_1.txt", polynom_file_2="polynomial_2.txt"):
    polyn_1 = ""
    polyn_2 = ""
    res_coef = []
    var = "x"
    out = ""
    with open(polynom_file_1, "r") as file:
        polyn_1 += file.readline()
    with open(polynom_file_2, "r") as file:
        polyn_2 += file.readline()

    # Убираем "= 0" и разделяем по "+"
    polyn_1 = polyn_1[0:-3].split("+")
    polyn_2 = polyn_2[0:-3].split("+")

    #Убираем всё, что после "*" для каждого элемента
    for polyn in [polyn_1, polyn_2]:
        for idx, item in enumerate(polyn):
            item = item.strip()
            item = item.partition('*')[0]
            polyn[idx] = int(item)


    if len(polyn_1) == len(polyn_2):
        for i in range(len(polyn_1)):
            res_coef.append(polyn_1[i]+polyn_2[i])

    k = len(res_coef)-1
    for idx, item in enumerate(res_coef):
        if idx == k:
            out += str(item) + " = " + "0"
        elif k - idx == 1:
            out += str(item)+"*"+var + " + "
        else:
            out += str(item)+"*"+var+"^" + str(k-idx) + " + "
    with open("res_polynomial.txt", "w") as file:
        file.write(out)

        

    print(polyn_1)
    print(polyn_2)
    print(res_coef)


sum_polynom()
