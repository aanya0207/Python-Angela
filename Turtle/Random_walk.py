from turtle import Turtle,Screen
import random

# Set up the Screen
screen = Screen()
screen.colormode(255)

# Set up the Turtle
tim = Turtle()
tim.shape("turtle")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colours = (r,g,b)
    return colours

directions = [0,90,180,270]
tim.pensize(10)
tim.speed("fastest")
for i in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.seth(random.choice(directions))


screen.exitonclick()