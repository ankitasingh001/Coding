''' https://leetcode.com/problems/number-of-1-bits/

    Author @ankitasingh001 '''



# Solution by using lookup table in O(1) time

# Define lookup as global variable

my_lookup = [0]*256 # Max input length here assumed as 256 

for i in range(0,256):
    my_lookup[i] = (i&1)     + my_lookup[i//2]

class Solution:
    def hammingWeight(self, n):
        # Divide the entered string into bits of length 8 and sum the counts
        return (my_lookup[n & 0xff ] + my_lookup[(n>>8)& 0xff]+ my_lookup[(n>>16) & 0xff] +my_lookup[(n>>24)])


        