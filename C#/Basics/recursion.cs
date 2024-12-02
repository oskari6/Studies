using System;
using System.Data;
using System.Text.RegularExpressions;
using System.Collections.Generic;

namespace MyApp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int>() { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            PrintNumbers(numbers, 100);
        }
        public static void PrintNumbers(List<int> numbers, int limit)
        {
            List<string> results = new List<string>();
            CreateExpressions(numbers, 1, numbers[0].ToString(), results);
            foreach(string expression in results)
            {
                double result = EvaluateExpression(expression);
                if (result == limit)
                {
                    string print = AddSpacesAroundOperators(expression); // spaces between
                    Console.WriteLine(print + " = 100"); 
                }
            }
        }
        static void CreateExpressions(List<int> numbers, int index, string current, List<string> results)
        {
            if (index == numbers.Count)
            {
                results.Add(current);
                return;
            }
            // +
            CreateExpressions(numbers, index + 1, current + "+" + numbers[index], results);
            // -
            CreateExpressions(numbers, index + 1, current + "-" + numbers[index], results);
            //  ""
            CreateExpressions(numbers, index + 1, current + numbers[index].ToString(), results);
        }
        static double EvaluateExpression(string expression)
        {
            DataTable table = new DataTable();
            object result = table.Compute(expression, string.Empty);
            return Convert.ToDouble(result);
        }
        static string AddSpacesAroundOperators(string input)
        {
            string pattern = @"(\+|\-|\*|\/)";
            string replacement = " $1 ";
            string result = Regex.Replace(input, pattern, replacement);
            return result;
        }
    }
}