from turtle import*

speed(0)

def eye():
    pendown()
    begin_fill()
    color("white")
    circle(25)
    end_fill()
    penup()

def pupil():
    pendown()
    begin_fill()
    color('black')
    circle(15)
    end_fill()
    penup()

def brow():
    pendown()
    pensize(5)
    forward(50)
    penup()




begin_fill()

color("#e6b800")

circle(100)

end_fill()

penup()

setposition(50,100)

eye()

setposition(50,125)

pupil()

setposition(-50,100)

eye()

setposition(-50,125)

pupil()

left(90)

setposition(30,30)

pendown()

begin_fill()

color("black")

circle(30,180)

left(90)

forward(60)

end_fill()

penup()

setposition(-90,135)

left(45)

brow()

setposition(90,135)

left(90)

brow()

setposition(150,150)

done()