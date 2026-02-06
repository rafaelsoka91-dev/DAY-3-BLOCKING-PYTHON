import turtle
import time
import random

print("This program draws shapes based on the number you enter in a uniform pattern.")
num_str = input("Enter the side number of the shape you want to draw: ")

if num_str.isdigit():
    squares = int(num_str)
else:
    squares = 4  # Default value if input is invalid
    print("Invalid input, defaulting to 4 sides.")

# Mathematical formula for the exterior angle of a regular polygon
angle = 360 / squares

turtle.speed(0) # Makes it draw faster
turtle.penup()

x = 0
y = 0
turtle.setpos(x, y)

numshapes = 8
for shape_count in range(numshapes):
    turtle.color(random.random(), random.random(), random.random())
    
    # Update movement variables
    x += 20 
    y += 45 # Using a larger angle shift to see the pattern clearly
    
    turtle.forward(x)
    turtle.left(y)
    
    # Draw the polygon
    turtle.begin_fill()
    turtle.pendown()
    for i in range(squares):
        turtle.forward(40)
        turtle.left(angle)
        turtle.penup()
        turtle.end_fill()

time.sleep(5)
turtle.bye()