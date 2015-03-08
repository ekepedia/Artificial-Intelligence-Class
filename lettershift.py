#######################################################################
# Eke Wokocha                                                         #
# February 19, 2015                                                   #
# Period 4                                                            #       
# Program Description: Shift letters down or up the alphabet by a     #
# predetermined amount called the "jump"                              #
#######################################################################

def shiftLetters( string , jump ):
    if (len(string) < 1):
        return string
    newString = []
    for s in string:
        ords = ord(s)
        if ords >= 65 and ords <= 90: # A = 65 Z = 90
            ords = (((ords - 65) + jump) % 26) + 65
            newString.append(chr(ords))
        elif ords >= 97 and ords <= 122: # a = 97 z = 122
            ords = (((ords - 97) + jump) % 26) + 97
            newString.append(chr(ords))
        else:
            newString.append(s)
    return ''.join(newString)
 
def main():
    stng = input('Enter String:\t')
    jump = eval(input('Enter jump:\t'))
    print(stng,' shifted ',jump,' letters.')
    print(shiftLetters(stng,jump))

if __name__ == '__main__':
    from random import *; from math import sqrt; from copy import deepcopy;
    from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+')
    print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')
 
