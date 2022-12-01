import turtle
import random

"""
Draws a circle of random color where the mouse is clicked.
"""

t = turtle.Turtle()
scn = turtle.Screen()
t.penup()

color_list = ['aqua', 'black', 'blue', 'fuchsia', 'gray', 'green', 'lime', 'maroon', 'navy', 'olive', 'orange', 'purple', 'red', 'silver', 'teal', 'white', 'yellow', 'violet']

def draw_circle(x, y):
    t.goto(x, y)
    t.color(color_list[random.randint(0, 10)])
    t.begin_fill()
    t.circle(40)
    t.end_fill()

scn.onclick(draw_circle)

scn.listen()
scn.mainloop()