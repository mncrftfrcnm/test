import math
import pyglet
import ratcave as rc
import threading
from threading import Timer,Thread
import time
# Create Window
window = pyglet.window.Window()

def update(dt):
    pass
pyglet.clock.schedule(update)

# Insert filename into WavefrontReader.
obj_filename = rc.resources.obj_primitives
obj_reader = rc.WavefrontReader(obj_filename)

# Create Mesh
cube = obj_reader.get_mesh('Sphere')
cube2 = obj_reader.get_mesh('Cube')
cube2.position.xyz = 0, 0, -3

tex = rc.Texture.from_image(rc.resources.img_uvgrid)                                                                                                                                        
#cube.textures.append(tex)

cube.rotation.y -= 40
cube.rotation.x += 450
cube2.rotation.y -= 34
cube2.rotation.x += 40
# Create Scene
scene = rc.Scene(meshes=[cube2])

@window.event
def on_draw():
    with rc.default_shader,tex:
        scene.draw()

def rotatecube():

    cube.rotation.y+=1
    cube.rotation.x+=1
    print(cube.rotation.x)
def on_clik():
    with rc.default_shader,tex:
        rotatecube()

    
class vf(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            
            time.sleep(0.05)
            on_clik()

        
beep = vf()
beep.start()


pyglet.app.run()

    # rotatecube()
    