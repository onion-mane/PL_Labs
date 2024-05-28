import turtle
turtle.shape('turtle')

n = int(input())
ang = 180 - (180/n)
turtle.width(2)
for i in range(n):
    turtle.forward(200)
    turtle.left(ang)
input()