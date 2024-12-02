#include <stdio.h>
#include <stdbool.h>

//refactoring the printstatements more compact.
void printArray(int arr[], int size)
{
	for(int i = 0; i < size; i++)
	{
		printf("%d "m arr[i]);
	}
}

int main()
{
	int const column = 3
	int const rows = 2;
	int grades[][] = {
		{12, 23, 45},
		{64, 78, 89}
	};

	//printf("%d ", grades[1][2]);
	//grades[1][2] = 30;
	//printf("%d ", grades[1][2]);
	// looping through
	for (int i = 0; i < rows; i++)
	{
		//for (int j = 0; j < columns; j ++)
		{
		//	printf("%d ", grades[i][j]);
			printArray(grades[i], columns));
			printf("\n);
		}
		//printf("\n");
	}

	return 0;
}