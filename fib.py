from math import sqrt

def F(n):
    return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144][n]

def main():
    print(F(12))

if __name__ == '__main__':
    from random import random, randint; from math import sqrt; from copy import deepcopy;
    from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+')
    print((clock()-START_TIME), 'seconds |'); print('      +================+')