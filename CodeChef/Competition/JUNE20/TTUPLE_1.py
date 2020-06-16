''' https://www.codechef.com/JUNE20B/problems/TTUPLE

    Author @ankitasingh001 '''


import numpy as np

def is_div(x,y):
    try:
        if (x%y !=0):
            return False
        if y==0:
            return False
        return True
    except ZeroDivisionError:
        return False

def div(x,y):
    return x//y

def singlemismatch(p,q,r,a,b,c):

    if (p==a and q==b) or (r==c and q==b ) or (p==a and r==c):
        return True
    return False

#Check if there are two mismatches -> to be done after running singlemismatch
def doublemismatch(p,q,r,a,b,c):

    if(p==a):
        return True
    if(q==b):
        return True
    if(r==c):
        return True
    return False

def check_div_equal(p,q,a,b):
    if is_div(a,p) and is_div(b,q):
        if div(a,p)==div(b,q):
            return True
    return False

def check_sum_equal(p,q,a,b):
    if (a-p) == (b-q):
        return True
    return False

#Try all three possibilities here
def fit_eqn_1(p,q,r,a,b,c):
    try:
        if is_div((b*p-a*q),(p-q)) and is_div((a-b),(p-q)):
            z = (b*p-a*q)//(p-q)
            k = (a-b)//(p-q)
            if(isinstance(z, int) and isinstance(k, int)):
                k1 = k*r +z
                k2 = k*r
                k3 = r+z
                if ( k1==c or k2==c or k3==c) :
                    return True
    except:
        return False
    return False

#Try all three possibilities here
def fit_eqn_2(p,q,r,a,b,c):
    if is_div((b*p-a*q),(a-b)) and is_div(a-b,p-q):
        z = (b*p-a*q)//(a-b)
        k = (a-b)//(p-q)
        if(isinstance(z, int) and isinstance(k, int)):
            k1 = k*(r+z)
            k2 = k*r
            k3 = r+z
            if ( k1==c or k2==c or k3==c) :
                return True
    return False


def check(p,q,r,a,b,c,stop=0):
    if stop>2:
        return stop
    if p==a and q==b and r==c :
        return stop
    #truefit,x,y = solve_equation(p,q,r,a,b,c)
    #if truefit and (x==1 or y==0):
     #   return stop+1
    if check_div_equal(q,r,b,c) and check_div_equal(p,r,a,c):
        return stop+1
    if (p-a) == (q-b) ==(r-c):
        return stop+1 
    if singlemismatch(p,q,r,a,b,c):
        return stop+1
    if doublemismatch(p,q,r,a,b,c):
        if(p==a):
            if check_div_equal(q,r,b,c) or check_sum_equal(q,r,b,c):
                return stop+1
        if(q==b):
            if check_div_equal(p,r,a,c) or check_sum_equal(p,r,a,c):
                return stop+1
        if(r==c):
            if check_div_equal(p,q,a,b) or check_sum_equal(p,q,a,b):
                return stop+1
        return stop+2
    if fit_eqn_1(p,q,r,a,b,c) or fit_eqn_1(q,r,p,b,c,a) or fit_eqn_1(r,p,q,c,a,b):
        return stop+2
    if fit_eqn_2(p,q,r,a,b,c) or fit_eqn_2(q,r,p,b,c,a) or fit_eqn_2(r,p,q,c,a,b):
        return stop+2
    else :
        k1,k2,k3,k4,k5,k6,k7,k8,k9 =3,3,3,3,3,3,3,3,3
        if is_div(a,p):
            k1 = check(a,q*a//p,r*a//p,a,b,c,stop+1)
            k4 = check(a,q,r*a//p,a,b,c,stop+1)
            k5 = check(a,q*a//p,r,a,b,c,stop+1)
        if is_div(b,q):
            k2 = check(p*b//q,b,r*b//q,a,b,c,stop+1)
            k6 = check(p,b,r*b//q,a,b,c,stop+1)
            k7 = check(p*b//q,b,r,a,b,c,stop+1)
        if is_div(c,r):
            k3 = check(p*c//r,q*c//r,c,a,b,c,stop+1)
            k8 = check(p,q*c//r,c,a,b,c,stop+1)
            k9 = check(p*c//r,q,c,a,b,c,stop+1)

        k10 =check(a,q+a-p,r+a-p,a,b,c,stop+1)
        k11 =check(p+b-q,b,r+b-q,a,b,c,stop+1)
        k12 = check(p+c-r,q+c-r,c,a,b,c,stop+1)
        k13 = check(a,q,r+a-p,a,b,c,stop+1)
        k14 = check(a,q+a-p,r,a,b,c,stop+1)
        k15 = check(p,b,r+b-q,a,b,c,stop+1)
        k16 = check(p+b-q,b,r,a,b,c,stop+1)
        k17 = check(p,q+c-r,c,a,b,c,stop+1)
        k18 = check(p+c-r,q,c,a,b,c,stop+1)
        return min(k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17,k18)
    return 3
#Test Cases

# print(check(10,20,30,15,35,40))
# print(check(2,3,5,18,20,24))
# print(check(0,2,0,0,0,0))
# print(check(2,2,2,6,7,7))


# print(fit_eqn_1(2,3,5,7,7,7))
# print(fit_eqn_2(2,3,5,7,7,7))

t  = int(input())
for i in range(t):
    p,q,r = map(int, input().split(" "))
    a,b,c = map(int, input().split(" "))
    print(check(p,q,r,a,b,c))



