int [,] RandomArray (int rows, int columns) // Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.
{
    Random rnd = new Random();
    int [,] array = new int [rows,columns];
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j <columns; j++)
        {

            array[i,j] = rnd.Next(-100, 100);
            

        }
    }
    return array;
}

void PrintArray<T> (T [,] array)
{
    int rows = array.GetUpperBound(0) + 1;    // количество строк
    int columns = array.Length / rows;        // количество столбцов
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j <columns; j++)
        {
            Console.Write($"{array[i, j]} \t");
        }
        Console.WriteLine();
    }
    Console.WriteLine();
}


void SortArray(int [,]array) // Задача 54: Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.
{
    int rows = array.GetUpperBound(0) + 1;    // количество строк
    int columns = array.Length / rows;        // количество столбцов
    int temp;
    for (int i = 0; i < rows; i++)
    {  
        for (int j = 0; j < columns-1; j++)
        {
            for (int k = j+1; k < columns; k++)
            {
                if (array[i,j]>array[i,k] )
                {
                    temp = array[i,k];
                    array[i,k] = array[i,j];
                    array[i,j] = temp;
                    //Swap<int>(ref array[i,j], ref array[i,j+1]);
                    
                }

            }
        }
    }
    PrintArray<int>(array);
    Console.WriteLine("__________________________________\n");
}

void MinSumArray(int [,]array) // Задача 56: Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.
{
    int rows = array.GetUpperBound(0) + 1;    // количество строк
    int columns = array.Length / rows;        // количество столбцов
    int []minRowSum = new int[rows];

    for (int i = 0; i < rows; i++)
    {  int sum = 0;
        for (int j = 0; j < columns; j++)
        {
            sum+= array[i,j];
        }
        minRowSum[i] = sum;
    }
    PrintArray(array);
    Console.WriteLine();
    Console.WriteLine($"Строка {Array.IndexOf(minRowSum, minRowSum.Min())} имеет наименьшую сумму {minRowSum.Min()}");
    Console.WriteLine("__________________________________\n");
}

int [,]MultiplyMatrix(int[,] matrix_1, int[,] matrix_2) // Задача 58: Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.
{
    int rows_1 = matrix_1.GetUpperBound(0) + 1;    // количество строк
    int columns_1 = matrix_1.Length / rows_1;        // количество столбцов

    int rows_2 = matrix_2.GetUpperBound(0) + 1;    // количество строк
    int columns_2 = matrix_2.Length / rows_2;        // количество столбцов

    if (columns_1 == rows_2)
    {
        int n = columns_1;
        int [,] result_matrix = new int [rows_1,columns_2];
        for (int i = 0; i < rows_1; i++)
        {
            for (int j = 0; j < columns_2; j++)
            {
                int cell = 0;
                for (int k = 0; k < n; k++)
                {
                    cell += matrix_1[i,k]*matrix_2[k,j];
                }
                result_matrix[i,j] = cell;
            }
            
        }
        return result_matrix;
    }

    else
    {
        Console.WriteLine("Матрицы несовместимы");
        return new int [0,0];
    }

}

void array3D(int N) // Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.
{
    int [,,] array = new int [N,N,N];
    List<int> dublicate = new List<int>();
    Random rnd = new Random();
    int value=rnd.Next(10,99);;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            for (int k = 0; k < N; k++)
            {
                while(dublicate.Contains(value))
                {
                    value=rnd.Next(10,99);
                }
                array[i,j,k] = value;
                dublicate.Add(value);
            }
        }
        
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j <N; j++)
        {
            for (int k = 0; k < N; k++)
            {
                Console.Write($"{array[i, j,k]}({i}, {j}, {k})  ");
            }
            Console.WriteLine();
        }
    }
    Console.WriteLine("__________________________________\n");

}
void SpiralArray(int N) //Напишите программу, которая заполнит спирально массив 4 на 4.
{
    int [,] array = new int[N,N];
    int iter = N/2 + N % 2; // кол-во итераций (сколько внутренних массивов в изначальном массиве), т.е. сколько раз нам нужно будет проходиться по пириметру этих внутреннихмассиввов.
    int count =0; // счетчик для значений, который будет пробегать по сторонам внутренних массивов.
    int pre_count = 0; // значение, с которого будет начинаться отсчёт в периметре нового массива
    int _n = N; // последний индекс массива
    for (int i = 0; i < iter; i++) // проходимся по всем внутренним массивам
    {
        count = 1;
        if (N==1) // но если осталась одна центральная ячейка, то заролняем её
        {
            array[i,i] = pre_count+ count;
        }
        for (int j = 0; j < _n-1-i; j++) // Проходим по стороне массива (или внутреннего массива)
        {
            // За одну проходку заполняем сразу 4 ячейки
            array[i,j+i] = pre_count + count;
            array[j+i,_n-1] = pre_count +N-1 + count;
            array[_n-1,_n-1-j] = pre_count +2*N-2+count;
            array[_n-1-j,i] = pre_count + 3*N-3 +count; 
            count++; 
        }
       pre_count+= 4*(N-1);
        _n= _n-1;
        N=N-2;      
    }
    PrintArray<int>(array);
}

Console.WriteLine("Задание 1 :");
SortArray(RandomArray(4,3));

Console.WriteLine("Задание 2 :");
MinSumArray(RandomArray(3,5));

Console.WriteLine("Задание 3 :");
int [,] matrix_1 = RandomArray(5,3);
int [,] matrix_2 = RandomArray(3,4);
PrintArray<int>(matrix_1);
PrintArray<int>(matrix_2);

Console.WriteLine("Результат произведения :");
PrintArray<int>( MultiplyMatrix(matrix_1, matrix_2));

Console.WriteLine("____________________________________________________");


Console.WriteLine("Задание 4 :");
array3D(4);

Console.WriteLine("Задание 5 :");
SpiralArray(5);

    