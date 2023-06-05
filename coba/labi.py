from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint

def update():
    global playerup

    if held_keys['i']:
        player.y += time.dt * playerup

app = Ursina ()
Sky(texture = "assets/Texture/sky/panorama_landscapes_186.jpg")
player = FirstPersonController()
ground = Entity(
    model = "plane",
    scale = 499,
    color = "#556B2F",
    texture = "assets/Texture/textures/aerial_grass_rock_diff_1k.jpg",
    texture_scale = (100,100),
    collider = "box"
)
playerup = 100







app.run()