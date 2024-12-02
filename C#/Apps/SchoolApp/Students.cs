using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Personnel
{
    public class Students : Users //perii Usersilta kaikki
    {
        public Students(string firstName, string lastName) : base(firstName, lastName) //perus muodostin joka periytyy user classin perus muodostimelta
        {
            
        }
    }
}
