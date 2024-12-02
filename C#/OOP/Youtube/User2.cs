using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    public class User //you can do data validation here
    {
        string _firstName = "Oskari"; //assigned a default
        public string FullName
        {
            get
            {
                return FirstName + " " + LastName;
            }
            set
            {
                value.Split(); //for getting FullName at once without seperate first and last
                // or .Substring
            }
        }
        public string FirstName
        { get; set; }
        //property customazation
        //{
        //    get
        //    {
        //        return _firstName;
        //    }
        //    set
        //    {
        //        _firstName = value.ToLower(); //gets the value from the program
        //    }
        //}
        //get set create a private field behind scenes
        //creating a getter

        public string LastName { get; set; }
        public override string ToString()
        {
            return FullName;
        }

        public string Output() //method overloading
            {
            return "My name is " + FullName;
            }
        public string Output(int times = 1) //creating a method, = 1 is default parameter
        {
            string message = "";
            for (int i = 0; i < times; i++)
            {
                message += FirstName + " " + LastName + "\n";
                //Console.WriteLine(FirstName);
                //Console.WriteLine(LastName);
            }
            return message;

        }

        public override int GetHashCode()
        {
            //return base.GetHashCode();
            return FullName.GetHashCode();
        }

        public override bool Equals(object obj)
        {
            if(FullName == ((User) obj).FullName)
            {
                return true;
            }
            return false;
        }

        public static void PrintUser(User user)
        {
            Console.WriteLine("Static method. Print User");
            user.Output(1);
        }

        public static void PrintUsers(List<User> users)
        {
            foreach(User user in users) 
            {
                Console.WriteLine("Static method. Print User");
                Console.WriteLine(user.Output(1));

            }
        }

        public static int Find(List<User>users, string fullName)
        {
            for(int i = 0; i < users.Count; i++)
            {
                if (users[i].FullName == fullName)
                {
                    return i;
                }               
            }
            return -1; //not all code paths return a value, use this to get a flag
        }
        public static int Find(List<User> users, User user)
        {
            for (int i = 0; i < users.Count; i++)
            {
                if (users[i].Equals(user))
                {
                    return i;
                }
            }
            return -1;
        }

        public static User GetUserFromList(List<User> users, User user)
        {
            foreach (User u in users)
            {
                if (u.Equals(user))
                {
                    return u;
                }
            }
            return null;
        }
    }
}
