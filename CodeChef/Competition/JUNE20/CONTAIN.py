


import numpy as np
from scipy import spatial
import matplotlib.path as mplPath
import numpy as np
from scipy.optimize import linprog

def in_hull(points, x):
    n_points = len(points)
    c = np.zeros(n_points)
    A = np.r_[points.T,np.ones((1,n_points))]
    b = np.r_[x, np.ones(1)]
    lp = linprog(c, A_eq=A, b_eq=b)
    return lp.success

def isInHull(P,hull):
    try:
        A = hull.equations[:,0:-1]
        b = np.transpose(np.array([hull.equations[:,-1]]))  
        isInHull = np.all((A @ np.transpose(P)) < np.tile(-b,(1,len(P))),axis=0)
    except:
        return [False]
    return isInHull


# points = np.array([[0,0],[1,1],[2,1],[7,0],[7,1],[7,7],[0,7],[3,4],[3,6],[4,2],[4,4],[5,1],[5,4],[5,5],[6,3]])
# points1 = np.array([[1,1],[2,1],[3,4],[3,6],[4,2],[4,4],[5,1],[5,4],[5,5],[6,3]])
# pt = np.array([[0,0],[4,4],[0,4],[4,0]])
# pt_arranged =np.array([[0,0],[0,4],[4,4],[4,0]])

#print(in_hull(points,[7,8]))

def count_layer_num(bbPath,candle,count):
    candle_x =candle[0]
    candle_y = candle[1]
    if(not (bbPath.contains_point([candle_x, candle_y]) and bbPath.contains_point([candle_x+.001, candle_y+0.001]) and bbPath.contains_point([candle_x-0.001, candle_y-.001]) and bbPath.contains_point([candle_x-0.001, candle_y])and bbPath.contains_point([candle_x, candle_y-.001]) and bbPath.contains_point([candle_x+0.001, candle_y]) and bbPath.contains_point([candle_x, candle_y+0.001]))):
        return count,False
    return count,True

def count_layer(hull,candle,count):
    k = isInHull([candle],hull)
    if(k[0]):
        return count,True
    return count,False

def ret_layer(points,candles,num):
    count =0
    count_arr = np.zeros(num,int)
    track_arr = np.ones(num, dtype=bool)
    try:
        while (points.size > 4  ):

            hull = spatial.qhull.ConvexHull(points,qhull_options='QJ')         
            pts = [points[i] for i in hull.vertices] 
            print("hull pts =",pts)
            bbPath = mplPath.Path(pts)
            for idx,candle in enumerate(candles):
                if(track_arr[idx]):
                    count_arr[idx],track_arr[idx] = count_layer_num(bbPath,candle,count)

            if((~track_arr).all()):
                break
            points = np.delete(points, hull.vertices,axis=0)

            mask = np.array(isInHull(points,hull))
            points = np.array(points[mask].tolist())
            count +=1
    except:
        count_arr[track_arr == True] = count
        return count_arr
    count_arr[track_arr == True] = count
    return count_arr

t  = int(input())
for i in range(t):
    n,p = map(int, input().split(" "))
    arr =  np.empty((0,2), int)
    inp =  np.empty((0,2), int)
    for j in range(n):
        x,y = map(int, input().split(" "))
        arr = np.append(arr, np.array([[x,y]]), axis=0)
    for j in range(p):
        x,y = map(int, input().split(" "))
        inp = np.append(inp, np.array([[x,y]]), axis=0)
    s =ret_layer(arr,inp,p)
    for m in s:
      print(m)

# start_time = time.time()
# print(ret_layer(points,[[3,3],[4,3],[7,0],[2,2],[1,1],[0,6]],6))
# print("--- %s seconds ---" % (time.time() - start_time))

