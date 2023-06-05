from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint
from labirinth import Labirinth
from ursina.prefabs.health_bar import HealthBar

# ********************************************************************************
def update():
    global playerup, rainbow_spd

    if held_keys['shift']:
        player.y += time.dt * playerup

    if held_keys['escape']:
        application.quit()

    if player.y < -10:
        player.position = (0,1,0)
    
    kunci.rotation_z += time.dt * 100
    kunci.rotation_x += time.dt * 100

    if held_keys['left mouse']:
        my_sword.rotation = (0, 0, 40)
        my_sword.y = -0.40
    
    else :
        my_sword.rotation = (0, 0, 68)
        my_sword.y = 4,
    
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    batu_kristal.color = color.rgb(R, G, B)
    distance = player.position - batu_kristal.position
    if distance.length() <= 2:
        Hb.value += 10
    
    distance2 = player.position - monster1.position
    if distance2.length() <= 2:
        Hb.value -= 3
    
    global monster_health
    if held_keys['left mouse'] and mouse.hovered_entity == monster1:
        monster_health -= 1
        if monster_health == 0:
            monster1.disable()
# ********************************************************************************
app = Ursina()

Sky(texture = "assets/Texture/sky/panorama_landscapes_186.jpg")
for i in range (1, 300):
    awan_rand1 = randint(-50, 50)
    awan_rand2 = randint(-50, 50)
    awan_rand3 = randint(-50, 50)
    awan = Entity(
    model='assets/cloud/cloud.glb',
    scale = 1,
    position = (awan_rand1+awan_rand2-i-awan_rand3, randint(50, 80), awan_rand3+awan_rand1-i-awan_rand2)
    )

Hb = HealthBar(bar_color = color.green,roundness=.5,max_value = 500, text_color = color.black)

my_sword = Entity(
    model = 'assets/Weapon/vorpal_sword.glb',
    parent = camera.ui,
    scale = 0.5,
    x = 0.5,
    y = -0.25,
    color = color.red, 
    rotation = (0, 0, 68)
)
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
Labirinth()
kunci = Entity(
    model = 'assets/Kunci/darkest_dungeon_key.glb',
    position = (49, 70, 22),
    scale = 0.3,
    rotation = (90, 90, 0),
    color = color.gold,
)

batu_kristal = Entity(
    model="../assets/Stone/crystal.glb",
    position=(0, 0, -1),
    scale=1.5,
)

monster_health = 10
monster1 = Entity(
    model = 'assets/monster/animated_beholder_dungeons__dragons.glb',
    collider = "box",
    scale = (0.005),
    position = (0, 5, 10),
    rotation = (0, -45, 0)
)
monster1.add_script(SmoothFollow(target=player,offset =[0,1,0],speed = 0.5,rotation_offset=[0,1,0],rotation_speed = 5))

for i in range (1, 10):
    tree_rand1 = randint(-50, 50)
    tree_rand2 = randint(-50, 50)
    tree_rand3 = randint(-50, 50)
    tree = Entity(model = 'assets/Tree/tree (1).glb',
        scale = (0.1),
        position = (tree_rand1+tree_rand3-tree_rand2, 0, tree_rand3-tree_rand1+tree_rand2),
        color = color.lime)

# ************ Main Menu **********************
class MainMenu(Entity):
    def __init__(self):
        super().__init__(parent=camera.ui)

        self.main_menu = Entity(parent=self, enabled=True)
        self.player = None

        def start():
            monster1.enabled = True
            self.player.enabled = True
            mouse.locked = True
            self.main_menu.disable()
            self.player.time_running = True
        
        Entity(model = "quad", scale = (0.8, 0.2, 0.2), texture = "assets/logo_trans", parent = self.main_menu,y=0.15)
        start_button = Button(
            text="S t a r t - G a m e",
            color=color.green,
            scale=(0.3, 0.1),
            y=-0.1,
            parent=self.main_menu,
        )
        quit_button = Button(
            text="Q u i t",
            color=color.red,
            scale=(0.3, 0.1),
            y=-0.22,
            parent=self.main_menu,
        )
        quit_button.on_click = application.quit
        start_button.on_click = start

monster1.disable()
player.disable()
mouse.locked = False
m = MainMenu()
m.player = player
# **************************************************
app.run()