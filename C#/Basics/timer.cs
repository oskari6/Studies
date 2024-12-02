using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Timers;
using System.IO;
using System.Diagnostics;

namespace TimerApp
{   //toinen app
    public static void Timer(int difficultyInt)//ajastin kesken
    {
        string timerAppPath = @"C:\Temp\Code - C#\TimerApp\bin\Debug\TimerApp.exe";
        string difficulty = difficultyInt.ToString();

        string tempFilePath = Path.Combine(Path.GetTempPath(), "difficulty.txt");
        File.WriteAllText(tempFilePath, difficulty);

        ProcessStartInfo startInfo = new ProcessStartInfo()
        {
            FileName = timerAppPath,
            Arguments = tempFilePath,
            UseShellExecute = true,
        };

        Process.Start(startInfo);
    }
    //timer app
    class Timer
    {
        private static int remainingTimeInSeconds;
        private static System.Timers.Timer timer;

        static void Main(string[] args)
        {
            string tempFilePath = args[0]; // args[0] is the path to the temporary file passed as argument
            string difficultyLevel = File.ReadAllText(tempFilePath);

            int difficulty = 1;
            SetTimer(difficulty);

            Console.WriteLine("Sinulla on vain rajallinen aika suorittaa peli läpi, pidä kiirettä!, aika vaikuttaa pisteisiin!");
            Console.ReadKey();
        }

        public static void SetTimer(int difficulty)
        {
            switch (difficulty)
            {
                case 1:
                    remainingTimeInSeconds = 600; // 10 minutes
                    break;
                case 2:
                    remainingTimeInSeconds = 480; // 8 minutes
                    break;
                case 3:
                    remainingTimeInSeconds = 420; // 7 minutes
                    break;
                case 4:
                    remainingTimeInSeconds = 360; // 6 minutes
                    break;
                case 5:
                    remainingTimeInSeconds = 300; // 5 minutes
                    break;
                default:
                    remainingTimeInSeconds = 60; // 1 minute
                    break;
            }

            timer = new System.Timers.Timer(1000);
            timer.Elapsed += OnTimedEvent;

            timer.AutoReset = true;
            timer.Enabled = true;
        }

        static void OnTimedEvent(object source, ElapsedEventArgs e)
        {
            remainingTimeInSeconds--;

            if (remainingTimeInSeconds <= 0)
            {
                timer.Stop();
                Console.WriteLine("Time has ended!");
                Environment.Exit(0);
            }
            else
            {
                TimeSpan timeSpan = TimeSpan.FromSeconds(remainingTimeInSeconds);
                Console.Write($"\rTime remaining: {timeSpan.Minutes}:{timeSpan.Seconds:00}   ");
            }
        }
    }
}
