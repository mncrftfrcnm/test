import pyglet
import ratcave as rc


# Create Window
window = pyglet.window.Window()

def update(dt):
    pass
pyglet.clock.schedule(update)

# Insert filename into WavefrontReader.
obj_filename = rc.resources.obj_primitives
obj_reader = rc.WavefrontReader(obj_filename)

# Create Mesh
cube = obj_reader.get_mesh("c")
cube.position.xyz = 0, 0, -3

tex = rc.Texture.from_image(rc.resources.img_uvgrid)                                                                                                                                        
#cube.textures.append(tex)

# cube.rotation.y += 45
# cube.rotation.x += 45
# Create Scene
scene = rc.Scene(meshes=[cube])

@window.event
def on_draw():
    with rc.default_shader,tex:
        scene.draw()
def rotatecube():

    cube.rotation.y+=1
    cube.rotation.x+=1

pyglet.app.run()