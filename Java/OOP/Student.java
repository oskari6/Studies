public class Student extends User2 implements Talk{
    public boolean verified = true;
    public String major;

    //constructor see placement, now that custom constuctor created cant call default in empty ()
    public Student() {
        System.out.println("Creating a student");
    }

    public Student(String fn, String ln) { //custom constructor
        //readonly fields assigned with constructor
        /*super(fn, ln);
         * remove lines below
         */
        firstName = fn;
        lastName = ln;
    }
    @Override
    public void sayHello() {
        System.out.println("Hi my my major is " + major + ". My name is  " 
        + firstName + " " + lastName);
    }

    //abstract methods no body
    //@Override
    //public abstract void sayHello();
}
