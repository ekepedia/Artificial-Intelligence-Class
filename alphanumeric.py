


def alpha():
    # step 0
    puzzle = input('words\t')
   # print (puzzle.split(' '))
    #step 0.5
  #  inva = set(for word[0] in puzzle.split(' '))
  #  exit(0)
  #  first = True
  #  last = False
  #  for letter in list(puzzle):
   #     if letter == '=':
   #         last = True
   #     if first and not letter in ['+','-','*','/',' ','=']:
   #         inva.append(letter)
   #         first = False
    #        if last: break
    #        continue
    #    if letter in ['+','-','*','/',' ']:
   #         first = True
 #   print(inva)
  #  exit(0)
    #step 1
    puzzle = puzzle.upper()

    #step 2
    from re import findall
    words = findall('[A-Z]+',puzzle)
    keys = ''.join(set(''.join(words)))
    print(words)
    inva = set(word[0] for word in words)
    #step 3
    from itertools import permutations
    solutionFound = False
    for values in permutations('1234567890',len(keys)):
        
        #step 4
        table = str.maketrans(keys, ''.join(values))
        con = False
        for let in inva:
            
            if table[ord(let)] == 48:
                con = True
        if con: continue;
        #step 5
        equation = puzzle.translate(table)
        
        #step 6
        if eval(equation):
            print ('---', equation)
            solutionFound = True
            
    if not solutionFound:
        print('No solutions exist')
    else:
        print('All solutions found')

def main():
    alpha()
    
    
    
if __name__ == '__main__':
    from random import random, randint; from math import sqrt; from copy import deepcopy;
    from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+')
    print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')
  