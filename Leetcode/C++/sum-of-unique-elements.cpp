/**
 * 
 * 
 * 
 * https://leetcode.com/problems/sum-of-unique-elements/
 * 
 * */
class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        map<int,int> maps;
        int count=0;
        for(int i=0;i<nums.size();i++)
        {
            maps[nums[i]] +=1;
        }
        for(auto i:maps)
        {
            if(i.second ==1)
                count=count+i.first;
        }
        return count;
    }
};