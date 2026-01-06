#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int a, b, t1, t2;

	scanf("%d %d", &a, &b);

	for (int i = a; i >= 0; i--) {
		for (int j = 0; j <= i; j++) {
			if (i + j == a && i - j == b) {
				printf("%d %d", i, j);
				exit(0);
			}
		}
	}
	printf("%d", -1);

	return 0;
}