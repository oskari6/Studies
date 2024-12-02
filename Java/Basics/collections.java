import java.util.List;
import java.io.File;
import java.util.Scanner;
import java.util.Set;

import Hashing.Position;
import Packages.Person;

import java.util.Collection;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Iterator;
import java.util.ListIterator;
import java.util.HashMap;
import java.util.HashSet;

public class  Collections{
    public static void main(String[] args) {
        //Queue
        LinkedList<String> names = new LinkedList<>();
        names.add("Oskari");
        names.add("Sue");
        names.add("Sally");

        Iterator<String> it = names.iterator();
        System.out.println(it.next());

        ListIterator<String> it2 = names.listIterator();
        it2.add("Susan");

        System.out.println(names.remove());
        System.out.println(names.remove());
        System.out.println(names.remove());
        
        //stack
        names.push("Oskari");
        names.push("Sue");
        names.push("Sally");
        System.out.println(names.pop());
        System.out.println(names.pop());
        System.out.println(names.removeFirst());

        ArrayList<Integer> ages = new ArrayList<Integer>();
        HashMap<String,Integer> ids = new HashMap<String,Integer>();
        ids.put("key", 5);

        Set<String> keys = ids.keySet();    //or .entrySet or .values
        for(String key : keys)  {
            System.out.println(key);
            System.out.println(ids.get(key));
        }

        Person p = new Person("email@email.com");
        Position pos1 = new Position(10, 10);
        p.position = pos1;

        Person q = new Person("email@email.com");
        Position pos2 = new Position(10, 10);
        q.position = pos2;

        //HashSets
        HashSet<String> words = new HashSet<String>();
        words.add("hello");//repeated string dont add as duplicate
        words.add("bye");  //position by hashcode number

        System.out.println(words.contains("hello"));
        HashSet<Person> people = new HashSet<Person>();
        people.add(p);
        people.add(q);
        System.out.println(people.contains(p));

        HashMap<String, Person> peeps = new HashMap<String, Person>();
        peeps.put("email@email.com", p);
        System.out.println(peeps.containsKey("email@email.com"));
        //hashMap can have duplicate data but not duplicate keys

        //Generic classes
        Item<String, String> item = new Item<String, String>();//last 2 types not required
        String hello = "hello";
        String bye = "bye";

        item.setX(hello);
        item.setY(bye);
        item.getX();
        item.getY();

        Item<Integer, String> pair = new Item<>();
        pair.setX(1);
        pair.setY("Hey");

        ArrayList<Item<Integer, String>> pairs = new ArrayList<>();
        pairs.add(pair);

        //inheritance
        ArrayList<Person> people2 = new ArrayList<Person>();
        //cant type a list that is typed to a derived class  
        Admin a = new Admin();
        people2.add(a);
        a.email = "email@email.com";
        
        ArrayList<Admin> admins = new ArrayList<Admin>();
        admins.add(a);
        //derived class list inheritance variation 
        //a list of admins, has to be casted into a person in the middle
        //list of persons and admins are no way connected inheritance wise
        //this if you cant change the code, (cant add wild card variation)
        /*ArrayList<Person> admins2 = new ArrayList<Person>();
        for(Admin admin : admins) {
            admins2.add((Person)admin);
        }*/

        doSomething(admins);

        //another approach
        List<Person> people3 = (List<Person>)(List<?>)admins;
        doSomething(people3);

    }
    static void doSomething(Person p) {
        System.out.println(p);
    }

    //wildcard ? usage, we get the desired result with extends keyword
    static void doSomething(ArrayList<? extends Person> people) {
        for(Person p : people) {
            System.out.println("email: " + p.email);
        }
    }

    static void doSomething(List<Person> people) {
        for(Person p : people) {
            System.out.println("email: " + p.email);
        }
    }
}
