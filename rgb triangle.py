import turtle as t
t.colormode(255)
t.shape('triangle')
for i in range(255):
    t.color(0,i,255-i)
    t.shapesize((255-i)/2)
    t.right(1)
    t.stamp()
