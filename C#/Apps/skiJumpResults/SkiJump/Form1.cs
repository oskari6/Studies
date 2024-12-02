using System.IO;
using static System.Net.Mime.MediaTypeNames;
using static System.Windows.Forms.LinkLabel;
namespace SkiJump
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        const string path = "C:\\Temp\\test.txt";

        Dictionary<double, string> results = new Dictionary<double, string>();
        public List<string> Printing()
        {
            List<string> lines = new List<string>();
            using (StreamReader sr = File.OpenText(path))
            {
                string line;
                while ((line = sr.ReadLine() ?? "0") != null)
                {
                    string[] myArray = line.Split(";");
                    try
                    {
                        List<double> scoresTwo = new List<double>();
                        List<double> scores = new List<double>();
                        scores.Add(double.Parse(myArray[2]));
                        scores.Add(double.Parse(myArray[3]));
                        scores.Add(double.Parse(myArray[4]));
                        scores.Add(double.Parse(myArray[5]));
                        scores.Add(double.Parse(myArray[6]));
                        scores.Sort();
                        string numberOne = scores[1].ToString();
                        string numberTwo = scores[2].ToString();
                        string numberThree = scores[3].ToString();

                        scoresTwo.Add(double.Parse(myArray[1]));
                        scoresTwo.Add(scores[2]);
                        scoresTwo.Add(scores[3]);
                        scoresTwo.Add(scores[4]);

                        double sum = 0.8 * scoresTwo[0] + (scoresTwo[1] + scoresTwo[2] + scoresTwo[3]);
                        string value = $"{myArray[0]}  {myArray[1]} metriä {numberOne}, {numberTwo}, {numberThree} {sum} pistettä";
                        results.Add(sum, value);
                    }
                    catch (Exception ex)
                    {
                        break;
                    }
                }

                var sortedResults = results.OrderByDescending(entry => entry.Key);
                foreach (KeyValuePair<double, string> kvp in sortedResults)
                {
                    lines.Add(kvp.Value);
                }
            }
            return lines;
        }


        private void button1_Click(object sender, EventArgs e)
        {
            using (StreamWriter txt = File.AppendText(path))
            {
                txt.Write(textBox1.Text + ";");
                txt.Write(textBox2.Text + ";");
                txt.Write(textBox3.Text + ";");
                txt.Write(textBox4.Text + ";");
                txt.Write(textBox5.Text + ";");
                txt.Write(textBox6.Text + ";");
                txt.Write(textBox7.Text);
                txt.WriteLine();
                txt.Close();
            }

            textBox1.Clear();
            textBox2.Clear();
            textBox3.Clear();
            textBox4.Clear();
            textBox5.Clear();
            textBox6.Clear();
            textBox7.Clear();

        }
        private void button2_Click(object sender, EventArgs e)
        {
            List<string> results = new List<string>();
            results = Printing();
            foreach (string result in results)
            {
                textBox10.AppendText(result + Environment.NewLine);
            }
        }
        private void button3_Click(object sender, EventArgs e)
        {
            textBox10.Clear();
        }

        private void textBox10_TextChanged(object sender, EventArgs e)
        {

        }


    }
}
