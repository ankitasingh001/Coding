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
        //sort(nums.begin(),nums.end());
        map<int,int> intmap;
        int counter =0;
        for (int i=0;i<nums.size();i++)
        {
            intmap[nums[i]] +=1;
        }
        for(auto i = intmap.begin();i!= intmap.end();i++)
        {   
            counter++;
            if(i->first>0)
                break;
            for (auto j = next(i);j!= intmap.end();j++)
            {
                
                if (i->second>=1)
                {
                    if(j->first>0)
                        break;
                    int subint= -(i->first+ j->first);
                    int hashint = intmap[subint];
                    //cout<<"here i am "<<i->first<<" "<<j->first<<" "<<hashint<<endl;
                    if((hashint >0))
                    {
                        vector<int> triplet{i->first,j->first,-(i->first+ j->first)};
                        set_of_vectors.insert(triplet);
                    }
                }
                if (i->second >1)
                {
                    /* code */
                    //cout<<"greater = "<<i->first<<endl;
                    int subint= -(i->first)*2;
                    int hashint = intmap[subint];
                    if((hashint >0))
                    {
                        vector<int> triplet{i->first,i->first,-(i->first+ i->first)};
                        set_of_vectors.insert(triplet);
                    }
                }
               
                
            }
             if(i->second >2 && i->first==0)
                    {
                        vector<int> triplet{0,0,0};
                        set_of_vectors.insert(triplet);
                    }
        }
        //cout<<"value of counter = "<<counter<<endl;
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
	vector<vector<int>> vec=s.threeSum(vec1);
      
    // Displaying the 2D vector 
    for (int i = 0; i < vec.size(); i++) { 
        for (int j = 0; j < vec[i].size(); j++) 
            cout << vec[i][j] << " "; 
        cout << endl; 
    } 
	return 0;
}