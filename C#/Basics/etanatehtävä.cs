using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Threading.Tasks;

namespace etanatehtävä1
{
    class Program
    {
        static void Main(string[] args)
        {
            //break
            int breakCmLoss = 30;
            int oneBreak = 10;
            int twoBreaks = 20;

            //cm
            int snailPerMinute = 5;

            int bucketOne = 10;
            int bucketTwo = 60; 
            int bucketThree = 150;
            int bucketFour = 300; //2 breaks
            int bucketFive = 310; //2 breaks

            int bucketOneSnail = bucketOne / snailPerMinute;
            int bucketTwoSnail = bucketTwo / snailPerMinute;
            int bucketThreeSnail = bucketThree / snailPerMinute;
            int bucketFourSnail = +((bucketFour + breakCmLoss * 2) / snailPerMinute) + twoBreaks;
            int bucketFiveSnail = +((bucketFive + breakCmLoss * 2) / snailPerMinute) + twoBreaks;


            Console.WriteLine("10cm ämpärissä etanalla menee: " + bucketOneSnail + "-minuuttia");
            Console.WriteLine("60cm ämpärissä etanalla menee: " + bucketTwoSnail + "-minuuttia");
            Console.WriteLine("150cm ämpärissä etanalla menee: " + bucketThreeSnail + "-minuuttia");
            Console.WriteLine("300cm ämpärissä etanalla menee: " + bucketFourSnail + "-minuuttia");
            Console.WriteLine("310cm ämpärissä etanalla menee: " + bucketFiveSnail + "-minuuttia");

            Console.ReadKey();
        }
    }
}

