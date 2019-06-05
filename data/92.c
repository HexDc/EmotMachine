#include <stdio.h>
main(){
	
    int i, j, k, day = 1;
    
    scanf("%d %d %d", &i, &j, &k);
    
    while (day%i != 0 || day%j != 0 || day%k != 0) {
        day++;
    }
    
    printf("%d", day);
}
