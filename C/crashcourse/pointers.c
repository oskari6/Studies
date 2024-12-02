#include <stdio.h>

int main()
{
    int pointed = 100;
    int *pointer = &pointed;
    //if you make a pointer and reference it with original or *newer variable, bot update
    int new = 6;
    pointer = &new;
    //now pointer no longer point to pointed, and they are not linked
    //pointers allow to change values inside of functions
    
    return 0;
}