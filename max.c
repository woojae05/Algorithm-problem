#include<stdio.h>

int main(){
    
    int a,b,c;
    int max;
    printf("세 정수의 최대값을 구합니다.\n");
    printf("a의 값:"); scanf("%d",&a);
    printf("b의 값:"); scanf("%d",&b);
    printf("c의 값:"); scanf("%d",&c);
    max = a;
    if(b>max) max=b;
    if(c>max) max=c;

    printf("최대값은 %d 입니다.",max);
    return 0;

    
}