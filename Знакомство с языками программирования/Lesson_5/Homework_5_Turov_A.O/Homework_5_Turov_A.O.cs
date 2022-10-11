
int [] RandomArray (int min = 0, int max = 100, int length = -1 ) // Функция для создания случайных массивов
{
    Random rnd  = new Random();
    if (length == -1) {length = rnd.Next(4,10);}
    int [] arr = new int [length]; 
    for (int i = 0; i < length; i++)
    {
        arr[i] = rnd.Next(min,max);   
    }

    return arr;
}

string strArray(int [] array, List <int> tags) // Функция для вывода массива, в котором указанные значения отмечены  подчёркиванием
{
    const string UNDERLINE = "\x1B[4m";
    const string RESET = "\x1B[0m";
    string str_arr = "[";
    for (int i = 0; i < array.Length; i++)
    {
        if (tags.Contains(i))
        {
            str_arr+=UNDERLINE + array[i]+ RESET+ ", ";
        }
        else
        {
            str_arr += array[i] + ", ";
        }
    }
    str_arr += "]";
    return str_arr;

}

void NumberOfEven(int [] array) // Задача 1: Задайте массив заполненный случайными положительными трёхзначными числами. Напишите программу, которая покажет количество чётных чисел в массиве.
{
    int count = 0;
    List <int> tags = new List<int>() ;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] % 2 == 0) 
        {
            count++;
            tags.Add(i);
        }
    }

    //Console.WriteLine( "["+string.Join(", ",array)+"] -> "+ count);
    string str = strArray(array, tags);
    Console.WriteLine(str + "-> " +count);
}

void SumOfOddNumbers (int [] array) // Задача 2: Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на НЕЧЁТНЫХ позициях.
{
    List <int> tags = new List<int>() ;
    int sum = 0;
        for (int i = 0; i < array.Length; i++)
    {
        if (i % 2 == 0)  // В условии указаны чётные индексы, т.к. начинается массив с 0 и нечётные позиции будут иметь чётные индексы 
        {
            sum+=array[i];
            tags.Add(i);
        }
    }
    string str = strArray(array, tags);
    Console.WriteLine(str + "-> " +sum);
}

void DiffMinMax(int [] array) // Задача 3: Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.
{
    List <int> tags = new List<int>() ;

    int result = array.Max()- array.Min();

    tags.Add(Array.IndexOf(array, array.Max())); // Добавляем в лист тэгов индексы макс и мин значения, чтобы потом их подчеркнуть (Мб можно лучше, но я не знаю как)
    tags.Add(Array.IndexOf(array, array.Min()));
    

    string str = strArray(array, tags);
    Console.WriteLine(str + "-> " + result);
}

NumberOfEven(RandomArray(100,999));
SumOfOddNumbers(RandomArray());
DiffMinMax(RandomArray());
