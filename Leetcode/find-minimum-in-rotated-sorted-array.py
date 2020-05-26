''' https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

    Author @ankitasingh001 

'''

#Solution in O(logn) time

class Solution:
    def findMin(self, nums):
        l=0
        r = len(nums)-1
        while(l<r):
            mid = (l+r) //2
            if nums[mid]>nums[r]:
                l = mid
            else:
                r = mid
            if (l == r+1)or (r== l+1):
                return min(nums[l],nums[r])

# Test cases 

S = Solution()
print(S.findMin([3,4,5,1,2] ))
print(S.findMin([4,5,6,7,0,1,2]))   



