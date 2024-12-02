#include <iostream>
#include <limits>
#include <vector>
#include <array>

int main()
{
    //based on foreach loop
    int data[] = {1, 2, 3, 4, 5, 6} //range based for loop (c++11 and up)

    for(int n : data)
    {
        std::cout << n << "\t";
    }

    /*for(int i = 0; i < 6; i++) //normal for loop
    {
        std::cout << data[i] << "\t";
    }
    std::cout << "\n"*/
}