import java.util.Scanner;

public class string_comaprison {

    public static void main(String[] args) {
        String password = "let me in";
        System.out.println("Guess the password:");

        Scanner scanner = new Scanner(System.in);
        String guess = scanner.nextLine();

        System.out.println(password.equals(guess)); //prefer this technique

        System.out.println(password == guess);

        String a = "hi";
        String b = "hi";
        System.out.println(a == b); //interned, some sort of caching
        //counter with this below
        String a = new String("hi");
        String b = new String("hi");
        System.out.println(a == b);

        int x = 10;
        int y = 10;

        System.out.println(x == y);
        
        //primitives - this works
        //int x = 5
        //String x = new String("This is an object");
        //objectives - this does not work
        //values of objects is a reference to object
    }
}
