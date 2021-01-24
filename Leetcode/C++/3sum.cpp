/* https://leetcode.com/problems/3sum/

    Author @ankitasingh001 

*/

/*
Please read the following for maps and undordered maps
https://www.geeksforgeeks.org/map-vs-unordered_map-c/

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
        set<vector<int> > set_of_vectors; 
        sort(nums.begin(),nums.end());
        map<int,int> intmap;
        int counter =0;
        
        for (int i=0;i<nums.size();i++)
        {
            intmap[nums[i]] +=1;
            int j=i+1,k=nums.size()-1;
            while(j<k)
            {
                if(nums[i]+nums[j]+nums[k]==0)
                {
                    vector<int> triplet{nums[i],nums[j],nums[k]};
                    sort(triplet.begin(),triplet.end());
                    set_of_vectors.insert(triplet);
                    j++;
                    k--;
                }
                if((nums[i]+nums[j]+nums[k]>0))
                    k--;
                if((nums[i]+nums[j]+nums[k]<0))
                    j++;
            }
            
        }
        triplets.assign(set_of_vectors.begin(),set_of_vectors.end());
        return triplets;
    }
};

//TEST CODE
int main()
{
	Solution s;
    vector<int> vect{-1,0,1,2,-1,-4}; 
    vector<int> vec1{0,0,0};
    string tmp = "ngxlkthsjuoqcpavbfdermiywz";
	vector<vector<int>> vec=s.threeSum(vect);
      
    // Displaying the 2D vector 
    for (int i = 0; i < vec.size(); i++) { 
        for (int j = 0; j < vec[i].size(); j++) 
            cout << vec[i][j] << " "; 
        cout << endl; 
    } 
	return 0;
}