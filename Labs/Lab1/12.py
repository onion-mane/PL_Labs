import turtle
turtle.shape('turtle')
def arc(len):
    for i in range(60):
        turtle.forward(len)
        turtle.left(3)
turtle.left(90)
for i in range(4):
    arc(3)
    arc(1)
input()