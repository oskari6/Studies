import java.util.Arrays;
import java.util.Scanner;

public class Basics {

    public static void main(String[] args) { //method
        System.out.println("What is your name?");

        //type identifier = new type();
        Scanner scanner = new Scanner(System.in);
        String name = scanner.nextLine();

        System.out.println("Hello " + name);

        String string = new String("This is a string");
        String easier = "Wow, that was easy!" + string;
        System.out.println(string + " :) ");
        System.out.println(easier);

        int x = 5; //primitive
        Integer y = 5; //object (5 is autoboxed)

        System.out.println(x);
        System.out.println(y);

        String[] grades = new String[1];
        System.out.println(Arrays.deepToString(grades)); //check array in arrays
        Arrays.parallelSort(grades); //large arrays
    }
    public String x = new String("hello");
}

//primitive types

//statically typed = variables are given data types up front
//dynamically typed = variables do not have data types
//literals - the value
//expression - evaluates to a value
//comment
//class - contains everything - has members
//methods - do something
//arguments - What you pass to a method
//parameters - Variable to store arguments (part of definition)
//statements - Telling the computer something
//properties - store something
//access modifier (public) - Who can use?
//static - No instance of class is needed
//object - instance of a class