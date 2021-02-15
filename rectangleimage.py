# Turtle is what is used to make the square.
import turtle
t = turtle.Turtle()
w = int(input("Enter the width of the rectangle:"))
l = int(input("Enter the length of the rectangle:"))
turtle.forward(l)
turtle.left(90)
turtle.forward(w)
turtle.left(90)
turtle.forward(l)
turtle.left(90)
turtle.forward(w)
turtle.left(90)
# Credits to https://www.geeksforgeeks.org/draw-square-and-rectangle-in-turtle-python/
