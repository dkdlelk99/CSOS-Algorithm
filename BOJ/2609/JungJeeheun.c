#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int N, M; // 입력받는 두수
    int smallnum = 0, bignum = 0, LCM = 0, GCD = 0;
    // 둘중 작은수, 큰수, 최소공배수, 최대공약수
    scanf("%d %d", &N, &M);
    if (N < M) {
        smallnum = N;
        bignum = M;
    }
    else {
        smallnum = M;
        bignum = N;
    }

    for (int i = 1; i <= smallnum; i++) {
        if ((N % i == 0) && (M % i == 0))
            GCD = i;
    }
    LCM = bignum;
    while ((bignum % N != 0) || (bignum % M != 0))
        LCM = ++bignum;
    printf("%d\n%d", GCD, LCM ); 
    return 0;
}
