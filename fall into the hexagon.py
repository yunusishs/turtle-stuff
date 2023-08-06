import turtle as t
from itertools import cycle
def hexagon(size):
    t.color(next(colors))
    t.forward(size)
    t.left(61)
    hexagon(size+1)
t.speed(0)
t.bgcolor('black')
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])
hexagon(1)
