from turtle import *
colormode(255)
shape('triangle')
speed(0)
for i in range(256):
    color(255-i,255-i,255-i)
    shapesize((256-i)/3)
    right(1)
    stamp()
