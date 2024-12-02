#include <iostream>
#include <limits>
#include <vector>
#include <array>
#include <fstream>

int main()
{
    //writing to files
    std::string filename;
    std::cin >> filename;

    std::ofstream file; //instance of oftream, fileo object
    //std::ofstream file("hello.txt"); //this works too
    file.open(filename.c_str(), std::ios::app); //c_str() optional in c++11
    
    if(file.is_open()) //shows in terminal
    {
        std::cout << "success\n";
    }

    std::vector<std::string> names;
    names.push_back("Oskari");
    names.push_back("Amy");
    names.push_back("Susan");

    for(std::string name : names)
    {
        file << name << std::endl;
    }
    file.close(); //not necessary always, has to do with errors
}