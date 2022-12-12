from turtle import Turtle, Screen
from random import *


colors = ['blue', 'red', 'green', 'black', 'yellow', 'orange', 'pink', 'purple']

class myTurtle(Turtle):
    def random_shape(self, x, y):
        self.penup()
        self.setposition(randint(-200,200),randint(-200,200))
        self.pendown()
        self.color(choice(colors))
        self.circle(randint(10,200), steps=randint(2,10))
        

    def __init__(self) -> None:
        super().__init__()
        self.random_shape(0, 0)
        self.onclick(self.random_shape)
        



x = myTurtle()

x.forward(50)


y = myTurtle()

y.backward(50)


screen = Screen()

screen.mainloop()