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
        //tulostus 2 riviä poistaen niin ei tule Anna numero linea.
        public void tulostus()
        {
            while (true)
            {
                Console.WriteLine("Anna numero2: ");
                int number = int.Parse(Console.ReadLine());
                Console.SetCursorPosition(0, Console.CursorTop - 2);

                // Clear the line by writing whitespace
                Console.WriteLine(new string(' ', Console.WindowWidth));

                // Move the cursor back to the beginning of the line
                Console.SetCursorPosition(0, Console.CursorTop - 1);
                if (number == 12345)
                {
                    Console.WriteLine(number);
                    break;
                }
                else
                {
                    continue;
                }
            }
        }
        static void Main(string[] args)
        {
            
        }
    }
}