import math
import turtle


class Body:
    def __init__(self, color, pen):
        self.color = color
        self.pen = pen

    def draw(self, x, y):
        self.pen.up()
        self.pen.goto(x, y)
        self.pen.down()
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        self.pen.forward(50)
        self.pen.right(90)
        self.pen.forward(50)
        self.pen.left(90)
        self.pen.forward(100)
        self.pen.right(90)
        self.pen.forward(50)
        self.pen.right(90)
        self.pen.forward(50)
        self.pen.right(90)
        self.pen.circle(25, 180)
        self.pen.right(90)
        self.pen.forward(40)
        self.pen.right(90)
        self.pen.circle(25, 180)
        self.pen.right(90)
        self.pen.forward(50)
        self.pen.right(90)
        self.pen.forward(50)
        self.pen.right(90)
        self.pen.forward(40)
        self.pen.left(45)
        self.pen.forward(math.sqrt(5000))
        self.pen.end_fill()


class Wheel:
    def __init__(self, color, pen):
        self.color = color
        self.pen = pen

    def draw(self):
        self.backTire()
        self.frontTire()

    def backTire(self):
        self.pen.up()
        self.pen.fillcolor(self.color)
        self.pen.left(90)
        self.pen.forward(50)
        self.pen.right(90)
        self.pen.forward(50)
        self.pen.down()
        self.pen.right(90)
        self.pen.begin_fill()
        self.pen.circle(25, 360)
        self.pen.end_fill()

    def frontTire(self):
        self.pen.up()
        self.pen.fillcolor(self.color)
        self.pen.left(90)
        self.pen.forward(90)
        self.pen.right(90)
        self.pen.down()
        self.pen.begin_fill()
        self.pen.circle(25, 360)
        self.pen.end_fill()


class Antenna:
    def __init__(self, pen):
        self.pen = pen

    def draw(self, x, y):
        self.pen.up()
        self.pen.goto(x - 50, y - 50)
        self.pen.down()
        self.pen.forward(60)


class Window:
    def __init__(self, color, pen):
        self.color = color
        self.pen = pen

    def draw(self, x, y):
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        self.pen.up()
        self.pen.goto(x + 5, y - 5)
        self.pen.down()
        self.pen.right(45)
        self.pen.forward(40)
        self.pen.right(90)
        self.pen.forward(40)
        self.pen.right(90)
        self.pen.forward(40)
        self.pen.right(90)
        self.pen.forward(40)
        self.pen.end_fill()


class Packages:
    def __init__(self, color, pen):
        self.color = color
        self.pen = pen

    def draw(self, x, y):
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        self.pen.up()
        self.pen.goto(x + 70, y - 50)
        self.pen.down()
        self.pen.forward(50)
        self.pen.right(90)
        self.pen.forward(10)
        self.pen.right(90)
        self.pen.forward(20)
        self.pen.left(90)
        self.pen.forward(40)
        self.pen.left(90)
        self.pen.forward(20)
        self.pen.right(90)
        self.pen.forward(10)
        self.pen.right(90)
        self.pen.forward(50)
        self.pen.right(90)
        self.pen.forward(60)
        self.pen.end_fill()
        self.pen.begin_fill()
        self.pen.up()
        self.pen.goto(x + 80, y)
        self.pen.down()
        self.pen.right(90)
        self.pen.forward(40)
        self.pen.right(90)
        self.pen.forward(40)
        self.pen.right(90)
        self.pen.forward(60)
        self.pen.right(90)
        self.pen.forward(40)
        self.pen.end_fill()
        self.pen.up()
        self.pen.goto(x + 80, y + 40)
        self.pen.down()
        self.pen.goto(x + 50, y - 50)
        self.pen.up()
        self.pen.goto(x + 120, y + 40)
        self.pen.down()
        self.pen.goto(x + 150, y - 50)


class Headlights:
    def __init__(self, headlightsColor, taillightColor, x, y, pen):
        self.headlightsColor = headlightsColor
        self.taillightColor = taillightColor
        self.x = x
        self.y = y
        self.pen = pen

    def draw(self):
        self.headlights()
        self.taillights()

    def headlights(self):
        self.pen.fillcolor(self.headlightsColor)
        self.pen.begin_fill()
        self.pen.up()
        self.pen.goto(self.x - 90, self.y - 60)
        self.pen.down()
        self.pen.right(90)
        self.pen.forward(20)
        self.pen.right(90)
        self.pen.forward(15)
        self.pen.right(90)
        self.pen.forward(20)
        self.pen.right(90)
        self.pen.forward(15)
        self.pen.end_fill()

    def taillights(self):
        self.pen.fillcolor(self.taillightColor)
        self.pen.begin_fill()
        self.pen.up()
        self.pen.goto(self.x + 130, self.y - 60)
        self.pen.down()
        self.pen.right(90)
        self.pen.forward(20)
        self.pen.right(90)
        self.pen.forward(15)
        self.pen.right(90)
        self.pen.forward(20)
        self.pen.right(90)
        self.pen.forward(15)
        self.pen.end_fill()


def vehicle(pen, x, y, bodycolor, windowcolor, packagecolor, wheelColor, headlightsColor, taillightColor):
    body = Body(bodycolor, pen)
    body.draw(x, y)
    window = Window(windowcolor, pen)
    window.draw(x, y)
    packages = Packages(packagecolor, pen)
    packages.draw(x, y)
    wheel = Wheel(wheelColor, pen)
    wheel.draw()
    antenna = Antenna(pen)
    antenna.draw(x, y)
    headlights = Headlights(headlightsColor, taillightColor, x, y, pen)
    headlights.draw()


screen = turtle.Screen()
screen.bgcolor('white')

vehicle(turtle.Turtle(), 60, 60, 'blue', 'lightblue', 'red', 'black', 'yellow', 'red')

screen.listen()
screen.mainloop()
