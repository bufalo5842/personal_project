import turtle

t = turtle.Turtle()

t.shape("turtle")
t.penup()
t.goto(-100, 100)
t.pendown()

for i in range(5):
    t.forward(200)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(200)
    t.left(90)
    t.forward(20)
    t.left(90)