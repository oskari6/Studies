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
            //ternary operator
            bool b;
            int k = int.Parse(Console.ReadLine());
            b = k < 5 ? true : false;

            int arvo;
            arvo = k < 10 ? 5 : 10;
            Console.WriteLine(arvo);

            string kylmyys;
            kylmyys = k < 0 ? "on kylmä" : "ei kylmä";
            Console.WriteLine(kylmyys);

            kylmyys = k < 0 ? (k < -5 ? (k < -10 ? "ihan helkkarin kylmä" : "tosi kylmä") : "perus kylmä") : (k > 5 ? "melko kylmä" : "ei ihan niin kylmä");
            Console.WriteLine(kylmyys);

            string[] weekDays =
            {
               "Maanantai",
               "Tiistai",
               "Keskiviikko",
               "Torstai",
               "Perjantai",
               "Lauantai",
               "Sunnuntai"
            };

            int[] numero2 = new int[5];
            numero2[0]= 1;
            numero2[1] = 2;
            numero2[2] = 3;
            numero2[3] = 4;
            numero2[4] = 5;

            Console.WriteLine(weekDays[0]);
            Console.WriteLine("Viikossa on: " +  weekDays.Length + " päivää.");

            /*1. Kirjoita ohjelma, jossa alustetaan yksi kokonaisluku (int) muuttuja arvolla nolla.
            Lisää muuttujaan arvoon 5. Pyydä käyttäjältä toinen kokonaisluku.
            Tulosta molemmat muuttujat järkevästi. (Älä tulosta muuttujia yksistään vaan muodosta niistä lause).*/


            int y = 0 + 5;

            Console.Write("Anna kokonaisluku: ");
            int number = int.Parse(Console.ReadLine());

           /*2.Edellistä ohjelmaa hyödyntäen, luo merkkijono - muuttuja(string),
            jonka arvoksi tulee ehto-operaattoria(?-operaattori) hyödyntäen kahden aiemmin luodun kokonaisluku - muuttujien vertailu.
            Mikäli ohjelman ennakkoon muodostama muuttuja on suurempi, antaa ehto-operaattori merkkijono - muuttujan arvoksi:
            "Antamasi luku on pienempi!".Ja jos käyttäjän antama luku on suurempi, arvoksi tulee: "Antamasi luku on suurempi!".
            Tulosta lopuksi määritetty merkkijono - muuttuja.*/

            string x = number < y ? "Antamasi luku on pienempi!" : "Antamasi luku on suurempi!";
            Console.WriteLine(x);
            Console.ReadLine();

            /*3. Kirjoita ohjelma, joka pyytää ja lukee kokonaisluvun käyttäjältä ja käyttämällä
            ?-operaattoria tulostaa “Ei”, jos luku on 0 ja muussa tapauksessa “Jaa”.*/

            Console.Write("Anna numero: ");
            int numberTwo = int.Parse(Console.ReadLine());

            string z = numberTwo == 0 ? "Ei" : "Jaa";

            Console.WriteLine(z);

            /*4. Kirjoita ohjelma, jossa määrittelet merkkijonotyyppisen (string) muuttujan ja desimaaliluku muuttujan.
            Ohjelman pitää pyytää ja lukea opiskelijan arvosana näppäimistöltä.
            Tämän jälkeen ohjelman tulee ?-operaattoria käyttämällä alustaa merkkijono-muuttuja siten,
            että jos arvosana on alle 4, sen arvoksi tulee “Opiskelija jää luokalle.”
            ja muussa tapauksessa “Opiskelija pääse luokalta!”. Lopussa ohjelman tulee tulostaa näytölle arvosana ja merkkijono.*/

            Console.Write("Anna arvosanasi: ");
            double grade = double.Parse(Console.ReadLine());

            string decision = grade < 4 ? "Opiskelija jää luokalle." : "Opiskelija pääse luokalta!";

            Console.WriteLine("arvosanalla " + grade + ", " + decision);

            /*Tehtävä 1.Kirjoita ohjelma, jossa määrittelet vakioluettelon(enumeration) vuodenajoista,
            siten että kevät on 1, kesä on 2 ja niin edelleen.Ohjelman pitää sitten tulostaa näytölle viesti,
            joka kertoo mikä on syksyn arvo. (Kts.linkki)*/


            int myVar = (int)Months.syyskuu;
            Console.WriteLine(myVar);
            
            //next
            int number = 0 + 5;

            Console.Write("Anna kokonaisluku: ");
            int input = int.Parse(Console.ReadLine());

            string comparison = number > input ? "Antamasi luku on pienempi!" : "Antamasi luku on suurempi!";
            char sign = comparison == "antamasi luku on pienempi" ? '>' : '<';
            string checkIfSame = number == input ? "Luvut ovat yhtä suuret" : $"{number} {sign} {input} | {comparison}";
            Console.WriteLine(checkIfSame);
        }
    }
}