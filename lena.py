def main():
    global WIDTH, HEIGHT
    file1 = open('lena.ppm','r')
    stng  = file1.readline()
    stng  = file1.readline()
    WIDTH = int(stng.split()[0])
    HEIGHT = int(stng.split()[1])
    stng  = file1.readline()
    print(stng)
    
    nums  = file1.read().split()
    print(nums[:10])
    file1.close()
    
    image = []
    for pos in range(0, len(nums), 3):
        RGB = ( int(nums[pos+0]),int(nums[pos+1]),int(nums[pos+2]) )
        image.append( int (0.2*RGB[0]+0.7*RGB[1]+0.1*RGB[2]) )
    printElaspedTime('Gray numbers are now created.')
    
    file1 = open('lenagray.ppm', 'w')
    for elt in image:
        file1.write(str(elt) + ' ')
    printElaspedTime('saved file numbers')
    file1.close()
    
    displayImageInWindow(image)
    
    root.mainloop()
    
class ImageFrame:
    global WIDTH,HEIGHT
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
    
from tkinter import Tk, Canvas, YES, BOTH, PhotoImage, NW
import tkinter
from time import clock
from random import choice
root = Tk()
WIDTH = None
HEIGHT = None

if __name__ == '__main__':
    from random import random, randint; from math import sqrt; from copy import deepcopy;
    from time import clock; START = clock(); main(); print('\n      +===<RUN TIME>===+')
    print('      |  %5.2f'%(clock()-START), 'seconds |'); print('      +================+')