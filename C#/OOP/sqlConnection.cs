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

namespace ConsoleApp1
{
    class Auto
    {
        public string merkki;
        public int vuosimalli;
        public double hinta;
        public bool myyty;
        public int id;

        public string connectionStr = "server=localhost;database=harjoitukset;uid=root;password=;";

        public Auto(string merkki, int vuosimalli, double hinta, bool myyty, int id)
        {
            this.merkki = merkki;
            this.vuosimalli = vuosimalli;
            this.hinta = hinta;
            this.myyty = myyty;
            this.id = id;
        }

        public void TallennaTiedot()
        {
            using (MySqlConnection connection = new MySqlConnection(connectionStr))
            {
                connection.Open();
                string insertQuery = "INSERT INTO Autot VALUES (@value1, @value2, @value3, @value4, @value5)";
                using (MySqlCommand command = new MySqlCommand(insertQuery, connection))
                {
                    command.Parameters.AddWithValue("@value1", this.merkki);
                    command.Parameters.AddWithValue("@value2", this.vuosimalli);
                    command.Parameters.AddWithValue("@value3", this.hinta);
                    command.Parameters.AddWithValue("@value4", this.myyty);
                    command.Parameters.AddWithValue("@value5", this.id);

                    int rowsAffected = command.ExecuteNonQuery();

                    // Check if data insertion was successful
                    if (rowsAffected > 0)
                    {
                        Console.WriteLine("Data added.");
                    }
                    else
                    {
                        Console.WriteLine("Failed!");
                    }
                }
                connection.Close();
            }
        }

        public void HaeTiedot()
        {
            using (MySqlConnection connection = new MySqlConnection(connectionStr))
            {
                connection.Open();
                string selectQuery = "SELECT * FROM Autot WHERE id = @value1";

                using (MySqlCommand command = new MySqlCommand(selectQuery, connection))
                {
                    command.Parameters.AddWithValue("@value1", this.id);
                    using (MySqlDataReader reader = command.ExecuteReader())
                    {
                        if(reader.HasRows)
                        {
                            while(reader.Read())
                            {
                                string column1 = reader.GetString(0);
                                int column2 = reader.GetInt32(1);
                                double column3 = reader.GetDouble(2);
                                bool column4 = reader.GetBoolean(3);
                                int column5 = reader.GetInt32(4);
                                
                                Console.WriteLine($"Tiedot: {column1}, {column2}, {column3}, {column4}, {column5}.");
                            }
                        }
                        else
                        {
                            Console.WriteLine("Failed!");
                        }
                    }
                }
                connection.Close();
            }
        }

        //Tässä määritellään NaytaTiedot()-metodi.
        public void NaytaTiedot()
        {
            Console.WriteLine("\tAuton tiedot");
            Console.WriteLine("\t------------");
            Console.WriteLine("\tAuton merkki: " + merkki);
            Console.WriteLine("\tAuton vuosimalli: " + vuosimalli);
            Console.WriteLine("\tAuton hinta: " + hinta);
            Console.WriteLine("\tAuto on myyty?: " + myyty);
            Console.WriteLine("\tAuton id: " + id);
        }
    }

    class Esimerkki5_2
    {
        static void Main(string[] args)
        {
            Auto auto = new Auto("Ford", 2004, 4000.40, false, 1);

            auto.NaytaTiedot();
            auto.TallennaTiedot();
            auto.HaeTiedot();
        }
    }
}

