#include <stdio.h>

int main(void)
{
	float a;
	
	while (1) {
		scanf("%f", &a);
		
		if (a < 0) {
			break;
		}
		else {
			printf("Objects weighing %0.2f on Earth will weigh %0.2f on the moon. \n", a, a * 0.167);
		}

	}

	return 0;
}