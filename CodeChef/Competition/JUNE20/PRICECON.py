''' https://www.codechef.com/JUNE20B/problems/PRICECON

    Author @ankitasingh001 '''

# Easy 2 minute problem

t  = int(input())
for i in range(t):
    sum_price =0
    n,p = map(int, input().split(" "))
    l= [int(item) for item in input().split(" ")] 
    for j in range(n):
        #k = [input(), int(input())] 
        if(l[j]>p):
            sum_price +=(l[j]-p)
    print(sum_price)


