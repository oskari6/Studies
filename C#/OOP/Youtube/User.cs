using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp2
{
    public abstract class User
    {
        public User()
        {
            Console.WriteLine("User being created");//default constructor
        }
        public User(string firstName, string lastName) //custom constructor
        {
            FirstName = firstName;
            LastName = lastName;
        }
        public bool Verified { get; set; } = false;
        public string FullName
        {
            get
            {
                return FirstName + " " + LastName;
            }
        }
        public string FirstName { get; } //remove set if you dont want these to be changed
        public string LastName { get; set; } //this too, to get read only properties
        public virtual void HelloToConsole() //virtual also in front of public, same
        {
            Console.WriteLine("Hi, my name is: " + FullName);
        }
    }
}
