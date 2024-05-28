import turtle
turtle.shape('turtle')
n = int(input())
for i in range(n):
    turtle.forward(50)
    turtle.back(50)
    turtle.right(360//n)
input()