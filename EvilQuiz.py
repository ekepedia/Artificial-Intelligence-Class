##################################################################
# Eke Wokocha                                                    #
# December 4, 2014                                               #
# Period 4                                                       #       
# Program Description: Reverse List 7 different ways             #
##################################################################

def reverseLst(Lst):
    assert type(Lst) is list and len(Lst) > 0 
    L    = len(Lst)
    Lst2 =  [Lst[(L - 1) - n] for n in range(L)]
    return Lst2
#-------------------------------------------------------------------------------------------------------------

def main():
#---Method 1. Use the built-in reverse function.
    Lst1 = [1,2,3,4,5,]
    Lst2 = deepcopy(Lst1)
    list.reverse(Lst2)
    print ('Method 1.', Lst1, Lst2) # Output: Method 1. [1,2,3,4,5] [5,4,3,2,1]
    
#-------------------------------------------------------------------------------------------------------------
#---Method 2. Use the built-in reversed function.
    Lst1 = [1,2,3,4,5,]
    Lst2 = list(reversed(Lst1))
    print ('Method 2.', Lst1, Lst2) # Output: Method 2. [1,2,3,4,5] [5,4,3,2,1]
    
#-------------------------------------------------------------------------------------------------------------
#---Method 3. Use slicing only--no loops.
    Lst1 = [1,2,3,4,5,]
    Lst2 = Lst1[::-1]
    print ('Method 3.', Lst1, Lst2) # Output: Method 3. [1,2,3,4,5] [5,4,3,2,1]
    
#-------------------------------------------------------------------------------------------------------------
#---Method 4. Use a for loop that works on this swap principle: a,b, = b,a.
    Lst1 = [1,2,3,4,5,]
    L    = len(Lst1)
    
    for n in range(L /2):
        Lst2[(L - 1) - n], Lst2[(L - 2) - n]  = Lst1[n], Lst1[n + 1 ]
    print ('Method 4.', Lst1, Lst2) # Output: Method 4. [1,2,3,4,5] [5,4,3,2,1]
    
#-------------------------------------------------------------------------------------------------------------
#---Method 5. Use a for loop (not a comprehension) that runs backward and copies each Lst1 element to Lst2.
    Lst1 = [1,2,3,4,5,]
    Lst2 = []
    for n in Lst1[::-1]:
        Lst2.append(n)
    print ('Method 5.', Lst1, Lst2) # Output: Method 5. [1,2,3,4,5] [5,4,3,2,1]

#-------------------------------------------------------------------------------------------------------------
#---Method 6. Use a list comprehension that runs backwards and copies each Lst1 element to Lst2.
    Lst1 = [1,2,3,4,5,]
    L    = len(Lst1)
    Lst2 =  [Lst1[(L - 1) - n] for n in range(L)]
    print ('Method 6.', Lst1, Lst2) # Output: Method 6. [1,2,3,4,5] [5,4,3,2,1]

#-------------------------------------------------------------------------------------------------------------
#---Method 7. This time, place method 6 in a function. Anticipate what you can be criticized for,
#             even if your function works perfectly.
    Lst1 = [1,2,3,4,5,]
    Lst2 = reverseLst(Lst1)
    print ('Method 7.', Lst1, Lst2) # Output: Method 7. [1,2,3,4,5] [5,4,3,2,1]
    
if __name__ == '__main__':
    from random import random, randint; from math import sqrt; from copy import deepcopy;
    from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+')
    print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')