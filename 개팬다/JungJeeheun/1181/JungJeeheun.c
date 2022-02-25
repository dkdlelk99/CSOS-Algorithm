#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {
    char word[20000][50]; // 2차배열에 단어를 입력받아서 행에는 순서 열에는 단어 저장
    char temp[50]; // 출력할단어 저장 // 짧은 단어부터
    int num = 0, N;

    scanf("%d", &N);
    for (int i = 0; i < N; i++)
        scanf("%s", word[i]);

    for (int i = 0; i < N-1; i++) {
        for (int j = i+1; j < N; j++) {
            if (strcmp(word[i], word[j]) > 0) {
                strcpy(temp, word[i]);
                strcpy(word[i], word[j]);
                strcpy(word[j], temp);
            }
        }
    }
    for (int i = 0; i < N; i++) {
        if (word[i] == word[i + 1])
            i++;
        printf("%s\n", word[i]);
    }
    return 0;
}
