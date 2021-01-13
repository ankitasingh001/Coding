/*  https://leetcode.com/problems/valid-parentheses/

   Author @ankitasingh001 
*/


#include<bits/stdc++.h>
using namespace std;
#include<string.h>
#include<algorithm>

class Solution {
public:
    void showstack(stack <char> s) 
    { 
        while (!s.empty()) 
        { 
            cout << '\t' << s.top(); 
            s.pop(); 
        } 
        cout << '\n'; 
    } 
    bool isValid(string s) {
        int l = s.length();
        stack<char> stck;
        for (int i=0;i<l;i++)
        {
            showstack(stck);
            cout<<endl;
            if(i==0)
            {
                stck.push(s[i]);
                continue;
            }
            if ( stck.top() == s[i])
                stck.pop();
            else
            {
                stck.push(s[i]);
            }
            
        }
        return stck.empty();
    }
};

//TEST CODE
int main()
{
	Solution s;
    string sa ="({})";
    cout<<s.isValid(sa);
    return 0;
}