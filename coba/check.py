from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint
from ursina.prefabs.health_bar import HealthBar

def update():
    global Hb

    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    batu_kristal.color = color.rgb(R, G, B)

    distance = player.position - batu_kristal.position
    if distance.length() <= 2:  # cek jika jarak antara pemain dan batu kristal kurang dari atau sama dengan 2
        Hb.value -= 1


app = Ursina()

Sky(texture="../assets/Texture/sky/panorama_landscapes_186.jpg")
player = FirstPersonController()

Hb = HealthBar(bar_color=color.green, roundness=.5, max_value=500, text_color=color.black)
ground = Entity(
    model="plane",
    scale=499,
    color="#556B2F",
    texture="../assets/Texture/textures/aerial_grass_rock_diff_1k.jpg",
    texture_scale=(100, 100),
    collider="box"
)

batu_kristal = Entity(
    model="../assets/Stone/crystal.glb",
    position=(0, 10, 0),
    scale=2,
)

monster = Entity(
    model = '../assets/monster/monster_plant(2).glb',
    collider = "sphere",
    scale = 0.005,
)
monster.add_script(SmoothFollow(target=player,offset =[0,1,0],speed = 1))

app.run()