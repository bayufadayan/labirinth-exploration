from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint


def update():

    global rainbow_spd
    rainbow_cube.rotation_x += time.dt * 200
    rainbow_cube.rotation_y += time.dt * 200
    rainbow_cube.x = rainbow_cube.x + time.dt * rainbow_spd
    rainbow_cube.y = rainbow_cube.y + time.dt * rainbow_spd
    if abs(rainbow_cube.x) > 3:
        rainbow_spd = -rainbow_spd

    R = randint(2, 255)
    G = randint(2, 255)
    B = randint(2, 255)
    rainbow_cube.color = color.rgb (R, G, B)

    if held_keys['left mouse']:
        trying.rotation = (0, 0, 40)
        trying.y = -0.40
        
    else :
        trying.rotation = (0, 0, 68)
        trying.x = 0.5

app = Ursina()

Sky()
player = FirstPersonController()
ground = Entity(
    model = "plane",
    scale = 499,
    color = color.lime,
    texture = "white_cube",
    texture_scale = (499,499),
    collider = "box"
)
wall1 = Entity(
    model = 'cube',
    texture = 'assets/Texture/textures/old_sandstone_02_diff_1k.jpg',
    scale = (2, 50, 20),
    position = (8, 0, 0),
    collider = 'box',
    texture_scale = (2, 2),
    rotation = (0,0,0),
)

wall2 = duplicate(
    wall1,
    position = (-8, 0, 0)
)

components1 = Entity(
    model = 'cube',
    collider = "mesh",
    position = (0,0,6),
    rotation = (0,0,0),
    texture = "brick",
)

trying = Entity(
    model = 'vorpal_sword.glb',
    parent = camera.ui,
    scale = 0.5,
    x = 0.5,
    y = -0.25,
    color = color.red, 
    rotation = (0, 0, 68)
)

x = Entity (
    model = 'cube',
    position = (0, 0, 0),
    scale = (1,1,1),
    color = color.blue
)

rainbow_cube = Entity(
    model = 'cube',
    position = (0,4,4),
    texture = "white_cube"
)
rainbow_spd = 1

app.run()