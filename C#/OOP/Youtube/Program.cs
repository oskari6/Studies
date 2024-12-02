using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using ConsoleApp2.Properties;

namespace ConsoleApp2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Program myProgram = new Program(); //this is a constructor
            myProgram.DoSomething(); //invoking a method
        }

        public void DoSomething()
        {
            Student me = new Student("Jingle", "gyro"); //custom constructor invocation
            //me.FirstName = "Jingle"; this is read only so it cannot be singed to
            me.Verified = true; //some classes could have default verification or when creating user this could be hit
            //Console.WriteLine(me.FullName);
            me.HelloToConsole(); //using the custom method we did earlier in another class

            Italk you = new Student("first", "last"); //interface invocation
            ((Student)you).Test//casting a class to access methods

            //Student you = new Student(); //if you delete the default constuctor you cant use this anymore

            //Teacher you = new Teacher();
            //you.FirstName = "Sally";

            //List<User> users = new List<User>() { me, you }; //we can now iterate through the names in a list

            //foreach (User u in users) //best way to go through a list
            //{
            //    u.HelloToConsole();
            //}
            Program myProgram = new Program();
            myProgram.Print(); //organizing other methods to instances like Print()

            Person person = new Person();
            person.FirstName = "Oskari";
            person.LastName = "Sulkakoski";

            //Console.WriteLine(person.getFullName()); //method
            //Console.WriteLine(person.FullName); //property
            //Console.ReadLine();
            Console.WriteLine("What do you think the name is?");
            string fullNameGuess = Console.ReadLine();

            Console.WriteLine("Second guess?");
            string fullNameGuess2 = Console.ReadLine();

            if (person.FullName == fullNameGuess) //java person.FullName.Equals("Oskari Sulkakoski")
            {
                Console.WriteLine("You got the name! You win");
                Console.ReadLine();
            } else if (person.FullName == fullNameGuess2)
            {
                Console.WriteLine("You got the name! you get 1/2 points");
                Console.ReadLine();
            }
            else
            {
                Console.WriteLine("Youre a dissapointment");
                Console.ReadLine();
            }
        }
    }
}
