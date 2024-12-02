class Program
{
    public static int n1;
    public static int n2;
    public static void Numbers()
    {   //syöte
        Console.WriteLine("Anna kaksi numeroa joltain väliltä (x-y): ");
        string input = Console.ReadLine() ?? "0";
            //listaus
        string[] numbers = input.Split("-");
        n1 = int.Parse(numbers[0]);
        n2 = int.Parse(numbers[1]);

        List<int> myList = new List<int>(n2);
        //listan täyttö
        for(int i = n1; i <= n2; i++)
        {
            myList.Add(i);
        }//tulostus
        Console.WriteLine($"{Aggregation(myList)} on pienin numero, joka voidaan jakaa tasan numeroilla {input}.");
    }
    public static int Gcd(int n1, int n2)
    {
        if (n2 == 0)//jos 1-0 syötteestä
        {
            return n1;//1 palautusnumero
        }
        return Gcd(n2, n1 % n2);//muuten palautetaan method call Gcd() jossa argumentit toka luku, ja 1,2 lukujen jäännös
    }

    public static int Aggregation(List<int> numbers)
    {   //LINQ methodilla aggregatetaan kaikki listan alkoit läpi ja annetaan greatest common divisor methodiin.
        //lcm(least common multiple tulee .Aggregate((S, val) kohdasta
        return numbers.Aggregate((S, val) => S * val / Gcd(S, val));
    }

    static void Main(string[] args)
    {
        Numbers();  //calling
    }
}