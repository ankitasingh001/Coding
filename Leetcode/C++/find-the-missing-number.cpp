/***
 * 
 * https://www.geeksforgeeks.org/find-the-missing-number/
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
    int missingNumber(vector<int>& nums) {
        int a=0;
        int b=0;
        for(int i=0;i<nums.size();i++)
        {
            a =a ^ nums[i];
        }
        for(int i=0;i<nums.size()+1;i++)
        {
            b=b^i;
        }
        return a^b;
    }
};

//test results
int main()
{
    Solution s;
    vector<int> vect{0,1,4,5,3};
    int res = s.missingNumber(vect);
    cout<<res<<endl;
    return 0;
}