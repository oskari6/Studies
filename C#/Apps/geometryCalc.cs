using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Switch
    {
        static void Main(string[] args)
        {
            /*Toteuta VIDEOIDEN 3 esimerkin ja  C#-prujun sivulta 32 alkavien esimerkkien pohjalta 
            * valikko-pohjainen konsolisovellus, joka osaa laskea ympyrän pinta-alan (annetaan säde), 
            * nelikulmion pinta-alan (annetaan leveys ja korkeus), 
            * sekä kolmion pinta-alan (annetaan kanta ja korkeus). 
            * Pinta-alojen laskukaavat joudut etsimään itse. Se on osa tehtävää smile

            Eli ohjelman valikko voisi näyttää esimerkiksi seuraavalta:
            *****************************************
                1. Ympyrän pinta-ala
                2. Nelikulmion pinta-ala
                3. Kolmion pinta-ala
                L  Lopetus
            *****************************************/

            //kysytään kunnes päätetään että peli on ohi
            while(true)
            {   //kokeillaan ohjelmaa ja jos tulee virheitä syötöissä tai muissa niin annetaan virhe viesti ja aloitetaan alusta
                try
                {   //tyhjennetään konsoli selkeyden vuoksi
                    Console.Clear();
                    Console.WriteLine("*****************************************");
                    Console.WriteLine("      1. Ympyrän pinta-ala");
                    Console.WriteLine("      2. Nelikulmion pinta-ala");            //graafinen valikko konsolille
                    Console.WriteLine("      3. Kolmion pinta-ala");
                    Console.WriteLine("      L  Lopetus");
                    Console.WriteLine("*****************************************");
                    string input = Console.ReadLine(); //luetaan syöte 1

                    if (input.Equals("1"))  //ympyrän toimenpiteet
                    {
                        Console.Write("Mikä on ympyrän säde (cm): ");
                        double.TryParse(Console.ReadLine(), out double radius); //jos vastaus ei sopiva niin arvoksi tulee nolla
                        double circleArea = Math.PI * radius * radius;
                        Console.WriteLine("Ymyprän pinta-ala on: " + circleArea);
                        Console.Write("Haluatko aloittaa alusta? paina \"Y\"): ");
                        string redo = Console.ReadLine();
                        if (redo.Equals("Y"))   //kysytään joka kierroksella halutaanko jatkaa
                        {
                            continue;
                        }
                        else
                        {
                            Console.WriteLine("Et painanut Y:tä, poistutaan..");
                            break;
                        }
                    }
                    if (input.Equals("2"))  //nelikulmion toimenpiteet
                    {
                        Console.Write("Mikä on nelikulmion pituus ja korkeus (cm), erota välilyönnillä: ");
                        string inputTwo = Console.ReadLine();
                        string[] dimensions = inputTwo.Split(" "); //otetaan kaksi lukua yhdellä kerralla, säilötään taulukkoon ja parsitaan doubleksi
                        double.TryParse(dimensions[0], out double height);
                        double.TryParse(dimensions[1], out double width);

                        double rectangleArea = height * width;
                        Console.WriteLine("Nelikulmion pinta-ala on: " + rectangleArea);
                        Console.Write("Haluatko aloittaa alusta? paina \"Y\"): ");
                        string redo = Console.ReadLine();
                        if (redo.Equals("Y"))
                        {
                            continue;
                        }
                        else
                        {
                            Console.WriteLine("Et painanut Y:tä, poistutaan..");
                            break;
                        }
                    }
                    if (input.Equals("3"))  //kolmion toimenpiteet
                    {
                        Console.Write("Mikä on kolmion kannan ja korkeuden pituus (cm), erota välilyönnillä: ");
                        string inputThree = Console.ReadLine();
                        string[] dimensionsTwo = inputThree.Split(" "); //sama säilömis taktiikka
                        double.TryParse(dimensionsTwo[0], out double widthTwo);
                        double.TryParse(dimensionsTwo[1], out double heightTwo);

                        double triangleArea = (widthTwo * heightTwo) / 2;
                        Console.WriteLine("Kolmion pinta-ala on: " + triangleArea);
                        Console.Write("Haluatko aloittaa alusta? paina \"Y\"): ");
                        string redo = Console.ReadLine();
                        if (redo.Equals("Y"))
                        {
                            continue;
                        }
                        else
                        {
                            Console.WriteLine("Et painanut Y:tä, poistutaan..");
                            break;
                        }
                    }
                    if (input.Equals("L"))
                    {
                        Console.Write("Lopetetaan.. näkemiin!");
                        break;
                    }
                } catch(Exception error)
                {
                    Console.WriteLine("Jokin meni pieleen.. Annoitko luvut oikein?");
                    break;
                }
            }
        }
    }
}
