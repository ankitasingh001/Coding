''' https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

    Author @ankitasingh001 

'''

#Solution in O(logn) time

class Solution:
    def findMin(self, nums):
        l=0
        r = len(nums)-1
        if(r==0):
            return nums[r]
        while(l<r):
            if (l == r+1)or (r== l+1) :
                return min(nums[l],nums[r])
            mid = (l+r) //2
            if nums[mid]>nums[r]:
                l = mid
            else:
                r = mid
            
# Test cases 

S = Solution()
print(S.findMin([1]))
print(S.findMin([0,1,2,3,4,5,6,7]))   



