#include<stdio.h>
int main() {
	char arr[100][100] = { {0, } };
	int n;
	int k=0;
	scanf("%d", &n);
	int sum = 65;
	for (int i = n-1; i >= 0;i--) {
		for (int j = n - 1; j >= 0; j--) {
			arr[i][j] = sum + k;
			k++;
			if (arr[i][j] == 90) {
				k = 0;
			}
		}
	
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			printf("%c ", arr[j][i]);
		}
		printf("\n");
	}
	
}