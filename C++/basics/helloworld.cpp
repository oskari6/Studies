#include <iostream> //(pre processor)
#include <vector>
#include <string>
#include <cmath>

//using is a declaration
//using namespace std; //using directive
using std::cout; //or this
using std::endl;
using std::cin;

//double power(double, int); //declaration
double power(double base, int exponent) //definition this can also be at the top
{
    double result = 1;
    for(int i = 0; i < exponent; i++)
    {
        result = result * base;
    }
    return result; //when functions return something, value has to be used. Variable, expression..
}

void print_pow(double base, int exponent)
{
    double myPower = power(base, exponent);
    //double power = pow(base, exponent);
    cout << base << " raise to the " << exponent << " power is " << myPower << endl;
    
}

int main()
{
    int slices;
    cout << "How many slices of pizza?: ";
    cin >> slices;
    cout << "You Have " << slices << " slices of pizza." << endl;
    
    printf("%i\n", slices);
    
   
   double base;
   int exponent;

    cout << "What is the base: ";
    cin >> base;
    cout << "what is the exponent: ";
    cin >> exponent;
    print_pow(base, exponent);
}

