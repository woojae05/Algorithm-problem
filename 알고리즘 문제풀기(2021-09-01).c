#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int f(int n) {
	if (n <= 1)
		return n;
	else return  f(n - 1) + f(n - 2);

}
int main() {
#if 0
	char code1 = 'a';
	char code2 = 65;

	code1++;
	code2++;

	printf("code1=%c, code1=%d\n", code1, code1);
	printf("code2=%c, code2=%d\n", code2, code2);
#endif

#if 0
	for (int i = 65; i <= 90; i++) {
		printf("%i %c/", i, i);
		if ((i - 65) % 6 == 5)printf("\n");
	}
	printf("\n");

	for (int i = 97; i <= 122; i++) {
		printf("%i %c/", i, i);
		if ((i - 97) % 6 == 5)printf("\n");
	}
#endif

#if 0
	char string[20];
	scanf("%s", &string);
	for (int i = 0; string[i] != '\0'; i++) {
		printf("%c", (string[i] >= 'a' && string[i] <= 'z') ? 
			(string[i] -= 'a' + 'A') : (string[i] -= 'A' + 'a'));
	}
#endif

#if 0
	int fibo[20] = { 0, };
	int n;
	scanf("%d", &n);
	fibo[0] = 0, fibo[1] = 1;
	for (int i = 2; i <= n; i++) {
		if (i > 1) {
			fibo[i] = fibo[i - 1] + fibo[i - 2];
		}
	}
	printf("%d", fibo[n]);
#endif

#if 1
	printf("%d", f(7));
#endif 
	return 0;
}