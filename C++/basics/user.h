#ifndef USER_H
#define USER_H

class User //private by default
{
    static int user_count;
    std::string status = "Gold"; //do these in constructors

    public:
        static int get_user_count();
        std::string first_name;
        std::string last_name;
        std::string get_status(); //basic setter

        void set_status(std::string status); //basic getter

        User(); //making a constructor and every time its hit: Contructor, this is default constructor

        User(std::string first_name, std::string last_name, std::string status);

        ~User(); //destructor

        virtual void output(); //virtual enables polymorphism, without= output im a user

        friend std::ostream& operator << (std::ostream& output, const User user);
        friend std::istream& operator >> (std::istream &input, User &user);
};
#endif