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
    class Kaupunki
    {
        string kaupunki;
        int asukasmäärä;
        public Kaupunki()
        {
            kaupunki = "Tuntematon";
            asukasmäärä = 0;
        }
        public Kaupunki(string kaupunki, int asukasmäärä)
        {
            this.kaupunki = kaupunki;
            this.asukasmäärä = asukasmäärä;
        }
        public void KaupunkiTiedot()
        {
            Console.WriteLine($"Kaupunki: {this.kaupunki}, asukasmäärä: {this.asukasmäärä}.");
        }
    }
    class Asukas
    {
        //attribuutit
        string nimi;
        double kengänkoko;
        Kaupunki tiedot;

        public Asukas(string nimi, double kengänkoko, Kaupunki tiedot)//muodostin
        {
            this.nimi = nimi;
            this.kengänkoko = kengänkoko;
            this.tiedot = tiedot;
        }
        public void AsukasTiedot()//tietojen tulostus oliosta
        {
            Console.WriteLine("-------------");
            Console.WriteLine($"Asukkaan nimi: {nimi}, kengännumero: {kengänkoko}");
            tiedot.KaupunkiTiedot();
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            Kaupunki ankkalinna = new Kaupunki("Ankkalinna", 10000);
            Kaupunki eiTiedossa = new Kaupunki();

            //uusi asukas
            Asukas asukasYksi = new Asukas("Aku Ankka", 38.5, ankkalinna);
            //toinen
            Asukas asukasKaksi = new Asukas("Hannu Hanhi", 40, eiTiedossa);

            //tiedot
            asukasYksi.AsukasTiedot();
            asukasKaksi.AsukasTiedot();
        }
    }
}