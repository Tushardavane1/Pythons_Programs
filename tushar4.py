import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pensize(2)
t.speed(0.001)
for i in range(90):
    turtle.color("red")
    turtle.forward(20)
    turtle.circle(100)
    turtle.left(24)
    turtle.right(30)
    turtle.forward(34)
turtle.done()    