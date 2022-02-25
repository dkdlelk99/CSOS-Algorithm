#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int N;

    scanf("%d", &N);                        // '('+')'두 아스키문자가 40 41인거 이용
    for (int i = 0; i < N; i++) {
        int j = 0, sum = 0;
        char arr[50] = { 0 };
        scanf("%s", arr);
        while (arr[j] != '\0') {
            if (sum < 0)
                break;
            if (arr[j] == '(')
                sum += 1;
            else
                sum -= 1;
            j++;
        }
        if (sum == 0)
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}
