import turtle
turtle.shape('turtle')
turtle.speed(1000)
def infinity(len):
    for i in range(120):
        turtle.forward(len)
        turtle.left(3)
    for i in range(120):
        turtle.forward(len)
        turtle.right(3)
for k in range(3):
    infinity(2)
    turtle.left(60)
input()