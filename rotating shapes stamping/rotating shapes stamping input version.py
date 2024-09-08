#all the parameters are shape, red, green, blue, and turn
from turtle import *

chosen_shape = input('Shape: ')

rgb = {'red':None, 'green':None, 'blue':None}
for i in rgb.keys():
    choice = input(i + ' "+" or "-" or "constant": ')
    if choice == "constant":
        value = int(input("Value: "))
    rgb[i] = choice
    
turn = int(input('Turn in degrees: '))

colormode(255)
shape(chosen_shape)
speed(0)

for i in range(256):
    for k in rgb.keys():
        if rgb[k] == "+":
            if k == 'red':
                red = i
            elif k == 'green':
                green = i
            elif k == 'blue':
                blue = i
        elif rgb[k] == "-":
            if k == 'red':
                red = 255-i
            elif k == 'green':
                green = 255-i
            elif k == 'blue':
                blue = 255-i
        else:
            if k == 'red':
                red = rgb[i]
            elif k == 'green':
                green = rgb[i]
            elif k == 'blue':
                blue = rgb[i]
    color(red, green, blue)
    shapesize((256-i)/8)
    right(turn)
    stamp()
