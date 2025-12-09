#include "header.h"

int power(int input, int exponent)
{
    int total = 1;
    for(int i = 0; i < exponent; i++)
    {
        total *= input;
    }
    return total;
}

int recursion(int input, int exponent)
{
    if(exponent < 1)
    {
        return 1;
    }
    return input * recursion(input, exponent-1);
}

void changeVal(int *input)//make it a pointer so value sticks
{
    *input = 9000; //pointer also here
}

int oldestValue(int ages[], int size)
{
    int largest = ages[0];
    for(int i = 0; i < size; i++)
    {
        if(ages[i] > largest)
        {
            largest = ages[i];
        }
    }
    return largest;
}