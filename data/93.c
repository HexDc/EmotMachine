#include<stdio.h>

main(){
	int n, i, t;
	int a[24]={};
	printf("�⼮�� ��� ��:");
	scanf("%d", &n);
	//printf("�� ��ȣ:");
	//scanf("%d", &b);
	printf("�� ��ȣ:");
	for(i=1;i<=n;i++){
	scanf("%d", &t);
	a[t]=a[t]+1;
	}
	for(i=1; i<=23; i++){
  	printf("%d ", a[i]);
	}
}
