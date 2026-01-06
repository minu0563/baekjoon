#include <stdio.h>
#include <string.h>

void replace(char* str) {
	for (int i = 0; str[i] != '\0'; i++) {
		if (str[i] == 'e') {
			str[i] = 'i';
		}
		else if (str[i] == 'i') {
			str[i] = 'e';
		}
		else if (str[i] == 'I') {
			str[i] = 'E';
		}
		else if (str[i] == 'E') {
			str[i] = 'I';
		}
	}
}


int main(void)
{
	char ch[100];

	while (fgets(ch, sizeof(ch), stdin) != NULL) {
		replace(ch);
		printf("%s", ch);
	}

	
	return 0;
}