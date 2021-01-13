/*
    https://leetcode.com/problems/maximum-product-of-word-lengths/

    Author @ankitasingh001 
*/

#include<bits/stdc++.h>
using namespace std;

struct Node
{
    int val =0;
};

class Solution {
public:
    int maxProduct(vector<string>& words) {
        int len = words.size();
        //unordered_map<char,Node> *charmap = new unordered_map<char,Node>[len];
        int *charmap = new int[len];
        memset(charmap, 0, sizeof(charmap));
        for(int i=0;i<len;i++)
        {
            for(int j=0;j<words[i].length();j++)
            {
                //cout<<((int)words[i][j]-96)<<endl;
                charmap[i] =  (1 << ((int)words[i][j]-96)) | charmap[i];
            }
        }
        long unsigned int max =0;
        for (int i=0;i<len;i++)
            {
                for (int j=i+1;j<len;j++)
                {
                    // bitset<26> y(charmap[i]);
                    // bitset<26> z(charmap[j]);
                    // cout<<"loop"<<endl;
                    // cout<<y<<endl<<z<<endl;
                    if(!((charmap[i]&charmap[j])))
                    {
                        long unsigned int prod = words[i].length()*words[j].length();
                        if(prod>max)
                            max= prod;
                    }
                }
            }
        return max;
    }
};

int main()
{
    Solution s;
    string sa ="bc";
    string sb ="bc";
    vector<string> vect{"abcw","baz","foo","bar","xtfn","abcdef"}; 
    string tmp = "ngxlkthsjuoqcpavbfdermiywz";
	cout<<s.maxProduct(vect);
    return 0;
}