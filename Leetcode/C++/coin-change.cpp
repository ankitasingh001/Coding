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
using namespace std;
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> arr(amount+1,999999999);
        arr[0]=0;
        for(int i=0;i<coins.size();i++)
        {
            arr[coins[i]]=1;
        }
        for(int i=1;i<=amount;i++)
        {
            for(int j=0;coin[j]<i;j++)
            {
                int coin = coins[j];
                arr[i] = min(arr[i],1+arr[i-coin]);
            }
        }
    }
};