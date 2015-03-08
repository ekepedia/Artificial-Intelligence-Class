#######################################################################
# Eke Wokocha                                                         #
# March 3, 2015                                                       #
# Period 4                                                            #       
# Program Description: Display noise and two lines                    #
#######################################################################

def main():  
    
    image = [0]*HEIGHT*WIDTH
    pos = (-WIDTH-1, -WIDTH, -WIDTH+1, -1, 0, 1, WIDTH-1, WIDTH, WIDTH+1)
    gas = (1,2,1,2,4,2,1,2,1)
    print(pos)
    image2 = [0] * WIDTH * HEIGHT 
    
    imageNoise(500,image2)
    drawLine(2,1,image2)
    drawLine(0,200,image2)
    drawCircle(200,200,100,image2)
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
    
def displayImageInWindow(image):
    global x
    x = ImageFrame(image)
    
def imageNoise(points, image):
    from random import randint
    for n in range (points):
        r = randint(0, HEIGHT - 1)
        c = randint(0, WIDTH  - 1)
        image[c*WIDTH + r] = 255
    return

def drawLine(m, b, image):
    for x in range(WIDTH):
        index = (m*(x) + b)*WIDTH + x
        if 0 <= index < len(image):
            image[index] = 255
    return

def drawCircle(cx,cy,r,image):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if( ( (x-cx)*(x-cx) + (y-cy)*(y-cy)) <= r*r):
                print("ASDFA")
                image[y*WIDTH + x] = 255
    return
    
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