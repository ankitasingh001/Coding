/***
 * 
 * 
 * 
 * https://leetcode.com/problems/counting-bits/
 * 
 * author : ankitasingh@001
 * 
 * */

#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> countBits(int num) {
        //declare a vector of size num and initialise with 0
        vector<int> v;
        v.push_back(0);
        v.push_back(1);
        int k=0;
        for(int i=2;i<=num;i++)
        {
            if(!(i&(i-1))) //number is a power of 2 or not
            {
                k= i;
                v.push_back(1);
            }
            else
            {
                v.push_back(1+ v[i-k]);
            }
            
        }
        return v;
    }
};


//TEST CODE
int main()
{
	Solution s;
    vector<int> v=s.countBits(18);
    for(int i=0;i<v.size();i++)
        cout<<v[i]<< " ";
    cout<<endl;
	return 0;
}