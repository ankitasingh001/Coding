/***
 * 
 * 
 * https://leetcode.com/problems/longest-common-subsequence/
 * 
 * 
 * author "ankitasingh001"
 * */
#include<bits/stdc++.h>
#include<string.h>
using namespace std;
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int len1 = text1.length();
        int len2 = text2.length();
        int arr[len1+1][len2+1];

        for(int i=0;i<=len2;i++)
            arr[0][i]=0;
        for(int i=0;i<=len1;i++)
            arr[i][0]=0;

        for(int i=1;i<=len1;i++)
        {
            for(int j=1;j<=len2;j++)
            {
                if(text1[i-1]==text2[j-1])
                {
                    arr[i][j] =arr[i-1][j-1]+1;
                }
                else
                {
                    arr[i][j] = max(arr[i-1][j],arr[i][j-1]);
                }
                
            }
        }
        return arr[len1][len2];
    }
};

int main()
{
    Solution s;
    string x ="abc";
    string y ="def";
    cout<<s.longestCommonSubsequence(x,y);
}