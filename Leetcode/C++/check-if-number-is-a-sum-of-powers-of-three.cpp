#include<bits/stdc++.h>
#include<bits/stdc++.h>
using namespace std;
#include<cmath>
class Solution {
public:
    bool checkPowersOfThree(int n) {
    int k=0,l=0,s=n;
    map<int,int> hashint;
     while(true)
     {
        double kk = log(s)/log(3);
        cout<<kk<<" ";
        if(hashint[floor(kk)]==1)
            return false;
        if(kk<1 && k!=0)
            return false;
        if(kk - floor(kk)!=0)
        {
            s= s- pow(3,floor(kk));
            hashint[floor(kk)]=1;
        }
        else
        {
            return true;
        }

        
     }   
    }
};

int main()
{
    Solution s;
    cout<<s.checkPowersOfThree(21);
    return 0;
}