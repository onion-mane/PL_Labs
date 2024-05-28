import turtle
from random import *
turtle.shape("turtle")
turtle.goto(0,0)
turtle.width(6)
turtle.forward(500)
turtle.back(800)
turtle.width(2)
vYstart = 20
x = -300
y = 0
Vx = 5
Vy = vYstart
dt = 0
ay = -1
while True:
    dt += 0.0005
    x += Vx * dt
    y += Vy * dt + ay * dt ** 2 / 2
    turtle.goto(x, y)
    Vy += ay * dt
    if y <= 0.004:
        turtle.goto(x, 0)
        Vy = vYstart*0.8
        vYstart *= 0.8
        ay = -1