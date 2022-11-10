import math


def is_day_off():  # Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
    input_day = int(input("Введите день недели: "))
    if 0 < input_day < 8:
        if input_day == 6 or input_day == 7:
            print('Да')
        else:
            print('Нет')
    else:
        print('День не корректный')
    print("_________________________________________")


# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def check_condition():

    print("X|Y|Z|RESULT")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                result = not (x or y or z) == (not x and not y and not z)
                print(x, y, z, int(result))
    print("_________________________________________")


def plane_number():  # Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
    x = int(input("Введите X: "))
    y = int(input("Введите Y: "))
    print("Плоскость: ")

    if x*y != 0:
        if x > 0 and y > 0:
            print('1')
        if x < 0 and y > 0:
            print('2')
        if x < 0 and y < 0:
            print('3')
        if x > 0 and y < 0:
            print('4')
    else:
        print("Данные не корректны")
    print("_________________________________________")


# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
def range_of_plane_number():
    number = int(input("Введите номер плоскости: "))
    if 0 < number < 5:
        if number == 1:
            print('X∈(0,∞), Yx∈(0,∞)')
        if number == 2:
            print('X∈(-∞,0), Yx∈(0,∞)')
        if number == 3:
            print('X∈(-∞,0), Yx∈(-∞,0)')
        if number == 4:
            print('X∈(0,∞), Yx∈(-∞,0)')
    else:
        print("Данные не корректны")
    print("_________________________________________")


# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
def euclidean_distance():
    x1, x2 = list(map(int, input(
        "Введите координаты точки A через запятую. (Пример: 3, 6): ").split(",")))
    y1, y2 = list(map(int, input(
        "Введите координаты точки B через запятую. (Пример: 2, 1): ").split(",")))
    result = math.sqrt((y1-x1)**2+(y2-x2)**2)
    print("Расстояние между точками =", result)
    print("_________________________________________")


is_day_off()
check_condition()
plane_number()
range_of_plane_number()
euclidean_distance()
