/***
 * 
 * https://www.geeksforgeeks.org/reverse-bits/
 * 
 * Author :@ankitasingh001
 * 
 * 
 * 
 * **/
#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int k=0;
        int j=0;
        int s=0;
        for (int i=31;i>=0;i--)
        {
            k = (n>>i)&1;
            if(k!=0)
                s = (1<<j) | s;
            j++;
        }
        return s;
    }
};

//test results
int main()
{
    Solution s;
    int res = s.reverseBits(43261596);
    cout<<res<<endl;
    return 0;
}