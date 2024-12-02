using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using classroom;
//tätä nimiavaruutta käytetty projektin läpi
namespace Personnel
{
    public class Users : IVerification //implimentataan interface tähän tiedostoon
    {   //muutamat globaalit muutujat helpottamaan vertailussa
        private const string teacher = "Opettaja";
        private const string student = "Opiskelija";
        private const string user = "Käyttäjä";
        
        //custom muodostin jossa otetaan etu ja sukunimi stringeinä argumentteihin
        public Users(string firstName, string lastName) //custom constructor
        {
            FirstName = firstName;
            LastName = lastName;
        }//getterit ja setterit niitä varten, set jos haluaa vaihtaa myöhemmin
        public string FirstName { get; set; }
        public string LastName { get; set; }
        //tervehdys viesti
        public string Output(int times = 1) //= 1 is default parameter
        {
            string message = "Hei, ";
            for (int i = 0; i < times; i++)
            {
                message += FirstName + " " + LastName;
            }
            return message;
        }
        //Tulostetaan käyttäjänimi joka on saatu etu-ja sukunimestä ja arvotaan numero perään
        public string UserName
        {
            get//vain get, ei setteriä koska haluta että voidaan muuttaa
            {
                return "Käyttäjänimesi on: " + FirstName + LastName + UserNum();
            }
        }
        //private koska miksi ei, otetaan random numero nimeen
        //random moduuli käyttäjätunnusta varten
        Random random = new Random();
        private int UserNum()
        {
            int randNum = random.Next(0, 1000);
            return (randNum);
        }
        //random moduuli salasanaa varten
        private static Random randomString = new Random();
        public string UserPassword(int length = 7) //max pituus 7
        {
            const string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"; //näistä kirjaimista
            return new string(Enumerable.Repeat(chars, length)//uusi string niistä ja toistetaan max pituuden verran charreja
                .Select(s => s[randomString.Next(s.Length)]).ToArray());//lambda expressionilla random järjestys ja suoraan taulukkoon, ja käyttöön
        }
        //annetaan status käyttäjälle
        public string Status(string status)
        {
            return "Stauksesi on: " + status;
        }
        //tervehditään oikean lailla
        public string Greeting(string status)
        {
            string result = "";
            if (status == user)
            {
                result =  "Tervetuloa kouluun!";
            }
            else if (status == student)
            {
                result = "Tervetuloa kouluun opiskelemaan!";
            }
            else if (status == teacher)
            {
                result = "Tervetuloa kouluun opettamaan!";
            }
            return result;
        }
        //annetaan työtunnit riippuen onko töissä koululla vai ei
        public string WorkHours(string status, int workDays)
        {
            string result = "";
            if(status == student)
            {
                result = $"Työtuntisi ovat {workDays * 6}.";
            }
            else if(status == teacher)
            {
                result = $"Työtuntisi ovat {workDays * 8}.";
            }
            return result;
        }
        //jos ei ole töissä tai opiskelemassa niin ei anneta mitään vielä
        public string WorkHours(bool eligibility = true)
        {
            if(!eligibility)
            {
                return "Sinulle ei ole annettu vielä työtunteja.";
            }
            return "Annoit väärän syötteen, vaihda statukseen jos et ole käyttäjä.";
        }

        //interfacen methodia käytetään hyväksi verifikaation tarkastelussa
        public void Verified(string status)
        {
            if (status == user)
            {
                Console.WriteLine("Et ole verifoitu");
            }
            else if (status == student || status == teacher)
            {
                Console.WriteLine("Olet verifioitu!");
            }
        }
    }
}
