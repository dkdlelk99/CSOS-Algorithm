#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int A, B, C;
	int value;
	int count[10] = { 0 };

	scanf("%d%d%d", &A, &B, &C);

	value = A * B * C;

	while (value > 0) {
		count[value % 10]++;
		value = value / 10;
	}

	for (int i = 0; i < 10;i++) 
		printf("%d\n", count[i]);

	return 0;
}
