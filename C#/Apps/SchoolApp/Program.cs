using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.NetworkInformation;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Xml.Linq;
using static System.Net.Mime.MediaTypeNames;
using Personnel;

namespace classroom
{
    class Project
    {
        static void Main(string[] args)
        {
            /*Toteuta VIDEOIDEN 4 ja  C#-prujun olio-ohjelmoinnin esimerkin avulla ohjelma, 
             * joka käyttää hyväkseen vähintään yhtä oliota. 
             * Olio voi olla esimerkkien tavoin joko samassa tiedostossa ja nimiavaruudessa pääohjelman kanssa, 
             * tai voit laittaa sen myös omaan tiedostoonsa ja omaan nimiavaruuteensa, 
             * jolloin se pitää linkittää using-lauseella pääohjelmaan mukaan.*/

            /*tässä ohjelmassa on opettajia, oppilaita ja käyttäjiä keitä ei ole vielä määritelty
             Kaikki saavat käyttäjätunnukset ja salasanat sekä tiedon työtunneista, statuksesta ja ovatko he verifioitu
            Jaoin ohjelmat eri tiedostoihin jotka kaikki käyttävät yhtä nimiavaruutta. Tein myös Interfacen ja kokeilin olio
            ohjelmointia projekti mielessä ekaa kertaa joten yritin tehdä vähän kaikenlaista ja selvittää miten eri jutut toimivat.
            Debugger auttoi paljon.*/

            //mainissa tehdään vain muodostimella uusi objekti ja käytetään DoOperation methodia missä kaikki tulostukset ovat
            Operations myOperation = new Operations();
            myOperation.DoOperation();
        }
    }
}