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
            /*4.Kirjoita ohjelma, jossa määrittelet kaksi char-tyyppiä
            olevaa taulukkoa, joiden koko on 10.Alusta ensin taulukoiden alkiot
            mielesi mukaan ja vertaile niitä sitten keskenään siten, että ohjelma
            tulostaa ne alkiot, jotka olivat taulukossa erilaisia.*/

            //tehdään kaksi char taulukkoa
            char[] myArrayOne = new char[10] { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' };
            char[] myArrayTwo = new char[10] { 'a', 'm', 'c', 'a', 'e', 'u', 'g', 'p', 'i', 'q' };

            //käännetään kaksi taulukkoa HashSeteiksi koska niissä voi olla vain uniikkeja arvoja ja on enemmän joustavuutta
            HashSet<char> uniqueOne = new HashSet<char>(myArrayOne);
            HashSet<char> uniqueTwo = new HashSet<char>(myArrayTwo);

            //Käyttämällä .ExceptWith methodia saadaan poistettua kaikki elementit HashSetistä jotka ovat samoja
            //vertaamalla sitä ristiin alkuperäiseen toiseen char taulukkoon. Jäljelle jää vain uniikit elementit molemmista taulukoista
            uniqueOne.ExceptWith(myArrayTwo);
            uniqueTwo.ExceptWith(myArrayOne);

            //kirjoitetaan taulukkojen arvot x2
            Console.Write("1. taulukon erilaiset: ");
            foreach (char c in uniqueOne)
            {
                Console.Write(c + " ");
            }

            Console.WriteLine();
            Console.Write("2. taulukon erilaiset: ");
            foreach (char c in uniqueTwo)
            {
                Console.Write(c + " ");
            }
        }
    }
}