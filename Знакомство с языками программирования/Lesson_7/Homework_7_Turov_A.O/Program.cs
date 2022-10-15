double [,] RandomArray (int rows, int columns) // Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.
{
    Random rnd = new Random();
    double [,] array = new double [rows,columns];
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j <columns; j++)
        {

            array[i,j] = Convert.ToDouble(rnd.Next(-1000, 1000))/100;
            

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

double Cell(double [,] array) // Задача 50. Напишите программу, которая на вход принимает позиции элемента в двумерном массиве, и возвращает значение этого элемента или же указание, что такого элемента нет.
{
    int rows = array.GetUpperBound(0) + 1;    // количество строк
    int columns = array.Length / rows;        // количество столбцов

    string? input;
    bool result;

    Console.Write("Row = ");
    input = Console.ReadLine();
    result = int.TryParse(input, out var input_row);
    Console.WriteLine();

    Console.Write("Column = ");
    input = Console.ReadLine();
    result = int.TryParse(input, out var input_column);
    Console.WriteLine();
    if (input_row*input_column > 0 && input_column<columns && input_row<rows)
    {
        return array[input_row, input_column];
    }
    else
    {
        Console.WriteLine("Таких позиций нет");
        return 0;
    }
    
}

void AverageOfColums(double [,] array )   // Задача 52. Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.
{
    int rows = array.GetUpperBound(0) + 1;    // количество строк
    int columns = array.Length / rows;        // количество столбцов

    double[] averages = new double [columns];

    for (int j = 0; j <columns; j++)
    {
        double sum =  0;
        for (int i = 0; i < rows; i++)
        {
            sum+=array[i,j];
        }
        averages[j] = sum/rows;
    }
            Console.WriteLine("[" + string.Join(", ", averages)+ "]");
}

PrintArray<double>(RandomArray(4,5));

double [,] array_1 = RandomArray(3,6);
PrintArray<double>(array_1);
Console.WriteLine(Cell(array_1));




double [,] array_2 = RandomArray(4,5);
PrintArray<double>(array_2);
AverageOfColums(array_2);