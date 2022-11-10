# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import random

n = int(input())
pos_list = [int(i) for i in input().split()]
n_range = list()
# pos_list = list()
product=1

for i in range(-n, n+1):
    n_range.append(i)


# with open("file.txt", "r") as file_obj:
#     pos_list = file_obj.read().splitlines()
#     pos_list = list(map(int, pos_list))

for pos in pos_list:
    product *=n_range[pos]

print(product)
