#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int asc[8] = { 1,2,3,4,5,6,7,8 }, des[8] = { 8,7,6,5,4,3,2,1 };
	int space[8];
	int i, j = 0, k = 0;

	for (i = 0; i < 8; i++)
		scanf("%d", &space[i]);

	while (space[j] == asc[j]) {
		j++;
		if (j == 8)
			break;
	}
	while (space[k] == des[k]) {
		k++;
		if (k == 8)
			break;
	}
	if (j == 8)
		printf("ascending");
	else if (k == 8)
		printf("descending");
	else
		printf("mixed");
	return 0;
}
