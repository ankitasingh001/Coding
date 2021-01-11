''' https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

    Author @ankitasingh001 '''

class Solution:
    def maxProfit(self, prices):
        arr =[0]*len(prices)
        for i in range(0,len(prices)-1):
            arr[i] = prices[i+1]-prices[i]
        profit = self.maxSubArraySum(arr,len(arr))
        return profit

    def maxSubArraySum(self,a,size): 
       
        max_so_far = 0
        max_ending_here = 0
       
        for i in range(0, size): 
            max_ending_here = max_ending_here + a[i] 
            if (max_so_far < max_ending_here): 
                max_so_far = max_ending_here 
  
            if max_ending_here < 0: 
                max_ending_here = 0   
        return max_so_far 


# Test cases

S = Solution()
print(S.maxProfit([7,1,5,3,6,4]))
print(S.maxProfit([7,6,4,3,1]))