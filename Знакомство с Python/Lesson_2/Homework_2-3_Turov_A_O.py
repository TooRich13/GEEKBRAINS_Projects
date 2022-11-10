# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму
n = int(input())
sequence = list()
for i in range(1, n+1):
    x = (1+(1/i))**i
    sequence.append(x)
sequence_sum = round(sum(sequence), 2)

print(sequence_sum)