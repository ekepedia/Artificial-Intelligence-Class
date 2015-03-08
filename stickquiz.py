#######################################################################
# Eke Wokocha                                                         #
# Feburary 12, 2014                                                   #
# Period 4                                                            #       
# Program Description: Four different probabilities to form a triangle#
# using four different definitions of "random"                        #
#######################################################################

def istriangle(pointA, pointB):
    if pointA > pointB:
        if pointB > 0.5 or (pointA-pointB) > 0.5 or (1-pointA) > 0.5:
            return False
    if pointB > pointA:
        if pointA > 0.5 or (pointB-pointA) > 0.5 or (1-pointB) > 0.5:
            return False
    return True

def puzzle1():
    runs = 10000000
    triangle = 0
    for trials in range(runs):
        r = random()                                    #r and r2 are the break points
        r2 = random()
        if istriangle(r,r2):
            triangle += 1
    print('Puzzle 1: The probability of forming a triangle is',round(triangle/runs,3))
    
def puzzle2():
    runs = 10000000
    triangle = 0
    for trials in range(runs):
        r = random()
        r2 = uniform(0,r)
        if r < 0.5:
            r2 = uniform(r,1)     
        if istriangle(r,r2):
            triangle += 1
    print('Puzzle 2: The probability of forming a triangle is',round(triangle/runs,3))
    
def puzzle3():
    runs = 10000000
    triangle = 0
    for trials in range(runs):
        r = random()
        r2 = uniform(0,r)
        probability = random()
        if probability < 0.5:
            r2 = uniform(r,1)           
        if istriangle(r,r2):
            triangle += 1
    print('Puzzle 3: The probability of forming a triangle is',round(triangle/runs,3))
    
def puzzle4():
    runs = 10000000
    triangle = 0
    for trials in range(runs):
        r = random()
        r2 = uniform(0,r)
        probability = random()
        if probability > r:
            r2 = uniform(r,1)           
        if istriangle(r,r2):
            triangle += 1
    print('Puzzle 4: The probability of forming a triangle is',round(triangle/runs,3))
    
def main():
    puzzle1()
    puzzle2()
    puzzle3()
    puzzle4()

if __name__ == '__main__':
    from random import *; from math import sqrt; from copy import deepcopy;
    from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+')
    print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')
    
Puzzle 1 answer : 0.250
Puzzle 2 answer : 0.386
Puzzle 3 answer : 0.193
Puzzle 4 answer : 0.250