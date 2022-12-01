import turtle as t

t.color('red', 'yellow')

t.begin_fill()
for _ in range(5):
    t.forward(100)
    t.right(360 / 5 * 2)
t.end_fill()

