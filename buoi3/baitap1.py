from turtle import *
shape("turtle")
tracer(2)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in colors:
    color(i)
    circle(100)
    left(60)
mainloop()