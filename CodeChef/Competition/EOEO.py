''' https://www.codechef.com/JUNE20B/problems/EOEO

    Author @ankitasingh001 '''


t  = int(input())
for i in range(t):
    n = int(input())
    if (n%2 ==1):
        print(n//2)
    else:
        while(n%2 ==0 ):
            n = n>>1

        print(n//2)

