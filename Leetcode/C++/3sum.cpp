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
        set<vector<int> > set_of_vectors; 
        sort(nums.begin(),nums.end());
        map<int,int> intmap;
        for (int i=0;i<nums.size();i++)
        {
            intmap[nums[i]] +=1;
        }
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]>0)
                break;
            for(int j=i+1;j<nums.size();j++)
            {
                int subint= -(nums[i]+nums[j]);
                int hashint = intmap[subint];
                if((hashint ==1 && nums[i]!= subint && nums[j]!= subint )) //|| (hashint>1 && (nums[i]==subint || nums[j]==subint))
                    {
                        vector<int> triplet{nums[i],nums[j],intmap[-(nums[i]+nums[j])]};
                        set_of_vectors.insert(triplet);
                        //cout<<nums[i]<<" "<<nums[j]<<" "<<-(nums[i]+nums[j])<<endl;
                    }

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