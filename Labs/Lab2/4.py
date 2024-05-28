import turtle
from random import *
import turtle

turtle.penup()
turtle.goto(300,300)
turtle.pendown()
turtle.goto(-300,300)
turtle.goto(-300,-300)
turtle.goto(300,-300)
turtle.goto(300,300)
number_of_turtles = 20
steps_of_time_number = 100


pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.left(randint(1,360))


while True:
    for unit in pool:
        unit.forward(5)
        if (unit.xcor() >= 300):
            unit.left(abs(180 - unit.heading()))
            unit.forward(10)
        if (unit.xcor() <= -300):
            unit.right(2 * unit.heading() - 180)
            unit.forward(10)
        if (unit.ycor() >= 300):
            unit.left(90 + unit.heading())
            unit.forward(10)
        if (unit.ycor() <= -300):
            unit.left(90 - unit.heading())
            unit.forward(10)