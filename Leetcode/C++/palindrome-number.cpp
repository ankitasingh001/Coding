''' https://leetcode.com/problems/palindrome-number/

    Author @ankitasingh001 

'''
class Solution {
public:
    bool isPalindrome(int x) {
        long long int t =x;
        long long int s=0;
        while(t>0)
        {
            long long int k = t%10;
            s = s*10+ k;
            t=t/10;
        }
        if(s==x)
            return true;
        return false;
    }
};
