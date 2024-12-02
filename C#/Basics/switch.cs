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
            Console.Write("Anna viikonpäivä numerona (maanantai on 1): ");
            int dayNum = int.Parse(Console.ReadLine());

            switch (dayNum)
            {
                case 1:
                    Console.WriteLine("maanantai");
                    break;
                case 2:
                    Console.WriteLine("tiistai");
                    break;
                case 3:
                    Console.WriteLine("keskiviikko");
                    break;
                case 4:
                    Console.WriteLine("torstai");
                    break;
                case 5:
                    Console.WriteLine("perjantai");
                    break;
                case 6:
                    Console.WriteLine("lauantai");
                    break;
                case 7:
                    Console.WriteLine("sunnuntai");
                    break;
                default:
                    Console.WriteLine("numero ei ole sopiva");
                    break;
         }
        
         Console.Write("Anna arvosanasi kokonaislukuna 1-10: ");
            int grade = int.Parse(Console.ReadLine());

            switch (grade)
            {
                case 1:
                case 2:
                    Console.WriteLine($" {grade} on huono arvosana");
                    break;
                case 3:
                case 4:
                case 5:
                    Console.WriteLine($" {grade} on kohtalainen arvosana");
                    break;
                case 6:
                case 7:
                case 8:
                    Console.WriteLine($" {grade} on hyvä arvosana");
                    break;
                case 9:
                    Console.WriteLine($" {grade} on kiitettävä arvosana");
                    break;
                case 10:
                    Console.WriteLine($" {grade} on erinomainen arvosana");
                    break;
                default:
                    Console.WriteLine("arvosana minkä syötit on virheellinen");
                    break;
            }
        
        /*3. Tee ohjelma, joka lukee lämpötilan celsiusasteina ja tulostaa lämpötilan mukaan seuraavasti
            < -20              superkylmää
            -20…<-10      tosi kylmää
            -10…<-0        kylmää
            +0…<+10       viileää
            +10…<+20     normaali
            +20…+30       lämmintä
            >30                kuumaa*/
            
        while (true)
            {
                Console.Write("Anna lämpötila: ");
                double temperature = double.Parse(Console.ReadLine());

                switch (temperature)
                {
                    case < -20:
                        Console.WriteLine("super kylmää");
                        break;
                    case double i when i >= -20 && i <= -10:
                        Console.WriteLine("tosi kylmää");
                        break;
                    case double i when i >= -10 && i <= 0:
                        Console.WriteLine("kylmää");
                        break;
                    case double i when i >= 0 && i <= 10:
                        Console.WriteLine("viileää");
                        break;
                    case double i when i >= 10 && i <= 20:
                        Console.WriteLine("normaali");
                        break;
                    case double i when i >= 20 && i <= 30:
                        Console.WriteLine("lämmintä");
                        break;
                    case >30:
                        Console.WriteLine("kuumaa");
                        break;
                    default:
                        Console.WriteLine("Arvo ei ole sopiva, yritä uudelleen");
                        break;
                }
            }

            /*3. Pyydä käyttäjältä kuluvan kuukauden numero. Tee tutkinta, joka tulostaa kuukauden numeron perusteella seuraavaa:
            4 - 5: Tulostetaan sana "kevät"
            6 - 8: Tulostetaan sana "kesä"
            9 - 10: Tulostetaan sana "syksy"
            11 - 3: Tulostetaan sana "talvi"*/

            Console.WriteLine("anna kuluvan kuukauden numero: ");
            int month = int.Parse(Console.ReadLine());

            switch (month)
            {
               case 1:
               case 2:
               case 3:
               case 11:
               case 12:
                   Console.WriteLine("talvi");
                   break;
               case 4:
               case 5:
                   Console.WriteLine("kevät");
                   break;
               case 6:
               case 7:
               case 8:
                   Console.WriteLine("kesä");
                   break;
               case 9:
               case 10:
                   Console.WriteLine("syksy");
                   break;
               default:
                   Console.WriteLine("arvo ei väliltä 1-12");
                   break;
            }

            if(Console.ReadKey().Key == ConsoleKey.Multiply) //.Key keyboard input
            if (month > 10 && month <= 12 || month > 0 && month <= 3) //if statement

            /*1. Kirjoita ohjelma joka toimii nelilaskimena.
            Ohjelma pyytää kaksi lukua ja laskutoimitusta varten merkin +, -, *, /
            ja suorittaa pyydetyn laskutoimituksen. Lopuksi ohjelma kysyy jatketaanko.*/

            while (true)
            { //kysytään numerot ja tallennetaan syötteet muuttujiin
                Console.WriteLine("Anna 2 numeroa välilyönnillä erotettuna: ");
                string input = Console.ReadLine();
                Console.WriteLine("Anna laskutoimitus merkki( +, -, *, / ): ");
                string inputTwo = Console.ReadLine();

                //tehdään taulukko ja sijoitetaan saadut numerot siihen
                string[] numbers = input.Split(" ");
                double.TryParse(numbers[0], out double numberOne);
                double.TryParse(numbers[1], out double numberTwo);

                //tarkastetaan minkä laskutoimitus merkin käyttäjä antoi ja tehdään oikea laskutoimitus ja tuloste
                string result = inputTwo switch //switch expression
                {
                    "+" => $"{numberOne} + {numberTwo} = {numberOne + numberTwo}",
                    "-" => $"{numberOne} - {numberTwo} = {numberOne - numberTwo}",
                    "*" => $"{numberOne} * {numberTwo} = {numberOne * numberTwo}",
                    "/" => $"{numberOne} / {numberTwo} = {numberOne / numberTwo}",
                    _ => "sopimaton syöte"
                };
                Console.WriteLine(result);
                Console.WriteLine("paina \"Y\" jos haluat jatkaa?: ");
                string repeat = Console.ReadLine();
                if (repeat == "Y")
                {
                    continue;
                }
                break;
            }
            
            /*2. Kirjoita ohjelma, joka kysyy käyttäjältä neljän kokeen pistemäärät (0-100) ja laskee niiden keskiarvon.
            Keskiarvon perusteella ohjelma antaa käyttäjälle arvosanan seuraavilla pisterajoilla:*/

            Console.Write("Anna 4. kokeen pistemäärät erotettuna pilkulla: ");
            string input = Console.ReadLine()?? "0";
            string[] grades = input.Split(',');
            double gradeOne = double.Parse(grades[0]);
            double gradeTwo = double.Parse(grades[1]);
            double gradeThree = double.Parse(grades[2]);
            double gradeFour = double.Parse(grades[3]);

            double mean = (gradeOne + gradeTwo + gradeThree + gradeFour) / 4;

            string result = mean switch
            {
                < 39 and > 0 => $"keskiarvo {mean}: 0, hylätty",
                < 49 and > 40 => $"keskiarvo {mean}: 1, tyydyttävä",
                < 60 and > 50 => $"keskiarvo {mean}: 2, kohtalainen",
                < 75 and > 61 => $"keskiarvo {mean}: 3, hyvä",
                < 90 and > 76 => $"keskiarvo {mean}: 4, hyvä",
                < 100 and > 91 => $"keskiarvo {mean}: 5, hylätty",
                _ => "antamasi luvut eivät ole oikeita"
            };
            Console.WriteLine(result);
        }
    }
}