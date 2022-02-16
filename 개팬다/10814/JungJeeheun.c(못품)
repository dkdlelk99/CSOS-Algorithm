#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {
    int N, atemp;
    int** string;
    int* age, stemp[100];
    scanf("%d", &N);

    string = (int**)malloc(sizeof(int*) * N);
    for (int i = 0; i < N; i++)
        string[i] = (int*)malloc(sizeof(int) * 100);

    age = malloc(sizeof(int) * N);

    for (int i = 0; i < N; i++)
        scanf("%d %s", &age[i], string[i]);
    for (int i = 0; i < N - 1; i++) {
        for (int j = i + 1; j < N; j++) {
            if ((age[i] != age[j]) && (age[i] > age[j])) {
                atemp = age[i];
                age[i] = age[j];
                age[j] = atemp;
                strcpy(string[i], stemp);
                strcpy(string[j], string[i]);
                strcpy(stemp, string[j]);
            }
        }
    }
    for(int i = 0; i < N; i++)
        printf("%d %s\n", age[i], string[i]);
    for (int i = 0; i < N; i++)
        free(string[i]);
    free(string);
    free(age);

    return 0;
}
