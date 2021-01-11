''' https://leetcode.com/problems/two-sum/

    Author @ankitasingh001 '''

#Using dictionary to find solution in O(n) time

from collections import defaultdict

class Solution:
    def twoSum(self, nums,target):
        d =defaultdict(int)
        for i in nums:
            d[i]=1
        for i in range(len(nums)):
            if d[nums[i]]+d[target-nums[i]] == 2:
                dest = target -nums[i]
                pos =i
                break
        for i in range(len(nums)):
            if nums[i]== dest:
                pos2 =i
                break
        return[pos,pos2]
        
S = Solution()
print(S.twoSum([2,7,11,15],9))