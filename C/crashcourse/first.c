#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include "header.h"

int main()
{
    //string format
    /*printf("%s hello", "hey");
    int radius = scanf("%d", &radius); //reference
    int size = 4; //this has to be done if array size needed
    char name[5] = "asdf";

    scanf("%4s", name); //no need fo reference & with array

    int letter = 0;//size
    while(name[letter] != "\0")//last letter null char
    {
        letter++;
    }
    printf("size of name is: ", letter);
    print("size of name is %lu\n", strlen(name));//string length function

    if(strcmp(name, "Oskari") == 0)//string compare function
    {
        print("you ge access");
    }

    char copy[20];
    strcpy(copy, name); //string copy function
    print("Copy of name is %s\n", copy);

    char lastName[] = "Curry";
    strcat(copy, lastName); //string concat function
    printf("Full name is %s\n", copy);
*/
    int y = power(4, 5);
    printf("%d\n", y);

    int recursive = recursion(5, 5);
    printf("%d\n", recursive);

    int x = 5;
    changeVal(&x); // % is required for pointer val
    printf("%d\n", x);

    int size = 7;
    int ages[] = {1, 4, 53, 23, 23, 9, 52};
    printf("%d\n", oldestValue(ages, size));
    //after compiling you get compiled object file .o
    
    return 0;
}