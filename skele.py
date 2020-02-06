import math
import turtle

screen = turtle.Screen()
screen.bgcolor('white')
obj = turtle.Turtle()


class Body:
    def __init__(self, color):
        self.color = color

    def draw(self, x, y):
        obj.up()
        obj.goto(x, y)
        obj.down()
        obj.fillcolor(self.color)
        obj.begin_fill()
        obj.forward(50)
        obj.right(90)
        obj.forward(50)
        obj.left(90)
        obj.forward(100)
        obj.right(90)
        obj.forward(50)
        obj.right(90)
        obj.forward(50)
        obj.right(90)
        obj.circle(25, 180)
        obj.right(90)
        obj.forward(40)
        obj.right(90)
        obj.circle(25, 180)
        obj.right(90)
        obj.forward(50)
        obj.right(90)
        obj.forward(50)
        obj.right(90)
        obj.forward(40)
        obj.left(45)
        obj.forward(math.sqrt(5000))
        obj.end_fill()


class Wheel:
    def __init__(self, color):
        self.color = color

    def draw(self):
        self.backTire()
        self.frontTire()

    def backTire(self):
        obj.up()
        obj.fillcolor(self.color)
        obj.right(45)
        obj.forward(100)
        obj.right(90)
        obj.forward(100)
        obj.down()
        obj.right(180)
        obj.begin_fill()
        obj.circle(25, 360)
        obj.end_fill()

    def frontTire(self):
        obj.up()
        obj.fillcolor(self.color)
        obj.left(90)
        obj.forward(90)
        obj.right(90)
        obj.down()
        obj.begin_fill()
        obj.circle(25, 360)
        obj.end_fill()


class Antenna:
    def draw(self):
        obj.up()
        obj.forward(50)
        obj.left(90)
        obj.forward(60)
        obj.right(90)
        obj.down()
        obj.forward(60)


class Window:
    def __init__(self, color):
        self.color = color

    def draw(self, x, y):
        obj = turtle.Turtle()
        obj.fillcolor(self.color)
        obj.begin_fill()
        obj.up()
        obj.goto(x + 5, y - 5)
        obj.down()
        obj.forward(40)
        obj.right(90)
        obj.forward(40)
        obj.right(90)
        obj.forward(40)
        obj.right(90)
        obj.forward(40)
        obj.end_fill()


class Packages:
    def __init__(self, color):
        self.color = color

    def draw(self, x, y):
        obj = turtle.Turtle()
        obj.fillcolor(self.color)
        obj.begin_fill()
        obj.up()
        obj.goto(x + 70, y - 50)
        obj.down()
        obj.left(90)
        obj.forward(50)
        obj.right(90)
        obj.forward(10)
        obj.right(90)
        obj.forward(20)
        obj.left(90)
        obj.forward(40)
        obj.left(90)
        obj.forward(20)
        obj.right(90)
        obj.forward(10)
        obj.right(90)
        obj.forward(50)
        obj.right(90)
        obj.forward(60)
        obj.end_fill()
        obj.begin_fill()
        obj.up()
        obj.goto(x + 80, y)
        obj.down()
        obj.right(90)
        obj.forward(40)
        obj.right(90)
        obj.forward(40)
        obj.right(90)
        obj.forward(60)
        obj.right(90)
        obj.forward(40)
        obj.end_fill()
        obj.up()
        obj.goto(x + 80, y + 40)
        obj.down()
        obj.goto(x + 50, y - 50)
        obj.up()
        obj.goto(x + 120, y + 40)
        obj.down()
        obj.goto(x + 150, y - 50)


class Headlights:
    def __init__(self, headlightsColor, taillightColor, x, y):
        self.headlightsColor = headlightsColor
        self.taillightColor = taillightColor
        self.x = x
        self.y = y

    def draw(self):
        self.headlights()
        self.taillights()

    def headlights(self):
        obj = turtle.Turtle()
        obj.fillcolor(self.headlightsColor)
        obj.begin_fill()
        obj.up()
        obj.goto(self.x - 90, self.y - 60)
        obj.down()
        obj.forward(20)
        obj.right(90)
        obj.forward(15)
        obj.right(90)
        obj.forward(20)
        obj.right(90)
        obj.forward(15)
        obj.end_fill()

    def taillights(self):
        obj = turtle.Turtle()
        obj.fillcolor(self.taillightColor)
        obj.begin_fill()
        obj.up()
        obj.goto(self.x + 130, self.y - 60)
        obj.down()
        obj.forward(20)
        obj.right(90)
        obj.forward(15)
        obj.right(90)
        obj.forward(20)
        obj.right(90)
        obj.forward(15)
        obj.end_fill()


def Vehicle(x, y, bodycolor, windowcolor, packagecolor, wheelColor, headlightsColor, taillightColor):
    body = Body(bodycolor)
    body.draw(x, y)
    window = Window(windowcolor)
    window.draw(x, y)
    packages = Packages(packagecolor)
    packages.draw(x, y)
    wheel = Wheel(wheelColor)
    wheel.draw()
    antenna = Antenna()
    antenna.draw()
    headlights = Headlights(headlightsColor, taillightColor, x, y)
    headlights.draw()


Vehicle(60, 60, 'blue', 'lightblue', 'red', 'black', 'yellow', 'red')

screen.listen()
screen.mainloop()
