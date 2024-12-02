namespace Calculator
{
    public partial class Form1 : Form
    {
        double FirstNumber;
        string Operation;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void n1_Click(object sender, EventArgs e)
        {
            if (calcBox.Text == "0" && calcBox.Text != null)
            {
                calcBox.Text = "1";
            }
            else
            {
                calcBox.Text = calcBox.Text + "1";
            }
        }

        private void n2_Click(object sender, EventArgs e)
        {
            if (calcBox.Text == "0" && calcBox.Text != null)
            {
                calcBox.Text = "2";
            }
            else
            {
                calcBox.Text = calcBox.Text + "2";
            }
        }

        private void n3_Click(object sender, EventArgs e)
        {
            if (calcBox.Text == "0" && calcBox.Text != null)
            {
                calcBox.Text = "3";
            }
            else
            {
                calcBox.Text = calcBox.Text + "3";
            }
        }

        private void n4_Click(object sender, EventArgs e)
        {
            if (calcBox.Text == "0" && calcBox.Text != null)
            {
                calcBox.Text = "4";
            }
            else
            {
                calcBox.Text = calcBox.Text + "4";
            }
        }

        private void n5_Click(object sender, EventArgs e)
        {
            if (calcBox.Text == "0" && calcBox.Text != null)
            {
                calcBox.Text = "5";
            }
            else
            {
                calcBox.Text = calcBox.Text + "5";
            }
        }

        private void n6_Click(object sender, EventArgs e)
        {
            if (calcBox.Text == "0" && calcBox.Text != null)
            {
                calcBox.Text = "6";
            }
            else
            {
                calcBox.Text = calcBox.Text + "6";
            }
        }

        private void n7_Click(object sender, EventArgs e)
        {
            if (calcBox.Text == "0" && calcBox.Text != null)
            {
                calcBox.Text = "7";
            }
            else
            {
                calcBox.Text = calcBox.Text + "7";
            }
        }

        private void n8_Click(object sender, EventArgs e)
        {
            if (calcBox.Text == "0" && calcBox.Text != null)
            {
                calcBox.Text = "8";
            }
            else
            {
                calcBox.Text = calcBox.Text + "8";
            }
        }

        private void n9_Click(object sender, EventArgs e)
        {
            if (calcBox.Text == "0" && calcBox.Text != null)
            {
                calcBox.Text = "9";
            }
            else
            {
                calcBox.Text = calcBox.Text + "9";
            }
        }

        private void n0_Click(object sender, EventArgs e)
        {
            if (calcBox.Text == "0" && calcBox.Text != null)
            {
                calcBox.Text = "0";
            }
            else
            {
                calcBox.Text = calcBox.Text + "0";
            }
        }

        private void nC_Click(object sender, EventArgs e)
        {
            calcBox.Text = "0";
        }

        private void nPoint_Click(object sender, EventArgs e)
        {
            calcBox.Text = calcBox.Text + ","; //pakko olla , ei voi olla .
        }

        private void nSum_Click(object sender, EventArgs e)
        {
            FirstNumber = Convert.ToDouble(calcBox.Text);
            calcBox.Text = "0";
            Operation = "+";
        }

        private void nSub_Click(object sender, EventArgs e)
        {
            FirstNumber = Convert.ToDouble(calcBox.Text);
            calcBox.Text = "0";
            Operation = "-";
        }

        private void nMulti_Click(object sender, EventArgs e)
        {
            FirstNumber = Convert.ToDouble(calcBox.Text);
            calcBox.Text = "0";
            Operation = "*";
        }

        private void nDiv_Click(object sender, EventArgs e)
        {
            FirstNumber = Convert.ToDouble(calcBox.Text);
            calcBox.Text = "0";
            Operation = "/";
        }

        private void nEquals_Click(object sender, EventArgs e)
        {
            double SecondNumber;
            double Result;

            SecondNumber = Convert.ToDouble(calcBox.Text);

            if (Operation == "+")
            {
                Result = (FirstNumber + SecondNumber);
                calcBox.Text = Convert.ToString(Result);
                FirstNumber = Result;
            }
            if (Operation == "-")
            {
                Result = (FirstNumber - SecondNumber);
                calcBox.Text = Convert.ToString(Result);
                FirstNumber = Result;
            }
            if (Operation == "*")
            {
                Result = (FirstNumber * SecondNumber);
                calcBox.Text = Convert.ToString(Result);
                FirstNumber = Result;
            }
            if (Operation == "/")
            {
                if (SecondNumber == 0)
                {
                    calcBox.Text = "Cannot divide by zero";
                }
                else
                {
                    Result = (FirstNumber / SecondNumber);
                    calcBox.Text = Convert.ToString(Result);
                    FirstNumber = Result;
                }
            }
        }
    }
}
