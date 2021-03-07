import random
import arcade
import os
from roomsetup import Room

SPRITE_SCALING = 0.25
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Sprite Rooms Example"

MOVEMENT_SPEED = 5
SPRITE_SCALING_PART_2 = 0

walls = ":resources:images/tiles/boxCrate.png"
grass_sprout = ":resources:images/tiles/grass_sprout.png"
trees = ":resources:images/topdown_tanks/treeGreen_large.png"
enemies = ":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png"
pathway = ":resources:images/tiles/stoneCenter.png"
playerUp = ":resources:images/alien/alienBlue_climb2.png"
playerDown = ":resources:images/alien/alienBlue_front.png"
playerRight = ":resources:images/alien/alienBlue_walk1.png"
playerLeft = ":resources:images/alien/alienBlue_jump.png"
bushes = ":resources:images/tiles/bush.png"
pebbles = ":resources:images/space_shooter/meteorGrey_med1.png"
gates = ":resources:images/items/ladderTop.png"

def setup_room_1():
    """
    Create and return room 1.
    If your program gets large, you may want to separate this into different
    files.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()
    room.background_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
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

    # If you want coins or monsters in a level, then add that code here.

    # Load the background image for this level.
    room.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")

    return room


def setup_room_2():
    """
    Create and return room 2.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()
    room.background_list = arcade.SpriteList()

    for i in range(150, 800, 32):
        gate = arcade.Sprite(gates, SPRITE_SCALING)
        gate.center_x = 785
        gate.center_y = i
        room.wall_list.append(gate)

    for i in range(100, 800, 100):
        bush = arcade.Sprite(bushes, SPRITE_SCALING+.2)
        bush.center_x = i
        bush.center_y = random.randint(200, 500)
        room.wall_list.append(bush)
        bush = arcade.Sprite(bushes, SPRITE_SCALING+.2)
        bush.center_x = i
        bush.center_y = random.randint(500, 700)
        room.wall_list.append(bush)
    for i in range(200, 800, 150):
        pebble = arcade.Sprite(pebbles, SPRITE_SCALING+.2)
        pebble.center_x = i+random.randrange(-25, 25)
        pebble.center_y = random.randint(20, 60)
        room.wall_list.append(pebble)
        pebble = arcade.Sprite(pebbles, SPRITE_SCALING+.2)
        pebble.center_x = i+random.randrange(-25, 25)
        pebble.center_y = random.randint(90, 125)
        room.wall_list.append(pebble)

    for i in range(1, 800):
        grass = arcade.Sprite(grass_sprout, SPRITE_SCALING)
        grass.center_x = random.randint(1, 800)
        grass.center_y = random.randint(1, 800)
        room.background_list.append(grass)
    for n in range(1, 5):
        for i in range(0, 900, 32):
            path = arcade.Sprite(pathway, SPRITE_SCALING)
            path.center_x = i
            path.center_y = n*32-10
            room.background_list.append(path)

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

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window

    room.background = arcade.load_texture(":resources:images/backgrounds/abstract_2.jpg")

    return room

def setup_room_3():
    """
    Create and return room 3.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()
    room.background_list = arcade.SpriteList()



    room.background = arcade.load_texture(":resources:images/backgrounds/stars.png")

    return room
class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.current_room = 0

        # Set up the player
        self.sprite1 = arcade.Sprite("playerDown.png", SPRITE_SCALING)
        
        self.rooms = None
        self.player_sprite = None
        self.enemy_sprite = None
        self.player_list = None
        self.enemy_list = None
        self.background_list = None
        self.physics_engine = None

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_sprite = arcade.Sprite(playerDown, SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
    

        # Our list of rooms
        self.rooms = []

        # Create the rooms. Extend the pattern for each room.

        room = setup_room_1()
        self.rooms.append(room)

        room = setup_room_2()
        self.rooms.append(room)
        
        room = setup_room_3()
        self.rooms.append(room)

        # Our starting room number
        self.current_room = 0

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.rooms[self.current_room].background)

        self.rooms[self.current_room].background_list.draw()

        if self.current_room == 1:
            self.rooms[self.current_room].enemy_list.draw()

        # Draw all the walls in this room
        self.rooms[self.current_room].wall_list.draw()
        
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        self.sprite1.set_position(400, 400)

        # Do some logic here to figure out what room we are in, and if we need to go
        # to a different room.
        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 0:
            self.player_sprite.center_x = 50
            self.player_sprite.center_y = 50

            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)                                                
        elif self.player_sprite.center_x < 0 and self.current_room == 1:
            self.player_sprite.center_x = 780
            self.player_sprite.center_y = 50

            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 1:
            self.player_sprite.center_x = 100
            self.player_sprite.center_y = 100

            self.current_room = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list) 
        elif self.player_sprite.center_x < 0 and self.current_room == 2:
            self.player_sprite.center_x = 775
            self.player_sprite.center_y = 50

            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
        if self.current_room == 1:
            colliding = arcade.check_for_collision_with_list(self.player_sprite, self.rooms[1].enemy_list)
            if len(colliding) > 0:
                self.player_sprite.center_x = 100
                self.player_sprite.center_y = 50
            if self.player_sprite.center_y <= 0:
                self.player_sprite.center_y = 0

        for enemy in self.rooms[self.current_room].enemy_list:
            enemy.center_y += enemy.change_y
            enemy.center_x += enemy.change_x

            if enemy.center_y <= 0 or enemy.center_y >= 800:
                enemy.change_y *= -1