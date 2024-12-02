using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Seuraavassa määritellään Sovellus-nimiavaruus.
namespace Sovellus
{
    //Seuraavassa määritellään Sovellus.Kayttoliittyma-
    //nimiavaruus.
    namespace Kayttoliittyma
    {
        //Seuraavassa määritellään 
        //Sovellus.Kayttoliittyma.Asiakas-luokka.
        class Asiakas
        {
            string nimi;

            public Asiakas(string nimi)
            {
                this.nimi = nimi;
            }

            //Seuraavassa määritellään TarkistaAsiakas()-metodi, 
            //jolla asiakkaan nimeä verrataan parametrina olevaan 
            //nimeen ja sen perusteella ilmoitetaan onko asiakkaan 
            //nimi oikein vai ei.
            public void TarkistaAsiakas(string nimi)
            {
                //Tässä verrataan nimi-kentän ja nimi-parametrin 
                //arvoja sisäänrakennetulla Equals()-metodilla.
                if (this.nimi.Equals(nimi))
                    System.Console.WriteLine(nimi + " on asiakkaan oikea nimi.");
                else
                    System.Console.WriteLine(nimi + " ei ole asiakkaan oikea nimi!");
            }
        } //Sovellus.Kayttoliittyma.Asiakas-luokka loppuu tähän.
    } //Sovellus.Kayttoliittyma-nimiavaruusloppuu tähän.
} //Sovellus-nimiavaruus loppuu tähän.
