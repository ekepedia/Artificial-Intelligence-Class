word = input('Type 6 letter word:     ')
fileName = 'words.txt'
file1 = open(fileName, 'r')
import linecache
for n in range(5000):
  string = linecache.getline(fileName,n+1)
  dif = 0
  for x in range(6):
    if word[x:x+1] != string[x:x+1]: dif += 1
  if dif == 1:
    print (string)
file1.close()
 
