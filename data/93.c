#include<stdio.h>

main(){
	int n, i, t;
	int a[24]={};
	printf("출석한 사람 수:");
	scanf("%d", &n);
	//printf("각 번호:");
	//scanf("%d", &b);
	printf("각 번호:");
	for(i=1;i<=n;i++){
	scanf("%d", &t);
	a[t]=a[t]+1;
	}
	for(i=1; i<=23; i++){
  	printf("%d ", a[i]);
	}
}
