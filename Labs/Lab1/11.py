import turtle
turtle.shape('turtle')
def infinity(len):
    for i in range(120):
        turtle.forward(len)
        turtle.left(3)
    for i in range(120):
        turtle.forward(len)
        turtle.right(3)
turtle.right(90)

infinity(2)
infinity(2.5)
infinity(3)
input()