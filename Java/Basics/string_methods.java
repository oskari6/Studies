import java.util.Scanner;
public class string_methods {

    public static void main(String[] args) {
        String k = "yummmm...MY OH MY chikcen pot pie\n";
        String password = "let me in";
        System.out.println("Guess the password: ");
        System.out.println(k.charAt(k.length() -1));
        String fullAd = k.concat(" Now with 20% more chicken"); // or x + "string"
        System.out.println(fullAd);
        System.out.println(fullAd.contains("chicken"));
        System.out.println(fullAd.indexOf("my", 3));
        System.out.println(fullAd.indexOf("my", fullAd.indexOf("my")+1));
        System.out.println(fullAd.lastIndexOf("my"));
        System.out.println(fullAd.toUpperCase());
        System.out.println(fullAd.toLowerCase());
        System.out.println(fullAd.strip()); //leading and trailing also
        System.out.println(fullAd.substring(9,17));
        System.out.println(fullAd.repeat(3));
        System.out.println(fullAd.equals("hello"));
        //input
        Scanner scanner = new Scanner(System.in);
        String guess = scanner.nextLine();

        System.out.println(password.equals(guess));
    }
}