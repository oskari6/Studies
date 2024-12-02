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
            /*Fantasia-pizzaan kuuluu neljä vapaavalinnaista täytettä.
            Luo ohjelma, jossa käyttäjä voi pyytää 2-4 vapaavalinnaista täytettä pizzaansa.
            Hae pizzan täytteet taulukosta.
            Palauta koodi ja kuvankaappaus konsolista, 
            jossa käyttäjä saa neljä täytettä uuteen pizzaansa.*/
            Random random = new Random();

            string[] toppings = new string[] {"tonnikala", "pepperoni", "salami", "kinkku", "ananas", "anjovis", "rucola", "prosciutto", "sardiini" };
            string order = "";
            for(int i = 0; i < 4; i++)
            {
                Console.WriteLine("Saatavilla olevat täytteet: ");
                Array.ForEach(toppings, n => Console.WriteLine(n + " "));
                Console.Write("Tämän hetkiset täytteet: " + order);
                Console.WriteLine();
                Console.WriteLine("Anna Fantasia pizzan täyte, jos et halua lisää täytteitä paina enter");
                Console.WriteLine("Jos haluat random täytteet kirjoita: random ");
                Console.Write("Anna täytteet: ");
                string input = Console.ReadLine()??"0".ToLower();
                
                if(input == "random")
                {
                    int randOne = random.Next(toppings.Length);
                    int randTwo = random.Next(toppings.Length);
                    int randThree = random.Next(toppings.Length);
                    int randFour = random.Next(toppings.Length);
                    order = toppings[randOne] + " " +  toppings[randTwo] + " " + toppings[randThree] + " " + toppings[randFour];
                    break;
                }
                if (input == "")
                {
                    break;
                }
                else
                {
                    for(int j = 0; i < toppings.Length; j++)
                    {
                        if (j == toppings.Length && input != toppings[toppings.Length - 1])
                        {
                            Console.Clear();
                            Console.WriteLine("Antamasi täyte ei löydy valikoimastamme.");
                            Console.ReadKey();
                            i--;
                            break;
                        }
                        if (input.Equals(toppings[j]))
                        {
                            order = order + toppings[j] + " ";
                            break;
                        }
                        else
                        {
                            continue;
                        }
                    }
                }
                Console.Clear();
            }
            Console.WriteLine("Haluamasi täytteet ovat: " + order);
        }
    }
}