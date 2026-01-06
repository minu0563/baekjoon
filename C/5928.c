#include <stdio.h>

int main(void) 
{
	int day, hour, min;
	int a = 11, b = 11, c = 11;
	int ans_1, ans_2, total_ans;

	scanf("%d %d %d", &day, &hour, &min);

	ans_1 = (day * 24 * 60) + (hour * 60) + min;
	ans_2 = (a * 24 * 60) + (b * 60) + c;

	if (ans_1 < ans_2) {
		printf("-1");
	}
	else {
		total_ans = ans_1 - ans_2;
		printf("%d", total_ans);
	}

	return 0;
}