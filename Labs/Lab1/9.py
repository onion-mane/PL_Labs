import turtle
turtle.shape('turtle')
a = 50
for n in range(3,14):
    turtle.pendown()
    ang = ((n - 2) * 180) / n
    print(ang)
    for i in range(n):
        turtle.forward(a)
        turtle.left(180 - ang)
    turtle.penup()
input()