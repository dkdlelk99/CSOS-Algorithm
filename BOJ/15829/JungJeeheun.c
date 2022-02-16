#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

int main() {
	int L, sum = 0, value;
	char string[50];

	scanf("%d", &L);
	scanf("%s", string);

	for (int i = 0; i < L; i++) {
		value = string[i];
		sum += (value - 96) * pow(31, i);
	}
	printf("%d", sum);
	return 0;
}
