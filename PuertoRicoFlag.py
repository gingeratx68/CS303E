# File: PuertoRicoFlag.py
# Student: Ginger Hudson
# UT EID: gsh628
# Course Name: CS303E
# 
# Date: 4/27/22
# Description of Program: Turtle graphics puerto rican flag
import turtle 
import sys 
def stripes(t, color, width, height, x, y):
    t.goto(x,y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for length in [width, height]*2:
        t.forward(length)
        t.right(90)
    t.end_fill()
    t.penup()
def triangle(t, color, length, x, y):
    t.goto(x,y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for tripoint in [30, 120, 120]:
        t.right(tripoint) # each angle in []
        t.forward(length)
    t.end_fill()
    t.penup()
    
def star(t, color, length, x, y):
    t.goto(x,y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.right(90)
    for linepoint in range(5):
        t.forward(length)
        t.right(144)
    t.end_fill()
    t.penup()
    


def main():
    window= turtle.Screen()
    t= turtle.Turtle()
    #t.setup(1200, 400, startx= 0, starty=0)
    t.speed(10)
    #quadrant 1
    myBlue   = '#00205B'
    myRed    = '#EF3340'
    myWhite  = '#FFFFFF'
    #make whole thing red first
    stripes(t, myRed, 600, 400, 0, 400)
    #white stripes
    stripes(t, myWhite, 600, 80, 0, 320)
    stripes(t, myWhite, 600, 80, 0, 160)
    #make triangle
    triangle(t, myBlue, 400, 0, 400)
    #make star
    star(t, myWhite, 100, 70, 220)
    

if __name__== "__main__":
    sys.exit(main())
