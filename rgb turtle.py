from turtle import *
colormode(255)
shape('turtle')
speed(0)
for i in range(256):
    color(255-i,255-i,255-i)
    shapesize((256-i)/2)
    right(1)
    stamp()
