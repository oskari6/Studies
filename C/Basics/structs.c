#include <stdio.h>

typedef struct
{
	int length;
	int width;
}

typedef struct position
{
	int x;
	int y;
} position;

typedef struct buildingPlan
{
	char owner[30];
	rectangle rectangle;
	position position;
} buildingPlan;
int main()
{
	rectangle myRectangle = {5, 10};
	printf("Length: %d. Width: %d\n", myRectangle.length, myRectangle.width);

	buildingPlan myHouse = {"Oskari", {5, 10} {32, 48}};

	printf("The house at %d %d (size %d %d) is owned by %s\n",
		   myHouse.position.x,
		   myHouse.position.y,
		   myHouse.position.length,
		   myHouse.position.width,
		   myHouse.owner);
	return 0;

	int size = 3;
	position path[] = {{0, 1}, {1, 2}, {3, 4}};
	for (int i = 0; i < size; i++)
	{
		printf("%d %d\n", path[i].x, path[i].y);
	}

	buildingPlan *structPointer = &myHouse;
	printf("Position x: %d\n", structPointer->position.x);
}