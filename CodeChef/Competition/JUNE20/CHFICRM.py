''' https://www.codechef.com/JUNE20B/problems/CHFICRM

    Author @ankitasingh001 '''

from collections import defaultdict

t  = int(input())
for i in range(t):
    di = defaultdict(int)
    n = int(input())
    l= [int(item) for item in input().split(" ")] 
    for j in range(n):
        if(l[j]==5):
            di["5"] +=1
        elif(l[j]==10):
            di["5"] -=1
            di["10"] +=1
            if(di["5"] <0):
                print("NO")
                break
        elif(l[j]==15):
            if(di["10"]>0):
                di["10"] -=1
            elif(di["5"]>1):
                di["5"] -=2
            else:
                print("NO")
                break
        if(j==(n-1)):
            print("YES")
    

