import turtle

def Koch_2(order=5, base_length=2, origin=(-300,200)):

    name = "Koch Curve 2"

screen = turtle.Screen()
screen.screensize()
screen.setup(width = 1.0, height = 1.0)
screen.title('snowflakes')



turtle.hideturtle()
turtle.delay(0)
turtle.speed(0)

turtle.penup()
turtle.goto(-300,200)
turtle.pendown()

seq = "F--F--F"
for i in range(5):
    new_seq = ""
    for char in seq:
        if char == "F": new_seq += "F+F--F+F"
        else:           new_seq += char
    seq = new_seq

turtle.color("#6AA5E1", "#6AA5E1")
for char in seq:
    if   char == "F": turtle.forward(2)
    elif char == "+": turtle.left(60)
    elif char == "-": turtle.right(60)

turtle.exitonclick()