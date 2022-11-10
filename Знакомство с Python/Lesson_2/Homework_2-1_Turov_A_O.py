from curses.ascii import isdigit

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
numbers = input()
result = 0
for char in numbers:
    if char.isdigit():
        result += int(char)
print(result)
