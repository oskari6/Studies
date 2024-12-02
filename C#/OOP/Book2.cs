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
     class Book
    {
        string name;
        readonly string writer;
        string publisher;
        private double price;
        static string theme = "";

        public string Writer
        {
            get { return writer; }
        }
        public double Price
        {
            get { return price; }
            set 
            {
                if(value > 30)
                {
                    price = value * 0.9;
                }
                else
                {
                    price = value;
                }
            }
        }

        public Book()
        {
            this.name = "";
            this.writer = "";
            this.publisher = "";
            this.Price = 0;
            theme = "";
        }

        public Book(string name, string writer, string publisher, double price, string theme)
        {
            this.name = name;
            this.writer = writer;
            this.publisher = publisher;
            this.Price = price;
            Book.theme = theme;
        }

        public void FindBook(string name, Book book)
        {
            if(name == book.name)
            {
                Console.WriteLine("Kirjan nimi: " + book.name);
                Console.WriteLine("Kirjan kirjoittaja: " + book.writer);
                Console.WriteLine("Kirjan kustantaja: " + book.publisher);
                Console.WriteLine("Kirjan hinta: " + book.price.ToString("0"));
                Console.WriteLine("Kirjan teema: " + Book.theme);
                Console.WriteLine("--------------------------");
            }
            else
            {
                Console.WriteLine("Kirjaa " + book + " ei löytynyt");
                Console.WriteLine("--------------------------");

            }
        }

        public static void ChangeTheme(string name)
        {
            Book.theme = name;
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            Book bookOne = new Book("kirja 1", "kirjailija 1", "kustantaja 1", 31, "tieto");
            Book bookTwo = new Book("kirja 2", "kirjailija 2", "kustantaja 2", 10.1, "romaani");

            bookOne.FindBook("kirja 1", bookOne);
            bookTwo.FindBook("kirja 2", bookTwo);
            Book.ChangeTheme("scifi");
            bookOne.FindBook("kirja 1", bookOne);
            bookTwo.FindBook("kirja 2", bookTwo);
            
            Console.WriteLine("Kirjailija ominaisuus: " + bookOne.Writer);
            Console.WriteLine("Kirjailija ominaisuus: " + bookTwo.Writer);
        }
    }
}