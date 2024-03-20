from turtle import *
wind= Turtle()

def bouton_exit():
    wind.tracer(0)
    exit = Turtle()
    exit.hideturtle()
    exit.penup()
    exit.goto(150, -250)
    exit.pendown()
    exit.pensize(5)
    exit.color("white")
    exit.begin_fill()
    for i in range(2):
        exit.pencolor("black")
        exit.forward(80)
        exit.right(90)
        exit.forward(40)
        exit.right(90)
    exit.end_fill()
    exit.penup()
    exit.goto(160, -275)
    exit.write("exit", font=("Courier", 14, 'normal'))
    wind.tracer(1)

bouton_exit()