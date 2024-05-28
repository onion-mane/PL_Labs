import turtle
turtle.shape('turtle')
length = 30
for i in range(10):
    for j in range(4):
        turtle.forward(length)
        turtle.left(90)
    turtle.penup()
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(180)
    turtle.pendown()
    length += 10
input()