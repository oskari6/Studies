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
            /*6. Tee ohjelma joka tulostaa konsolille seuraavanlaisen kuvion. Käytä for-toistorakennetta.

            *
            **
            ***
            ****
            *****
            ******
            *******
            ******** */

            for (int i = 0; i < 8; i++)
            {
                for (int j = 0; j < i; j++)
                {
                    Console.Write("*");
                }
                Console.WriteLine();
            }

            //7. Muuta tehtävää 6 siten, että ohjelma tulostaa niin monta riviä,
            //kun käyttäjä haluaa, maksimi on yhdelle riville sopiva merkkimäärä

            while(true)
            {
                Console.Write("Kuinka monta riviä haluat tulostaa: ");
                int.TryParse(Console.ReadLine(), out int amount);

                if (amount > 120)
                {
                    Console.WriteLine("Liian paljon, anna uusi arvo");
                    continue;
                }
                else
                {
                    for (int i = 0; i < amount; i++)
                    {
                        for (int j = 0; j < i; j++)
                        {
                            Console.Write("*");
                        }
                        Console.WriteLine();
                    }
                }
            }

            //fibonacci sequence
            int x = 0;
            int y = 1;
            int z = 0;

            for(int i = 0; i < 20; i++)
            {
                z = x + y; //kahden edellisen summa
                Console.WriteLine(z); //esitys
                x = y; //seuraava numero sarjassa
                y = z; //toisen summattavan numeron arvon muunto
            }
            /*2.Kirjoita ohjelma, jossa määrittelet int-tyyppiä olevan taulukon, 
            jonka koko on 10.Alusta taulukko for-toistolauseella sekä parillisilla että parittomilla luvuilla.
            Laske tämän jälkeen taulukossa olevien parittomien lukujen summa.
            Vihje: continue-lauseella pääset toistolauseen kierrosten yli*/

            //tehdään taulukko
            int[] myArray = new int[10];
            //tuodaan taulukon täyttöä varten random moduuli
            Random random = new Random();

            //täytetään taulukko random numeroilla
            for (int i = 0; i < myArray.Length; i++)
            {
                int randNum = random.Next(1, 20);
                myArray[i] = randNum;
            }

            //muuttuja parittomien laskemiselle
            int count = 0;

            //näytetään taulukon arvot
            Console.WriteLine("Taulukon numerot:");
            //käydään taulukon arvot läpi
            for (int i = 0; i < myArray.Length; i++)
            {
                Console.WriteLine(myArray[i]);
                //jos ei ole jakojäännös 0 on pariton ja lasketaan muutujaan
                if (myArray[i] % 2 != 0)
                {
                    count++;
                }
                else
                {//jos ei pariton niin seuraava iteraatio
                    continue;
                }
            }//esitetään tulos
            Console.WriteLine("parittomien määrä: " + count);

            /*3.Kirjoita ohjelma, joka pyytää käyttäjältä ylärajan luvun ja tulostaa alkuluvut(prime numbers), jotka ovat sitä pienempiä tai joka on yhtä suuri kuin se itse.
            Vihje: Alkuluku on positiivinen kokonaisluku, joka on jaollinen vain ykkösellä ja
            itsellään.*/

            //kysytään raja
            Console.Write("Anna isoin luku, johon asti haluat tietää alkuluvut: ");
            int.TryParse(Console.ReadLine(), out int limit);
            //tehdään taulukko numeroilla jotka ylettyy rajaan asti, 
            int[] numbers = new int[limit + 1];

            //koska 1 ei ole alkuluku
            for(int i = 2; i < numbers.Length; i++)
            {
                numbers[i]= i;
            }
            //katsotaan jokainen luku läpi yksi kerrallaan onko kantaluku
            for (int i = 2; i <= limit; i++)
            {   //tehdään muuttuja jossa oletetaan että luku on kantaluku
                bool isPrime = true;
                //tehdään toinen looppi jossa tarkastetaan ulomman loopin arvot taulukon arvojen kanssa
                for(int j = 2; j < i; j++) 
                {   //jos jakojäännöstä ei jää, ei luku voi olla kantaluku -> hylky
                    if(i % numbers[j] == 0)
                    {
                        isPrime = false;
                        break;
                    }
                }//jos on niin se tulostetaan muuttujan avulla
                if (isPrime)
                {
                    Console.WriteLine(i);
                }
            }
            /*4.Kirjoita ohjelma, joka tulostaa näytölle 20 lukua seuraavasta sarjasta.
            Vihje: lukuun ottamatta ensimmäistä lukua, jokainen luku on itseään edeltävien lukujen summa. 
            Ensimmäisen luvun perusteella voit laskea kaikki muut luvut. 1, 1, 2, 4, 8, 16, …*/

            int num = 1;
            Console.WriteLine(1);

            for (int i = 1; i < 20; i++)
            {
                Console.WriteLine(num);
                num = num * 2;
            }
        }
    }
}