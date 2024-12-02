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
        internal class Book
        {
            public string name;
            public string writer;
            public int id;
            public double price;
            public Book()
            {
                this.name = "Ei saatavilla";
                this.writer = "Ei saatavilla";
                this.id = 0;
                this.price = 0;
            }
            public Book(string name, string writer, int id, double price)
            {
                this.name = name;
                this.writer = writer;
                this.id = id;
                this.price = price;
            }

            public void PrintBook()
            {
                Console.WriteLine("Kirjan nimi: " + name);
                Console.WriteLine("Kirjan kirjoittaja: " + writer);
                Console.WriteLine("Kirjan id: " + id);
                Console.WriteLine("Kirjan kpl hinta: " + price);
                Console.WriteLine();
            }
            public void CompareBook(Book book)
            {
                if(this.price > book.price)
                {
                    Console.WriteLine(this.name + " on kalliimpi kuin " + book.name);
                }
            }
        }
        public static void Main(string[] args)
        {
            Book bookOne = new Book("kirja1", "Kirjoittaja1", 1, 10.5);
            /*bookOne.PrintBook();*/
            Book bookTwo = new Book();
            /*bookTwo.PrintBook();*/
            Book bookThree = new Book("kirja3", "Kirjoittaja3", 2, 12.5);

            bookThree.CompareBook(bookOne);
        }
    }
}