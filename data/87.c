#include <stdio.h>

main(){

    int i;
	int j, sum = 0;
    scanf("%d", &i);
 
    for (j=1;;j++) {
        sum += j;
        if (sum >= i) {
            break;
        }
    }
    printf("%d", sum);
 
    return 0;
}
