''' https://www.codechef.com/status/ANUMLA 

    Author @ankitasingh001 '''
# Python3 program to print sums of 
# all possible subsets. 
  
# Prints sums of all subsets of arr[l..r]
from collections import defaultdict
import copy
import math


# Calculate sum of all subsets
def subsetSums(arr, l, r,dupli_dict, sum = 0):      
    if (l > r): 
        dupli_dict[sum] -=1
        return    
    subsetSums(arr, l + 1, r,dupli_dict, sum + arr[l])   
    subsetSums(arr, l + 1, r,dupli_dict, sum) 

# Input subset in the dictionary form
t  = int(input())
for i in range(t):
    input_dict = defaultdict(int)
    dupli_dict = {}
    n = int(input()) 
    inp_list = list(map(int,input().strip().split()))[:pow(2,n)] 

    # Storing all sum values in subset as a dictionary 
    for inp in inp_list:
        input_dict[inp] +=1
    dupli_dict = input_dict.copy()
    reconstructed_list = []

    #Iterating and adding elements to the list one by one
    for k,v in sorted(input_dict.items()):
        if dupli_dict[k]>0:
            while(dupli_dict[k]>0):
                if(k==0 and dupli_dict[k]==1):
                    break
                dupli_dict= input_dict.copy()
                reconstructed_list.append(k)
                subsetSums(reconstructed_list, 0, len(reconstructed_list)-1,dupli_dict)
            if(len(reconstructed_list)>=n):
                break

    # Print reconstructed list
    for r in reconstructed_list:
        print(r, end = " ")
    print()
