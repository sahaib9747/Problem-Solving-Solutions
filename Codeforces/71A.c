#include <stdio.h>
#include <string.h>
 
int main()
{
    int n;
    char array[101];
    scanf("%d", &n);
    while(n){
        scanf("%s", &array);
        int strLen = strlen(array);
        if (strLen > 10){
            printf("%c%d%c\n", array[0], strLen-2, array[strLen-1]);
        }
        else{
            printf("%s\n", array);
        }
        n--;
    }
    return 0 ;
}
 