#include <stdio.h>
#include <math.h>

int main(void)
{
	float a;
	
	while (1) {
		scanf("%f", &a);

		if (a == 0) {
			break;
		}

		printf("%0.2lf \n", (float)1 + a + pow(a, 2) + pow(a, 3) + pow(a, 4));
	}

	return 0;
}