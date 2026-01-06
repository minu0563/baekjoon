#include <stdio.h>

int main(void)
{
	int a;
	int b, c, d;
	
	scanf("%d", &a);
	printf("Gnomes: \n");

	for (int i = 0; i < a; i++) {
		scanf("%d %d %d", &b, &c, &d);

		if (b > c && c > d) {
			printf("Ordered \n");
		}
		else if (d > c && c > b) {
			printf("Ordered \n");
		}
		else {
			printf("Unordered \n");
		}
	}
	return 0;
}