/**
 * https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/
 * 
 * */

#include<bits/stdc++.h>
using namespace std;
#include<string.h>
class Solution {
public:
    int minimumLength(string s) {
        int len  = s.length();
        int i=0,j=len-1;
        while(i<j)
        {
            if(s[i]!=s[j])
                break;
            char c = s[i];
            while(s[i]==s[i+1])
            {
                i++;
                if(i==j)
                    return 0;
            }
            char cc = s[j];
            while(s[j]==s[j-1])
            {
                j--;
                if(j==i)
                    return 0;
            }
            if(s[i]==s[j])
            {
                if(j-i==1 || j==i)
                    return 0;
                i=i+1;
                j=j-1;
            }
        }
        return j-i+1;
    }
};