/**
 * 
 * https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
 * 
 * author @ankitasingh001
 * 
 * */

#include<climits>
#include<bits/stdc++.h>
class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
    int max_so_far_pos = INT_MIN, max_ending_here_pos = 0;
    int max_so_far_neg= INT_MIN ,max_ending_here_neg =0;
    vector<int> nums_neg(nums.size());
    for (int i = 0;i < nums.size(); i++) 
    { 
        nums_neg[i]= -nums[i];
    }
    for (int i = 0;i < nums.size(); i++) 
    { 
        max_ending_here_pos = max_ending_here_pos + nums[i]; 
        if (max_so_far_pos < max_ending_here_pos) 
            max_so_far_pos = max_ending_here_pos; 
  
        if (max_ending_here_pos < 0) 
            max_ending_here_pos = 0; 
        
    }
    for (int i = 0;i < nums_neg.size(); i++) 
    { 
        max_ending_here_neg = max_ending_here_neg + nums_neg[i]; 
        if (max_so_far_neg < max_ending_here_neg) 
            max_so_far_neg = max_ending_here_neg; 
  
        if (max_ending_here_neg < 0) 
            max_ending_here_neg = 0; 
        
    }
    return max(max_so_far_pos,max_so_far_neg); 
    }
};