using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class companyObjects
    {
        internal class Employee
        {
            public string name;
            public int id;
            public string assignment;
            public double pay;

            public Employee()
            {
                this.name = name;
                this.id = id;
                this.assignment = assignment;
                this.pay = pay;
            }
            public Employee(string name, int id, string assignment, double pay)
            {
                this.name = name;
                this.id = id;
                this.assignment = assignment;
                this.pay = pay;
            }
            public Employee(Employee employee)
            {
                this.name = employee.name;
                this.id = employee.id;
                this.assignment = employee.assignment;
                this.pay = employee.pay;
            }

            public void ComparePay(Employee employee)
            {
                double difference = this.pay - employee.pay;
                if(difference < 0)
                {
                    difference = Math.Abs(difference);
                    Console.WriteLine($"Palkkasi on {difference} pienempi kuin {employee.name}");
                }
                else
                {
                    Console.WriteLine($"Palkkasi on {difference} suurempi kuin {employee.name}");
                }
                Console.WriteLine();

            }
            public void PrintDetails()
            {
                Console.WriteLine("Työntekijän nimi: " + this.name);
                Console.WriteLine("Työntekijän id: " + this.id);
                Console.WriteLine("Työntekijän työtehtävä: " + this.assignment);
                Console.WriteLine("Työntekijän palkka: " + this.pay);
                Console.WriteLine();
            }
        }
        internal class Company
        {
            public string name;
            public string address;
            public string phoneNumber;
            public double income;
            public double outlay;

            public Company()
            {
                this.name = "Ei saatavilla";
                this.address = "Ei saatavilla";
                this.phoneNumber = "";
                this.income = 0;
                this.outlay = 0;
            }
            public Company(string name, string address, string phoneNumber, double income, double outlay)
            {
                this.name = name;
                this.address = address;
                this.phoneNumber = phoneNumber;
                this.income = income;
                this.outlay = outlay;
            }
            public Company(Company company)
            {
                this.name = company.name;
                this.address = company.address;
                this.phoneNumber = company.phoneNumber;
                this.income = company.income;
                this.outlay = company.outlay;
            }

            public void Revenue(Company company)
            {
                double revenue = (this.income - this.outlay) / this.outlay * 100;

                if (revenue > 300)
                {
                    Console.WriteLine($"{this.name}: Tulot olivat {revenue.ToString("0")} %:a parempi kuin menot. Yrityksellä menee hyvin");
                }
                else if (revenue > 200 && revenue < 300)
                {
                    Console.WriteLine($"{this.name}: Tulot olivat {revenue.ToString("0")} %:a parempi kuin menot. Yrityksellä menee  tyydyttävästi");
                }
                else
                {
                    Console.WriteLine($"{this.name}: Tulot olivat {revenue.ToString("0")} %:a parempi kuin menot. Yrityksellä menee  kehnosti");
                }
            }
        }
        static void Main(string[] args)
        {
            Company company1 = new Company("company1", "road 123", "0401234567", 100000, 51000);
            Company company2 = new Company("company2", "road 321", "0401234237", 1000000, 100000);
            Company copiedCompany = new Company(company1);

            copiedCompany.Revenue(copiedCompany);
            company2.Revenue(company1);

            Employee[] myArray = new Employee[5];
            myArray[0] = new Employee("worker1", 1, "task1", 20000); 
            myArray[1] = new Employee("worker2", 2, "task2", 30000); 
            myArray[2] = new Employee("worker3", 3, "task3", 40000); 
            myArray[3] = new Employee("worker4", 4, "task4", 50000); 
            myArray[4] = new Employee("worker5", 5, "task5", 60000);

            foreach(Employee emp in myArray)
            {
                emp.PrintDetails();
            }

            for(int i = 0; i < 5; i++)
            {
                Console.Write(myArray[i].name + ": ");
                myArray[i].ComparePay(myArray[4-i]);
            }
        }
    }
}
