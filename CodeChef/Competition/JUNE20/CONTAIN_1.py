''' https://www.codechef.com/JUNE20B/problems/CONTAIN

    Author @ankitasingh001 '''

import numpy as np
import math
from scipy import spatial


RIGHT = "RIGHT"
LEFT = "LEFT"

def inside_convex_polygon(point, vertices):
    previous_side = None
    n_vertices = len(vertices)
    for n in range(n_vertices):
        a, b = vertices[n], vertices[(n+1)%n_vertices]
        affine_segment = v_sub(b, a)
        affine_point = v_sub(point, a)
        current_side = get_side(affine_segment, affine_point)
        if current_side is None:
            return False 
        elif previous_side is None: 
            previous_side = current_side
        elif previous_side != current_side:
            return False
    return True

def get_side(a, b):
    x = cosine_sign(a, b)
    if x < 0:
        return LEFT
    elif x > 0: 
        return RIGHT
    else:
        return None

def v_sub(a, b):
    return (a[0]-b[0], a[1]-b[1])

def cosine_sign(a, b):
    return a[0]*b[1]-a[1]*b[0]





def convex_hull(points):
    
    if len(points) <= 2:
        return points
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []

    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
            lower.pop()

        lower.append(p)

    upper = []
    rev_points = points[::-1] 
    for p in rev_points:

        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
            upper.pop()

        upper.append(p) 

    if (np.array(upper[1]==lower[len(lower) - 2])).all():
       return np.array(points[0:len(upper)])
        
    return np.array(lower[:-1] + upper[:-1])


def count_layer_num(hull,candle,count):
    if(inside_convex_polygon(candle,hull)):
        return count,True
    return count,False

def ret_layer(points,candles,num):

    count =0
    count_arr = np.zeros(num,int)
    track_arr = np.ones(num, dtype=bool)
    points = points[np.lexsort(np.rot90(points))]

    while(len(points)>2):
        hull = convex_hull(points)
        for idx,candle in enumerate(candles):
            if(track_arr[idx]):
                count_arr[idx],track_arr[idx] = count_layer_num(hull,candle,count)

        if((~track_arr).all()):
            break

        a1_rows = points.view([('', int)] * points.shape[1])
        a2_rows = hull.view([('',int)] * hull.shape[1])
        points =np.setdiff1d(a1_rows, a2_rows).view(points.dtype).reshape(-1, points.shape[1])
        count +=1

    count_arr[track_arr == True] = count
    return count_arr



t  = int(input())
for i in range(t):
    n,p = map(int, input().split(" "))
    arr =  np.empty((0,2), int)
    inp =  np.empty((0,2), int)
    for j in range(n):
        x,y = map(int, input().split(" "))
        arr = np.append(arr, [[x,y]], axis=0)
    for j in range(p):
        x,y = map(int, input().split(" "))
        inp = np.append(inp, [[x,y]], axis=0)
    s =ret_layer(np.array(arr,dtype=int),np.array(inp,dtype=int),p)
    for m in s:
      print(m)

# print (convex_hull([(0, 0), (2, 2), (2, 0),(0, 1),(0,2),(1,2),(1,0),(2,1),(1,1)]))
# print(inside_convex_polygon([1,0],[[0, 0], [1, 0], [2, 0],[2, 1],[2,2],[1,2],[0,2],[0,1]]))


# print(inside_convex_polygon([3,4],[[1,1],[2,2],[5,5],[9,9],[0,9]]))
# print(convex_hull([[1,1],[2,2],[5,5],[9,9],[0,9]]))

# points = np.array([[0,0],[1,1],[2,1],[7,0],[7,1],[7,7],[0,7],[3,4],[3,6],[4,2],[4,4],[5,1],[5,4],[5,5],[6,3]],dtype=int)
# points1 = [[1,1],[2,1],[3,4],[3,6],[4,2],[4,4],[5,1],[5,4],[5,5],[6,3]]
# pt = [[0,0],[4,4],[0,4],[4,0]]
# pt_arranged =[[0,0],[0,4],[4,4],[4,0]]

# ex = np.array([[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]],dtype=int)

# print(ret_layer(points,np.array([[3,3],[4,3],[7,0],[2,2],[1,1],[0,6]],dtype=int),6))
# poly = [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2], [1, 2], [0, 2], [0, 1]]
# print(ret_layer(ex,[[3,3],[4,3],[7,0],[2,2],[1,1],[0,6]],6))

# 1
# 6 2
# 0 0
# 6 0
# 3 4
# 2 1
# 4 1
# 3 3
# 6 6
# 3 3
