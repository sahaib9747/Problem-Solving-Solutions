#include <iostream>
#include <math.h>
using namespace std;
int main(){
    int tCase;
    cin >> tCase;
    
    while(tCase){
        int input;
        cin >> input;
        int x = sqrt(input);
        if (x * x== input){
            cout << "YES" << endl;
            
        }
        else{
            cout << "NO" << endl;
        }
        tCase--;
    }
    return 0;
}