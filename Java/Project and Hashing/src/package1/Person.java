package package1;
import java.util.Objects; //for override alternative

public class Person {
    public String email;
    public Position position;

    public Person(String email) {  //constructor
        this.email = email;
    }

    //right click, source action, generate hashcode and equals

    /*@Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((email == null) ? 0 : email.hashCode());
        return result;
    }*/
    //another approach, works the same way
    @Override
    public int hashCode() {
       return Objects.hash(email, position);
    }
     
    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Person other = (Person) obj;
        if (email == null) {
            if (other.email != null)
                return false;
        } else if (!email.equals(other.email))
            return false;
        if (position == null) {
            if (other.position != null)
                return false;
        } else if (!position.equals(other.position))
            return false;
        return true;
    }

    public Person() { 
    }
}
