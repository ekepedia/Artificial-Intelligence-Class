def importDictionary():
    import pickle
    dict = pickle.load(open('dict.txt','rb'))
    for x in dict:
        dict[x] = (dict[x] , 'xxx', 0 )
    return dict


def g(lisst):
    return len(lisst)

def getCol(arr):
    a = []
    for x in range(len(arr)):
        a.append(arr[x][1])
    return a

def getIndexCol(arr, n):
    for x in range(len(arr)):
        if( arr[x][1] == n ):
            return x
     

def h(start, end):
    dif = 0
    for x in range(len(start)):
        if(start[x] != end[x]):
            dif += 1
    return dif

def Astar(dictt, start, end):
    closed = {}
    popc = 0
    path = []
    node = start
    gval = g(path)
    fval = gval + h(node,end)
    queue = [[fval,node,path,gval]]
    while queue:
        popc+=1
        queue.sort()
        (fval,node,path,gval) = queue.pop(0)
        
        if(node == end):
             print ( path + [node]) 
             print ( len(path + [node]) )
             print(popc)
             break
             
        closed[node] = [fval,node,path,gval]
        #print(closed)
        for chi in dictt[node][0]:
            pathN = path + [node]
            nodeN = chi
            gvalN = g(pathN)
            fvalN = gvalN + h(chi,end)
            newChi = [fvalN,chi,pathN,gvalN]
            
            #print(newChi)
            if nodeN in closed:
                if(closed[nodeN][3] > gvalN):
                       del closed[nodeN]
                       close[nodeN] = newChi
                       print("chane ") 
            else:
                if nodeN in getCol(queue):
                    if queue[getIndexCol(queue,nodeN)][3] > gvalN :
                        queue[getIndexCol(queue,nodeN)] = newChi
                else:
                    queue.append(newChi)
                    
dict = importDictionary()
s = input('strat')
d = input('ded')
Astar(dict,s,d)
Astar(dict,d,s)