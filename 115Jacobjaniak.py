#   a115_buggy_image.py
import turtle as trtl

num_turtle = trtl.Turtle()
num_turtle.pensize(40)
num_turtle.circle(20)
w = 6
y = 70
z = 380 / w
num_turtle.pensize(5)
n = 0
while (n < w):
  num_turtle.goto(0,0)
  num_turtle.setheading(z*n)
  num_turtle.forward(y)
  n = n + 1
num_turtle.hideturtle()
wn = trtl.Screen()
wn.mainloop()