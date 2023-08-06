import turtle as t
t.colormode(255)
t.shape('square')
t.speed(0)
for i in range(255):
    t.color(255-i,255-i,255-i)
    t.shapesize((255-i)/3)
    t.right(1)
    t.stamp()
