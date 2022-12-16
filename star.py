import turtle

anms = turtle.Turtle()
ts = turtle.Screen()
ts.title("bintang")
anms.speed(1)

anms.penup()
anms.goto(-150,60)
anms.pendown()
anms.color("gold", "gold")

anms.begin_fill()
anms.forward(270)
anms.right(144)
anms.forward(270)
anms.right(144)
anms.forward(270)
anms.right(144)
anms.forward(270)
anms.right(144)
anms.forward(270)
anms.right(144)
anms.hideturtle()
anms.end_fill()

turtle.exitonclick()