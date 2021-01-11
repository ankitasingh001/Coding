''' https://leetcode.com/problems/max-dot-product-of-two-subsequences/

    Author @ankitasingh001 

'''

'''
Time -> O(n^2)
Runtime: 300 ms, faster than 99.23% of Python3 online submissions for Max Dot Product of Two Subsequences.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Max Dot Product of Two Subsequences.
'''

class Solution:
    def maxDotProduct(self, nums1, nums2):
        # Larger one should be arr1

        if (len(nums1) >len(nums2)):
            arr1 = nums1
            arr2 = nums2
        else:
            arr1 = nums2
            arr2 = nums1
        
        len1 = len(arr1)
        len2 = len(arr2)

        #Initialising array with minimum values in a way the algo works
        minimum =min(0,arr1[0],arr2[0])

        max_prev = [minimum]*(len1+1)
        max_curr = [0]*(len1)
        max_curr.insert(0,minimum)

        # For each inserted element in the second array see if the new max value is better than old 
        for j in range (0,len2):
            for i in range (0,len1):
                # To counter minimum (negative) value added when not needed
                if ((max_prev[i]== minimum)):
                    max_curr[i+1] = max(max_prev[i+1],(arr1[i]*arr2[j]),max_curr[i])
                else:
                    max_curr[i+1] = max(max_prev[i+1],max_prev[i]+(arr1[i]*arr2[j]),max_curr[i])
            
            max_prev = max_curr.copy() 
            print(max_curr)   

        return max_curr[len1]

# Test cases :

S = Solution()
print(S.maxDotProduct([2,1,-2,5],[3,0,-6]))  
print(S.maxDotProduct([3,-2],[2,-6,7]))
print(S.maxDotProduct([-1,-1],[1,1]))
print(S.maxDotProduct([-5,-1,-2],[3,3,5,5]))
print(S.maxDotProduct([-3,-8,3,-10,1,3,9],[9,2,3,7,-9,1,-8,5,-1,-1]))

        