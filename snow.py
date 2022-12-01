import turtle

t = turtle.Turtle()

t.shape("turtle")
t.color("blue")


for i in range(6):
    t.left(30 + 60*i)
    t.forward(100)
    t.forward(-30)
    t.left(60)
    t.forward(30)
    t.forward(-30)
    t.right(120)
    t.forward(30)
    t.forward(-30)
    t.home()

