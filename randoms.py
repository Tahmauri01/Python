from turtle import *
from random import randint
from random import choice as randchoice

speed(0)

colors = ['white', 'blue', 'red', 'green', 'black', 'yellow', 'orange', 'pink', 'purple', ]


for i in range(100000):
    
    pencolor(randchoice(colors))
    fillcolor(randchoice(colors))
    pensize(randint(1,10))
    begin_fill()

    circle(randint(10,200), steps=randint(4,10), extent=randint(45,360))
    end_fill()
    penup()
    setposition(randint(-400,400), randint(-400,400))
    pendown()

done()