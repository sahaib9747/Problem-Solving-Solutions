#include <stdio.h>
 
int checkYear(int num){
    int arr[4];
    int n = 0, temp, r;
    temp = num;
 
    // reverse it
    while(temp != 0)
   {
      r = temp%10;
      arr[n] = r;
      temp = temp/10;
      n++;
   }
 
 
    for (int i = 0; i < 4; i++){
        for(int j=i+1; j < 4; j++){
            if (arr[j] == arr[i]){
                return 0;
            }
        }
    }
    return 1;
}
 
int main(){
 
    int number;
   scanf("%d",&number);
   number++;
 
   while(1){
    if(checkYear(number)){
        printf("%d\n", number);
        break;
    }
    number++;
 
   }
}