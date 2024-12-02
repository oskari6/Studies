using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Reflection.PortableExecutable;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace ConsoleApp1
{
    public class Program
    {
        static void Main(string[] args)
        {
            /*Kirjoita ohjelma, joka kysyy viiden mäkihyppääjän yhden kierroksen
             * hypyn mitan ja viiden tuomarin pisteet (0–20, puolen pisteenvälein),
             * tallentaa tiedot tiedostoon ja tulostaa tulostus näytölle*/
            List<double> scores = new List<double>();
            
            Dictionary<double, string> results = new Dictionary<double, string>();
            bool isTrue = true;
            while (isTrue)
            {
                Console.WriteLine("Mäkihypyn tulospalvelu");
                Console.WriteLine("----------------------");
                Console.WriteLine("1. Pisteiden syöttö");
                Console.WriteLine("2. Tulosten tulostus");
                int input = int.Parse(Console.ReadLine() ?? "0");
                Console.Clear();

                string path = "C:\\Temp\\test.txt";
                if (input == 1)
                {
                    Console.WriteLine("Pisteiden syöttö");
                    Console.WriteLine("----------------------");
                    Console.Write("Hyppääjän nimi: ");
                    string inputTwo = Console.ReadLine() ?? "0";
                    Console.Write("Hypyn pituus: ");
                    int inputThree = int.Parse(Console.ReadLine() ?? "0");
                    Console.Write("Tuomari 1: ");
                    double inputFour = double.Parse(Console.ReadLine() ?? "0");
                    scores.Add(inputFour);
                    Console.Write("Tuomari 2: ");
                    double inputFive = double.Parse(Console.ReadLine() ?? "0");
                    scores.Add(inputFive);
                    Console.Write("Tuomari 3: ");
                    double inputSix = double.Parse(Console.ReadLine() ?? "0");
                    scores.Add(inputSix);
                    Console.Write("Tuomari 4: ");
                    double inputSeven = double.Parse(Console.ReadLine() ?? "0");
                    scores.Add(inputSeven);
                    Console.Write("Tuomari 5: ");
                    double inputEight = double.Parse(Console.ReadLine() ?? "0");
                    scores.Add(inputEight);
                    Console.WriteLine("----------------------");
                    Console.WriteLine("Pisteet tallennettu!");
                    Console.Clear();
                    scores.Sort();

                    using (StreamWriter sw = File.AppendText(path))
                    {
                        sw.Write($"{inputTwo}; {inputThree};{scores[1]};{scores[2]};{scores[3]};{scores[0]};{scores[4]}");
                    }
                    continue;
                }
                else if (input == 2)
                {
                    Console.WriteLine("Tulokset");
                    Console.WriteLine("----------------------");

                    using (StreamReader sr = File.OpenText(path))
                    {
                        string line;

                        while ((line = sr.ReadLine() ?? "0") != null)
                        {
                            string[] myArray = line.Split(";");
                            try
                            {
                                List<double> scoresTwo = new List<double>();

                                scoresTwo.Add(double.Parse(myArray[1]));
                                scoresTwo.Add(double.Parse(myArray[2]));
                                scoresTwo.Add(double.Parse(myArray[3]));
                                scoresTwo.Add(double.Parse(myArray[4]));

                                double sum = 0.8 * scoresTwo[0] + (scoresTwo[1] + scoresTwo[2] + scoresTwo[3]);
                                string value = $"{myArray[0]}  {myArray[1]} metriä {myArray[2]}, {myArray[3]}, {myArray[4]} {sum} pistettä";
                                results.Add(sum ,value);
                                isTrue = false;
                            } catch (Exception ex)
                            {
                                Console.WriteLine("");
                                break;
                                isTrue = false;
                            }
                        }
                        var sortedResults = results.OrderByDescending(entry => entry.Key);
                        foreach (KeyValuePair<double, string> kvp in sortedResults)
                        {
                            Console.WriteLine(kvp.Value);
                        } 
                    }
                }
                else
                {
                    Console.WriteLine("Virhe");
                    continue;
                }
            }
        }
    }
}