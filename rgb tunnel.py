from turtle import *
colormode(255)
speed(0)
ht()
def s(n, r, g, b):    
    color(r, g, b)
    bgcolor(r, g, b)
    circle((i/2)+(n/2))
    left(1)

for i in range(256):
    s(1, 0 , 255 - i, i)
for i in range(256):
    s(257, i, 0, 255 - i)
for i in range(256):
    s(513, 255 - i, i, 0)

bgcolor(0, 0, 0)
