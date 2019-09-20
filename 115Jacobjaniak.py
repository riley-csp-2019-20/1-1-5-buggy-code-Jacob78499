#   a115_buggy_image.py
import turtle as trtl

num_turtle = trtl.Turtle()
num_turtle.speed(20)
num_turtle.pensize(40)
num_turtle.circle(20)
num_leg = 8
leg_length = 90
leg_placement = 10000 / num_leg
num_turtle.pensize(5)
leg_count = 0
while (leg_count < num_leg):
  print("leg_placement*leg_count=", leg_placement*leg_count)
  num_turtle.goto(0,20)
  num_turtle.setheading(leg_placement*leg_count)
  num_turtle.forward(leg_length)
  leg_count = leg_count + 1
num_turtle.hideturtle()

num_turtle.penup()
num_turtle.goto(35,50)
num_turtle.pendown()
num_turtle.begin_fill()
num_turtle.circle(25)
num_turtle.end_fill()

num_turtle.goto(30,50)
num_turtle.begin_fill()
num_turtle.color("red")
num_turtle.circle(2)
num_turtle.penup()
num_turtle.goto(20,57)
num_turtle.pendown()
num_turtle.begin_fill()
num_turtle.circle(2)
num_turtle.end_fill()

wn = trtl.Screen()
wn.mainloop()

