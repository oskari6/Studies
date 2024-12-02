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
            /*Toteuta ohjelma perinteistä hirsipuuta varten. Laita 10 sanaa taulukkoon, 
            * joista ohjelma arpoo sanan hirsipuu-peliä varten. Käyttäjälle näkyy sanaa 
            * varten viivat ja käyttäjälle näkyy virheiden lukumäärä väärän arvauksen 
            * jälkeen. Lopuksi onnitellaan voittajaa ja kysytään, haluaako pelaaja jatkaa.*/

            string[] words = new string[] { "uskonto", "mankeli", "rosolli", "sarveke", "alamäki", "lipasto", "ehtoisa", "liittyä", "koukuta", "tiistai" };
            Random random = new Random();

            while(true)
            {
                int randomNum = random.Next(words.Length);
                string randomWord = words[randomNum];
                Console.WriteLine(randomWord);
                string hiddenWord = "_______";
                for (int i = 0; i < 13; i++)
                {
                    Console.WriteLine("Arvattava sana:" + hiddenWord);
                    Console.WriteLine("Sinulla on " + (13 - i) + " arvausta jäljellä");
                    Console.WriteLine("Yritä arvata sana tai kirjain: ");
                    string guess = Console.ReadLine() ?? "0";

                    if (guess.Length > 1)
                    {
                        if (guess == randomWord)
                        {
                            Console.WriteLine("Voitit pelin arvasit oikean sanan " + randomWord);
                            break;
                        }
                        else
                        {
                            Console.WriteLine("Arvauksesi oli väärin");
                            Console.ReadKey();
                            Console.Clear();
                            continue;
                        }
                    }
                    else
                    {
                        int count = 0;
                        for(int j = 0; j < randomWord.Length; j++)
                        {
                            char guessChar = char.Parse(guess);
                            int index = randomWord.IndexOf(guess);
                            StringBuilder sb = new StringBuilder(hiddenWord);

                            while (index != -1)
                            {
                                sb[index] = guessChar;
                                index = randomWord.IndexOf(guess, index + 1);
                            }

                            hiddenWord = sb.ToString();
                            count++;
                            i = i - count / 7;
                            Console.Clear();
                        }

                        if (hiddenWord == randomWord)
                        {
                            Console.WriteLine("Voitit pelin arvasit oikean sanan " + randomWord);
                            break;
                        }

                        if (!randomWord.Contains(guess))
                        {
                            Console.WriteLine("Ei sisällä");
                            Console.ReadKey();
                            Console.Clear();
                            i++;
                        }
                    }
                }
                Console.Write("Haluatko pelata uudestaan? (Y/n)");
                string input = Console.ReadLine() ?? "0";

                if(input == "Y")
                {
                    Console.Clear();
                    continue;
                }
                else if(input == "n" || input != "Y") 
                {
                    Console.Clear();
                    break;
                }
            }
        }
    }
}