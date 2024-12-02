#include "math_utils.h"

namespace utilz
{
    double area(double length) //square
    {
        return length * length;
    }

    double area(double length, double width) //rectangle
    {
        return length * width;
    }

    double area(Rectangle rectangle)
    {
        return rectangle.length * rectangle.width;
    }

    double pow(double base, int pow) //default parameter 2
    {
        int total = 1;
        for(int i = 0; i < pow; i++)
        {
            total *= base;
        }
        return total;
    }
}
