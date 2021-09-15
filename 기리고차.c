#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

void main() {
	int input_num1, input_num2;
	int tmp1, tmp2, tmp3;
	scanf("%d %d", &input_num1, &input_num2);

	// 북소리 기준 10리 단위 이동 거리
	tmp1 = input_num1 / 3;				
	// 북소리 기준 10리 단위 이동 후 5리 단위 추가 이동 여부
	tmp2 = input_num1 % 3;				
	// 마지막 북소리 이후 종소리 갯수 파악 
	tmp3 = input_num2 - (tmp1 * 2 * 13) - (tmp2 * 13);		
	// 입력 값 오류 체크
	if (tmp2 == 2 || tmp3== 2 || input_num2 < tmp1 * 13)
	{
		printf("INPUT NUMBER Error");
		return 0;
	}
	//				
	printf("%.1f", (tmp1 * 10)	// 북소리 기준 10리 단위 계산
		+ (tmp2 * 5)			// 북소리 기준 5리 단위 계산
		+ (tmp3 / 3 * 1)		// 종소리 기준 1리 단위 계산
		+ ((tmp3 % 3) * 0.5));	// 종소리 기준 0.5리 단위 계산
}