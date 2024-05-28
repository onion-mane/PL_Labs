import turtle
turtle.shape('turtle')
turtle.width(2)
dist = 1
for i in range(1440//5):
    turtle.forward(dist)
    turtle.left(5)
    dist += 0.01
input()