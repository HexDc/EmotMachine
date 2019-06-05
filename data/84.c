#include<stdio.h>

int main(){
    int a, b, c;
    int i,j,k;
    scanf("%d %d %d", &a, &b, &c);
    for(i=0; i<a; i++){
        for(j=0; j<b; j++){
            for(k=0; k<c; k++){
                printf("%d %d %d\n", i, j, k);
            }
        }
    }
    printf("%d\n", a*b*c);
}
