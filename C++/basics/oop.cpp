#include <iostream>
#include <string>
#include "user.h"
#include "teacher.h"
#include "student.h"

void do_something(User user) //& after User and teacher and student outputs come
{
    user.output();
}

int main()
{
    /*User me; //instance of struct
    me.first_name = "Oskari";
    me.last_name = "Sulkakoski";
    //me.status = "Gold"; //private
    std::cout << "Status: " << me.get_status() << std::endl;
    */
    /*std::vector<User> users;
    //user.push_back(User()); //default, also legal

    User user1, user2, user3;
    user1.first_name = "Sally";
    user1.last_name = "Swan";

    user2.first_name = "Jake";
    user2.last_name = "Johnson";

    user3.first_name = "Oskari";
    user3.last_name = "Sulkakoski";

    users.push_back(user1);
    users.push_back(user2);
    users.push_back(user3);

    User user;
    user.first_name = "Jake";
    user.last_name = "Johnson";

    std::cout << add_user_if_not_exists(users, user) << std::endl;
    std::cout << users.size() << std::endl;*/

    // User user("Oskari", "Sulkakoski", "Silver");
    // std::cout << user.get_status() << std::endl;

    /*User user;
    user.set_status("Tacos"); //no status
    std::cout << user.get_status() << std::endl;
    return 0;*/

    /*User user, user1, user2, user3, user4;
    std::cout << User::get_user_count() << std::endl;
    user.~User(); //destuctor
    std::cout << User::get_user_count() << std::endl;*/

    //Insertion operator overload
    /*User user;
    std::cin >> user;
    /*user.first_name = "Oskari";
    user.last_name = "Sulkakoski";
    user.set_status("Gold");
    std::cout << user << std::endl;*/

    //friend function
    /*User user;
    output_status(user);*/

    //friend function for operator overload
    /*User user;
    user.first_name = "Oskari";
    user.last_name = "Sulkakoski";
    user.set_status("Gold");
    std::cout << user << std::endl;*/

    //same put input
    /*User user;
    std::cin >> user;
    std::cout << user << std::endl;*/

    /*Teacher teacher;
    teacher.first_name = "Teach";
    std::cout << teacher.first_name << std::endl;
    teacher.output();*/

    Teacher teacher;
    User& u1 = teacher; //polymorphism
    u1.output(); //created virtual void output(); in user.h

    Student student;
    User& u2 = student;
    student.output();

    do_something(u1);
    do_something(u2);
}