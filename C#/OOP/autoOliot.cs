using System;
using System.Collections;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Net.Mail;
using System.Security.Policy;
using System.Text;
using System.Threading.Tasks;
using static System.Runtime.InteropServices.JavaScript.JSType;
using System.IO;
using static System.Net.Mime.MediaTypeNames;
using static System.Reflection.Metadata.BlobBuilder;
using System.Reflection;

namespace ConsoleApp1
{
    public class Program
    {
        public static void Main(string[] args)
        {
            class Auto
            {
                //Seuraavassa määritellään luokan attribuutit. 
                public string omistaja;
                public string merkki;
                public string väri;
                public int vuosimalli;
                public decimal hinta;
                public bool myyty;
                public double autonHinta;
                public bool katsastus;

                public void KuukausiMaksu(int kuukaudet)
                {
                    double price = this.autonHinta;
                    int iteration = 1;
                    for (; kuukaudet > 0; kuukaudet--)
                    {
                        double maksu = price / kuukaudet;
                        double withTax = maksu + (price * 1.02 - price);
                        Console.Write("Kuukausi erä " + iteration +": " + withTax.ToString("0.0") + " euroa.");
                        Console.WriteLine();
                        price = price - withTax;
                        iteration++;
                    }
                }

                public void AlustaTiedot(string omistaja, string merkki, string väri, int vuosimalli,
                decimal hinta, bool myyty, double autonHinta, bool katsastus)
                {
                    this.omistaja = omistaja;
                    this.merkki = merkki;
                    this.väri = väri;
                    this.vuosimalli = vuosimalli;
                    this.hinta = hinta;
                    this.myyty = myyty;
                    this.autonHinta = autonHinta;
                    this.katsastus = katsastus;
                }

                //Seuraavassa määritellään VertaaMalli()-metodi, jolla 
                //auton vuosimallia tarkistetaan. Huomaa, että koska 
                //luokan attribuutti on samanniminen kuin metodin parametri
                //vuosimalli, luokan attribuutti erotetaan 
                //this-operaattorilla.
                public string VertaaMalli(int vuosimalli)
                {
                    if (this.vuosimalli > vuosimalli)
                        return
                        "Auto on " + vuosimalli + " vuosimallia uudempi!";
                    else
                        return
                        "Auto ei ole " + vuosimalli + " vuosimallia uudempi!";
                }

                //Tässä määritellään NaytaTiedot()-metodi, joka tulostaa
                //luokan attribuutien arvot näytölle.
                public void NaytaTiedot()
                {
                    System.Console.WriteLine("Omistajan " + omistaja + " auton tiedot");
                    System.Console.WriteLine("------------");
                    System.Console.WriteLine("Auton merkki: " + merkki);
                    Console.WriteLine("Auton väri on " + väri);
                    System.Console.WriteLine("Auton vuosimalli: " +
                    vuosimalli);
                    System.Console.WriteLine("Auton hinta: " + hinta);
                    System.Console.WriteLine("Auto on myyty?: " + myyty);
                }
                public void Katsastus(bool katsastus, string katsastusPvm)
                {
                    DateTime compareTo = DateTime.Parse(katsastusPvm);
                    DateTime now = DateTime.Parse("5/3/2024");

                    TimeSpan timeDiff = now.Subtract(compareTo);
                    int days = timeDiff.Days;

                    if(this.vuosimalli > 2020)
                    {
                        if (katsastus)
                        {
                            Console.WriteLine("Autoa ei pidä katsastaa");
                            Console.WriteLine("Seuraava katsastus: " + (730 - days) + " päivän päästä.");
                        }
                        else
                        {
                            Console.WriteLine("Auto pitää katsastaa");
                            Console.WriteLine("Katsastus pvm oli: " + days + " päivää sitten.");
                        }
                    }
                    else
                    {
                        if (katsastus)
                        {
                            Console.WriteLine("Autoa ei pidä katsastaa");
                            Console.WriteLine("Seuraava katsastus: " + days + " päivän päästä.");
                        }
                        else
                        {
                            Console.WriteLine("Auto pitää katsastaa");
                            Console.WriteLine("Katsastus pvm oli: " + days + " päivää sitten.");
                        }
                    }
                }
            }

            class OOP1
            {
                static void Main(string[] args)
                {
                    Auto auto = new Auto();
                    Console.Write("Anna auton tiedot (nimi, merkki, väri, vuosi, hinta, status, hinta2, katsastus-status) erota välilyönnillä: ");
                    string input = Console.ReadLine()?? "0";
                    string[] details = input.Split(' ');

                    auto.AlustaTiedot(details[0], details[1], details[2], int.Parse(details[3]), decimal.Parse(details[4]), bool.Parse(details[5]), double.Parse(details[6]), bool.Parse(details[7]));

                    auto.NaytaTiedot();

                    Console.WriteLine(auto.VertaaMalli(2010));

                    auto.KuukausiMaksu(12);
                    auto.Katsastus(bool.Parse(details[7]), "1/1/2024");
                }
            }
        }
    }
}