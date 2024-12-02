using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Switch
    {
        static void Main(string[] args)
        {
            /*Toteuta C#-prujun sivulta 36 alkavan TIETOKILPAILUN
            * tai seuraavana olevan KERTOTAULU-PELIN innoittamana näiden 
            * esimerkkien pohjalta oma tietokilpailu tai laskutaitoa 
            * (esim. yhteenlasku peli) testaava peli. 
            * Tarkemman aiheen voit valita itse.*/

            bool exit = false;
            Console.WriteLine("Hei, tervetuloa matematiikka peliin!");
            while (!exit)
            {
                try
                {
                    Console.Write("Anna 2 numeroa laskettavaksi erotettuna välilyönnillä: ");
                    string input = Console.ReadLine();
                    Console.Write("Anna operaattori jolla lasku tehdään (+, -, *, /, %): ");
                    string inputTwo = Console.ReadLine();

                    string[] numbers = input.Split(" ");
                    int.TryParse(numbers[0], out int numberOne);
                    int.TryParse(numbers[1], out int numberTwo);

                    if (inputTwo.Equals("+"))
                    {
                        int sum = numberOne + numberTwo;
                        Console.WriteLine("Numeroidesi summa on: " + sum);
                    }
                    else if (inputTwo.Equals("-"))
                    {
                        int extract = numberOne - numberTwo;
                        Console.WriteLine("Numeroidesi erotus on: " + extract);
                    }
                    else if (inputTwo.Equals("*"))
                    {
                        int multiply = numberOne * numberTwo;
                        Console.WriteLine("Numeroidesi kertolasku on: " + multiply);
                    }
                    else if (inputTwo.Equals("/"))
                    {
                        int division = numberOne / numberTwo;
                        Console.WriteLine("Numeroidesi jako on: " + division);
                    }
                    else if (inputTwo.Equals("%"))
                    {
                        int remainder = numberOne % numberTwo;
                        Console.WriteLine("Numeroidesi jakojäännös on: " + remainder);
                    }
                    else
                    {
                        Console.WriteLine("Antamasi operaattori ei ole sopiva.");
                        continue;
                    }
                } catch (Exception numberFail)
                {
                    Console.WriteLine("Et antanut numeroita ollenkaan, yritä uudelleen..");
                    continue;
                }
                

                do
                {
                    Console.WriteLine("Haluatko jatkaa (Y/n");
                    string repeat = Console.ReadLine();

                    if (repeat == "Y")
                    {
                        break;
                    }
                    else if (repeat.Equals("n"))
                    {
                        Console.WriteLine("poistutaan..");
                        exit = true;
                        break;
                    }
                    else
                    {
                        Console.WriteLine("Sopimaton syöte");
                    }
                } while (true);
                Console.Clear();
                
            }
        }
    }
}
