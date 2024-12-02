using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Personnel
{
    public class Operations
    {   //kaikki toiminnot tehdään täällä, pois mainin tieltä
        public void DoOperation()
        {   //tarkoitukset:
            //Koulu ohjelma
            //käyttäjät erikseen
            //tervehdys viesti
            //username
            //password
            //mikä olet, opiskelija, opettaja etc.
            //työtunnit

            //helpottamaan argumentteihin
            //Statukset
            const string teacher = "Opettaja";
            const string student = "Opiskelija";
            const string user = "Käyttäjä";

            //First User
            Users userOne = new Users("Oskari", "Sulkakoski");
            Console.WriteLine(userOne.Output());
            Console.WriteLine(userOne.UserName);
            Console.WriteLine("Salanasi on: " + userOne.UserPassword());
            Console.WriteLine(userOne.Status(user));
            Console.WriteLine(userOne.Greeting(user));
            userOne.Verified(user);
            Console.WriteLine(userOne.WorkHours(false) + "\n");

            //First Student
            Students studentOne = new Students("Opiskelija", "Yksi");
            Console.WriteLine(studentOne.Output());
            Console.WriteLine(studentOne.UserName);
            Console.WriteLine("Salanasi on: " + userOne.UserPassword());
            Console.WriteLine(studentOne.Status(student));
            Console.WriteLine(studentOne.Greeting(student));
            studentOne.Verified(student);
            Console.WriteLine(studentOne.WorkHours(student, 5) + "\n");

            //First Teacher
            Teachers teacherOne = new Teachers("Opettaja", "Yksi");
            Console.WriteLine(teacherOne.Output());
            Console.WriteLine(teacherOne.UserName);
            Console.WriteLine("Salanasi on: " + userOne.UserPassword());
            Console.WriteLine(teacherOne.Status(teacher));
            Console.WriteLine(teacherOne.Greeting(teacher));
            teacherOne.Verified(teacher);
            Console.WriteLine(teacherOne.WorkHours(teacher, 6) + "\n");
        }
    }
}
