+using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Net.Mail;
using System.Security.Policy;
using System.Text;
using System.Threading.Tasks;

namespace Syöte
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //lambda expression
            Func<int, int> square = x => x * x;
            Console.WriteLine(square(4));

            //switch expression utilizing lambda
            string result = inputTwo switch
            {
                "+" => $"{numberOne} + {numberTwo} = {numberOne + numberTwo}",
                "-" => $"{numberOne} - {numberTwo} = {numberOne - numberTwo}",
                "*" => $"{numberOne} * {numberTwo} = {numberOne * numberTwo}",
                "/" => $"{numberOne} / {numberTwo} = {numberOne / numberTwo}",
                _ => "sopimaton syöte"
            };
            Console.WriteLine(result);
                    }
    }
}