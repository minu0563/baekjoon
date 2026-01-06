#include <stdio.h>

int main(void)
{
	int a, b[5], count = 0;

	scanf("%d", &a);

	for (int i = 0; i < 5; i++) {
		scanf("%d", &b[i]);
		if (b[i] == a) {
			count++;
		}
	}

	printf("%d", count);

	return 0;
}