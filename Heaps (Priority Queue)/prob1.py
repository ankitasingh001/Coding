''' https://www.codechef.com/JULY17/problems/IPCTRAIN 

    Author @ankitasingh001 '''

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
           print(len_list)
           index = find_index(self.list,len_list,start)
           a,b = self.list[index-1][0],self.list[index-1][1]
           c,d = start,start+lectures-1
           if(not range_intersection(a,b,c,d)):
               self.list.insert(index-1,[c,d])
           while (range_intersection(a,b,c,d)):
               r1,r2 = merge_ranges(a,b,c,d)
            

l = [[1,3],[5,6],[8,8],[12,15],[17,20],[23,34]]           
print(find_index(l,6,22))

print(range_intersection(3,8,8,13))
print(merge_ranges(3,8,8,13))