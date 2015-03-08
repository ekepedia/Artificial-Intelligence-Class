
##################################################################
# Eke Wokocha                                                    #
# September 18 , 2014                                            #
# Period 4                                                       #       
# Program Description: Import a list of words from an file into  #
# an dictionary, put the words into an array, and look for a path#
# to the array                                                   #
##################################################################



startW = input('start word:          ')
endW = input('start word:          ')
path = []
def importDictionary():
    import pickle
    dict = pickle.load(open('dict.txt','rb'))
    for x in dict:
        dict[x] = (dict[x] , 'xxx', 0 )
    return dict

dict = importDictionary()
queue = []
popc= 0
queue.append(startW)
dict[startW] = (dict[startW][0] , startW , 1)
while len(queue) > 0:
    w = queue.pop(0);
    popc += 1
    dict[w] = (dict[w][0] , dict[w][1] , 1)
    for x in dict[w][0]:
        #print(dict[x][2])
        if dict[x][1] == 'xxx':
            dict[x] = (dict[x][0] , w , 0)
        if dict[x][2] == 0:
            queue.append(x)
        #print(len(queue))  
        
for x in dict:
        dict[x] = (dict[x][0] , dict[x][1], 0 )
print('\nDONE MAKING TREE\n')
c = 0
queue.append(startW)
while(len(queue) > 0 ):
    w = queue.pop()
    
    if( w == endW ):
        p = w
        while( p != startW ):
            path.append(p)
            p = dict[p][1]
        path.append(startW)
        print(popc)
        break
    for x in dict[w][0]:
        if not dict[x][2]:
            queue.append(x)
            dict[x] = (dict[x][0] , dict[x][1], 1 )
if len(path):
    path.reverse 
    print(path)
    exit()
    
print('no path found')
