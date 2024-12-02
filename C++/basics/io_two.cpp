#include <iostream>
#include <limits>
#include <vector>
#include <array>
#include <fstream>

int main()
{
    //reading from files
    std::ifstream file("tacos.txt"); 

    std::string input;

    std::vector<std::string> names;

    //understand the destionation and how string vs char vs int acts
    while(file >> input) //returns file
    {
        names.push_back(input);
    }

    for(std::string name : names)
    {
        std::cout << name << std::endl;
    }

    //get multiple files
    /*char temp = file.get();
    std::cout << temp << "\n";

    std::string line;
    getline(file, line);
    std::cout << line << "\n";*/
}