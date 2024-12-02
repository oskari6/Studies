import java.util.Scanner;
import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;

public class arrays2 {
    public static void main(String[] args) {
        int[] grades1 = {1,2,3,72,5};
        int[] grades2 = {1,2,3,72,5};
        //String[] grades = new String[5];
        //Arrays.fill(grades1, ""); //fills array, empty strings

        if(grades1 == grades2) { //doesnt work
            System.out.println("equal");
        }

        if(grades1.equals(grades2)) { //doesnt work

        }

        System.out.println(grades1 + " " + grades2);

        List<String> testing = Arrays.asList(grades1);

        if(Arrays.equals(grades1, grades2)) { //this works, doesnt check if it is the exact same array
            System.out.println("equals finally");
        }
        //Arrays.sort(grades); //Arrays.parallelSort(grades); large arrays
        //System.out.println(Arrays.toString(grades));
    }
}


