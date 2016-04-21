import turtle, math, random

def drawArc(turtle,dy):
    turtle.setheading(0)
    for i in range(21):
        turtle.forward(dy/12)
        turtle.right(9)

def drawD(d,width1,height1,x1,y1):
    d.up()
    d.goto(x1,y1)
    d.down()
    d.setheading(90)
    d.forward(height1)
    drawArc(d,height1)

def drawB(b,width2,height2,x2,y2):
    b.up()
    b.goto(x2,y2)
    b.down()
    b.setheading(90)
    b.forward(height1)
    drawArc(b,(height2)/2)
    drawArc(b,(height2)/2)


x1 = -100
y1 = 0
height1 = 150
width1 = 50

x2 = 0
y2 = 0
height2 = 150
width2 = 50

d = turtle.Turtle()
b = turtle.Turtle()

def go():
    drawD(d,width1,height1,x1,y1)
    drawB(b,width2,height2,x2,y2)

go()
