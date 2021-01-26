/*
https://leetcode.com/problems/sum-of-two-integers/

Author @ankitasingh001

*/

#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int getSum(int a, int b) {
         
        int x =a;
        int y=b;
        while(y!=0)
        {
            //carry bits
            //unsigned int because it did not work on leetcode compiler
            int carry =(unsigned int) x & (unsigned int)y;
            //xor 
            x = (unsigned int)x^(unsigned int)y;
            //shift carry bits
            y= (unsigned int)carry<<1;
        }
        return x;
    }
};


//TEST CODE
int main()
{
	Solution s;
    int vec=s.getSum(2,-6);
    cout<<(vec)<<endl;
	return 0;
}