import random
import arcade
import os
from roomsetup import Room

# Scaling variables
SPRITE_SCALING = 0.25
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)
SPRITE_SCALING_PART_2 = 0

# Inititial variables for screen details
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Sprite Rooms Example"

# Initial variables for object sprites
walls = ":resources:images/tiles/boxCrate.png"
grass_sprout = ":resources:images/tiles/grass_sprout.png"
trees = ":resources:images/topdown_tanks/treeGreen_large.png"
enemies = ":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png"
pathway = ":resources:images/tiles/snowCenter.png"
bushes = ":resources:images/tiles/bush.png"
pebbles = ":resources:images/space_shooter/meteorGrey_med1.png"
gates = ":resources:images/items/ladderTop.png"
watersprite = ":resources:images/tiles/water.png"
bridgepaths = ":resources:images/tiles/boxCrate_double.png"
bridgerails = ":resources:images/tiles/bridgeB.png"

class rooms():
    def setup_room_1(): # Create and returns the first room
        # Initializes a room object
        room = Room()

        # Sprite lists
        room.wall_list = arcade.SpriteList()
        room.enemy_list = arcade.SpriteList()
        room.background_list = arcade.SpriteList()

        # Creates the the crates for the maze in the first room
        for x in range(0, 800, 32):
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = x+17
            wall.center_y = 794
            room.wall_list.append(wall)

        for x in range(0, 800, 32):
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = x+17
            wall.center_y = 7
            room.wall_list.append(wall)

        for y in range(80, 800, 32):
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = 795
            wall.center_y = y+20
            room.wall_list.append(wall)
            
        for y in range(0, 800, 32):
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = 4
            wall.center_y = y+17
            room.wall_list.append(wall)
        
        for x in range(0, 350, 32): #1
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = x+15
            wall.center_y = 700
            room.wall_list.append(wall)

        for x in range(0, 350, 32): #2
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = x+500
            wall.center_y = 700
            room.wall_list.append(wall)
        
        for y in range(0, 100, 32): #3
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = 336
            wall.center_y = y+605
            room.wall_list.append(wall)

        for y in range(0, 125, 32): #4
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = 500
            wall.center_y = y+605
            room.wall_list.append(wall)
        
        for x in range(0, 170, 32): #5
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = x+500
            wall.center_y = 580
            room.wall_list.append(wall)
        
        for y in range(450, 640, 32): #6
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = 660
            wall.center_y = y-30
            room.wall_list.append(wall)
        
        for y in range(400, 490, 32): #9
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = 297
            wall.center_y = y+15
            room.wall_list.append(wall)
        
        for x in range(370, 500, 32): #8
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = x-70
            wall.center_y = 415
            room.wall_list.append(wall)
        
        for x in range(300, 450, 32): #7
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = x+228
            wall.center_y = 420
            room.wall_list.append(wall)
        
        for x in range(180, 330, 32): #10
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = x-10
            wall.center_y = 500
            room.wall_list.append(wall)
        
        for x in range(150, 250, 32): #11
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = x-70
            wall.center_y = 585
            room.wall_list.append(wall)
        
        for y in range(0, 580, 32): #12
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = 80
            wall.center_y = y+10
            room.wall_list.append(wall)
        
        for y in range(150, 500, 32): #13
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = 170
            wall.center_y = y+3
            room.wall_list.append(wall)
        
        for x in range(170, 220, 32): #14
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = x
            wall.center_y = 123
            room.wall_list.append(wall)
        
        for y in range(0, 800, 32): #15
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = 4
            wall.center_y = y+17
            room.wall_list.append(wall)
        
        for x in range(330, 500, 32): #17
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = x
            wall.center_y = 290
            room.wall_list.append(wall)
        
        for y in range(100, 290, 32): #18
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = 490
            wall.center_y = y
            room.wall_list.append(wall)
        
        for x in range(500, 630, 32): #19
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = x-8
            wall.center_y = 100
            room.wall_list.append(wall)
        
        for y in range(100, 250, 32): #20
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = 622
            wall.center_y = y
            room.wall_list.append(wall)
        
        for y in range(100, 250, 32): #21
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = 710
            wall.center_y = y
            room.wall_list.append(wall)
        
        for x in range(710, 800, 32): #22
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = x
            wall.center_y = 100
            room.wall_list.append(wall)
        
        for y in range(0, 290, 32): #23
            wall = arcade.Sprite(walls, SPRITE_SCALING+SPRITE_SCALING_PART_2)
            wall.center_x = 330
            wall.center_y = y
            room.wall_list.append(wall)

        room.wall_list.append(wall)

        # Load the background image for this level.
        room.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")

        return room


    def setup_room_2(): # Create and return the second room
        # Initializes a room object
        room = Room()

        # Sprite lists
        room.wall_list = arcade.SpriteList()
        room.enemy_list = arcade.SpriteList()
        room.background_list = arcade.SpriteList()

        # Creates the sprites for the gate
        for i in range(150, 800, 32):
            gate = arcade.Sprite(gates, SPRITE_SCALING)
            gate.center_x = 797
            gate.center_y = i
            room.wall_list.append(gate)

        # Creates the sprites for the bushes
        for i in range(100, 800, 100):
            bush = arcade.Sprite(bushes, SPRITE_SCALING+.2)
            bush.center_x = i
            bush.center_y = random.randint(200, 500)
            room.wall_list.append(bush)
            bush = arcade.Sprite(bushes, SPRITE_SCALING+.2)
            bush.center_x = i
            bush.center_y = random.randint(500, 700)
            room.wall_list.append(bush)
        
        # Creates the sprites for the pebbles
        for i in range(200, 800, 150):
            pebble = arcade.Sprite(pebbles, SPRITE_SCALING+.2)
            pebble.center_x = i+random.randrange(-25, 25)
            pebble.center_y = random.randint(20, 60)
            room.wall_list.append(pebble)
            pebble = arcade.Sprite(pebbles, SPRITE_SCALING+.2)
            pebble.center_x = i+random.randrange(-25, 25)
            pebble.center_y = random.randint(90, 125)
            room.wall_list.append(pebble)

        # Creates the sprites for the grass
        for i in range(1, 800):
            grass = arcade.Sprite(grass_sprout, SPRITE_SCALING)
            grass.center_x = random.randint(1, 800)
            grass.center_y = random.randint(1, 800)
            room.background_list.append(grass)
        
        # Creates the sprites for the path
        for n in range(1, 5):
            for i in range(0, 900, 32):
                path = arcade.Sprite(pathway, SPRITE_SCALING)
                path.center_x = i
                path.center_y = (n*32-10)
                room.background_list.append(path)
        for n in range(1, 5):
            for i in range(0, 900, 32):
                indent = random.randrange(-5, 5)
                path = arcade.Sprite(pathway, SPRITE_SCALING)
                path.center_x = i
                path.center_y = (n*32-10)+indent
                room.background_list.append(path)

        # Creates the sprites for the enemies
        for i in range(1, 5):
            enemy = arcade.Sprite(enemies, SPRITE_SCALING+0.1)
            enemy.center_x = 100+150*i
            enemy.center_y = random.randrange(0, 800)
            enemy.change_y = 7
            enemy.change_x = 0
            room.enemy_list.append(enemy)
        for i in range(1, 5):
            enemy = arcade.Sprite(enemies, SPRITE_SCALING+0.1)
            enemy.center_x = 150+150*i
            enemy.center_y = random.randrange(0, 800)
            enemy.change_y = 7
            enemy.change_x = 0
            room.enemy_list.append(enemy)
        
        # Creates the sprites for the trees
        for i in range(1, 11):
            tree = arcade.Sprite(trees, SPRITE_SCALING + random.randrange(75, 100)/100)
            tree.center_x = 20+random.randrange(0, 25)
            tree.center_y = 100 + i*70
            room.wall_list.append(tree)
        for i in range(1, 13):
            tree = arcade.Sprite(trees, SPRITE_SCALING + random.randrange(75, 100)/100)
            tree.center_x = i*70+20
            tree.center_y = 775+random.randrange(0, 25)
            room.wall_list.append(tree)

        # REDUNDANT CODE FOR NOW, MAY BE USEFUL LATER
        # Load the background image for this level.
        # room.background = arcade.load_texture(":resources:images/backgrounds/abstract_2.jpg")

        return room

    def setup_room_3(): # Create and returns the third room
        # Initializes a room object
        room = Room()

        # Sprite lists
        room.wall_list = arcade.SpriteList()
        room.enemy_list = arcade.SpriteList()
        room.background_list = arcade.SpriteList()

        # Load the background image for this level.
        room.background = arcade.load_texture(":resources:images/backgrounds/stars.png")

        # Creates the water sprites
        for n in range(1, 5):
            for i in range(0, 350, 32):
                water = arcade.Sprite(watersprite, SPRITE_SCALING)
                water.center_x = 400 + (n*32)
                water.center_y = i
                room.wall_list.append(water)
            for i in range(450, 800, 32):
                water = arcade.Sprite(watersprite, SPRITE_SCALING)
                water.center_x = 400 + (n*32)
                water.center_y = i
                room.wall_list.append(water)
        for n in range(1, 5):
            for i in range(0, 350, 32):
                indent = random.randrange(-5, 5)
                water = arcade.Sprite(watersprite, SPRITE_SCALING)
                water.center_x = 400+(n*32)+indent
                water.center_y = i
                room.wall_list.append(water)
            for i in range(450, 800, 32):
                indent = random.randrange(-5, 5)
                water = arcade.Sprite(watersprite, SPRITE_SCALING)
                water.center_x = 400+(n*32)+indent
                water.center_y = i
                room.wall_list.append(water)
        
        for n in range(-2, 2):
            for i in range(350, 630, 32):
                bridgepath = arcade.Sprite(bridgepaths, SPRITE_SCALING*0.95)
                bridgepath.center_x = i
                bridgepath.center_y = 400+n*32
                room.background_list.append(bridgepath)


        return room