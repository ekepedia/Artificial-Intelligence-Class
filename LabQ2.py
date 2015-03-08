
##################################################################
# Eke Wokocha	                                                 #
# September 9 , 2014                                             #
# Period 4                                                       #       
# Program Description: Import a list of words from an file into  #
# an array. Find all of the neighbors of each words and put them #
# into a dictionary, with the word as the key and the neighbors  #
# as the values. Then export the dictionary to a file as a byte  #
# code.                                                          #
##################################################################


# --------- Definied Functions -----------------------------------


def importfileintoarray(fileName):
    import linecache
    WordsfileName = fileName
    WordsFile = open(WordsfileName, 'r')
    ArrayofWords = []
    for indexInFile in range(5000):
        wordFromFile = linecache.getline(WordsfileName,indexInFile+1)
        if ( wordFromFile == '' ):
            break;
        ArrayofWords.append(wordFromFile[:6])
    return ArrayofWords
        
def getNeighbors(str , array):
    ArrayofNeighbors = []
    for indexInFile in array:
        wordFromFile = indexInFile
        differenceFromWrittenWords = 0
        for indexinString in range(6):
            if str[indexinString:indexinString + 1] != wordFromFile[indexinString:indexinString + 1]: 
                differenceFromWrittenWords += 1
            if( differenceFromWrittenWords > 1 ):
                break
        if differenceFromWrittenWords == 1:
            ArrayofNeighbors.append(wordFromFile[:6])
    return ArrayofNeighbors

def makeDictionary(array):  
    Dict = {}
    for indexInFile in array:
        wordFromFile = indexInFile
        if wordFromFile== '':
            break
        arrayofNeighbors = getNeighbors(wordFromFile, array)
        Dict[wordFromFile[:6]] = arrayofNeighbors
    return Dict
 
def DumpintoFile( Dictionary):
    DictFile = open('dict.txt','wb')
    import pickle
    pickle.dump(Dictionary, DictFile)

# --------- Main  --------------------------------------------------

def main():
    WordArray = importfileintoarray('words.txt')
    print(WordArray)
    Dictionary = makeDictionary(WordArray)
    print( Dictionary.keys()) 
    DumpintoFile( Dictionary )
    
if __name__ == '__main__':
        from random import random, randint; from math import sqrt; from copy import deepcopy;
        from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+');
        print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')
    	
