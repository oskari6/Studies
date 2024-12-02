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
    class Asiakas
    {
        protected string nimi;
        protected int id;
        protected string osoite;

        public Asiakas()
        {
            nimi = "Tuntematon";
            id = 0;
            osoite = "";
        }

        public Asiakas(string nimi, int id, string osoite)
        {
            this.nimi = nimi;
            this.id = id;
            this.osoite = osoite;
        }

        public string AsiakkaanTiedot
        {
            get
            {
                return nimi + " " + id + " " + osoite + "\n";
            }
        }
    }

    class EtuAsiakas : Asiakas
    {
        decimal ostot;
        decimal saastot;

        public EtuAsiakas() : base()
        {
            ostot = 0m;
        }

        public EtuAsiakas(string nimi, int id, string osoite, decimal ostot, decimal saastot) :
        base(nimi, id, osoite)
        {
            this.ostot = ostot;
            this.nimi = nimi;
            this.id = id;
            this.osoite = osoite;
            this.saastot = saastot;
        }

        public decimal LaskeBonus()
        {
            if (ostot >= 500 && ostot < 1000)
                return 0.03m * ostot;
            else if (ostot >= 1000 && ostot < 1500)
                return 0.04m * ostot;
            else if (ostot >= 1500)
                return 0.05m * ostot;
            else
                return 0.0m;
        }

        public string LuokitteleAsiakas()
        {
            if (saastot >= 500 && saastot < 1000)
                return "hopea-asiakas";
            else if (saastot >= 1000 && saastot < 2000)
                return "kulta-asiakas";
            else if (saastot >= 2000)
                return "timanttiasiakas";
            else
                return "tavis";
        }
    }

    class Esimerkki7_1
    {
        static void Main(string[] args)
        {
            Asiakas asiakas1 = new Asiakas();
            Asiakas asiakas2 = new Asiakas("Dorothy", 100, "tie 1");
            EtuAsiakas etuAsiakas1 = new EtuAsiakas();
            EtuAsiakas etuAsiakas2 = new EtuAsiakas("Alfred", 200, "tie 2", 1456.40m, 1000m);

            System.Console.WriteLine("Asiakkaan tiedot: " + asiakas1.AsiakkaanTiedot);

            System.Console.WriteLine("Asiakkaan tiedot: " + asiakas2.AsiakkaanTiedot);

            System.Console.WriteLine("Etuasiakkaan tiedot: " + etuAsiakas1.AsiakkaanTiedot);

            System.Console.WriteLine("Etuasiakkaan bonus on: {0, 0:c2}", etuAsiakas1.LaskeBonus());

            System.Console.WriteLine("Etuasiakkaan tiedot: " + etuAsiakas2.AsiakkaanTiedot);

            System.Console.WriteLine("Etuasiakkaan bonus on: {0, 0:c2}", etuAsiakas2.LaskeBonus());
            string saasto = etuAsiakas2.LuokitteleAsiakas();
            Console.WriteLine("Olet " + saasto);
        }
    }
}