from math import *
from tkinter import *
import random

WIDTH = 400
HEIGHT = 300

def GUI():
    root = Tk()
    c = Canvas(root, width=WIDTH, height=HEIGHT, bg = 'white')
    c.pack()
    dot(c, WIDTH/2, HEIGHT/2)
    dot(c, WIDTH/2+30, HEIGHT/2-40)
    triangle(c, (WIDTH/2+50, HEIGHT/2-40), (WIDTH/2-60, HEIGHT/2+20), (WIDTH/2, HEIGHT/2-70))
    root.mainloop()
    
def Backend():
    pass

def dot(c,x,y):
    c.create_oval(x-3, y-3, x+3, y+3, fill="black")

def triangle(c, dot1, dot2, dot3):
    x1, y1 = dot1
    x2, y2 = dot2
    x3, y3 = dot3
    c.create_line(x1, y1, x2, y2)
    c.create_line(x2, y2, x3, y3)
    c.create_line(x3, y3, x1, y1)
    dot(c, x1, y1)
    dot(c, x2, y2)
    dot(c, x3, y3)

def algorithmFinder():
    pass

def line(c, x1, y1, x2, y2):
    c.create_line(x1,y1,x2,y2)
    
if __name__ == "__main__":
    GUI()
    
