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
            /*Tee ohjelma jossa heitetään kahta noppaa. Ohjelma kertoo heittojen tulokset.
            Tavoite on saada samat numerot, ohjelma kertoo lopuksi,
            montako heittoa tarvittiin samojen heittämiseen.*/

            int i = 0;

            while (true)
            {
                Console.Write("Heitä noppa 1 painamalla enter");
                Console.ReadLine();
                Random randomOne = new Random();
                int diceOne = randomOne.Next(1, 7);
                Console.WriteLine("1. numero: " + diceOne);

                Console.Write("Heitä noppa 2 painamalla enter");
                Console.ReadLine();
                Random randomTwo = new Random();
                int diceTwo = randomTwo.Next(1, 7);
                Console.WriteLine("2. numero: " + diceTwo);

                if (diceOne == diceTwo)
                {
                    Console.WriteLine("Numerot ovat samat!");
                    break;
                }
                else
                {
                    Console.WriteLine("Numerot eivät ole samat..");
                }
                i++;
            }
        }
    }
}