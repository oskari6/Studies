using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Personnel
{
    public class Teachers : Users //perii Usersilta kaikki
    {
        public Teachers(string firstName, string lastName) : base(firstName, lastName) //perus muodostin joka periytyy user classin perus muodostimelta
        {
            
        }
    }
}
