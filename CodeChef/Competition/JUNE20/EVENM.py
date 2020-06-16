
''' https://www.codechef.com/JUNE20B/problems/EVENM

    Author @ankitasingh001 '''


t  = int(input())
for i in range(t):
    n = int(input())
    for j in range(1,n+1):
        m= n*j
        if ((j&1)==0):
            for k in range(m,m-n,-1):
                print(k, end =" ") 

        else:
            for itr in range(m-n+1,m+1):
                print(itr, end =" ")
        print("")