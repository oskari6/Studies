#ifndef math_utils
#define MATH_UTILS

struct Rectangle
{
    double length;
    double width;
};

namespace utilz
{
    double area(double length); //square

    double area(double length, double width); //rectangle

    double area(Rectangle rectangle);

    double pow(double base, int pow = 2); //default parameter 2
}

#endif