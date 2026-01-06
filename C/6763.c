#include <stdio.h>

int main(void) 
{
	int a, b;
	int c;

	scanf("%d", &a);
	scanf("%d", &b);

	if (b - a <= 0) {
		printf("Congratulations, you are within the speed limit!");
	}
	else if (1 <= b - a && b - a <= 20) {
		printf("You are speeding and your fine is $100.");
	}
	else if (21 <= b - a && b - a <= 30) {
		printf("You are speeding and your fine is $270.");
	}
	else if (31 <= b - a) {
		printf("You are speeding and your fine is $500.");
	}

	return 0;
} 