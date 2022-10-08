void SecondDigit(int number ) // Задача 1: Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа.
{
    if (Math.Abs(number)< 99 && Math.Abs(number)> 999 ) {Console.WriteLine("Number is not correct");}
    Console.WriteLine((Math.Abs(number) / 10) % 10);
}

void ThirtDigit(int number) // Задача 2: Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.
{
    if (Math.Abs(number)>99)
    {
        Console.WriteLine(Math.Abs(number) % 10);
    }
    else
    {
        Console.WriteLine("No third digit");
    }
}

void isWeekend(int numberOfDay) // Задача 3: Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
{
    if (numberOfDay>0 && numberOfDay<8)
    {
        if (numberOfDay>5) 
        {
            Console.WriteLine("Yes");
        }
        else 
        {
            Console.WriteLine("No");
        }
    } 
    else
    {
        Console.WriteLine("Number is not correct");
    }

}

SecondDigit(321);
ThirtDigit(637);
isWeekend(6);