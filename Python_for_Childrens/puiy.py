import vpython
from vpython import *
import random
import pygame
import dolibe_vp
import pygame.mixer
from pyjoycon import *
import pyjoycon

scene.width = scene.height = 600
scene.background = color.white
scene.range = 1.3
N = 15000
scene.title = f'A {N}-element points object with random radii and colors'
# Display frames per second and render time:
scene.append_to_title("<div id='fps'/>")

run = True
def Runbutton(b):
    global run
    if b.text == 'Pause':
        run = False
        b.text = 'Run'
    else:
        run = True
        b.text = 'Pause'

button(text='Pause', bind=Runbutton)
scene.append_to_caption("""
To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate.""")

p = []
last = vec(0,0,0)
for i in range(N):
    next = last+0.1*vec.random()
    while mag(next) > 1: # if next is outside the sphere, try another random value
        next = last+0.1*vec.random()
    p.append({'pos':next, 'radius':0.002+0.04*random(), 'color':(vec(1,1,1)+vec.random())/2})
    last = next
c = points(pos=p, size_units='world')
while True:
    rate(60)
    if run: # Currently there isn't a way to rotate a points object, so rotate scene.forward:
        scene.forward = scene.forward.rotate(angle=-0.005, axis=vec(0,1,0))