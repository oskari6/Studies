#include <stdio.h>
// typedef and rectangle; make it possible to not use struct inside main
typedef struct
{
    int length; // Myrectangle.length
    int width;  // Myrectangle.width
} rectangle;

typedef struct
{
    int x;
    int y;
} position;

typedef struct
{
    char owner[30];
    rectangle rectangle;
    position position;
} buildingPlan;

int main()
{
    rectangle myRectangle = {5, 10};
    buildingPlan myHouse = {"Oskari", {5, 10}, {32, 40}};
    printf("The house at %d %d (size %d %d) is owned by %s\n",
           myHouse.position.x,
           myHouse.position.y,
           myHouse.rectangle.length,
           myHouse.rectangle.width,
           myHouse.owner);

    // storing structs in array
    int size = 3;
    position path[] = {{0, 1}, {1, 2}, {3, 4}};
    for (int i = 0; i < size; i++)
    {
        printf("%d %d\n", path[i].x, path[i].y);
    }

    buildingPlan *structPointer = &myHouse;
    printf("Position x: %d\n", structPointer->position.x);
    //-> to access values of the pointer

    return 0;
}