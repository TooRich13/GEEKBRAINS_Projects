double Pow (int number,int pow) // Задача 1: Напишите функцию, используя цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.
{
    double result=1;
    if (pow >= 0)
    {
        for (int i = 0; i < pow; i++)
    {
        result*=number;
    }
    }
    else 
    {
        Console.WriteLine("Power of number is not correct");
    }
    return result;
} 

void SumOfDigit(int number) // Задача 2: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.
{
    number = Math.Abs(number);
    int length = (int)Math.Log10(number) + 1;
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum+= number % 10;
        number = number / 10;
    }

   Console.WriteLine(sum);
}

void PrintArray (params int[] numbers)
{
    if (numbers.Length ==8)
    {
        Console.WriteLine("[" + string.Join(", ", numbers)+ "]");
    }
    else 
    {
        Console.WriteLine("Enter 8 numbers");
    }

}

Console.WriteLine(Pow(3,5));
SumOfDigit(8763);
PrintArray(8,7,6,5,4,3,2,1);
