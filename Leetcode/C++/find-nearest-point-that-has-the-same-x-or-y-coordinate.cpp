#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int nearestValidPoint(int x, int y, vector<vector<int>>& points) {
        int min = 99999999,i=0,k=-1,sum=0;
        for (auto &row:points)
        {
          if ((row[0]==x)||(row[1]==y))
          {
              sum = abs(x-row[0])+abs(y-row[1]);
              if(min>sum)
              {
                min=sum;
                k=i;
              }
          }
          i++;
    }
    return k;
    }
};