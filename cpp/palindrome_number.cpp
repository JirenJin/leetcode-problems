#include<iostream>
#include<cmath>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0) return false;
        if(x<10) return true;
        int x_tmp = x;
        int n = 0;
        while(x_tmp > 0){
            x_tmp /= 10;
            n += 1;
        }
        while(n > 1){
            int h = x / pow(10, n-1);
            int l = x - x/10*10;
            if(h!=l) return false;
            else{
                x = (x - h*pow(10, n-1) - l) / 10;
                n -= 2;
            }
        }
        return true;
    }
};

int main(){
    Solution a;
    int x = 16561;
    cout << boolalpha << a.isPalindrome(x);
    x = 1342;
    cout << boolalpha << a.isPalindrome(x);
}
