''' https://leetcode.com/problems/maximum-subarray/

    Author @ankitasingh001 '''

'''
1. Kadane's algorithm -> best way also applied in buy and sell stock problem
2. This is D&C mechanism
'''

class Solution:
    def maxSubArray(self, nums):
        return self.max_subarray(nums,0,len(nums)-1)

    def find_max_including_mid(self,arr,left,right,mid):
        right_sum = 0
        left_sum  = 0
        max_right = -9999 # Not taking array values as sum might be less than an array element
        max_left  = -9999 # Ideally should be - infinity

        # Find maximum sum of right side of array

        for i in range(mid,left-1,-1):
            left_sum = left_sum+ arr[i]
            if(left_sum>max_left):
                max_left =left_sum
        
        # Find maximum sum of left side of array

        for i in range(mid+1,right+1):
            right_sum =right_sum+arr[i]
            if(right_sum>max_right):
                max_right = right_sum

        return(max(max_left,max_right,max_left+max_right))

    def max_subarray(self,arr,l,r):
        if l==r :
            return arr[l]

        m = (l+r)//2

        return (max(self.max_subarray(arr,l,m),self.max_subarray(arr,m+1,r),self.find_max_including_mid(arr,l,r,m)))

#Test cases

S = Solution()
print(S.maxSubArray([2,3, -4, 5, -7]))