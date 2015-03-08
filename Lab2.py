



def main():
   word = input('Type 6 letter word:     ')
   fileName = 'words.txt'
   fileName2 = 'dict.txt'
   file1 = open(fileName, 'r')
   import linecache
   for n in range(5000):
       word = linecache.getLine(fileName, n+1)
       lst = []
       for n in range(5000):
          string = linecache.getline(fileName,n+1)
	  dif = 0
	  for x in range(6):
	      if word[x:x+1] != string[x:x+1]: dif += 1
	  if dif == 1:
	      lst.append(string)

   file1.close()
  
