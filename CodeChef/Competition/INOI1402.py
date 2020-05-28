''' https://www.codechef.com/INOIPRAC/problems/INOI1402

    Author @ankitasingh001 '''


# Solves all pair shortest path via Floyd Warshall Algorithm
import numpy as np
def floydWarshall(graph,V): 

    #dist = list(map(lambda i : map(lambda j : j , i) , graph)) 
    dist = np.array(graph)
    # K times to obtain minimum path    
    for k in range(V):  
        # pick all vertices as source one by one 
        for i in range(V):  
            # Pick all vertices as destination for the above picked source 
            for j in range(V):  
                # If vertex k is on the shortest path from  
                # i to j, then update the value of dist[i][j] 
                dist[i][j] = min(dist[i][j] ,dist[i][k]+ dist[k][j] )

    dist = np.where(dist ==np.inf , 0, dist) 

    #Finding minimum of all shortest paths
    maxi = 0
    for i in range(V):
        for j in range(V):
            if maxi<dist[i][j]:
                maxi =dist[i][j]

    return int(maxi)

#Taking input and printing required distance 

n,e = map(int, input().split(" "))
gr = np.full((n,n), np.inf)

# Initialise weights for both a->b and b->a
for i in range(e):
    v1,v2,w = map(int, input().split(" "))
    gr[v1-1][v2-1] = w
    gr[v2-1][v1-1] = w

# Initialise weights for a->a as 0
for i in range(n):
    gr[i][i] = 0

# Apply Floyd Warshall to get minimum distances between routes and then calculate maximum among them
print(floydWarshall(gr,n))

