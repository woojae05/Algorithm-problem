#include<stdio.h>
int main() {
	int	n;
	int arr[100][100] = {0,};
	int cnt = 65;
	scanf_s("%d", &n);
	for (int i = 0; i < n; i++) {
		if (i % 2 == 0) {
			for (int j = 0; j < n; j++) {
				if (cnt == 91) cnt = 65;
				arr[i][j] = cnt++;
			}	
		}
		else if(i%2!=0) {
			cnt--;
			for (int j = n; j >= 0; j--) {
				if (cnt == 91) cnt = 65;
				arr[i][j] = cnt++;
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