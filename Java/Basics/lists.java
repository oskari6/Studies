import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

//import java.util.LinkedList;

public class lists {
    public static void main(String[] args) {
        List<Integer> grades = new ArrayList<Integer>(); //or linkedList
        grades.add(5);
        grades.add(10);
        grades.add(1,7);

        System.out.println(grades.get(0));
        System.out.println(grades.get(1));
        System.out.println(grades.get(2));
        System.out.println(grades.indexOf(7));
        System.out.println(grades.indexOf(70));
        System.out.println(grades.contains(7));

        if(!grades.isEmpty())
        {
            System.out.println(grades.get(0)); //or .remove
        } //test if there is anything before checking indexes
        List<Integer> grades2 = Arrays.asList(5, 3, 2, 6, 3); //adding to list fast
        
        System.out.println(Arrays.toString(grades2.toArray()));//has to be converted back to array momentarily
        
    }
}

//Java api documentation google it

