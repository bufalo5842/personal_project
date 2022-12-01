import turtle
"""
draw captain america shield
"""
t = turtle.Turtle()
t.up()

# red circle
t.goto(0, -150)
t.color('red', 'red')

t.begin_fill()
t.circle(150)
t.end_fill()

# white circle
t.up()
t.goto(0, -120)
t.color('white', 'white')

t.begin_fill()
t.circle(120)
t.end_fill()

# red circle
t.goto(0, -90)
t.color('red', 'red')

t.begin_fill()
t.circle(90)
t.end_fill()

# blue circle
t.goto(0, -60)
t.color('blue', 'blue')

t.begin_fill()
t.circle(60)
t.end_fill()

# draw star
t.goto(0, -60)
t.color('white', 'white')
t.begin_fill()

t.setheading(290)
for i in range(5):
    t.left(144)
    t.forward(110)
t.end_fill()


t.hideturtle()

t.mainloop()