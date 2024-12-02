import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Files{
    public static void main(String[] args) {
        try
        {
                 String line = "";
                Scanner kb = new Scanner(new File ("test.txt"));
            while(kb.hasNextLine())
            {
                  line = kb.nextLine();
                 System.out.println(line);
            }
             kb.close();
        }
        catch(FileNotFoundException fnf)
        {
            System.out.println("File not found " + fnf);
        }
    }
}