''' https://www.codechef.com/JUNE20B/problems/XYSTR

    Author @ankitasingh001 '''

# One minute problem

t  = int(input())
for i in range(t):
    count=0
    j=0
    string = input()
    while j < (len(string)-1):
        if (string[j]!=string[j+1]):
            count +=1
            j +=2
        else:
            j+=1
    print(count)
            