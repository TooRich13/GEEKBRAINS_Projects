# Напишите программу, которая принимает на вход число n и выдает набор произведений чисел от 1 до n.
n = int(input())
output_list = list()
factorial = 1
for i in range(1, n+1):
    factorial *= i
    output_list.append(factorial)
#print(output_list)
print(" ".join(map(str, output_list)))
