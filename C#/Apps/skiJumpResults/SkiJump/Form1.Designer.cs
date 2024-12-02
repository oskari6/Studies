namespace SkiJump
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            textBox1 = new TextBox();
            textBox2 = new TextBox();
            textBox3 = new TextBox();
            textBox4 = new TextBox();
            textBox5 = new TextBox();
            textBox6 = new TextBox();
            textBox7 = new TextBox();
            button1 = new Button();
            textBox10 = new TextBox();
            button2 = new Button();
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            label4 = new Label();
            label5 = new Label();
            label6 = new Label();
            label7 = new Label();
            label8 = new Label();
            button3 = new Button();
            SuspendLayout();
            // 
            // textBox1
            // 
            textBox1.Location = new Point(89, 73);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(100, 23);
            textBox1.TabIndex = 0;
            // 
            // textBox2
            // 
            textBox2.Location = new Point(89, 117);
            textBox2.Name = "textBox2";
            textBox2.Size = new Size(100, 23);
            textBox2.TabIndex = 1;
            // 
            // textBox3
            // 
            textBox3.Location = new Point(89, 161);
            textBox3.Name = "textBox3";
            textBox3.Size = new Size(100, 23);
            textBox3.TabIndex = 2;
            // 
            // textBox4
            // 
            textBox4.Location = new Point(89, 205);
            textBox4.Name = "textBox4";
            textBox4.Size = new Size(100, 23);
            textBox4.TabIndex = 3;
            // 
            // textBox5
            // 
            textBox5.Location = new Point(89, 249);
            textBox5.Name = "textBox5";
            textBox5.Size = new Size(100, 23);
            textBox5.TabIndex = 4;
            // 
            // textBox6
            // 
            textBox6.Location = new Point(89, 293);
            textBox6.Name = "textBox6";
            textBox6.Size = new Size(100, 23);
            textBox6.TabIndex = 5;
            // 
            // textBox7
            // 
            textBox7.Location = new Point(89, 337);
            textBox7.Name = "textBox7";
            textBox7.Size = new Size(100, 23);
            textBox7.TabIndex = 6;
            // 
            // button1
            // 
            button1.Location = new Point(89, 366);
            button1.Name = "button1";
            button1.Size = new Size(100, 28);
            button1.TabIndex = 9;
            button1.Text = "tallenna";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // textBox10
            // 
            textBox10.AcceptsReturn = true;
            textBox10.Location = new Point(372, 49);
            textBox10.Multiline = true;
            textBox10.Name = "textBox10";
            textBox10.ReadOnly = true;
            textBox10.Size = new Size(365, 386);
            textBox10.TabIndex = 10;
            textBox10.WordWrap = false;
            textBox10.TextChanged += textBox10_TextChanged;
            // 
            // button2
            // 
            button2.Location = new Point(89, 400);
            button2.Name = "button2";
            button2.Size = new Size(100, 28);
            button2.TabIndex = 11;
            button2.Text = "tulosta";
            button2.UseVisualStyleBackColor = true;
            button2.Click += button2_Click;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(117, 55);
            label1.Name = "label1";
            label1.Size = new Size(33, 15);
            label1.TabIndex = 12;
            label1.Text = "Nimi";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(99, 99);
            label2.Name = "label2";
            label2.Size = new Size(78, 15);
            label2.TabIndex = 13;
            label2.Text = "Hyppy pituus";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(108, 143);
            label3.Name = "label3";
            label3.Size = new Size(54, 15);
            label3.TabIndex = 14;
            label3.Text = "1. pisteet";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(108, 187);
            label4.Name = "label4";
            label4.Size = new Size(54, 15);
            label4.TabIndex = 15;
            label4.Text = "2. pisteet";
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Location = new Point(108, 231);
            label5.Name = "label5";
            label5.Size = new Size(54, 15);
            label5.TabIndex = 16;
            label5.Text = "3. pisteet";
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Location = new Point(108, 275);
            label6.Name = "label6";
            label6.Size = new Size(54, 15);
            label6.TabIndex = 17;
            label6.Text = "4. pisteet";
            // 
            // label7
            // 
            label7.AutoSize = true;
            label7.Location = new Point(108, 319);
            label7.Name = "label7";
            label7.Size = new Size(54, 15);
            label7.TabIndex = 18;
            label7.Text = "5. pisteet";
            // 
            // label8
            // 
            label8.AutoSize = true;
            label8.Font = new Font("Segoe UI", 20F);
            label8.Location = new Point(493, 9);
            label8.Name = "label8";
            label8.Size = new Size(116, 37);
            label8.TabIndex = 19;
            label8.Text = "Tulokset";
            // 
            // button3
            // 
            button3.Location = new Point(195, 400);
            button3.Name = "button3";
            button3.Size = new Size(100, 28);
            button3.TabIndex = 20;
            button3.Text = "tyhjennä";
            button3.UseVisualStyleBackColor = true;
            button3.Click += button3_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(775, 450);
            Controls.Add(button3);
            Controls.Add(label8);
            Controls.Add(label7);
            Controls.Add(label6);
            Controls.Add(label5);
            Controls.Add(label4);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(button2);
            Controls.Add(textBox10);
            Controls.Add(button1);
            Controls.Add(textBox7);
            Controls.Add(textBox6);
            Controls.Add(textBox5);
            Controls.Add(textBox4);
            Controls.Add(textBox3);
            Controls.Add(textBox2);
            Controls.Add(textBox1);
            Name = "Form1";
            Text = "Form1";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private TextBox textBox1;
        private TextBox textBox2;
        private TextBox textBox3;
        private TextBox textBox4;
        private TextBox textBox5;
        private TextBox textBox6;
        private TextBox textBox7;
        private Button button1;
        private TextBox textBox10;
        private Button button2;
        private Label label1;
        private Label label2;
        private Label label3;
        private Label label4;
        private Label label5;
        private Label label6;
        private Label label7;
        private Label label8;
        private Button button3;
    }
}
