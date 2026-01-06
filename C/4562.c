#include <stdio.h>

int main(void)
{
	int a;
	int b, l;
	scanf("%d", &a);

	for (int i = 0; i < a; i++) {
		scanf("%d %d", &b, &l);

		if (b - l >= 0) {
			printf("MMM BRAINS \n");
		}
		else {
			printf("NO BRAINS \n");
		}
	}
	return 0;
}