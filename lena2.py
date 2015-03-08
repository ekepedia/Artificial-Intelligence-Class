def main():
    file1 = open('lenagray.ppm','r')     
    nums  = file1.read().split()
    for x in range(len(nums)):
        nums[x] = int(nums[x])
    print(nums[:10])
    file1.close()
    
    image = nums
    pos = (-WIDTH-1, -WIDTH, -WIDTH+1, -1, 0, 1, WIDTH-1, WIDTH, WIDTH+1)
    gas = (1,2,1,2,4,2,1,2,1)
    print(pos)
    image2 = [0] * WIDTH * HEIGHT
    for n in range(36):
        for row in range(1,HEIGHT-1):
            for col in range(1,WIDTH-1):
                sim = 0
                for c in range(len(pos)):
                    sim += image[row*WIDTH + col+pos[c]]*gas[c]
                image2 [row*WIDTH + col] = sim//16
    
    
    displayImageInWindow(image2)
    
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