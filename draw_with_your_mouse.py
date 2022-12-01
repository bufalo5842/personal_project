import turtle

"""
A tool that allows you to draw the picture you want with the mouse
"""
t = turtle.Turtle()

scn = turtle.Screen()

t.pensize(3)

def draw(x,y):
    t.goto(x, y)

def turnleft():
    t.left(10)

def turnright():
    t.right(10)

scn.onclick(draw)
scn.onkey(t.penup, 'w')
scn.onkey(t.pendown, 's')
scn.onkey(turnleft, 'a')
scn.onkey(turnright, 'd')
scn.onkey(t.clear, 'Delete')
scn.listen()
scn.mainloop()
