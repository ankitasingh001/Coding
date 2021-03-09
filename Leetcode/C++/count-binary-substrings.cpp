/***
 * 
 * 
 * 
 * https://leetcode.com/problems/count-binary-substrings/
 * 
 * */
#include<bits/stdc++.h>
using namespace std;
#include<string.h>
class Solution {
public:
    int countBinarySubstrings(string s) {
        int len = s.length();
        int fir=0,sec=0,sum=0;
        char k = s[0];
        fir=1;
        bool turn1= false;
        bool turn2 = false;
        for(int i=1;i<len;i++)
        {
           if(s[i]==s[i-1])
              fir++;

           if(s[i]!=s[i-1] && turn1 == false)
              {
                  turn1 =true;
                  sec = fir;
                  fir =1;
              }
            if(s[i]!=s[i-1] && turn1 == true)
                {
                    //turn1 = false;
                    sum += (fir<sec?fir:sec);
                    fir =1;
                if(i==(len-1))
                    break;
                }
         if(i==(len-1))
           {
               sum += (fir<sec?fir:sec);
               break;
           }
        }
        return sum;
    }
};