##################################################################
# Eke Wokocha                                                    #
# November 20 , 2014                                             #
# Period 4                                                       #       
# Program Description: Solve Suduko                              #
################################################################## 

count = 0
def createMatrix():
    return [[8,0,0,0,0,0,0,0,0,],
            [0,0,3,6,0,0,0,0,0,],
            [0,7,0,0,9,0,2,0,0,],
            [0,5,0,0,0,7,0,0,0,],
            [0,0,0,0,4,5,7,0,0,],
            [0,0,0,1,0,0,0,3,0,],
            [0,0,1,0,0,0,0,6,8,],
            [0,0,8,5,0,0,0,1,0,],
            [0,9,0,0,0,0,4,0,0,],]


def Mprint(matrix):
    for x in matrix:
        for y in x:
            print(y, end = '-')
        print()
    print()

def steprow(matrix):
    for x in range(len(matrix)):
        zero = []
        num = set()
        for y in range(len(matrix[0])):
            if matrix[x][y] == 0:
                zero.append([x,y])
            else:
                num.update({matrix[x][y],})
        num = {1,2,3,4,5,6,7,8,9} - num
        if len(zero) == 1 & len(num) == 1:
            matrix[zero[0][0]][zero[0][1]] = num.pop()
            #print("CALL STEP ONE:")
            step1(matrix)

def stepcol(matrix):
    for y in range(len(matrix)):
        zero = []
        num = set()
        for x in range(len(matrix[0])):
            if matrix[x][y] == 0:
                zero.append([x,y])
            else:
                num.update({matrix[x][y],})
        num = {1,2,3,4,5,6,7,8,9} - num
        if len(zero) == 1 & len(num) == 1:
            matrix[zero[0][0]][zero[0][1]] = num.pop()
            #print("CALL STEP ONE:")
            step1(matrix)

def stepbloc(matrix, blockr , blockc):
    zero = []
    num = set()
    for x in range(0+blockr,3+blockr):
        for y in range(0+blockc,3+blockc):
            if matrix[x][y] == 0:
                zero.append([x,y])
            else:
                num.update({matrix[x][y],})
    num = {1,2,3,4,5,6,7,8,9} - num
    if len(zero) == 1 & len(num) == 1:
        matrix[zero[0][0]][zero[0][1]] = num.pop()
        #print("CALL STEP ONE:")
        step1(matrix)

def step1(matrix):
    steprow(matrix)
    stepcol(matrix)
    for r in range(0,7,3):
        for c in range(0,7,3):
            stepbloc(matrix,r,c)
            
def possible(x,y,matrix):
    poss = set([1,2,3,4,5,6,7,8,9,])
    poss -= set([j[y] for j in matrix])
    poss -= set([j for j in matrix[x]])
    blockr = 0 if x < 3 else 3 if x < 6 else 6
    blockc = 0 if y < 3 else 3 if y < 6 else 6
    poss -= set([matrix[j][k] for j in range(0+blockr,3+blockr) for k in range(0+blockc,3+blockc)])
    if(len(poss) == 1):
        matrix[x][y] = poss.pop()
    return poss

def step2a(matrix):
    for x in range(len(matrix)):
        allposs = []
        for y in range(len(matrix[x])):
            poss = possible(x,y,matrix)
            allposs.append(poss)
        step2b(matrix,allposs,x)    
                
def step2b(matrix,poss , x):
    for j in range(len(poss)):
            setj = poss[j]
            if(len(setj) == 1):
                matrix[x][j] = setj.pop()
                step1(matrix)
                
def full(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if matrix[x][y] == 0:
                return False
    return True

def small(matrix):
    smallx = -1
    smally = -1
    smallsize = 10
    for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if(matrix[x][y] == 0):
                    xysize = len(possible(x,y,matrix))
                    if xysize < smallsize and xysize > 0:
                        smallx      = x
                        smally      = y
                        smallsize   = xysize
    return (smallx,smally)
    
def guess(matrix):
    step1(matrix)
    step2a(matrix)
    x, y = small(matrix)
    if full(matrix) or (len(possible(x,y,matrix)) == 0) or correct(matrix):
        global count
        count += 1
        return matrix
    Cmatrix = deepcopy(matrix)
    for predicititon in possible(x,y,matrix):
        matrix[x][y] = predicititon
        matrix = guess(matrix)
        if correct(matrix):
            print("Trick Three Done:")
            Mprint(matrix)
            exit()
        matrix = Cmatrix
    return matrix

def correct(matrix):
    return full(matrix) and correctRows(matrix) and correctColumns(matrix) and correctBlocks(matrix) 
    
def correctRows(matrix):
    for x in matrix:
        seen = []
        for y in range(9):
            if x[y] in seen:
                return False
            seen.append(x[y])
    return True
            
def correctColumns(matrix):
    for x in range(9):
        seen = []
        for y in range(9):
            if matrix[y][x] in seen:
                return False
            seen.append(matrix[y][x])
    return True
            
def correctBlocks(matrix):            
    for roffset in range(0,9,3):
        for coffset in range(0,9,3):
            seen = []
            for x in range(0,3):
                for y in range(0,3):
                    if matrix[roffset+x][coffset+y] in seen:
                        return False
                    seen.append(matrix[roffset+x][coffset+y])            
    return True
        

def main():
    masterMatrix = createMatrix()
    print("Original Suduko:")
    Mprint(masterMatrix)
    step1(masterMatrix)
    print("Trick One Done:")
    Mprint(masterMatrix)
    step2a(masterMatrix)
    print("Trick Two Done:")
    Mprint(masterMatrix)    
    guess(deepcopy(masterMatrix))
    if(correct(masterMatrix)):
        print("Trick Three Done:")
        Mprint(masterMatrix)
    else:
        print("NO SOLUTION FOUND")
        print(count, end=" ")
        print("attempts made")
    

if __name__ == '__main__':
    from random import random, randint; from math import sqrt; from copy import deepcopy;
    from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+')
    print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')
  
