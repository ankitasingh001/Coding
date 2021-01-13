/* https://leetcode.com/problems/verifying-an-alien-dictionary/

    Author @ankitasingh001 

*/

#include<bits/stdc++.h>
using namespace std;
#include<string.h>
#include<algorithm>

class Solution {

public:

    bool lexo_compare(string a,string b)
    {
        int l1 = a.length();
        int l2 = b.length();
        int len =  l1>l2 ? l1 :l2;
        for(int i=0;i<len;i++)
        {
            if ((i>l1)||(i>l2))
                break;
            if (a[i]<b[i])
                return true;
            else
            {
                if(a[i]==b[i])
                    continue;
                else
                {
                    return false;
                }
                
            }
            
        }
        return true;
    }
    bool isAlienSorted(vector<string>& words, string order) {
        unordered_map<char,char> charmap;
        for (int i =0;i<26;i++)
        {
            charmap[order[i]] = char(i+97);
        }
        for (int i =0;i<words.size();i++)
            {
                for (int j=0;j< words[i].length();j++)
                {
                    words[i][j] = charmap[words[i][j]];
                }
            }
    bool istrue = true;
    for (int i=0;i<words.size()-1;i++)
    {
        
        if (!lexo_compare(words[i],words[i+1]))
        {
            istrue = false;
            break;
        }
    }
	return istrue;
    }
};

//TEST CODE
int main()
{
	Solution s;
    string sa ="bc";
    string sb ="bc";
    vector<string> vect{"kuvp","q"}; 
    string tmp = "ngxlkthsjuoqcpavbfdermiywz";
	cout<<s.isAlienSorted(vect, tmp);
    //cout<<s.lexo_compare(sb,sa);
    cout<<"hello executed";
	return 0;
}
