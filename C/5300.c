#include <stdio.h>

int main(void)
{
	int a, b = 0;
	scanf("%d", &a);

	for (int i = 1; i <= a+1; i++) {
		if (i == a && b != 6) {
			printf("%d Go!", i);
			break;
		}

		if (b == 6) {
			b = 1;
			printf("Go! %d ", i);
		}
		else {
			b++;
			printf("%d ", i);
		}
	}

	return 0;
}