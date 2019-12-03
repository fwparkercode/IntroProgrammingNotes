
from turtle import *

my_turtle = Turtle()
my_screen = Screen()

my_turtle.pencolor("red")
my_turtle.fillcolor("yellow")
my_turtle.speed(0)
my_turtle.shape("turtle")

my_turtle.begin_fill()

for i in range(36):
    my_turtle.forward(200)
    my_turtle.left(170)
    my_turtle.forward(200)
my_turtle.end_fill()

my_turtle.begin_fill()
my_turtle.width(5)
my_turtle.pencolor("blue")
my_turtle.fillcolor("green")

for i in range(500):
    my_turtle.forward(i)
    my_turtle.right(30)

# my_turtle.penup()
# my_turtle.pendown()
# my_turtle.goto(x, y)
# my_turtle.setheading(0 to 360)

my_turtle.end_fill()

my_screen.exitonclick()

