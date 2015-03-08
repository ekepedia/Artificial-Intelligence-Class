##################################################################
# Eke Wokocha                                                    #
# September 29 , 2014                                            #
# Period 4                                                       #       
# Program Description: Import a list of words from an file into  #
# an dictionary, put the words into an array, and look for a path#
# to the array using an A* search method                         #
##################################################################

def importDictionary():
    import pickle
    dict = pickle.load(open('dict.txt','rb'))
    for x in dict:
        dict[x] = (dict[x] , 'xxx', 0 )
    return dict

def g(lst):
    return len(lst)

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
    for index in range(len(start)):
        if(start[index] != end[index]):
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
             print ( path + [node] ) 
             print ( len(path + [node]) )
             print ( popc )
             break
             
        closed[node] = [fval,node,path,gval]

        for chi in dictt[node][0]:
            pathN = path + [node]
            nodeN = chi
            gvalN = g(pathN)
            fvalN = gvalN + h(chi,end)
            newChi = [fvalN,chi,pathN,gvalN]
            
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
def main():                    
    dict = importDictionary()
    s = input('start\t')
    d = input('end\t')
    if( not s in dict.keys() ):
	    print(s + " not in dictionary")
	    exit()
    if( not d in dict.keys() ):
	    print(d+ " not in dictionary")
	    exit()
    print("\n")
    Astar(dict,s,d)
    print("\n")
    Astar(dict,d,s)

if __name__ == '__main__':
        from random import random, randint; from math import sqrt; from copy import deepcopy;
        from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+');
        print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')
        
