void isPalindrome(int number) // Задача 1: Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.
{
    if (number>9999 && number<100000)
    {
        int digit1 = number %10;
        int digit2 = (number %100)/10;
        int digit4 = (number %10000)/1000;
        int digit5 = number/10000;

        if (digit1==digit5 && digit2==digit4)
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

void EuclidDistance (int [] vector1, int [] vector2, int n = 3) // Задача 2: Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.
{
    double dist = 0;
    if (vector1.Length==n && vector2.Length == n)
    {
        for (int i = 0; i < vector1.Length-1; i++)
        {
            dist += Math.Pow(vector2[i]- vector1[i], 2) ;
        }
        dist = Math.Sqrt(dist);
    }
    else
    {
        Console.WriteLine("Vectors is not correct");
    }
    Console.WriteLine(dist);
} 

void TableOfSquare( int number)   // Задача 3: Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.
{
    double [] table = new double [Math.Abs(number)];
    for (int i = 0; i <Math.Abs(number); i++)  
    {
        table[i] = Math.Pow(i+1,3); 
    }
    Console.WriteLine(string.Join(",",table));
}

isPalindrome(12321);
isPalindrome(12345);
EuclidDistance(new int[]{3,6,8},new int[]{2,1,-7});
TableOfSquare(5);