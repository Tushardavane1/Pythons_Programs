import turtle
t = turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
turtle.speed(0.1)
col=("yellow","red","pink","cyan","light green","blue")

for i in range(150):
    turtle.pencolor(col[i%6])
    turtle.circle(150-i/2,90)
    turtle.lt(90)
    turtle.circle(150-i/3,90)
    turtle.lt(60)
turtle.done()    