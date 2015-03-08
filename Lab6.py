##################################################################
# Eke Wokocha                                                    #
# September 29 , 2014                                            #
# Period 4                                                       #       
# Program Description: Import a list of words from an file into  #
# an dictionary, put the words into an array, and look for a path#
# to the array using an A* search method                         #
##################################################################


#----------- Functions -------------------------------------
def importfileintoarray(filename):
    file1 = open(filename, 'r')
    nodes = {}
    while(1):  
        letter = ''
        x = ''
        y = ''
        current = file1.read(7)
        if current == '':
            break
        while(current != ' '):
            letter += current
            current = file1.read(1)
        current  = file1.read(1)
        while(current != ' '):
            x += current
            current = file1.read(1)
        current = file1.read(1)
        while(current != '\n'):
            y += current
            current = file1.read(1)
        longi = float(x)
        lati = float(y)
        nodes[letter] = [longi,lati]
    return nodes

from math import pi , acos , sin , cos
def distance(y1,x1, y2,x2):
   R   = 3958.76 # miles
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R
   
def neighbors(dictt):
    file1 = open('rrEdges.txt')
    book = {}
    while(1):
        a = file1.read(7)
        if a == '':
            break
        file1.read(1)
        b = file1.read(7)
        file1.read(1)
        dist = distance(dictt[a][0],dictt[a][1],dictt[b][0],dictt[b][1])
        if not a in book.keys():
            book[a] = [[[b,dist]],'xxx',0]
        else:  
            book[a][0].append([b,dist])
        if not b in book.keys():
            book[b] = [[[a,dist]],'xxx',0]
        else:  
            book[b][0].append([a,dist])
    return book

def getCol(arr):
    a = []
    for x in range(len(arr)):
        a.append(arr[x][1])
    return a

def getIndexCol(arr, n):
    for x in range(len(arr)):
        if( arr[x][1] == n ):
            return x
        
def Astar(dictt, start, end):
    closed = {}
    popc = 0
    path = []
    node = start
    gval = 0
    fval = gval
    queue = [[fval,node,path,gval]]
    while queue:
        popc+=1
        queue.sort()
        (fval,node,path,gval) = queue.pop(0)
        
        if(node == end):
             print ( path + [node] ) 
             print ( "Path Length : "+str(len(path + [node])) )
             print ( "Distance: " + str(gval) )
             print ( "Pops : " + str(popc) )
             break
        
        
        closed[str(node)] = [fval,node,path,gval]
        for chi in dictt[node][0]:
            pathN = path + [node]
            nodeN = chi[0]
            gvalN = gval + chi[1]
            print( type(gval) )
            fvalN = gvalN + distance(chi[0],chi[1],dictt[end][0][0],dictt[end][0][1])
            newChi = [fvalN,nodeN,pathN,gvalN]
            
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
    
# --------- Main  --------------------------------------------------
def main():
    nodes = importfileintoarray('rrNodes.txt')
    book = neighbors(nodes)
    s = input('start\t')
    d = input('end\t')
    Astar(book,s,d)
   
    
    
    
if __name__ == '__main__':
    from random import random, randint; from math import sqrt; from copy import deepcopy;
    from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+')
    print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')
  
