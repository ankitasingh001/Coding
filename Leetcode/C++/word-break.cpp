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
        bool arr[len+1][len+1];
        memset(arr,false,sizeof(arr));
        int k=0,tmp=0;
        for(int i=0;i<wordDict.size();i++)
        {
            //cout<<wordDict[i]<<endl;
            dictionary[wordDict[i]]=true;
        }
        for(int i=0;i<len;i++)
        {
            string n(1,s[i]);
            arr[i][i] = dictionary[n];
            //cout<<(arr[i][i]);
        }
        tmp=1;
        for(int i=len-1;i>=0;i--)
        {
            k=tmp;
            for(int j=0;j<=i;j++)
            {   
                bool exists = false;
                for(int l=j;l<k;l++)
                    exists = exists || (arr[j][l]&&arr[l+1][k]);
                if((exists)||dictionary[s.substr(j,k-j+1)]) 
                    arr[j][k]= true;
                //cout<<arr[j][k]<< " ";
                k++;
            }
            tmp++;
            //cout<<endl;
        }
        return arr[0][len];
    }
};

//test
int main()
{
    Solution s;
    vector<string> vec{"a", "b"};
    string str="ab";
    cout<<s.wordBreak(str,vec);
}