void MinMax (int a, int b) // Задача 1: Напишите программу, которая на вход принимает два числа и выдаёт, какое число большее, а какое меньшее.
    {
        if (a>b){Console.WriteLine($"max={a} min{b}");}
        else if (b>a) {Console.WriteLine($"max={b} min={a}");}
        else if (b==a) {Console.WriteLine($"numbers are equal ");}
        else {Console.WriteLine("error");}
    }

void Max(params int[] numbers) // Задача 2: Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.
    {
        int max = numbers[0];
        foreach (int item in numbers)
        {
            if (max < item)
            {
                max = item; 
            }
        }
        Console.WriteLine(max);
    }
    
void  isEven(int number) // Задача 3: Напишите программу, которая на вход принимает число и выдаёт, является ли число чётным (делится ли оно на два без остатка).
    {
        if (number %2==0)
        {
            Console.WriteLine("Yes");
        }
        else
        {
            Console.WriteLine("No");
        }
    }

void EvenNumbers (int n) // Задача 4: Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
    {
        List<int> evennubers  = new List<int>();
        for (int i = 2; i<=n;i=i+2)
        {
            evennubers.Add(i);
        }

        Console.WriteLine(string.Join(",",evennubers));
    }

MinMax(4,9);
Max(85,54,76);
isEven(8);
isEven(9);
EvenNumbers(10);