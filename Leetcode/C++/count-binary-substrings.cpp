/***
 * 
 * 
 * 
 * https://leetcode.com/problems/count-binary-substrings/
 * 
 * */
#include<bits/stdc++.h>
using namespace std;
#include<string.h>
class Solution {
public:
    int countBinarySubstrings(string s) {
        int len = length(s)
        int fir=0,sec=0;
        for(i=1;i<len;i++)
        {
            if(s[i]==s[i-1])
                fir++
            if(s[i]!=s[i+1])
        }
    }
};