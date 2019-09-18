#   a115_buggy_image.py
import turtle as trtl

num_turtle = trtl.Turtle()
num_turtle.pensize(40)
num_turtle.circle(20)
num_leg = 6
leg_length = 70
leg_placement = 360 / num_leg
num_turtle.pensize(5)
leg_count = 0
while (leg_count < num_leg):
  print("leg_placement*leg_count=", leg_placement*leg_count)
  num_turtle.goto(0,0)
  num_turtle.setheading(leg_placement*leg_count)
  num_turtle.forward(leg_length)
  leg_count = leg_count + 1
num_turtle.hideturtle()
wn = trtl.Screen()
wn.mainloop()