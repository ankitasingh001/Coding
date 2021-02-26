/**
 * 
 * 
 * https://leetcode.com/problems/house-robber-ii/
 * 
 * */
 

#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int robonce(vector<int>& nums) {
        int len =nums.size();
        if(len==0)
            return 0;
        if(len==1)
            return nums[0];
        int temp[len];
        int max_so_far = nums[0];
        temp[0]= nums[0];
        temp[1] = nums[0]>nums[1]?nums[0]:nums[1];
        for(int i=2;i<nums.size();i++)
        {
            temp[i] = (temp[i-2]+nums[i])>temp[i-1]?(temp[i-2]+nums[i]):temp[i-1];
        }
        return temp[len-1];
    }
    int rob(vector<int>& nums) {
        /* Remember this*/
        if(nums.size()==1)
            return nums[0];
        vector<int> nums1 = nums;
        vector<int>::iterator it,it1;
          it = nums.begin();
          nums.erase(it);
          it1 = nums1.end();
          nums1.erase(it1-1);
          return max(robonce(nums),robonce(nums1));
         return 1;
    }
};

int main()
{
    Solution s;
    vector<int> v{1,3,6,9,50,3,5,50};
    cout<<s.rob(v);
    return 0;
}