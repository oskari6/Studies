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
            /*"Vanhan tarun mukaan Vietnamin pääkaupungin Hanoin temppeliin asetettiin maailman alussa pronssilevy, 
            * jossa on pystyssä kolme timanttista neulaa. Jokainen neuloista on kyynärän korkuinen ja yhtä paksu kuin kimalaisen ruumis. 
            * Yhteen näistä neuloista pinottiin torniksi 64 erikokoista kultaista kiekkoa suuruusjärjestykseen, suurin alimmaksi.

            Tätä kutsuttiin Hanoin torniksi.

            Temppelin papit siirtävät tauotta kiekkoja neulasta toiseen. 
            Temppelin muuttumattomien lakien mukaan kiekkoja saa siirtää vain yhden kerrallaan, eikä suurempi kiekko koskaan saa joutua pienemmän päälle. 
            Lopulta koko torni on saatava siirrettyä ensimmäiseltä timanttineulalta viimeiselle, ja tarun mukaan silloin koittaa maailmanloppu. 
            Temppelin papit eivät vielä ole saaneet tornia valmiiksi ja siirtelevät kiekkoja tälläkin hetkellä. Tuleekohan maailmanloppu pian?"

            Onneksi, me löysimme paljon pienemmän Hanoin tornin. Meiltä löytyy kolme timanttista neulaa, 
            jossa on neljä eri kokoista kultaista kiekkoa.
            Alkutilanteessa, kaikki kiekot ovat ensimmäisellä neulalla ja suuruusjärjestyksessä, jossa suurin on alin.
            Pienempi kiekko ei voi olla isomman kiekon alla.

            Kirjoita ohjelma, jossa kiekot siirretään kolmanteen neulaan.
            Tulosta myös kaikki siirrot.*/

            //painavien kiekko = 4, kevyin 1
            var needleOne = new List<int>() { 4, 3, 2, 1 };
            var needleTwo = new List<int>() { };
            var needleThree = new List<int>() { };

            for (int i = 1; i < 16; i++)
            {
                switch (i)
                {
                    case 1:
                        needleTwo.Add(1);
                        needleOne.RemoveAt(3);
                        Console.WriteLine("1. needle: " + String.Join(", ", needleOne));
                        Console.WriteLine("2. needle: " + String.Join(", ", needleTwo));
                        Console.WriteLine("3. needle: " + String.Join(", ", needleThree) + "\n");
                        continue;
                    case 2:
                        needleThree.Add(2);
                        needleOne.RemoveAt(2);
                        Console.WriteLine("1. needle: " + String.Join(", ", needleOne));
                        Console.WriteLine("2. needle: " + String.Join(", ", needleTwo));
                        Console.WriteLine("3. needle: " + String.Join(", ", needleThree) + "\n");
                        continue;
                    case 3:
                        needleThree.Add(1);
                        needleTwo.RemoveAt(0);
                        Console.WriteLine("1. needle: " + String.Join(", ", needleOne));
                        Console.WriteLine("2. needle: " + String.Join(", ", needleTwo));
                        Console.WriteLine("3. needle: " + String.Join(", ", needleThree) + "\n");
                        continue;
                    case 4:
                        needleTwo.Add(3);
                        needleOne.RemoveAt(1);
                        Console.WriteLine("1. needle: " + String.Join(", ", needleOne));
                        Console.WriteLine("2. needle: " + String.Join(", ", needleTwo));
                        Console.WriteLine("3. needle: " + String.Join(", ", needleThree) + "\n");
                        continue;
                    case 5:
                        needleOne.Add(1);
                        needleThree.RemoveAt(1);
                        Console.WriteLine("1. needle: " + String.Join(", ", needleOne));
                        Console.WriteLine("2. needle: " + String.Join(", ", needleTwo));
                        Console.WriteLine("3. needle: " + String.Join(", ", needleThree) + "\n");
                        continue;
                    case 6:
                        needleTwo.Add(2);
                        needleThree.RemoveAt(0);
                        Console.WriteLine("1. needle: " + String.Join(", ", needleOne));
                        Console.WriteLine("2. needle: " + String.Join(", ", needleTwo));
                        Console.WriteLine("3. needle: " + String.Join(", ", needleThree) + "\n");
                        continue;
                    case 7:
                        needleTwo.Add(1);
                        needleOne.RemoveAt(1);
                        Console.WriteLine("1. needle: " + String.Join(", ", needleOne));
                        Console.WriteLine("2. needle: " + String.Join(", ", needleTwo));
                        Console.WriteLine("3. needle: " + String.Join(", ", needleThree) + "\n");
                        continue;
                    case 8:
                        needleThree.Add(4);
                        needleOne.RemoveAt(0);
                        Console.WriteLine("1. needle: " + String.Join(", ", needleOne));
                        Console.WriteLine("2. needle: " + String.Join(", ", needleTwo));
                        Console.WriteLine("3. needle: " + String.Join(", ", needleThree) + "\n");
                        continue;
                    case 9:
                        needleThree.Add(1);
                        needleTwo.RemoveAt(2);
                        Console.WriteLine("1. needle: " + String.Join(", ", needleOne));
                        Console.WriteLine("2. needle: " + String.Join(", ", needleTwo));
                        Console.WriteLine("3. needle: " + String.Join(", ", needleThree) + "\n");
                        continue;
                    case 10:
                        needleOne.Add(2);
                        needleTwo.RemoveAt(1);
                        Console.WriteLine("1. needle: " + String.Join(", ", needleOne));
                        Console.WriteLine("2. needle: " + String.Join(", ", needleTwo));
                        Console.WriteLine("3. needle: " + String.Join(", ", needleThree) + "\n");
                        continue;
                    case 11:
                        needleOne.Add(1);
                        needleThree.RemoveAt(1);
                        Console.WriteLine("1. needle: " + String.Join(", ", needleOne));
                        Console.WriteLine("2. needle: " + String.Join(", ", needleTwo));
                        Console.WriteLine("3. needle: " + String.Join(", ", needleThree) + "\n");
                        continue;
                    case 12:
                        needleThree.Add(3);
                        needleTwo.RemoveAt(0);
                        Console.WriteLine("1. needle: " + String.Join(", ", needleOne));
                        Console.WriteLine("2. needle: " + String.Join(", ", needleTwo));
                        Console.WriteLine("3. needle: " + String.Join(", ", needleThree) + "\n");
                        continue;
                    case 13:
                        needleTwo.Add(1);
                        needleOne.RemoveAt(1);
                        Console.WriteLine("1. needle: " + String.Join(", ", needleOne));
                        Console.WriteLine("2. needle: " + String.Join(", ", needleTwo));
                        Console.WriteLine("3. needle: " + String.Join(", ", needleThree) + "\n");
                        continue;
                    case 14:
                        needleThree.Add(2);
                        needleOne.RemoveAt(0);
                        Console.WriteLine("1. needle: " + String.Join(", ", needleOne));
                        Console.WriteLine("2. needle: " + String.Join(", ", needleTwo));
                        Console.WriteLine("3. needle: " + String.Join(", ", needleThree) + "\n");
                        continue;
                    case 15:
                        needleThree.Add(1);
                        needleTwo.RemoveAt(0);
                        Console.WriteLine("1. needle: " + String.Join(", ", needleOne));
                        Console.WriteLine("2. needle: " + String.Join(", ", needleTwo));
                        Console.WriteLine("3. needle: " + String.Join(", ", needleThree) + "\n");
                        continue;
                    _:
                        break;
                }
            }
            Console.WriteLine("Yhteensä 15 siirtoa!");
        }
    }
}
