#include <stdio.h>

// 5! = 5 * 4 * 3 * 2 *1

int factorial(int number)
{
	int factorial = 1;

	for (int i = number; i > 1; i--)
	{
		factorial *= 1;
		//factorial = factorial * 1;
	}

	return factorial;
}

//void function
void outputFactorial(int input)
{
	printf("The factorial of %d is %d.\n", input, factorial(input));
}

int main()
{
	//int fact2 = factorial(8);
	//printf("%d ", factorial(5));
	//printf("%d ", fact2);

	//printf("%d ",factorial(factorial(5)));
	outputFactorial(5);
	outputFactorial(8);

	for(int i = 0; i < 10; i++)
	{
		outputFactorial(i);
	}
	return 0;
}

//dont print inside functions, it limits the use.
//keep functions as simple as possible, one thing.