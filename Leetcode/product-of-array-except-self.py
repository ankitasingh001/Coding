''' https://leetcode.com/problems/product-of-array-except-self/

    Author @ankitasingh001 '''

'''
Note : Division operator not to be used and time complexity = O(n)
Possible methods :
  1. Use log-antilog
  2. Use pow because x/y = xy^-1
  3. Use two arrays to store forward /backward product
'''



class Solution:
    def productExceptSelf(self, nums):
        arr = [1]*(len(nums)+1)
        arr1 = [1]*len(nums)
        k=1
        kk=1
        for i in reversed(range(0,len(nums))):
            k *= nums[i]
            arr[i] =k
        for i in range(len(nums)):
            arr1[i] = kk * arr[i+1]
            kk = kk* nums[i]
        return arr1


'''Test cases:'''

S = Solution()
print(S.productExceptSelf([2,7,11,15]))


        
            