#filename = 'liberint.txt'
import sys
from vpython import *
from random import *
filename = 'liberint.txt'
# yt = str(ty)
t = []
images = ['treesmall.gif','bushsmall.gif']
#[1,1,1,1,0,0,0,0,1,1,1,1,2,0,0,0,0,1,1,1,1,0,0,1,1,1,1,2,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,2,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,2]
x,y,z = 0,0,0
def do_liberint(liberint, blocks):
    global x,y,z

    x,y = 0,0
    filename = liberint
    # yt = str(ty)
    t = []
    with open(filename, 'r') as file_object:
        contents = file_object.read()
        for yuu in contents:
            t.append(yuu)
            

    for yu in t:
        if yu == '0':
            x -= 0.9
        if yu == '1':
            blocks.append(sphere(pos=vector(x,y,z), color=color.cyan, size=.4*vector(3,3,3)))
        if yu == '2':
            x = 0
            y -= 0.9
        if yu == '3':
            x, y = 0, 0
            z -= 0.9