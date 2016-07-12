import turtle

def drawSquare(someTurtle):
    someTurtle.speed(.2)
    someTurtle.shape("turtle")
    for i in range(1,5):
        someTurtle.forward(50)
        someTurtle.right(90)

def drawPetals(someTurtle):
    someTurtle.speed(.5)
    someTurtle.shape("turtle")
    someTurtle.forward(43)
    for i in range(1,50):
        someTurtle.right(4)
        someTurtle.forward(.5)
    someTurtle.forward(43)
    

    
def drawArt():
    window = turtle.Screen()
    window.bgcolor("white")
    brad = turtle.Turtle()
    for i in range(1, 74):
        if i % 2 == 0:
           brad.color("blue")
        else:
            brad.color("red")
        drawSquare(brad)
        brad.right(5)
    for i in range(1,12):
        brad.color("white")
        drawPetals(brad)
    brad.right(90)
    brad.forward(70)
    brad.color("green")
    brad.forward(80)
    window.exitonclick()

drawArt()
