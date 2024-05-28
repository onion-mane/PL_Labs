import turtle
turtle.shape('turtle')
def arc(len):
    for i in range(60):
        turtle.forward(len)
        turtle.right(3)
def circle(len):
    for i in range(120):
        turtle.forward(len)
        turtle.left(3)
turtle.width(2)

turtle.fillcolor("Yellow")
turtle.begin_fill()
circle(4)
turtle.end_fill()

turtle.penup()
turtle.left(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(40)

turtle.pendown()
turtle.fillcolor("Red")
turtle.begin_fill()
circle(1)
turtle.penup()
turtle.end_fill()

turtle.back(80)

turtle.pendown()
turtle.fillcolor("Red")
turtle.begin_fill()
circle(1)
turtle.penup()
turtle.end_fill()

turtle.left(90)
turtle.forward(60)
turtle.pendown()
turtle.width(4)
turtle.color("Blue")
arc(2)
input()