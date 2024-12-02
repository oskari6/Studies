import java.util.List;

public abstract class User2 implements Talk{ //everything that cant exist label it abstract
    public String firstName;
    public String lastName;
    public boolean verified = false; 
    public enum status {active, inactive, probation};
    public status status;
    // public void sayHello() { //final keyword 

    // }
    // public void sayHello() {
    //     System.out.println("Hi! I'm user. My name is " + firstName + " " + lastName);
    // }
    // public abstract void sayHello();

}

//super to invoke User version of sayHello
// public void sayHello() {
//     super.sayHello(); //this
//     System.out.println("User version");
// }

//readonly fields assigned with constructor
// public abstract class User2 { 
//     public String firstName;
//     public String lastName;
    
//     public User(String fn, String ln) {
//         firstName = fn;
//         lastName = ln;
//     }
// }