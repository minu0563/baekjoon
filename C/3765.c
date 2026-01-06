#include <stdio.h>

int main(void)
{
	char ch[200];

	while (fgets(ch, sizeof(ch), stdin) != NULL) {
		printf("%s", ch);
	}

	return 0;
}