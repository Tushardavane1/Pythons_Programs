Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t=turtle.Turtle()
>>> s=turtle.Screen()
>>> s.bgcolor("black")
>>> s.penclor("white")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s.penclor("white")
AttributeError: '_Screen' object has no attribute 'penclor'
>>> s.pencolor("white")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s.pencolor("white")
AttributeError: '_Screen' object has no attribute 'pencolor'. Did you mean: '_bgcolor'?
>>> s.pencolor("green")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s.pencolor("green")
AttributeError: '_Screen' object has no attribute 'pencolor'. Did you mean: '_bgcolor'?
>>> t.pencolor("green")
