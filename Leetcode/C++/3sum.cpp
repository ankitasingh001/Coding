/* https://leetcode.com/problems/3sum/

    Author @ankitasingh001 

*/

struct node
{
    int val =0;
};
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> triplets;
        sort(nums.begin(),nums.end());
        map<int,int> intmap;
        for (int i=0;i<nums.size();i++)
        {
            intmap[nums[i]] =1;
        }
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]>0)
                break;
            for(int j=i+1;j<nums.size();j++)
            {
                if(intmap[-(nums[i]+nums[j])]==1)
                    {
                        vector<int> triplet{nums[i],nums[j],intmap[-(nums[i]+nums[j])]};
                        triplets.push_back(triplet);
                        cout<<nums[i]<<" "<<nums[j]<<" "<<intmap[-(nums[i]+nums[j])]<<endl;
                    }

            }
        }
        return triplets;
    }
};

//TEST CODE
int main()
{
	Solution s;
    vector<int> vect{-1,0,1,2,-1,-4}; 
    string tmp = "ngxlkthsjuoqcpavbfdermiywz";
	s.threeSum(vect);
	return 0;
}