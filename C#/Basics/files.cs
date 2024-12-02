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
            string path = @"C:\Temp\test.txt";
            if (!File.Exists(path))
            {
                string text = "terve" + Environment.NewLine + "terveisin";
                File.WriteAllText(path, text);
            }

            string path = @"C:\Temp\index.html";
            if (!File.Exists(path))
            {
                string text = "<!DOCTYPE html>" + Environment.NewLine + "<html>" + Environment.NewLine + "<head>" + "hei"
                    + "</head>" + Environment.NewLine + "<body>" + Environment.NewLine + "</body>" + Environment.NewLine + "</html>";
                File.WriteAllText(path, text);
            }

            string path = @"C:\Temp\index.html";
            if (File.Exists(path))
            {
                string readText = File.ReadAllText(path);
                Console.WriteLine(readText);
            }

            //1. Kirjoita ohjelma, joka tallentaa seuraavan runon tiedostoon

            string path = @"C:\Temp\test.txt";
            string[] poem = {
                "Tänne jäin, tänne jäin tuska mielessäin",
                "Koska menee junia kotiinpäin?",
                "Nolla kaks kolkytkuus",
                "Nyt soi Pieksämäen asemalla blues"}; 

            File.WriteAllLines(path, poem);

            /*Kirjoita ohjelma, joka lukee edellisen tiedoston ja 
            * tulostaa runon seuraavan mallin mukaan keskitetysti:*/

            string path = @"C:\Temp\test.txt";

            string[] readText = File.ReadAllLines(path);
            Console.WriteLine(readText[0].PadLeft(150));
            Console.WriteLine(readText[1].PadLeft(145));
            Console.WriteLine(readText[2].PadLeft(141));
            Console.WriteLine(readText[3].PadLeft(147));

            /*Kirjoita ohjelma, joka kysyy käyttäjältä, kuinka monta riviä tallennetaan tiedostoon.
            Ohjelma tallentaa merkkijonoa käyttäjän antaman määrän. Voi laittaa tulostumaan lisäksi
            konsoliin.*/

            string path = @"C:\Temp\test.txt";

            Console.Write("Kuinka monta riviä tallennetaan: ");
            int.TryParse(Console.ReadLine(), out int amount);
            Console.WriteLine("----------------------------------");
            for (int i = 1; i < amount + 1; i++)
            {
                Console.WriteLine($"Tämä on {i} rivi {amount} tallennettavasta");
            }
            Console.WriteLine("----------------------------------");

            using (StreamWriter sw = File.AppendText(path))
            {
                sw.WriteLine($"Kuinka monta riviä tallennetaan: {amount}");
                sw.WriteLine("----------------------------------");
                for (int i = 1; i < amount+1; i++)
                {
                    sw.WriteLine($"Tämä on {i} rivi {amount} tallennettavasta");
                }
                sw.Write("----------------------------------");
            }

            /*4. Kirjoita ohjelma, jossa lisäät tehtävän 1 ja 2 tiedostoon toisen 
                * ”säkeistön” ja tulostat koko runon tehtävän 2 mallin mukaan*/
            string path = @"C:\Temp\test.txt";
            string[] poem = {
                "Tänne jäin, tänne jäin tuska mielessäin",
                "Koska menee junia kotiinpäin?",
                "Nolla kaks kolkytkuus",
                "Nyt soi Pieksämäen asemalla blues"};

            File.WriteAllLines(path, poem);

            string[] poemTwo = {
                "",
                "Asema on ja vähän vankilaa",
                "Kristillinen opisto josta tulvahtaa",
                "Synkkä jumalisuus",
                "Ja soi Pieksämäen asemalla blues"};

            File.AppendAllLines(path, poemTwo);

            string[] readText = File.ReadAllLines(path);

            for (int i = 0; i < readText.Length; i++)
            {
                int padding = (39 - readText[i].Length) / 2;
                Console.WriteLine(readText[i].PadLeft(150-padding));
            }

            /*Kirjoita ohjelma, joka kysyy viiden mäkihyppääjän yhden kierroksen 
            * hypyn mitan ja viiden tuomarin pisteet (0–20, puolen pisteenvälein), 
            * tallentaa tiedot tiedostoon ja tulostaa tulostus näytölle*/

            Console.Write("Anna 5-hyppääjän tämän kierroksen hypyn mitat erotettuna pilkulla (,):");
            string input = Console.ReadLine() ?? "0";
            string[] numbers = input.Split(',');

            int jumpOne = int.Parse(numbers[0]);
            int jumpTwo = int.Parse(numbers[1]);
            int jumpThree = int.Parse(numbers[2]);
            int jumpFour = int.Parse(numbers[3]);
            int jumpFive = int.Parse(numbers[4]);

            Console.Write("Anna 5-hyppääjän tämän kierroksen tuomarien tulokset erotettuna välilyönnillä:");
            string inputTwo = Console.ReadLine() ?? "0";
            string[] score = inputTwo.Split(' ');

            double scoreOne = double.Parse(score[0]);
            double scoreTwo = double.Parse(score[1]);
            double scoreThree = double.Parse(score[2]);
            double scoreFour = double.Parse(score[3]);
            double scoreFive = double.Parse(score[4]);

            string path = @"C:\Temp\test.txt";
            using (StreamWriter sw = File.AppendText(path))
            {
                sw.WriteLine("Tulokset");
                sw.WriteLine($"Hyppääjä 1: Pituus: {jumpOne}, Pisteet: {scoreOne}");
                sw.WriteLine($"Hyppääjä 2: Pituus: {jumpTwo}, Pisteet: {scoreTwo}");
                sw.WriteLine($"Hyppääjä 3: Pituus: {jumpThree}, Pisteet: {scoreThree}");
                sw.WriteLine($"Hyppääjä 4: Pituus: {jumpFour}, Pisteet: {scoreFour}");
                sw.WriteLine($"Hyppääjä 5: Pituus: {jumpFive}, Pisteet: {scoreFive}");
            }

            using (StreamReader sr = File.OpenText(path))
            {
                string s = "";
                while((s = sr.ReadLine()) != null)
                {
                    Console.WriteLine(s);
                }
            }
        }
    }
}