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
        vector<int> arr(amount+1,-1);
        arr[0]=0;
        for(int i=0;i<coins.size();i++)
        {
            arr[coins[i]]=1;
        }
        for(int i=0;i<coins.size();i++)
        {
            for(int j=1;j<=amount;j++)
            {

            }
        }
    }
};