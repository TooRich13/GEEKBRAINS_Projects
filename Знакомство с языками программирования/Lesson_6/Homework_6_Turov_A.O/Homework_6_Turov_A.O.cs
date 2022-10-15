string strArray(int [] array, List <int> tags) // Функция для вывода массива, в котором указанные значения отмечены  подчёркиванием. Принимает массив и лист тэгов, где указаны индексы значений, которые нужно подчеркнуть
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
void MoreZero ()
{
    Console.WriteLine("Введите целые числа через запятую" );
    string str =Console.ReadLine();
    int [] numbers = str.Split(new char[] {','} ).Select(x => int.Parse(x)).ToArray();
    List<int> tags = new List<int>();
    for (int i = 0; i < numbers.Length; i++)
    {
        if (numbers[i]<0)
        {
            tags.Add(i);
        }
    }
    string out_str = strArray(numbers, tags);
    Console.WriteLine(out_str + "-> " + tags.Count);

}
void IntersectionPoint() // Напишите программу, которая найдёт точку пересечения двух прямых, заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.
{
    string? input;
    bool result;
    Console.WriteLine("Введите коэфициенты для 2 прямых вида: y = k1*x + b1, y = k2*x + b2");

    Console.WriteLine("b1 = ");
    input = Console.ReadLine();
    result = double.TryParse(input, out var b1);

    Console.WriteLine("k1 = ");
    input = Console.ReadLine();
    result = double.TryParse(input, out var k1);
    
    Console.WriteLine("b2 = ");
    input = Console.ReadLine();
    result = double.TryParse(input, out var b2);

    Console.WriteLine("k2 = ");
    input = Console.ReadLine();
    result = double.TryParse(input, out var k2);

    double x = (b2-b1)/(k1-k2);
    double y = k1*x+b1;

    Console.WriteLine($"x={x}, y={y}");
}


MoreZero();
IntersectionPoint();