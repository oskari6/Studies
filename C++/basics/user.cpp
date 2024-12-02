#include <iostream>
#include <vector>
#include "user.h"

    int User::get_user_count()
    {
        return user_count;
    }
        std::string User::get_status()//basic setter
        {
            return status;
        }
        void User::set_status(std::string status)//basic getter
        {
            if(status == "Gold" || status == "Silver" || status == "Bronze")
            {
                this-> status = status;
            }
            else
            {
                this-> status = "No status";
            }
        }

        User::User() //making a constructor and every time its hit: Contructor, this is default constructor
        { //remove this and you have no default constructor.
            //std::cout << "Constructor\n";
            std::cout << "User created\n";
            user_count++;
        }
        User::User(std::string first_name, std::string last_name, std::string status)
        {
            this-> first_name = first_name; //specifies the class level variable
            this-> last_name = last_name; //first one acts as the object
            this-> status = status; //this is how you make default values
            user_count++;
        }

        User::User::~User() //destructor
        {
            //std::cout << "Destructor\n";
            user_count--;
        }

        void User::output()
        {
            std::cout << "Iam a user\n";
        }
        //access to private data members
        //friend void output_status(User user);
        std::ostream& operator << (std::ostream& output, const User user);
        std::istream& operator >> (std::istream &input, User &user);

//access to private data members
/*void output_status(User user)
{
    std::cout << user.status;
}*/

/*struct User //public by default
{
    std::string get_status()
    {
        return status;
    }
    std::string first_name;
    std::string last_name;
    private:
        std::string status = "Gold";
};
*/

int User::user_count = 0; //you cant set this to 0 in the class =
 //inline doesnt work, do it here outside

/*int add_user_if_not_exists(std::vector<User> &users, User user)
{
    for(int i = 0; i < users.size(); i++)
    {
        if(users[i].first_name == user.first_name &&
        users[i].last_name == user.last_name)
        {
            return i;
        }
    }
    users.push_back(user);
    return users.size() -1;
}*/

std::ostream& operator << (std::ostream& output, const User user)
{
    output << "First name: " << user.first_name << "\nLast name: "<< user.last_name <<
    "\nStatus: " << user.status;
    return output;
}

std::istream& operator >> (std::istream &input, User &user)
{
    input >> user.first_name >> user.last_name >> user.status;
    return input;
}