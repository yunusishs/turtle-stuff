from turtle import *
colormode(255)
shape('square')
speed(0)
for i in range(256):
    color(255-i,255-i,255-i)
    shapesize((256-i)/8)
    right(1)
    stamp()
