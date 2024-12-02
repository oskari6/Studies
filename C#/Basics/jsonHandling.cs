using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class jsonHandling
    {
        public class JsonItem
        {
            public string nimi { get; set; }
            public string kirjailija { get; set; }
            public int id { get; set; }
            public double kappalehinta { get; set; }
            public string ISBN_tunnus { get; set; }
        }
        public class Book
        {
            public string name;
            public string writer;
            public int id;
            public double price;
            public readonly string isbn;

            public Book()
            {
                this.name = "Ei saatavilla";
                this.writer = "Ei saatavilla";
                this.id = 99;
                this.price = 0;
                this.isbn = "";
            }
            public Book(string name, string writer, int id, double price, string isbn)
            {
                this.name = name;
                this.writer = writer;
                this.id = id;
                this.price = price;
                this.isbn = isbn;
            }

        public void IsbnReader(int id)
            {
                string filePath = @"C:\Temp\isbn.json";
                string jsonRead = File.ReadAllText(filePath);

                var fileItems = JsonConvert.DeserializeObject<Dictionary<string, JsonItem>>(jsonRead);

                JsonItem found = null;
                foreach (var kvp in fileItems)
                {
                    if (kvp.Value.id == id)
                    {
                        found = kvp.Value;
                        break;
                    }
                }
                if (found != null)
                {
                    Console.WriteLine($"Name: {found.nimi}");
                    Console.WriteLine($"Author: {found.kirjailija}");
                    Console.WriteLine($"Price: {found.kappalehinta}");
                    Console.WriteLine($"ISBN: {found.ISBN_tunnus}\n");
                }
                else
                {
                    Console.WriteLine($"Kirjaa id:llä {id} ei ole.");
                }
            }

            public void IsbnWriter(Book book)
            {
                string filePath = @"C:\Temp\isbn.json";
                string jsonRead = File.ReadAllText(filePath);

                JsonItem newBook = new JsonItem
                {
                    nimi = book.name,
                    kirjailija = book.writer,
                    id = book.id,
                    kappalehinta = book.price,
                    ISBN_tunnus = book.isbn
                };
                var jsonEntry = JsonConvert.SerializeObject(newBook, Formatting.Indented);
                jsonEntry = $"{{\n  \"{book.name}{book.id}\": {jsonEntry}}}";
                jsonEntry = jsonEntry.Trim('{', '}');

                string existingJson = File.ReadAllText(filePath);

                int index = existingJson.LastIndexOf('}', existingJson.LastIndexOf('}') - 1);

                string modifiedJson = existingJson.Substring(0, index);
                modifiedJson = modifiedJson + "},";
                string appendedJson = $"{modifiedJson}{jsonEntry}  }}\n}}";

                File.WriteAllText(filePath, appendedJson);

                Console.WriteLine("Written into isbn.json\n");
            }
        }
        static void Main(string[] args)
        {
            /*OOP2 tehtävässä tehtyyn kirjaluokkaan tehdään muutama lisäys.
            Lisätään luokan kentäksi ISBN-tunnus. Tämä on oliokohtainen, vain-luku tyyppinen ominaisuus.
            Luodaan kaksi metodia;
            toinen lukee uuden kirjan tiedot olemasta olevasta tiedostosta, jossa on rakenne;

            ja toinen metodi, joka kirjoittaa tiedostoon ylläolevaan muotoon.*/

            Book bookOne = new Book("kirja1", "Kirjoittaja1", 3, 10.5, "999-999-99-9999-9");
            Book bookTwo = new Book();
            Book bookThree = new Book("kirja3", "Kirjoittaja3", 4, 12.5, "000-000-00-0000-0");
            bookThree.IsbnReader(1);
            bookThree.IsbnReader(2);

            bookOne.IsbnWriter(bookOne);
            bookTwo.IsbnWriter(bookTwo);
            bookThree.IsbnWriter(bookThree);

            bookOne.IsbnReader(bookOne.id);
            bookTwo.IsbnReader(bookTwo.id);
            bookThree.IsbnReader(bookThree.id);
        }
    }
}
