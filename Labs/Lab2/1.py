import turtle
from random import *
while True:
    turtle.forward(randint(10,50))
    if (random() >= 0.5):
        turtle.left(randint(1,90))
    else:
        turtle.right(randint(1, 90))