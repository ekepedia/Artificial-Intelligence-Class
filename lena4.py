def main():
    file1 = open('lenagray.ppm','r')     
    nums  = file1.read().split()
    HIGH = 125
    for x in range(len(nums)):
        nums[x] = int(nums[x])
    print(nums[:10])
    file1.close()
    from math import sqrt
    image = nums
    pos = (-WIDTH-1, -WIDTH, -WIDTH+1, -1, 0, 1, WIDTH-1, WIDTH, WIDTH+1)
    Sx = (-1,0,1,-2,0,2,-1,0,1)
    Sy = (1,2,1,0,0,0,-1,-2,-1)
    print(pos)
    image2 = [ [0,0,0,0,0] for elt in range(HEIGHT*WIDTH)]
    for row in range(1,HEIGHT-1):
        for col in range(1,WIDTH-1):
            sxx = 0
            syy = 0
            for c in range(len(pos)):
                sxx += image[row*WIDTH + col+pos[c]]*Sx[c]
                syy += image[row*WIDTH + col+pos[c]]*Sy[c]
            image2[row*WIDTH + col][0] = sqrt(sxx*sxx+syy*syy)
            from math import atan2
            image2[row*WIDTH + col][1] = theta(atan2(syy,sxx))
            image2[row*WIDTH + col][2] = 0
            image2[row*WIDTH + col][3] = 0
            image2[row*WIDTH + col][4] = 0
            
    
    for row in range(1,HEIGHT-1):
        for col in range(1,WIDTH-1):
            direc = image2[row*WIDTH + col][1]
            first,second = matrixindex(direc)
            index = row*WIDTH + col
            m = max([image2[index][0],image2[index+first][0],image2[index+second][0]])
            if image2[row*WIDTH + col][0] == m:
                image2[row*WIDTH + col][2] = 1
                if(image2[index][0] > HIGH):
                    image2[index][4] = 1
    image = [ (255 if x[4] else 0)  for x in image2]
    
    displayImageInWindow(normalize(image))
    
    root.mainloop()
    
class ImageFrame:
    def __init__(self, image, COLORFLAG = False):
        self.img = PhotoImage(width = WIDTH, height = HEIGHT)
        for row in range(HEIGHT):
            for col in range(WIDTH):
                num = image[row*WIDTH + col]
                if COLORFLAG == True:
                    kolor = '#%02x%02x%02x' % (num[0], num[1], num[2])
                else:
                    kolor = '#%02x%02x%02x' % (num, num, num)
                self.img.put(kolor, (col,row))
        c = Canvas(root, width = WIDTH, height = HEIGHT); c.pack()
        c.create_image(0,0, image = self.img, anchor = NW)
        printElaspedTime('displayed image')
        
def printElaspedTime( msg = 'time' ):
    length = 30
    msg = msg[:length]
    tab = '.'*(length-len(msg))
    print('--' + msg.upper() + tab + ' ', end = ' ')
    time = round(clock() - START, 1)
    print( '%2d'%int(time/60), ' min :', '%4.1f'%round(time%60, 1), \
        ' sec', sep = '')
    
def displayImageInWindow(image):
    global x
    x = ImageFrame(image)
 
def theta(angle):
    from math import pi
    angle = abs(angle)*360/2*pi
    if angle <= 45/2:
        return 0;
    if angle <=135/2:
        return 1
    if angle <=(135+90)/2:
        return 2
    if angle <=(180+135)/2:
        return 3
    return 0

def normalize(image, intensity =255):
    m = max(image)
    printElaspedTime('normalize')
    return [int(x*intensity/m) for x in image]
def matrixindex(direction):
    pos = (-WIDTH-1, -WIDTH, -WIDTH+1, -1, 0, 1, WIDTH-1, WIDTH, WIDTH+1)
    if(direction == 1):
        return pos[2],pos[6]
    if(direction == 2):
        return pos[1],pos[7]
    if(direction == 3):
        return pos[0],pos[8]
    if(direction == 0):
        return pos[3],pos[5]
def fixCellAt(image, index):
    if image(index)[3] == 1: 
        return
    image(index)[3] = 1
        

from tkinter import Tk, Canvas, YES, BOTH, PhotoImage, NW
import tkinter
from time import clock
from random import choice
root = Tk()
WIDTH = 512
HEIGHT = 512

if __name__ == '__main__':
    from random import random, randint; from math import sqrt; from copy import deepcopy;
    from time import clock; START = clock(); main(); print('\n      +===<RUN TIME>===+')
    print('      |  %5.2f'%(clock()-START), 'seconds |'); print('      +================+')