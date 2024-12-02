using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Serialization;

namespace ConsoleApp1
{
    class Oop
    {
        static void Main(string[] args)
        {
            Oop myProgram = new Oop(); //instantiate
            myProgram.doSomething();
        }

        public void doSomething()
        {
            //User user = new User();
            //user.FirstName = "Oskari";
            //user.LastName = "Sulkakoski";

            User me = new User();
            me.FirstName = "Oskari";
            me.LastName = "Sulkakoski";
            //Console.WriteLine(me.GetHashCode());

            User you = new User();
            you.FirstName = "John";
            you.LastName = "Smith";
            //Console.WriteLine(you.GetHashCode());

            List<User> users = new List<User>() { me, you};
            User search = new User();
            search.FirstName = "John";
            search.LastName = "Smith";

            //Console.WriteLine(User.Find(users, search)); //method overload

            //Console.WriteLine(me.Equals(you)); //Overridden equals method

            //Console.WriteLine(me.GetHashCode() == you.GetHashCode());

            Console.WriteLine(User.GetUserFromList(users, search));

            /*  Console.WriteLine(user);*///toString override

            //User user2 = new User();
            //user2.FirstName = "Chip";

            //User user3 = new User();
            //user3.LastName = "Bond";

            //List<User> users = new List<User>() {user, user2, user3 };
            //Console.WriteLine(User.Find(users, "Chip ")); //note the space, weaknedd in the previous code

            //Console.WriteLine(user.Output()); // how to invoke the overloaded method
            //User.PrintUser(user);

            //User user2 = new User();
            //user2.FirstName = "Chocolate";

            //List<User> users = new List<User>();
            //users.Add(user);
            //users.Add(user2);

            //User.PrintUsers(users);

            //List<string> firstNames = new List<string>() {"Oskari", "John", "Sub" };

            //List<string> lastNames = new List<string>() {"Sulkakoski", "Athon", "Scriber" };

            //List<User> users = new List<User>();

            //for(int i = 0; i < firstNames.Count; i++)
            //{
            //    User user = new User();
            //    user.FirstName = firstNames[i];
            //    user.LastName = lastNames[i];
            //    users.Add(user);
            //}

            /*User me = new User();*/
            //me.FirstName = "Oskari";
            //me.LastName = "Sulkakoski";

            //string  msg = me.Output(1);
            //Console.WriteLine(msg);
            //other way
            //Console.WriteLine(me.Output(1));

            //Console.WriteLine(me.FullName);


            //User you = new User();
            //you.FirstName = "Sub";
            //you.LastName = "Scriber";

            //List<User> users = new List <User>();
            //users.Add(me); users.Add(you);

            //foreach (User usr in users)
            //{
            //    //Console.WriteLine(usr.FullName);
            //}
            //takeUser(users[0]);
            //Console.WriteLine(users[0].FullName);

            User user = new User();
            user.FirstName = "sally";
            Test(user);
            Console.WriteLine(user.FirstName);
        }
        public void Test(User i)
        {
            //i = new User(); //now it doensnt work obviously
            i.FirstName = "Samantha";
        }
        public void takeUser(User user)
        {
            user = new User();
            user.FirstName = "Cae";
            Console.WriteLine(user.FullName);
        }
    }
}
