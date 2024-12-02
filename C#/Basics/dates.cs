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
            /*Kirjoita ohjelma, joka ottaa vastaan käyttäjän syötteenä syntymäpäivän. 
            * Tässä pitää harjoitella päivämäärän ottamista syötteenä, oletetaan että käyttäjä syöttää vain päivän ja kuukauden.
            Ohjelma laskee, kuinka monta päivää on käyttäjän syntymäpäivään. Jos syntymäpäivä on tänään, ohjelma onnittelee käyttäjää. 
            Jos syntymäpäivästä on kulunut alle viikko, ohjelma antaa myöhästyneet onnittelut.
            Tulostukset käyttäjäystävällisenä.*/

            Console.Write("Anna syntymäpäiväsi muodossa, päivä kuukausi : ");
            string input = Console.ReadLine() ?? "0";
            string[] numbers = input.Split(' ');

            DateTime date = new DateTime(2024, int.Parse(numbers[1]), int.Parse(numbers[0]));
            TimeSpan untilBirthday = Birthday(date);
            int days = untilBirthday.Days;

            if(days == 0)
            {
                Console.WriteLine("Syntymäpäiväsi on tänään!");

            }
            else if(days < 0 && days >= -7)
            {
                Console.WriteLine("Syntymäpäiväsi oli " + Math.Abs(days) + " päivää sitten.");
                Console.WriteLine("Myöhästyneet onnittelut!");
            }
            else if(days < -7)
            {
                TimeSpan spanTwo = date - DateTime.Today;
                int daysTwo = Math.Abs(spanTwo.Days);
                int newDays = 366 - Math.Abs(daysTwo) - 1;
                Console.WriteLine("Syntymäpäivääsi on " + newDays + " päivää..");
            }
            else
            {
                Console.WriteLine("Syntymäpäivääsi on " + days + " päivää..");
            }
        }
        public static TimeSpan Birthday(DateTime birthday)
        {
            DateTime today = DateTime.Now;
            TimeSpan difference = birthday - today;
            
            return difference;
        }
    }
}