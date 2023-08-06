import turtle as t
t.colormode(255)
t.speed('fastest')
t.shape('turtle')
for i in range(255):
    t.color(i,0,255-i)
    t.shapesize((255-i)/2)
    t.right(1)
    t.stamp()
