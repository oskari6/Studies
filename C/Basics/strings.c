#include <stdio.h>

int main()
{
	printf("What is you favorite food?: ");
	char favFood[50];
	scanf("%49s", favFood);
	printf("%s\n", favFood);

	//other option int charCount = strlen(favFood);

	int charCount = 0;

	while(favFood[charCount] != '\0')
	{
		charCount ++;
	}

	printf("The charachter count is %d\n", charCount);
	return 0;
}

