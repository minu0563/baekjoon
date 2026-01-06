#include <stdio.h>

int main(void)
{
	int a;
	char ch[60];

	scanf("%d", &a);
	getchar();

	for (int i = 0; i < a; i++) {
		fgets(ch, sizeof(ch), stdin);
		printf("%d. %s", i + 1, ch);
	}

	return 0;
}