#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int a, b, c, d, e;
	int verif;
	
	scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);

	verif = (a * a + b * b + c * c + d * d + e * e) % 10;
	printf("%d", verif);

	return 0;
}
