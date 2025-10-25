#include <stdio.h>

int main()
{
	int slices = 20;
	int *p = &slices;

	printf("Slices : %d\n", slices);
	printf("Slices (throughpointer); %d\n", *p);

	slices = 21;

	printf("Slices : %d\n", slices);
	printf("Slices (throughpointer); %d\n", *p);

	*p = 25;

	printf("Slices : %d\n", slices);
	printf("Slices (throughpointer); %d\n", *p);
	
	slices++;

	//*p++; -> *(p++);
	(*p)++;

	printf("Slices: %d\n", slices);
	printf("Slices (through pointer): %d\n", *p);

	int pointed = 100;
    int *pointer = &pointed;
    //if you make a pointer and reference it with original or *newer variable, bot update
    int new = 6;
    pointer = &new;
    //now pointer no longer point to pointed, and they are not linked
    //pointers allow to change values inside of functions
	
	return 0;
}