from turtle import *

def dashLine():
    forward(50)
    penup()
    forward(50)
    pendown()


def backDash():
    penup()
    backward(50)
    pendown()
    backward(50)


def dashSquare():
    dashLine()
    dashLine()
    dashLine()
    left(90)
    dashLine()
    dashLine()
    dashLine()
    left(90)
    dashLine()
    dashLine()
    dashLine()
    left(90)
    dashLine()
    dashLine()
    dashLine()
    left(90)

dashSquare()

x = 1

# while x == 1:
    # dashLine()
    # penup()
    # backward(100)
    # pendown()
    # backDash()
    # break

