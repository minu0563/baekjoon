#include <stdio.h>

int main(void) {
	int a, b;
	int fib_0[41] = { 1, 0 };
	int fib_1[41] = { 0,1 };

	for (int i = 2; i <= 40; i++) {
		fib_0[i] = fib_0[i - 1] + fib_0[i - 2];
		fib_1[i] = fib_1[i - 1] + fib_1[i - 2];
	}

	scanf("%d", &a);

	for (int i = 0; i < a; i++) {
		scanf("%d", &b);
		printf("%d %d \n", fib_0[b], fib_1[b]);
	}
}