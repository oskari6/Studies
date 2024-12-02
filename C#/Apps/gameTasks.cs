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
using MySql.Data.MySqlClient;
using Google.Protobuf.WellKnownTypes;

namespace ConsoleApp1
{
    class User
    {
        public List<string> actions = new List<string>() {"find", "kill", "save", "travel", "build"};
        public string rare = "boss-fight";
        public List<string> target1 = new List<string>() {"enemy", "animal", "prisoner"};
        public List<string> target2 = new List<string>() {"on foot", "on boat" };
        public string target3 = "house";
        public List<int> amount = new List<int>(50);
        public List<string> location = new List<string>() {"city x", "city y", "city z", "city b", "city a", };

        public void Amount()
        {
            for (int num = 1; num <= 51; num++)
            {
                amount.Add(num);
            }
        }

        public void Randomizer()
        {
            Random random = new Random();
            int rareTask = random.Next(100);
            if(rareTask == 1)
            {
                Console.WriteLine("Olet päässyt boss-fightiin");
                Console.WriteLine("Tehtävä: tapa boss");
                Console.WriteLine("3-kertaa");
                Console.WriteLine("Kohteessa: " + location[4]);
            }
            else
            {
                Console.WriteLine("Arvotaan toimintaa..");
                Console.ReadKey();
                int n1 = random.Next(actions.Count());
                if (actions[n1].Equals("find") || actions[n1].Equals("kill") || actions[n1].Equals("save"))
                {
                    Console.WriteLine("Tehtävä: " + actions[n1]);

                    Console.WriteLine("Arvotaan kohdetta..");
                    Console.ReadKey();
                    int n2 = random.Next(target1.Count());
                    Console.WriteLine("Kohde: " + target1[n2]);

                    Console.WriteLine("Arvotaan määrää..");
                    Console.ReadKey();
                    Amount();
                    int n3 = random.Next(amount.Count());
                    Console.WriteLine(amount[n3] + " kertaa.");

                    Console.WriteLine("Arvotaan kohdetta..");
                    Console.ReadKey();
                    int n4 = random.Next(location.Count());
                    Console.WriteLine("Kohteessa: " + location[n4]);
                }
                else if (actions[n1].Equals("travel"))
                {
                    Console.WriteLine("Tehtävä: " + actions[n1]);
                    Console.WriteLine("Arvotaan kohdetta..");
                    Console.ReadKey();
                    int n2 = random.Next(target2.Count());
                    Console.WriteLine("Matkustus tapa: " + target2[n2]);
                    Console.WriteLine("Arvotaan määrää..");
                    Console.ReadKey();
                    Amount();
                    int n3 = random.Next(amount.Count());
                    Console.WriteLine(amount[n3] + " kilometriä.");

                    Console.WriteLine("Arvotaan kohdetta..");
                    Console.ReadKey();
                    int n4 = random.Next(location.Count());
                    Console.WriteLine("Kohteeseen: " + location[n4]);
                }
                else
                {
                    Console.WriteLine("Tehtävä: " + actions[n1]);
                    Console.WriteLine("Arvotaan kohdetta..");
                    Console.ReadKey();
                    Console.WriteLine("Asia: " + target3);
                    Console.WriteLine("Arvotaan määrää..");
                    Console.ReadKey();
                    Amount();
                    int n3 = random.Next(amount.Count());
                    Console.WriteLine(amount[n3] + " kertaa.");

                    Console.WriteLine("Arvotaan kohdetta..");
                    Console.ReadKey();
                    int n4 = random.Next(location.Count());
                    Console.WriteLine("Lokaatioon: " + location[n4]);
                }
            }
        }
        static void Main(string[] args)
        {
            User player = new User();
            player.Randomizer();
        }
    }
}

