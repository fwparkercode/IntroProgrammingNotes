import turtle

my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_turtle.speed(0)

my_turtle.shape('turtle')
screen = turtle.Screen()
screen.bgcolor('white')

# my_turtle.goto(0, 0)  # goes directly to x, y
# my_turtle.goto(200, 0)

# # for i in range(90):
# #     my_turtle.left(91)
# #     my_turtle.forward(200)
#
# # for i in range(1000):
# #     my_turtle.left(1)
# #     my_turtle.forward(i / 1000)
# #
# # my_turtle.penup()
# # my_turtle.goto(0, 0)
# my_turtle.pencolor('red')
# my_turtle.backward(150)
#
# my_turtle.fillcolor("orange")
# my_turtle.begin_fill()
#
# for i in range(36):
#     my_turtle.forward(300)
#     my_turtle.right(170)
#
# my_turtle.end_fill()
#
# my_turtle.goto(0, 0)
# my_turtle.backward(100)
# my_turtle.pencolor('yellow')
#
# for i in range(36):
#     my_turtle.forward(200)
#     my_turtle.right(170)
#
# my_turtle.fillcolor('blue')
# my_turtle.begin_fill()
#
# for i in range(4):
#     my_turtle.left(90)
#     my_turtle.forward(200)
#
# my_turtle.end_fill()
#
# my_turtle.penup()
# my_turtle.goto(0, 0)
# my_turtle.pendown()

# for i in range(180):
#     my_turtle.forward(i * 2)
#     my_turtle.right(178)
#     my_turtle.forward(i * 5)

my_turtle.penup()
my_turtle.goto(0, 0)
my_turtle.pendown()

for i in range(5, 500, 5):
    my_turtle.forward(i)
    my_turtle.right(90)

screen.exitonclick()