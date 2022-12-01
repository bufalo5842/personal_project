import turtle as t

t.title("South Korea")
t.shape("turtle")
t.color("red")
t.begin_fill()
t.penup()
t.goto(-200, 0)
t.right(90)
t.pendown()

# red Part
t.circle(100, 180)
t.circle(-100, 180)
t.left(180)
t.circle(200, 180)
t.end_fill()

# blue part
t.color("blue")
t.begin_fill()
t.circle(100, 180)
t.circle(-100, 180)
t.circle(-200, 180)
t.end_fill()

