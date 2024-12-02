import java.util.ArrayList;
import java.util.List;

public class OOP3{
    public static void main(String[] args) {
        Student s = new Student("smartie", "Not a candy");
        s.major = "Mustache design";
        //System.out.println(s.major);
        s.major= "Mustachee desgin";
        s.firstName = "Smartie";
        s.lastName = "Not a candy";
        //s.sayHello();

        Teacher t = new Teacher();
        t.firstName = "Teach";
        t.lastName = "er";

        List<User2> users = new ArrayList<User2>();
        users.add(s); users.add(t);

        for (User2 u : users) {
            u.sayHello();
        }
    System.out.println(s.firstName);

    List<Talk>thingsThatTalk = new ArrayList<Talk>();
    thingsThatTalk.add(s);

    // s.status = s.status.probation(); //enum
    System.out.println(s.status);

    switch(s.status) {
    case probation:
        System.out.println("ouch");
        break;
    case active:
        System.out.println("great");
        break;
    case inactive:
        System.out.println("come back");
        break;
        }
    }
}


