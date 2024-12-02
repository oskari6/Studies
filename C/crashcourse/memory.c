#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

void function()
{
    // int static x = 0; //statically lives for the lifetime of the program
}

typedef struct
{
    char name[30];
    int age;
    bool isVerified;
} user;

user *createUser(char name[], int age, bool isVerified) // when you want to return a pointer
{
    user *newUser = malloc(sizeof(user));
    strcpy(newUser->name, name);
    newUser->age = age;
    newUser->isVerified = isVerified;
    return newUser;
}
int main()
{ // dynamically sized array
    int size;
    printf("how many elements?:");
    scanf("%d", &size); // take address of operator

    int *arr = malloc(size * sizeof(int)); // memory allocation, if not enough memory gives null instead of int

    if (arr == 0) // if not enough memory
    {
        printf("Invalid pointer, error allocating memory\n");
    }
    else
    {
        printf("You are good to go\n");
    }

    // asking for values
    for (int i = 0; i < size; i++)
    {
        scanf("%d", &arr[i]);
    }

    // printing values
    for (int i = 0; i < size; i++)
    {
        printf("arr[%d] = %d\n", i, arr[i]);
    }

    // this for no memory leak
    free(arr);

    // making users with pointers
    user *me = createUser("Oskari", 72, false);
    printf("Oskari is %d years old!\n,", me->age);
    return 0;
}