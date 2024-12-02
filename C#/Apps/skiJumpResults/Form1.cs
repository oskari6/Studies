using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        const string path = "C:\\Temp\\test.txt";

        private void nameBox_TextChanged(object sender, EventArgs e)
        {
            using (StreamWriter sw = File.AppendText(path))
            {

            }

        }
        private void jumpBox_TextChanged(object sender, EventArgs e)
        {

        }
        
        private void pointsBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void pointsBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void pointsBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void pointsBox4_TextChanged(object sender, EventArgs e)
        {

        }

        private void pointsBox5_TextChanged(object sender, EventArgs e)
        {

        }

        private void placeBox_TextChanged(object sender, EventArgs e)
        {

        }

        private void resultsBox_TextChanged(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            button1.Visible = true;
        }
        private void button1_Click(object sender, EventArgs e)
        {
            TextWriter txt = new StreamWriter(path);
            txt.Write(nameBox.Text + ";");
            txt.Write(jumpBox.Text + ";");
            txt.Write(pointsBox1.Text + ";");
            txt.Write(pointsBox2.Text + ";");
            txt.Write(pointsBox3.Text + ";");
            txt.Write(pointsBox4.Text + ";");
            txt.Write(pointsBox5.Text);
            txt.Close();
        }
    }
}
