''' https://www.codechef.com/JUNE20B/problems/TTUPLE

    Author @ankitasingh001 '''

def sumcheck(p,q,r,a,b,c):
    if((a-p)==(b-q)and r==c):
        return True
    return False


def prodcheck(p,q,r,a,b,c):
    if((a//p)==(b//q)and (r==c)and(a%p ==0) and (b%q==0)):
        return True
    return False

def allcheck(a,b,c,p,q,r,stop=0):
    if((p==a)and q==b):
        return 1
    if((p!=a)and (q!=b)):
        if (p-a)==(q-b): 
            return 2
        if((a%p ==0) and (b%q==0) and (a//p == b //q)):
            return 2
    if(stop ==0):
        return min(allcheck(c,a,b,r,a-b+q,b,1),allcheck(c,b,a,r,b-a+p,a,1),allcheck(c,a,b,r,(a//b)*q,b,1),allcheck(c,b,a,r,(b//a)*p,a,1))
    return 3

def triplecheck(a,b,c,p,q,r):
    if((p==a)and (q==b) and(r==c)):
        return 0
    elif(((a//p)==(b//q)==(c//r)) and (c%r==0)and(a%p ==0) and (b%q==0)):
        return 1
    elif((p-a)==(q-b)==(r-c)):
        return 1
    elif(prodcheck(p,q,r,a,b,c) or prodcheck(q,r,p,b,c,a) or prodcheck (r,p,q,c,a,b)):
        return 1
    elif(sumcheck(p,q,r,a,b,c) or sumcheck(q,r,p,b,c,a) or sumcheck(r,p,q,c,a,b)):
        return 1
    else:
        return (min(allcheck(a,b,c,p,q,r,0),allcheck(b,c,a,q,r,p,0),allcheck(c,a,b,r,p,q,0)))


t  = int(input())
for i in range(t):
    p,q,r = map(int, input().split(" "))
    a,b,c = map(int, input().split(" "))
    print(triplecheck(a,b,c,p,q,r))