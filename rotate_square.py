import turtle
"""
draw rotating circle
"""
rotate = turtle.Turtle()
rotate.shape('turtle')

color_list = ['aqua', 'black', 'blue', 'fuchsia', 'gray', 'green', 'lime', 'maroon', 'navy', 'olive', 'orange', 'purple', 'red', 'silver', 'teal', 'white', 'yellow', 'violet']


n = int(turtle.textinput('Count', 'Enter the number of squares to create : ')) # ask how many square you want to draw

for i in range(n):
    rotate.fillcolor(color_list[i%len(color_list)])
    rotate.begin_fill()
    for i in range(4):
        rotate.forward(100)
        rotate.left(90)              # rotate squares left
    rotate.end_fill()
    rotate.left(int(360/n))          # make circle with squares
