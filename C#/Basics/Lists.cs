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
            List<int> grades = new List<int>() { 5, 10, 26, 34, 26, 26, 26, 2, 23, 26, 200};
            List<int> grades2 = new List<int>() { 5, 10, 26, 34, 26, 26, 26, 2, 23, 26, 200 };

            if(grades.SequenceEqual(grades2)) //compare list items
            {
                Console.WriteLine("equals!");
            }

            for ( int i = 0; i < grades.Count; i++ ) //iterate through list
            {
                grades[i] *= 2;
                Console.WriteLine(grades[1]);
            }

            foreach(int grade in grades)
            {
                Console.WriteLine(grade);
            }
            
            //grades.Add(5);
            //grades.Add(10);

            //methods
            grades.Add(30);
            grades.Insert(2, 15);//shifts everything over
            grades.Clear();
            grades = new List<int>(); //same result
            grades.Remove(10);
            grades.RemoveAt(1);
            if(grades.Contains(80))
            {
                Console.WriteLine("found");
            }
            if(grades.IndexOf(23) == -1)
            {
                Console.WriteLine("true");
            }
            if (grades.LastIndexOf(26) == 9)
            {
                Console.WriteLine("true");
            }


            Console.WriteLine(grades[0]);

            //nested foreach loops
            List<List<int>> studentGrades = new List<List<int>>()
                {
                new List<int> { 5,10,26},
                new List<int> { 34,26,26 },
                new List<int> { 26, 2, 23,26,200 } };

            foreach(List<int> grades1 in studentGrades.ToArray())
            {
                foreach (int grade in grades1)
                {
                    Console.WriteLine(grade + "\t");
                }
                Console.WriteLine();
            }

            //same with jagged
            int[][] studentGrades1 = 
                {
                new int[] { 5,10,26},
                new int[] { 34,26,26 },
                new int[] { 26, 2, 23,26,200 } 
            };

            foreach (int[] grades1 in studentGrades1)
            {
                foreach (int grade in grades1)
                {
                    Console.WriteLine(grade + "\t");
                }
                Console.WriteLine();
                //for each works for lists and jagged arrays, 2d arrays have to be done with for loops nested
            }

            //list conversion / array conversion
            List<int> stuff = new List<int>() { 5, 60 ,3, 50};

            int[] myArr = stuff.ToArray();

            List<int> myList = studentGrades1[0].ToList();

            //reverse and sort list
            stuff.Sort();
            stuff.Reverse();

            foreach(int s in stuff)
            {
                Console.WriteLine(s);
            }
            
            /*1. Toteuta ohjelma, joka luo uuden listan annetusta listasta siten, 
             * että jokainen alkio kerrotaan kolmella (3). Huom! 
             * Ohjelman pitää toimia yhdellä tai useammalla alkiolla, esimerkissä on neljä alkiota
            Tulostus:
            Lista 1: 1, 2, 3 ja 4
            Lista 2: 3, 6, 9 ja 12
            */

            //luodaan 2 listaa, alustetaan ensimmäinen arvoilla ja toinen tyhjäksi
            List<int> myListOne = new List<int>() {1, 2, 3, 4};
            List<int> myListTwo = new List<int>();

            //kerrotaan jokainen 1 listan arvo 3:lla ja lisätään toiseen listaan linq methodilla
            myListOne.ForEach(num => myListTwo.Add(num * 3));
            //displayataan tulokset
            Console.Write("1. Lista: ");
            myListOne.ForEach(num => Console.Write(num + ", "));

            Console.WriteLine();

            Console.Write("2. Lista: ");
            myListTwo.ForEach(num => Console.Write(num + ", "));

                /*Toteuta ohjelma, joka luo uuden listan annetusta listasta siten, 
                * että jokainen alkio kerrotaan kolme kertaa itsellään
                Esimerkki tulostus:
                Lista 1: 1, 2, 3 ja 4
                Lista 2: 1, 8, 27 ja 64
                */

                //alustetaan 2 listaa molemmat double tyyppiä koska Math.Pow methodi ei huoli int tyyppiä
                List<double> myListOne = new List<double>() { 1, 2, 3, 4 };
                List<double> myListTwo = new List<double>();
                //käydään 1 listan alkoit läpi Math.Pow methodia korottamalla 3.een poweriin
                myListOne.ForEach(num => myListTwo.Add(Math.Pow(num, 3)));
                //displaytaan list
                Console.Write("1. Lista: ");
                myListOne.ForEach(num => Console.Write(num + ", "));

                Console.WriteLine();

                Console.Write("2. Lista: ");
                myListTwo.ForEach(num => Console.Write(num + ", "));at

            /*Toteuta ohjelma, joka luo uuden listan annetusta listasta siten, 
             * että jokaisen alkion alkuun ja loppuun lisätään #-merkki
            Esimerkki tulostus:
            Lista 1: 1, 2, 3 ja 4
            Lista 2: #1#, #2#, #3# ja #4#*/
            //alustetaan molemmat listat, toinen string tyyppiseksi koska halutaan #:t mukaan
            List<double> myListOne = new List<double>() { 1, 2, 3, 4 };
            List<string> myListTwo = new List<string>();
            //lisätään toiseen listaan alkoit #:jen kannsa
            myListOne.ForEach(num => myListTwo.Add("#" + num + "#"));
            //displaytaan list
            Console.Write("1. Lista: ");
            myListOne.ForEach(num => Console.Write(num + ", "));

            Console.WriteLine();

            Console.Write("2. Lista: ");
            myListTwo.ForEach(num => Console.Write(num + ", "));

            /*Toteuta ohjelma, joka luo uuden listan annetusta listasta siten, 
            * että jokainen alkio korvataan alkiolla, jossa alkuperäinen alkio esiintyy neljä kertaa
            Esimerkki tulostus:
            Lista 1: 1, 2, 3 ja 4
            Lista 2: 1111, 2222, 3333 ja 4444*/
            //listojen alustus, toinen tyhjä
            List<int> myListOne = new List<int>() { 1, 2, 3, 4 };
            List<int> myListTwo = new List<int>();
            //katsotaan onko numerot minkä kokoisia
            for (int i = 0; i < myListOne.Count; i++)
            {
                if (myListOne[i] >= 100)//ei mahdu
                {
                    Console.WriteLine("Taulukossa olevat luvut eivät mahdu int tietotyyppiin");
                    break;
                }
                else if (myListOne[i] >= 10)//99 asti
                {
                    myListTwo.Add(myListOne[i] * 1010101);
                }
                else//normi
                {
                    myListTwo.Add(myListOne[i] * 1111);
                }
            }
            //displaytaan list
            Console.Write("1. Lista: ");
            myListOne.ForEach(num => Console.Write(num + ", "));

            Console.WriteLine();

            Console.Write("2. Lista: ");
            myListTwo.ForEach(num => Console.Write(num + ", "));
            /*Jatka edellistä tehtävää. Ohjelma laskee lukujen keskiarvon ja poistaa listalta keskiarvoa lähimmän luvun. 
            * Tulosta listasta keskiarvo, poistettu numero ja listan sisältö. 
            Toteuta ainakin metodeilla 
            laskeKeskiarvo (keskiarvon laskeminen metodin avulla)
            etsiPoistettava (hakee listalta poistettavan numeron)*/
        static void Main(string[] args)
        {
            //tehdään lista
            List<double> myList = new List<double>();
            //kysytään arvot niin kauan kun käyttäjä haluaa
            while (true)
            {
                Console.Write("Anna numero jos et halua antaa numeroa paina enter: ");
                string input = Console.ReadLine() ?? "0";
                //jos tyhjä niin poistutaan
                if (string.IsNullOrEmpty(input))
                {
                    break;
                }
                else
                {
                    double inputConverted = double.Parse(input);
                    myList.Add(inputConverted);
                }
            }
            //tehdään muuttujat laskuoperaatioita varten
            int count = 0;
            double mean;
            double sum = 0;
            //lista läpi
            foreach (double num in myList)
            {
                count++;
                sum += num;
            }//tulostukset arvoille
            Console.WriteLine("Lista numeroista: ");
            TulostaLista(myList);
            mean = sum / count;
            Console.WriteLine($"Alkioita yhteensä: {count}");
            Console.WriteLine($"Alkioiden keskiarvo: {mean}");
            Console.WriteLine($"Minimi: {myList.Max()}");
            Console.WriteLine($"Maksimi: {myList.Min()}");
            LaskeKeskiarvo(count, sum);
            etsiPoistettava(myList, mean);
        }
        public static void TulostaLista(List<double> list)//normi tulostus
        {
            foreach (int i in list)
            {
                Console.WriteLine(i);
            }
        }
            public static void LaskeKeskiarvo(double count, double sum)//keskiarvo
            {
                double mean = sum / count;
                Console.WriteLine($"Keskiarvo on: {mean}.");
            }
            public static void etsiPoistettava(List<double> list, double mean)//poisto
            {
                double closest = list[0];//annetaan vain jokin arvo lähimmälle ei väliä mikä
                double minDif = Math.Abs(list[0] - mean);//alusteaan myös minimi ero

                for (int i = 0; i < list.Count; i++)//.count = listan pituus
                {
                    double currentDif = Math.Abs(list[i] - mean);//alustetaan ero ensimmäisellä kierroksella

                    if (currentDif < minDif)//jos pienempi
                    {
                        closest = list[i];//lähin
                        minDif = currentDif;//ja pienin
                    }
                }
                Console.WriteLine($"Poistettu numero lähinnä keskiarvoa oli: {closest}");
                list.Remove(closest);//poistoon
            }
                /*Kirjoita metodi, joka ottaa vastaan muutaman sanan lauseen ja palauttaa lauseen niin, 
                * että sanojen kirjaimet ovat aakkosjärjestyksessä. Sanojen pituudet pysyvät samoina. 
                * Metodin syötteenä otetaan vain pieniä kirjaimia, ei numeroita tai muita merkkejä.
                Esim. 𝙻𝚊𝚞𝚜𝚎𝙹𝚊𝚛𝚓𝚎𝚜𝚝𝚢𝚔𝚜𝚎𝚎𝚗("𝚖𝚊𝚝𝚒𝚗 𝚊𝚞𝚝𝚘 𝚘𝚗 𝚙𝚞𝚗𝚊𝚒𝚗𝚎𝚗"); -> "𝚊𝚒𝚖𝚗𝚝 𝚊𝚘𝚝𝚞 𝚗𝚘 𝚊𝚎𝚒𝚗𝚗𝚗𝚞𝚙"*/

                Console.Write("Anna lause: ");
                string lause = Console.ReadLine()??"0";
                LauseJärjestykseen(lause);
        }
        public static void LauseJärjestykseen(string lause)
            {
                lause = lause.ToLower();
                string[] pieces = lause.Split(' ');
                List<string> newPieces = new List<string>();

                for(int i = 0; i < pieces.Length; i++)
                {
                    newPieces.Add(pieces[i]);
                    newPieces[i] = new string(newPieces[i].OrderBy(c => c).ToArray());
                }

                foreach (string word in newPieces)
                {
                    Console.Write(word + " ");
                }
            }
    }
}