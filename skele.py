import turtle, math
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
        obj.circle(25,180)
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
    obj.fillcolor('black')

    def drawTires(self):
        self.backTire()
        self.frontTire()

    def backTire(self):
        obj.up()
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
        obj.left(90)
        obj.forward(90)
        obj.right(90)
        obj.down()
        obj.begin_fill()
        obj.circle(25, 460)
        obj.end_fill()


class Antenna:
    def draw(self):
        obj.goto(0,0)
        obj.forward(100)
        
class Window:
    def __init__(self, color):
        self.color = color
    def draw(self, x, y):
        obj = turtle.Turtle()
        obj.fillcolor(self.color)
        obj.begin_fill()
        obj.up()
        obj.goto(x+5, y-5)
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
        obj.goto(x+70, y-50)
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
        obj.goto(x+80, y)
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
        obj.goto(x+80, y+40)
        obj.down()
        obj.goto(x+50, y-50)
        obj.up()
        obj.goto(x+120, y+40)
        obj.down()
        obj.goto(x+150, y-50)

def Vehicle(x, y, bodycolor, windowcolor, packagecolor):
    body = Body(bodycolor)
    body.draw(x, y)
    window = Window(windowcolor)
    window.draw(x, y)
    packages = Packages(packagecolor)
    packages.draw(x, y)
print(Vehicle(60, 60, 'blue', 'lightblue', 'red'))
screen.listen()

screen.listen()
screen.mainloop()
