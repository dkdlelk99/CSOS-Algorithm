#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	while(1)
	{
	int i = 0, j = 0, k = 0;
	char palin[99999];
	
	scanf("%s", palin);

	if (palin[0] == '0')
		break;
	while (palin[i] != '\0')
		i++;
	for (; j < i; j++) {
		if (palin[j] != palin[i - j - 1])
			break;
		else
			k++;
	}
	if (k == i)
		printf("yes\n");
	else
		printf("no\n");
	}
	return 0;
}
