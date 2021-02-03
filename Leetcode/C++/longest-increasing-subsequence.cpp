/**
 * 
 * https://leetcode.com/problems/longest-increasing-subsequence/
 * 
 * author @ankitasingh001
 * 
 * */

#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int len = nums.size();
        int arr[len];
        int overall_max=0;
        for(int i=0;i<len;i++)
        {
            arr[i]=1;
            int maxi =1;
            for(int j=0;j<i;j++)
            {
                if(nums[i]>nums[j])
                {
                    maxi= max(maxi,arr[i]+arr[j]);
                }
            }
            arr[i]= maxi;
            //cout<<arr[i]<<" ";
            if(overall_max<arr[i])
                overall_max = arr[i];
        }
        return overall_max;
    }
};

int main()
{
    vector<int> v{1,3,6,7,9,4,10,5,6};
    Solution s;
    cout<<s.lengthOfLIS(v)<<endl;

}