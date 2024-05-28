import turtle
from random import *
turtle.shape("turtle")
turtle.penup()
turtle.back(300)
turtle.pendown()
turtle.width(2)
number_x, number_y = turtle.xcor(), turtle.ycor()
def do_action(act):
    match act:
        case 0:
            turtle.penup()
        case 9:
            turtle.pendown()
        case 8:
            turtle.forward(10)
        case 1:
            turtle.goto(number_x, 40 + number_y)
        case 2:
            turtle.goto(20 + number_x, 40 + number_y)
        case 3:
            turtle.goto(number_x, 20 + number_y)
        case 4:
            turtle.goto(20 + number_x, 20 + number_y)
        case 5:
            turtle.goto(number_x, number_y)
        case 6:
            turtle.goto(20 + number_x, number_y)

index_list = [(0, 3, 9, 2, 6),
              (0, 1, 9,  2, 4, 5, 6),
              (0, 2, 9, 1, 3, 4, 6, 5, 6),
              (0, 1, 9,  2, 4, 5, 6),
              (0, 1, 9,  2, 4, 5, 6),
              (0, 1, 9,  2, 4, 5, 6)]

for numb in index_list:
    for action in numb:
        do_action(action)
    turtle.penup()
    do_action(8)
    number_x, number_y = turtle.xcor(), turtle.ycor()
turtle.done()