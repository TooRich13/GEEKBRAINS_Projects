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
    Console.WriteLine("__________________________________\n");
}

static void Swap<T>(ref T lhs, ref T rhs)
{
    T temp;
    temp = lhs;
    lhs = rhs;
    rhs = temp;
}

void SortArray(int [,]array) // Задача 54: Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.
{
    int rows = array.GetUpperBound(0) + 1;    // количество строк
    int columns = array.Length / rows;        // количество столбцов

    for (int i = 0; i < array.Length; i++)
    {  
        for (int j = 0; j < array.Length-1; j++)
        {
            if (array[i,j]>array[i,j+1] )
            {
                Swap<int>(ref array[i,j], ref array[i,j+1]);
            }
        }
    }
}

void MinSumArray(int [,]array) // Задача 56: Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.
{
    int rows = array.GetUpperBound(0) + 1;    // количество строк
    int columns = array.Length / rows;        // количество столбцов

    int []minRowSum = new int[rows];

    for (int i = 0; i < array.Length; i++)
    {  int sum = 0;
        for (int j = 0; j < array.Length; j++)
        {
            sum+= array[i,j];
        }
        minRowSum[i] = sum;
    }
    Console.WriteLine($"Строка{Array.IndexOf(array, minRowSum.Min())} имеет наименьшую сумму {minRowSum.Min()}");
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

void SpiralArray(int N)
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

SpiralArray(5);
    