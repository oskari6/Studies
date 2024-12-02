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
using System.Runtime.CompilerServices;
using System.ComponentModel;

namespace ConsoleApp1
{
    class Program
    {   //alustetaan kortit maineen, jokerit valmiiksi nimetty,
        //lisäksi kaksiulotteinen lista korttipakkaa varten, ja hashsetti uniikkeja arvoja varten
        public static List<string> spades = new List<string>();
        public static List<string> hearts = new List<string>();
        public static List<string> clubs = new List<string>();
        public static List<string> diamonds = new List<string>();
        public static List<string> jokers = new List<string>() { "j1", "j2" };
        public static List<List<string>> cards = new List<List<string>>();
        public static HashSet<string> cards2 = new HashSet<string>();

        public static void FillList(List<string> suit)
        {   //listan täyttö listan nimen perusteella
            for (int i = 1; i < 13; i++)
            {
                if (suit.Equals(spades))
                {
                    suit.Add("s" + i);
                }
                if (suit.Equals(hearts))
                {
                    suit.Add("h" + i);
                }
                if (suit.Equals(clubs))
                {
                    suit.Add("c" + i);
                }
                if (suit.Equals(diamonds))
                {
                    suit.Add("d" + i);
                }
            }   //korttipakkaan lisäys
            cards.AddRange([spades, hearts, clubs, diamonds, jokers]);
        }

        public static void RandCards(int amount)
        {   //korttien arvonta
            Random random = new Random();
            int n1, n2; //arvonta numerot
                //niin kauan kun kortteja ei ole hashsetissä määrää enempää, ei ota tuplia
            while (cards2.Count < amount)
            {
                n1 = random.Next(cards.Count); // random maa
                n2 = random.Next(cards[n1].Count); // random kortti maasta, dynaaminen pituus niin jokerit toimii vaikka pieni lista
                cards2.Add(cards[n1][n2]); // lisätään arvottuihin
            }

            Console.WriteLine("Korttisi: ");    //tulostus
            foreach(string card in cards2)
            {
                Console.WriteLine(card);
            }
        }
        static void Main(string[] args)
        {   //calling
            FillList(spades);
            FillList(clubs);
            FillList(hearts);
            FillList(diamonds);
            FillList(jokers);

            RandCards(5);
        }
    }
}