#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main() {
	int n;
	int arr[20][20] = { 0, };
	int cnt=65;
	scanf("%d", &n);
	for (int i = 0; i < n;i++) {
		for (int j = n-1; j > i;j--) {
			printf("  ");
		}
		for (int j = 0; j <= i;j++) {
			arr[i][j] = cnt;
			printf("%c ",arr[i][j+n]);
			if (cnt == 91) cnt = 65;
			cnt ++;
		}
		printf("\n");
	}
}