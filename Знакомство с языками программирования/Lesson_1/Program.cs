static string MinMax (int a, int b) // Задача 1: Напишите программу, которая на вход принимает два числа и выдаёт, какое число большее, а какое меньшее.
    {
        if (a>b){return $"max={a} min{b}";}
        else if (b>a) {return $"max={b} min={a}";}
        else if (b==a) {return $"numbers are equal ";}
        else {return "error";}
    }

static int Max(params int[] numbers) // Задача 2: Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.
    {
        int max = numbers[0];
        foreach (int item in numbers)
        {
            if (max < item)
            {
                max = item; 
            }
        }
        return max;
    }
    
static string isEven(int number) // Задача 3: Напишите программу, которая на вход принимает число и выдаёт, является ли число чётным (делится ли оно на два без остатка).
    {
        if (number %2==0)
        {
            return "Yes";
        }
        else
        {
            return "No";
        }
    }

static List<int> EvenNumbers (int n) // Задача 4: Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
    {
        List<int> evennubers  = new List<int>();
        for (int i = 2; i<=n;i=i+2)
        {
            evennubers.Add(i);
        }

        return evennubers;
    }

Console.WriteLine("Задача 1 (входные данные: 5,7 ) : \n "+MinMax(5,7)); //Вывод решения Задачи 1 с входными данными: 5,7 

Console.WriteLine("Задача 2 (входные данные: 2,3,7 ) : \n "+Max(2,3,7)); //Вывод решения Задачи 2 с входными данными: 2,3,7

Console.WriteLine("Задача 3 (входные данные: 8 ) : \n "+isEven(8)); //Вывод решения Задачи 3 с входными данными: 8

Console.WriteLine("Задача 3 (входные данные: 9 ) : \n "+isEven(9)); //Вывод решения Задачи 3 с входными данными: 9

List<int> evennum = EvenNumbers(11);  
Console.WriteLine("Задача 4 (входные данные: 11) : \n "+string.Join(",", evennum)); //Вывод решения Задачи 4 с входными данными: 11