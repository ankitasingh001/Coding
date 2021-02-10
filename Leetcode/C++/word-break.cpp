/**
 * 
 * 
 * https://leetcode.com/problems/word-break/
 * 
 * author @ankitasingh001
 * 
 * */
#include<string.h>
#include<bits/stdc++.h>
#include<stdlib.h>
using namespace std;
class Solution {
    
public:
    bool isInDictionary(string word, map<string,bool> &dict)
    {
        if(dict.find(word) != dict.end())
            return true;
        else
            return false;
    }

    bool wordBreak(string s, vector<string>& wordDict) {
        map<string,bool> dictionary ;
        int len = s.length();
        bool arr[len][len];
        memset(arr,false,sizeof(arr));
        int k=0,tmp=0;
        for(int i=0;i<wordDict.size();i++)
        {
            cout<<wordDict[i]<<endl;
            dictionary[wordDict[i]]=true;
        }
        for(int i=0;i<len;i++)
            arr[i][i] = dictionary[to_string(s[i])];
        tmp=1;
        for(int i=len-1;i>=0;i--)
        {
            k=tmp;
            for(int j=0;j<=i;j++)
            {   
                //cout<<"values = "<<j<<" "<<k<<" ";
                //cout<<arr[j][k-1]<<" "<<arr[j+1][k]<<" "<<s.substr(j,k-j+1)<<" end ";
                if(arr[j][k-1]||arr[j+1][k]||dictionary[s.substr(j,k-j+1)])
                    arr[j][k]= true;
                k++;
                cout<<arr[j][k]<< " ";
            }
            tmp++;
            cout<<endl;
        }
        return arr[len-1][len-1];
    }
};

//test
int main()
{
    Solution s;
    vector<string> vec{"cats", "dog", "sand", "and", "cat"};
    string str="catsandog";
    cout<<s.wordBreak(str,vec);
}