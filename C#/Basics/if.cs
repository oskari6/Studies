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
            //leap year
            if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0))
            {
                Console.WriteLine("Vuosi on karkausvuosi");
            }
            else
            {
                Console.WriteLine("Vuosi ei ole karkaus vuosi");
            }

            /*1. Toteuta ohjelma, joka pyytää käyttäjää syöttämään etunimensä.
            Mikäli käyttäjän nimen pituus on suurempi kuin 5 merkkiä,
            ohjelma tulostaa tekstin "pitkä nimi". Muutoin ohjelma tulostaa tekstin "lyhyt nimi".

            Lisätehtävä: Jos vastaa Joni, pitää tulostaa paras nimi!!!
            Lisälisätehtävä: Jos kolmas kirjain on k, tulostetaan lopuksi teksti "3. kirjain on k"
            Lisälisälisätehtävä: Jos käyttäjä vastaa suoraan enterillä, kysy uudestaan*/

            while (true)
            {
                Console.Write("Anna etunimesi: ");
                string firstName = Console.ReadLine().ToLower();
                string favName = "Oskari";

                favName = favName.ToLower();

                if (string.IsNullOrEmpty(firstName)) //checks for nulls
                {
                    Console.WriteLine("Laiton vastaus: ");
                }
                else
                {
                    if (firstName.Length > 5)
                    {
                        Console.WriteLine("Pitkä nimi");
                    }
                    else
                    {
                        Console.WriteLine("Lyhyt nimi");
                    }

                    if (firstName == favName)
                    {
                        Console.WriteLine("Paras nimi");
                    }
                    if (firstName.Length > 3 && firstName[2] == 'k')
                    {
                        Console.WriteLine("3. kirjain on k");
                    }
                }
            }
            /*Kirjoita ohjelma, joka laskee kuinka monta vokaalia annetussa merkkijonossa/stringissä on."*/

            Console.Write("Anna pokemonin nimi: ");
            string pokemon = Console.ReadLine()?? "0".ToLower();

            int count = 0;

            for (int i = 0; i < pokemon.Length; i++)
            {
                
                string vowels = pokemon[i].ToString();
                if ("aeiouy".Contains(vowels))
                {
                    Console.Write(pokemon[i]);
                    count++;
                }
            }
            Console.WriteLine();
            Console.WriteLine("Vokaalit: " + count);
        }
    }
}