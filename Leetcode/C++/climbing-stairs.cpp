/**
 * 
 * https://leetcode.com/problems/climbing-stairs/
 * 
 * author : @ankitasingh001
 * 
 * **/

#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int climbStairs(int n) {
        int v[n+1];
        v[0]=1;
        v[1]=1;
        for(int i=2;i<=n;i++)
        {
            v[i]=v[i-1]+v[i-2];
        }
        return v[n];
    }
};

int main()
{
    Solution s;
    int num = s.climbStairs(3);
    cout<<num<<endl;
}