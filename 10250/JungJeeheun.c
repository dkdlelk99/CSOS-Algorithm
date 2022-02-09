#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int H, W, N, T;

	scanf("%d", &T);

	for (int i = 0; i < T; i++) {
		scanf("%d %d %d", &H, &W, &N);
		if (N <= 9 * H)
			printf("%d0%d\n", (N - 1) % H + 1, (N - 1) / H + 1);
		else
			printf("%d%d\n", (N - 1) % H + 1, (N - 1) / H + 1);
	}
	return 0;
}
