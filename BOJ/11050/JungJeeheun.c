#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int N, K;
	int Nfac = 1, Kfac = 1, NKfac = 1;
	scanf("%d %d", &N, &K);
	
	for (int i = 1; i <= N; i++)
		Nfac = Nfac * i;
	for (int i = 1; i <= K; i++)
		Kfac = Kfac * i;
	for (int i = 1; i <= N - K;i++)
		NKfac = NKfac * i;
	printf("%d", Nfac / (Kfac * NKfac));
	return 0;
}
