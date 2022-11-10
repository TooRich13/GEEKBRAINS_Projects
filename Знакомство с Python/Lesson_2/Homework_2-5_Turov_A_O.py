# Реализуйте алгоритм перемешивания списка.

numbers = [int(i) for i in input().split()]
for index, value in enumerate(numbers):
    if (value) % 2 == 0 and index != 0:
        numbers[index], numbers[index - 1] = numbers[index - 1], numbers[index]
    elif (value) % 2 == 1 and index != len(numbers)-1:
        numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]


print(" ".join(map(str, numbers)))
