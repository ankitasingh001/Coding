/***
 * 
 * 
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 * 
 * author @ankitasingh001
 * 
 * */
#include<bits/stdc++.h>
#include<string.h>
using namespace std;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char,int> maps;
        int len = s.length();
        int k1=0,k2=0,max=0;
        for(int i=1;i<=len ;i++)
        {
            if(maps[s[i-1]]>0)
            {
                 k2= maps[s[i-1]];
                 if (max<(i-k2))
                    max= i-k2;
            }
            else
            {
                maps[s[i]]=i;
            }              
        }
        return max+1;
    }
};

int main()
{
    Solution s;
    cout<<s.lengthOfLongestSubstring("pwwkew");
}