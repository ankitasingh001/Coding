''' https://leetcode.com/problems/container-with-most-water/

    Author @ankitasingh001 

'''
# O(n) solution

class Solution:
    # Increment left/right after comparision
    def maxArea(self, height):
        l=0
        r =len(height)-1
        area = 0
        while(l<r):
            tmp = (min(height[l],height[r]))*(r-l)
            area  = max(tmp,area)
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
        return area

# Test cases 

S = Solution()
print(S.maxArea( [1,8,6,2,5,4,8,3,7]))



        