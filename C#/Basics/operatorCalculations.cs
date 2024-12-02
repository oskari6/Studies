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
            Console.Write("anna kk palkkasi: ");
            double salary = double.Parse(Console.ReadLine());

            Console.Write("anna veroprosenttisi: ");
            double taxRate = double.Parse(Console.ReadLine());

            double finalSalary = salary * (1 - (taxRate / 100)); //fastest way

            double taxesPaid = salary - finalSalary;

            Console.WriteLine(finalSalary.ToString("#.##"));
            Console.WriteLine("veron osuus nettopalkasta: " + taxesPaid.ToString("#.## veroja")); //## on numeroita

            Console.Write("anna tuotteen hinta: ");
            double tuotteenHinta = double.Parse(Console.ReadLine());

            Console.Write("Anna tuotteen alennus prosentti: ");
            double alennusProsentti = double.Parse(Console.ReadLine());

            double alennettuHinta = tuotteenHinta * (1 - (alennusProsentti / 100));
            double alennettuMäärä = tuotteenHinta - alennettuHinta;

            Console.Write("Tuotteen hinta alennuksen jälkeen on: " + alennettuHinta + " euroa\n");
            Console.WriteLine("Alennuksen määrä on: " + alennettuMäärä + " euroa\n");

            //3.Kirjoita ohjelma, joka lukee tuotteen hinnan, laskee siitä ALV:n joka on 24 % tuotteen hinnasta ja tulostaa näytölle ALV: n
            //määrän sekä tuotteen hinnan ilman ALV: tä.
            //Tutustu ja kokeile rahamäärien tulostuksessa rahayksikköformaattia(c tai C).

            const double Alv = 0.24;
            Console.Write("give me a price: ");
            double itemPrice = double.Parse(Console.ReadLine());

            double priceWoVat = itemPrice / (1 + Alv);
            double vatAmount = itemPrice - priceWoVat;

            Console.WriteLine("ALV:n osuus hinnasta: " + vatAmount.ToString("C"));
            Console.WriteLine("tuotteen hinta ilman ALV:ia: " + priceWoVat.ToString("C"));
        }
    }
}