/**
 * 
 * 
 * https://leetcode.com/problems/coin-change/
 * 
 * Author @ankitasingh001
 * 
 * **/
#include<bits/stdc++.h>
#include<math.h>
#include<stdint.h>
#include<limits.h>
using namespace std;
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector <int> arr(amount+2,INT_MAX);
        arr[0]=0;
        for(int i=0;i<coins.size();i++)
        {
            arr[coins[i]]=1;
        }
        for(int i=1;i<=amount;i++)
        {
            for(int j=0;j<coins.size();j++)
            {
                if(arr[i-coins[j]]!= INT_MAX)
                {
                    arr[i] = min((arr[i-coins[j]]+1),arr[i]);
                }
            }
        }
        if(arr[amount]== INT_MAX)
            return -1;
        return arr[amount];
    }
};
/***
 * Code that ran on leetcode (some case modifications)
 * */
//test

#include<bits/stdc++.h>
#include<math.h>
#include<stdint.h>
#include<limits.h>
using namespace std;
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector <long> arr(amount+2,999999);
        sort(coins.begin(),coins.end());
        arr[0]=0;
        for(int i=1;i<=amount;i++)
        {
            for(int j=0;j<coins.size()&&coins[j]<=i;j++)
            {
                arr[coins[j]]=1;
                if((i-coins[j])>0 && arr[i-coins[j]] != 999999)
                {
                   arr[i] = min((arr[i-coins[j]]+1),arr[i]);
                }
            }
        }
        if(arr[amount]== 999999)
            return -1;
        return arr[amount];
    }
};

int main()
{
    vector<int> v{1};
    Solution s;
    cout<<s.coinChange(v,0)<<endl;

}