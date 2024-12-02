#include <iostream>

double squared(double x)
{
    return x * x;
}
int main()
{
    if(squared(5) == 25) //testing
    {
        std::cout << "Test passed\n";
    }
}