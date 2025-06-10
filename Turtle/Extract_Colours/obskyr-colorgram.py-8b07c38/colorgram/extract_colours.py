#Extract Colours from image 
import colorgram
def extract_colours_from_image():
    rgb = []
    colours = colorgram.extract(r'C:\Users\aanya\Python Angela\Turtle\Extract_Colours\golden-retriever-dog-21668976.webp',30)
    for color in colours:
     r = color.rgb.r
     b = color.rgb.b
     g = color.rgb.g 
     new_colour = (r,g,b)
     rgb.append(new_colour)
    print(rgb) 
    return rgb


import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.penup()
tim.speed("fastest")
tim.hideturtle()
colours_list = extract_colours_from_image()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
# Create a dot 
number_of_dots = 100
for i in range (1,number_of_dots+1):
    tim.dot(20,random.choice(colours_list))
    tim.forward(50)
    if(i%10 ==0):
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()