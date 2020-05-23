''' https://www.codechef.com/JULY17/problems/IPCTRAIN 

    Author @ankitasingh001 '''
# Using dictionary for priority data
from collections import defaultdict
import sys

## UTILITY FUNCTIONS FOR MAIN CODE ##

# Check if ranges (a,b) and (c,d) intersect or not
def range_intersection(a,b,c,d):
    if (a>=c-1 and a<=d ) or ((b>=c-1) and (b<=d)):
        return True
    if (c>=a-1 and c<=b ) or ((d>=a-1) and (d<=b)):
        return True
    return False

# Merge ranges (a,b) and (c,d) if they intersect
def merge_ranges(a,b,c,d):
    k = a if a < c else c
    tot_dist = (b-a)+(d-c)+1
    return k,k+tot_dist

# Binary search within list to find appropriate index to put the range
def find_index(list,len_list,start):
    l=0
    r=len_list
    while l<r :
        mid = (l + r )// 2
        #if list[mid][0]== start :
         #   return mid

        if list[mid][0] <=start :
            l = mid + 1
        else :
            r = mid 
    return l



# Store all alloted ranges in format [[2,3],[5,8],[12,16]] and so on..

class add_lec:

    # Initialise list,total sadness and maximum range of days allowed
    def __init__(self,max_range): 
        self.list= [] 
        self.max_Range = max_range
        self.total_sad = 0
    
    # Add sadness as required
    def add_sadness(self,start,lectures,sadness):
        if self.list == []:
            if(start + lectures-1 > self.max_Range):
                self.total_sad += (start +lectures-1-self.max_Range)*sadness
                self.list.append([start,self.max_Range])
            else:
                self.list.append([start,start+lectures-1])
        else:
            len_list = len(self.list)
            index = find_index(self.list,len_list,start)
            index_one = index
            a,b = self.list[index_one-1][0],self.list[index_one-1][1]
            c,d = start,start+lectures-1
            added =False
                

            while (range_intersection(a,b,c,d)):
                added = True
                r1,r2 = merge_ranges(a,b,c,d)
                del self.list[index_one-1] 
                if(index_one+1>len(self.list) or index_one<=0):
                    break
                a,b = self.list[index_one-1][0],self.list[index_one-1][1]
                c,d = r1,r2
            
            if(added is True):
                if r2>self.max_Range :
                    insert_index = find_index(self.list,len(self.list),r1)
                    self.total_sad += (r2-self.max_Range )*sadness
                    self.list.insert(insert_index,[r1,self.max_Range])
                else:
                    insert_index = find_index(self.list,len(self.list),r1)
                    self.list.insert(insert_index,[r1,r2])

            if(index_one <len_list and added is False):
                a,b = self.list[index_one][0],self.list[index_one][1]
                while (range_intersection(a,b,c,d)):
                    added = True
                    r1,r2 = merge_ranges(a,b,c,d)
                    del self.list[index_one] 
                    if(index_one+1>len(self.list) ):
                        break
                    a,b = self.list[index_one][0],self.list[index_one][1]
                    c,d = r1,r2
                if(added is True):
                    if r2>self.max_Range:
                        insert_index = find_index(self.list,len(self.list),r1)
                        self.total_sad += (r2-self.max_Range )*sadness
                        self.list.insert(insert_index,[r1,self.max_Range])
                    else:
                        insert_index = find_index(self.list,len(self.list),r1)
                        self.list.insert(insert_index,[r1,r2])

            if(added is False):
                if d>self.max_Range:
                    self.total_sad += (d-self.max_Range)*sadness
                    self.list.insert(index,[c,self.max_Range])
                else:
                    self.list.insert(index,[c,d])

    def print_var(self):
        print("LIST =",self.list)
        print("TOTAL SADNESS =",self.total_sad)
        print("RANGE ALLOWED = ",self.max_Range)



# l = [[1,3],[5,6],[8,8],[12,15],[17,20],[23,34]]           
# print(find_index(l,6,8))

# print(range_intersection(3,4,1,5))
# print(merge_ranges(3,4,1,5))

# tmp = add_lec(5)
# tmp.add_sadness(1,1,150)
# tmp.print_var()
# tmp.add_sadness(5,2,200)
# tmp.print_var()
# tmp.add_sadness(2,4,100)
# tmp.print_var()

# my_dict = defaultdict(list)
# #my_dict[200]=[[2,5]]
# my_dict[400].append([5,5])
# my_dict[200].append([7,8])
# for k,v in sorted(my_dict.items()):
#     for j in v:
#         print(j)
# print(my_dict)

n  = int(input())
for i in range(n):
    l1,l2 = map(int, input().split(" "))   
    my_dict = defaultdict(list)
    rep = add_lec(l2)
    for r in range(l1):
        start,lect,sadness = map(int, input().split(" "))
        my_dict[sadness].append([start,lect])
    for k,v in sorted(my_dict.items(),reverse=True):
        for j in v:
            rep.add_sadness(j[0],j[1],k)
    print(rep.total_sad)