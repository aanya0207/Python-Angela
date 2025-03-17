from turtle import Turtle, Screen
import random
# Set up the Turtle
tim = Turtle()
tim.shape("turtle")
# Draw shapes with different number of sides
def draw_shape(sides):
    for j in range(sides):
            angle = 360 / sides
            tim.forward(100)
            tim.right(angle)
# List of colors for turtles
colours = ["CornflowerBlue","DarkOrchid","forest green", "blue", "yellow", "coral", "black",
          "beige", "slate gray", "orange", "red", "turquoise"]

for shape_side_n in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()  # Keeps the window open until clicked