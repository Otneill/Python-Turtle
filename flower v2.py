"""
Bunga V2
"""

import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor('black')
t.pencolor('#000000')
t.speed(100)
col = ('pink','magenta','purple','blue')

for n in range(5):
    for x in range(8):
        t.speed(x+10)
        for i in range(2):
            t.pensize(2)
            t.circle(8+n*20,90)
            t.lt(90)
        t.lt(45)
    t.pencolor(col[n%4])
s.exitonckick()