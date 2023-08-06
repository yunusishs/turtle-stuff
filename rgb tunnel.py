import turtle
turtle.colormode(255)
turtle.speed('fastest')
turtle.ht()
def s(n, r, g, b):    
    turtle.color(r, g, b)
    turtle.bgcolor(r, g, b)
    turtle.circle((i/2)+(n/2))
    turtle.left(360/255)

for i in range(255):
    s(1, 0 , 255 - i, i)
for i in range(255):
    s(256, i, 0, 255 - i)
for i in range(255):
    s(511, 255 - i, i, 0)

turtle.bgcolor(0, 0, 0)
