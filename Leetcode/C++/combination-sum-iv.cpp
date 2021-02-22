/**
 * 
 * https://leetcode.com/problems/combination-sum-iv/
 * 
 * 
 * author :ankitasingh001
 * **/

#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        int arr[target+1];
        sort(nums.begin(), nums.end()); 
        memset(arr,0,sizeof(arr));
        arr[0]=1;
        for(int i=1;i<=target;i++)
        {
            for(int j=0;j<nums.size();j++)
            {
                if((i-nums[j])<0)
                    break;
                // Calculate sum till each point
                arr[i] += arr[i-nums[j]];
                cout<<arr[i]<<" ";
            }
            cout<<arr[i]<<endl;
        }
        return arr[target];
    }
};

int main()
{
    Solution s;
    vector<int> n{3,33,333};
    cout<<s.combinationSum4(n,10000);
}