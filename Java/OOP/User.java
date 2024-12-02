import java.util.List;

public class User {
    //members - methods and properties
    private String firstName;
    private String lastName;
    String favFood; //field
    
    public void output1(int times) {
        for(int i = 0; i < times; i++) {
            System.out.println(firstName + " " + lastName);
        }
    }
    public String getFullName1() {
        return firstName + " " + lastName;
    }

    public String output2() {
        return "Hi, my name is " + firstName + " " + lastName +".";
    }

     public String output3() {
        return "Hi, my name is " + getFirstName() + " " + getLastName() +".";    
    }

    public String getFullName2() {
        return getFirstName() + " " + lastName; //see you can also use mehtods inside
    }

    //getter
    public String getFirstName() {
        return firstName.toUpperCase(); //this is basically blokcing access now, see public changed to private
    }

    //setter needs to go with getter
    public void setFirstName(String fn) {
        firstName = fn.strip().toLowerCase(); //here you can change or add methods and it affects the way these get sotred, not printed out
    }

    public String getLastName() {
        return lastName.toUpperCase();
    }

    public void setLastName(String ln) {
        lastName = ln;
    }

    public static void printUser(User u) { //static
            System.out.println(u.getFullName2());
    }

    public static void printUsers(List<User> users) { //not tied to one user
        for(User u : users) {
            System.out.println(u.getFullName2());
        }
     }

//73
    public String output(boolean nice) {
        if(nice) {
            return "You are a beautiful person. - " + getFullName2() + ".";
        }
        return "You are a freak. - " + getFullName2() + ".";
    }
    
    ////Searching list for Custom objects
    public static int searchList(List<User> users, String fn, String ln) {
        return searchList(users, fn + " " + ln);
    }

    public static int searchList(List<User> users, String fullName) {
        for(int i = 0; i < users.size(); i++) {
            if(users.get(i).getFullName2().equals(fullName)) {
                return i;
            }
        } //if you want other than -1 change tolowercases away, they are messing with result
        return -1;
    }

    //Overide toString
    @Override
    public String toString() {
        return "User [getFullName2()=" + getFullName2() + "]";
    }
    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((firstName == null) ? 0 : firstName.hashCode());
        result = prime * result + ((lastName == null) ? 0 : lastName.hashCode());
        return result;
    }

    //Override equals 
        @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        User other = (User) obj;
        if (firstName == null) {
            if (other.firstName != null)
                return false;
        } else if (!firstName.equals(other.firstName))
            return false;
        if (lastName == null) {
            if (other.lastName != null)
                return false;
        } else if (!lastName.equals(other.lastName))
            return false;
        return true;
    }
    //Overload the search to take in  a user object
    public static int searchList(List<User> users, User u) {
        return searchList(users, u.getFullName2());
    }

    //returning custom objects
    public static User findUser(List<User> users, User u) {
        for(User user : users) {
            if(user.equals(u)) {
                return user;
            }
        }
        return null;
    }
    //passing by value or reference
    public void changeCrap(User x) {
        x.setFirstName("Changed");
    }
}
