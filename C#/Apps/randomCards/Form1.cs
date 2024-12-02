using System.IO.Compression;
using System.Windows.Forms;

namespace WinFormsApp1
{
    public partial class Form1 : Form
    {
        private List<string> bmpFiles = new List<string>(); // List to store BMP file paths
        private Random random = new Random();
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string directoryPath = @"C:\Temp\Code - C#\randomCards\bin\card-BMPs";
            if (Directory.Exists(directoryPath))
            {
                bmpFiles.AddRange(Directory.GetFiles(directoryPath, "*.bmp"));
            }
            else
            {
                MessageBox.Show("BMP directory not found!");
                return;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            foreach (PictureBox pictureBox in Controls.OfType<PictureBox>())
            {
                if (bmpFiles.Count == 0)
                {
                    MessageBox.Show("No more BMP files left!");
                    return;
                }

                int randNum = random.Next(bmpFiles.Count);
                string bmpFile = bmpFiles[randNum];

                pictureBox.Image = Image.FromFile(bmpFile);

                bmpFiles.RemoveAt(randNum);
            }
        }
        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox3_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox4_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox5_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox6_Click(object sender, EventArgs e)
        {

        }
    }
}
