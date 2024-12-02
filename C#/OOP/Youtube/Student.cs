using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp2
{
    public class Student : User, Italk //iplmenets the Italk interface
    {

        public Student() //default constructor
        {
            Console.WriteLine("Creating object");
        }

        //base comes from the User level constuctor since removing set doesnt allow us to create it here
        public Student(string firstName, string lastName) : base(firstName, lastName)//custom constructor
        {
            
        }

        public int Test { get; set; } //interface creation on a higher clas level

        public override void HelloToConsole()
        {
            Console.WriteLine("Hi, I'm a student, my name is " + FullName.ToUpper());
        }
    }
}
