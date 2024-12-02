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
class Esimerkki6_8
{
    static void Main(string[] args)
    {
        //Tässä luodaan asiakas-olio, joka on instanssi  
        //Sovellus.Kayttoliittyma.Asiakas-luokasta. Huomaa, 
        //että luokan nimi joudutaan merkitsemään 
        //nimiavaruuksien kautta. 
        Sovellus.Kayttoliittyma.Asiakas asiakas = new
        Sovellus.Kayttoliittyma.Asiakas("Sara");

        //Tässä kutsutaan TarkistaAsiakas()-metodi.
        asiakas.TarkistaAsiakas("Susan");

        //Tässä kutsutaan taas TarkistaAsiakas()-metodi uudella 
        //parametrin arvolla.
        asiakas.TarkistaAsiakas("Sara");

        //Tässä luodaan yhteys-olio, joka on instanssi 
        //Sovellus.Tietokantayhteys.AvaaYhteys-luokasta.
        Sovellus.Tietokantayhteys.AvaaYhteys yhteys = new
        Sovellus.Tietokantayhteys.AvaaYhteys();
        Console.WriteLine("Loppu");
        Console.ReadLine();
    }
}

