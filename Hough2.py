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
        
def drawLine(m, b, image):
    for x in range(WIDTH):
        y = int(m*(x) + b)
        index = y*WIDTH + x
        if m > 5:
            for p in range(y-10,y+10):
                index = p*WIDTH + x
                if 0 <= index < len(image):
                    image[index] = 255
        else:
            if 0 <= index < len(image):
                image[index] = 255
    return

from tkinter import Tk, Canvas, YES, BOTH, PhotoImage, NW
import tkinter
from time import clock
from random import choice
root = Tk()
WIDTH = 512
HEIGHT = 512

def frange(start,stop,step):
    i = start
    terminate = stop - (step/10)
    while i < terminate:
        yield i
        i += step
        
def displayImageInWindow(image):
    global x
    x = ImageFrame(image)
    
def main():  
    image = [0]*HEIGHT*WIDTH
    pos = (-WIDTH-1, -WIDTH, -WIDTH+1, -1, 0, 1, WIDTH-1, WIDTH, WIDTH+1)
    gas = (1,2,1,2,4,2,1,2,1)
    print(pos)
    image2 = [0] * WIDTH * HEIGHT 
    from math import sin,cos,tan,pi,atan2,degrees
    x = 250; y = 250
    for theta in frange(.1, 3.14, 0.1):
        m = tan(theta)
        b = 250 - m*250
        drawLine(m,b,image2)
        print(m,b)
    displayImageInWindow(image2)
    root.mainloop()
    
if __name__ == '__main__':
    from random import random, randint; from math import sqrt; from copy import deepcopy;
    from time import clock; START = clock(); main(); print('\n      +===<RUN TIME>===+')
    print('      |  %5.2f'%(clock()-START), 'seconds |'); print('      +================+')
        
        
