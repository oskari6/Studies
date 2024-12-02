#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isPrime(int input)
{
	for (int i = sqrt(input); i > 1; i--)
	{
		if(input % i == 0)
		{
			return false;
		}
	}
	return true;
}

int main()
{
	//get input from user
	//print all primes from that number down to zero (down to 2)
	int input;
	printf("anna numero");
	scanf("%d", &input);

	for(int i = input; i > 1; i--)
	{
		bool prime = isPrime(i);
		if (prime)
		{
			printf("%d Is Prime!\n");
		}
	}
	return 0;
}