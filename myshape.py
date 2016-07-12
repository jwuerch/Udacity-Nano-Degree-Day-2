import turtle

def drawTriangle(someTurtle, length):
    someTurtle.speed(1)
    someTurtle.color("black")
    someTurtle.shape("turtle")
    for i in range(1,4):
        someTurtle.left(120)
        someTurtle.forward(length)

def drawArt():
    window = turtle.Screen()
    window.bgcolor("white")
    brad = turtle.Turtle()
    drawTriangle(brad, 200)
    drawTriangle(brad, 20)
    window.exitonclick()

drawArt()
