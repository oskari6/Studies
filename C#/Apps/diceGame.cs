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
            /*Kirjoita ohjelma, jossa heität noppaa, jonka jälkeen kone arpoo oman numeronsa. 
            * Heittoja on 5 . Jokaisen heiton jälkeen kerrotaan, kumpi. Ohjelma kertoo voittajan tai tasapelin. 
            * Jomman kumman voittaessa ohjelma kerää tilastoa taulukkoon ja tulostaa sen pelin loputtua. 
            * Ohjelma myös kysyy, halutaanko peliä jatkaa vai lopettaa.*/

            int i = 0;
            string[] results = { };
            int winCount = 0;
            int lossCount = 0;

            while (true)
            {
                Console.WriteLine("Tervetuloa peliin");
                Console.Write("Nopan heittoja on 5 ja pelaat konetta vastaan");
                Console.ReadLine();

                while (i < 5)
                {
                    Console.Write("Heitä noppa painamalla enter: ");
                    Console.ReadLine();
                    Random random = new Random();
                    int playerThrow = random.Next(1, 7);

                    Console.Write("Sait numeron: " + playerThrow + "\n");
                    Console.Write("Kone heittää nyt noppaa, paina enter nähdäksesi luku");
                    Console.ReadLine();

                    Random randomTwo = new Random();
                    int machineThrow = randomTwo.Next(1, 7);

                    Console.Write("Kone on heittänyt numeron: " + machineThrow + "\n");
                    Console.ReadLine();

                    if (machineThrow > playerThrow)
                    {
                        Console.WriteLine("Hävisit, kone heitti isomman silmäluvun, paina enter jatkaaksesi");
                        results = results.Append("L").ToArray();
                        i++;
                        lossCount++;

                        if(i < 5)
                        {
                            Console.WriteLine("Tulokset tällä hetkellä: ");
                            foreach (var value in results)
                            {
                                Console.WriteLine(value);
                            }
                            Console.ReadLine();
                        }
                    }
                    else if (machineThrow < playerThrow)
                    {
                        Console.WriteLine("Voitit, heitit isomman silmäluvun, paina enter jatkaaksesi");
                        results = results.Append("W").ToArray();
                        i++;
                        winCount++;

                        if (i < 5)
                        {
                            Console.WriteLine("Tulokset tällä hetkellä: ");
                            foreach (var value in results)
                            {
                                Console.WriteLine(value);
                            }
                            Console.ReadLine();
                        }
                    }
                    else
                    {
                        Console.WriteLine("Tasapeli, pelataan uusi kierros, paina enter jatkaaksesi");
                        Console.ReadLine();
                    }
                }
                Console.WriteLine("Tulokset: ");
                foreach (var value in results)
                {
                    Console.Write(value + ", ");
                }
                Console.ReadLine();

                if(winCount > lossCount)
                {
                    Console.WriteLine("Voitit pelin konetta vastaan!");
                }
                else
                {
                    Console.WriteLine("Hävisit konetta vastaan..");
                }

                Console.Write("Haluatko pelata uudestaan? Y/n: ");
                char newTry = char.Parse(Console.ReadLine());

                if (newTry == 'Y')
                {
                    i = 0;
                    continue;
                }
                else if (newTry == 'n')
                {
                    break;
                }
                else
                {
                    Console.WriteLine("Sopimation syöte, poistutaan pelistä");
                    break;
                }
            }
        }
    }
}