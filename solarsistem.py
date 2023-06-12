from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import numpy as np


def update():
    global t
    t = t + 0.1
    angle = np.pi*40/180
    
    radius_1 = 7
    mercury.x = np.cos(t)*radius_1
    mercury.z = np.sin(t)*radius_1    

    radius_2 = 8
    venus.x = np.cos(t+angle)*radius_2
    venus.z = np.sin(t+angle)*radius_2    

    radius_3 = 10
    earth.x = np.cos(t+angle*2)*radius_3
    earth.z = np.sin(t+angle*2)*radius_3    

    radius_4 = 12
    mars.x = np.cos(t+angle*3)*radius_4
    mars.z = np.sin(t+angle*3)*radius_4

    radius_5 = 13
    jupiter.x = np.cos(t+angle*4)*radius_5
    jupiter.z = np.sin(t+angle*4)*radius_5  
    
    radius_6 = 15
    saturn.x = np.cos(t+angle*5)*radius_6
    saturn.z = np.sin(t+angle*5)*radius_6  

    radius_7 = 16
    uranus.x = np.cos(t+angle*6)*radius_7
    uranus.z = np.sin(t+angle*6)*radius_7  

    radius_8 = 18
    neptune.x = np.cos(t+angle*7)*radius_8
    neptune.z = np.sin(t+angle*7)*radius_8  

    radius_9 = 20
    pluto.x = np.cos(t+angle*8)*radius_9
    pluto.z = np.sin(t+angle*8)*radius_9  

app = Ursina()

player = FirstPersonController()
Sky(texture = "assets/Texture/sky/2k_jupiter.jpg")
ground = Entity(
    model = "plane",
    scale = 499,
    color = "#556B2F",
    texture = "assets/Texture/textures/aerial_grass_rock_diff_1k.jpg",
    texture_scale = (100,100),
    collider = "box"
)

sun = Entity(model='sphere',color=color.red, scale=10, y = 10, texture = 'assets/Texture/textures/coast_sand_rocks_02_diff_1k.jpg')

mercury = Entity(model='sphere',color=color.gray, scale=1.4, y = 10, texture = 'assets/Texture/textures/rock_pitted_mossy_diff_1k.jpg')
venus = Entity(model='sphere',color=color.orange, scale=2, y = 10, texture = 'assets/Texture/textures/defense_wall_diff_1k.jpg')
earth = Entity(model='sphere',color=color.blue, scale=2.7, y = 10, texture = 'assets/Texture/textures/coast_sand_rocks_02_diff_1k.jpg')
mars = Entity(model='sphere',color=color.violet, scale=2, y = 10, texture = 'assets/Texture/sky/2k_jupiter.jpg')
jupiter = Entity(model='sphere',color=color.yellow, scale=4, y = 10, texture = 'assets/Texture/textures/rock_pitted_mossy_diff_1k.jpg')
saturn = Entity(model='sphere',color=color.white, scale=3.4, y = 10, texture = 'assets/Texture/textures/rock_pitted_mossy_diff_1k.jpg')
uranus = Entity(model='sphere',color=color.cyan, scale=4, y = 10, texture = 'assets/Texture/textures/defense_wall_diff_1k.jpg')
neptune = Entity(model='sphere',color=color.gold, scale=3.4, y = 10, texture = 'assets/Texture/textures/coast_sand_rocks_02_diff_1k.jpg')
pluto = Entity(model='sphere',color=color.pink, scale=1.4, y = 10, texture = 'assets/Texture/textures/coast_sand_rocks_02_diff_1k.jpg')

t = -np.pi

app.run()