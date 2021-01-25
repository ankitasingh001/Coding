/*
https://leetcode.com/problems/sum-of-two-integers/

Author @ankitasingh001

*/

class Solution {
public:
    int getSum(int a, int b) {
         
        int x =a;
        int y=b;
        while(y!=0)
        {
            //carry bits
            int carry = x&y;
            //xor 
            x = x^y;
            //shift carry bits
            y= carry<<1;
        }
        return x;
    }
};