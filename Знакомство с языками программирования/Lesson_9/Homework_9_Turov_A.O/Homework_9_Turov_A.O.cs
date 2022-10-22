void N_1(int N) // Задача 64: Задайте значение N. Напишите программу, которая выведет все натуральные числа в промежутке от N до 1. Выполнить с помощью рекурсии.
{
    if (N>0)
    {
        Console.WriteLine(N);  
        N--;
        N_1(N);  
    }
    if (N<0)
    {
        Console.WriteLine(N);  
        N++;
        N_1(N); 
    }
}

N_1(5);

int sum_recurs(int m, int n, int sum = 0) // Задайте значения M и N. Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N.
{
    int i;
    if (n-m>0) { i = 1;}
    else {i = -1;}
    if (Math.Abs(n-m)==0)
    {
        sum+=m;
        return sum;
    } 
        sum +=m+n;
        m+=i;
        n-=i;
        return sum_recurs(m,n,sum);
}
 Console.WriteLine(sum_recurs(1,15));

int Ackerman(int m, int n) // Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.
{
    if (m>=0 && n>=0 )
    {
        if (m==0) { return n+1;}
        if (n==0) {return Ackerman(m-1,1);}
        n = Ackerman(m,n-1);
        m--;
        return Ackerman(m,n);
    }
    else
    {
        Console.WriteLine("Numbers is not correct");
        return 0;
    }
}
Console.WriteLine(Ackerman(3,2));