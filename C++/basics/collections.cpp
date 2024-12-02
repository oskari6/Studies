#include <iostream>
#include <limits>
#include <vector>
#include <array>

namespace utilz
{
    void print_array(int array[], int size)
    {
        for(int i = 0; i < size; i++)
        {
            std::cout << array[i] << "\t";
        }
        std::cout << std::endl;
    }
}

void print_vector(std::vector<int> &data) //& copies the memory locationn. Passing by reference. new 12 every iteration
{
    data.push_back(12);

    for(int i = 0; i < data.size(); i++)
    {
        std::cout << data[i] << "\t";
    }
    std::cout << "\n";
}

void print_stl_array(std::array <int, 20> data, int size) //STL array
{
    for(int i = 0; i < size; i++)
    {
        std::cout << data[i] << "\t";
    }
    std::cout << "\n";
}

int main()
{
    // const int SIZE = 100;
    // int guesses[SIZE];
    
    // int count = 0;

    // for(int i = 0; i < SIZE; i++)
    // {
    //     if(std::cin >> guesses[i])
    //     {
    //         count ++;
    //         //input worked
    //     }
    //     else
    //     { // invalid character
    //         break;
    //     }
    // }
    // print_array(guesses, count);
    // std:: cin.clear(); //clears the input
    // std::cin.ignore(10000, '\n'); //removes the invalid inputs out of array
    // std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); //clears all if needed
    // //sizeof give bytes as length 
/*
    //vectors
    std::vector<int> data = {1, 2, 3};
    data.push_back(12);
    std::cout << data[data.size()-1] << std::endl;
    data.pop_back();
    std::cout << data[data.size()-1] << std::endl; //no extra space in length

    //STL array
    std:: array <int, 20> data = {1, 2, 3};
    print_stl_array(data, 3);*/

    int data[] = {1, 2, 3};
    utilz::print_array(data, 3);
    std::cout << data[0] << std::endl;
}