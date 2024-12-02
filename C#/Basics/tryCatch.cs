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
            /*1. Palauta try-catch jossa pyydät käyttäjältä kaksi lukua, jotka jaetaan. 
            * Jos käyttäjä syöttää jakajaksi nollan, tulee ilmoitus ettei nolla voi jakaa.*/

            while(true)
            {
                try
                {   //kysytään luvut kerrallaan
                    Console.Write("Anna 2. lukua erotettuna välilyönnillä: ");
                    string input = Console.ReadLine();
                    //viedään talukkoon ja muutetaan decimaaliksi
                    string[] numbers = input.Split(' ');

                    decimal.TryParse(numbers[0], out decimal firstNumber);
                    decimal.TryParse(numbers[1], out decimal secondNumber);
                    //jako muuttujaan
                    decimal division = firstNumber / secondNumber;
                    Console.WriteLine($"{firstNumber} jaettuna {secondNumber} = {division}");
                    //jos virhe niin oikea virhe viesti
                }catch (DivideByZeroException excpetionOne)
                {
                Console.WriteLine("VIRHE: " + excpetionOne.Message);
                }
            }

            /*2. Pyydä käyttäjältä kokonaislukua. Hyväksy ja tulosta luku. 
            * Jos käyttäjä antaa jonkin muun luvun tai merkin, tulosta viesti, Ei ollut kokonaisluku.*/
            while(true)
            {
                try
                {   //kysytään luku
                    Console.Write("Anna luku: ");
                    int input = int.Parse(Console.ReadLine()); //luetaan normi parsella integeriksi
                    Console.WriteLine(input);//tulostetaan
                }
                catch(FormatException excpetionOne) //formatException koska luku ei ole oikeassa muodossa
                {
                    Console.WriteLine("VIRHE! Ei ollut kokonaisluku");
                }
            }
        }
    }
}