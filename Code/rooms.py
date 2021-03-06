from roomsetup import Room
import arcade

SPRITE_SCALING = 0.25
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Sprite Rooms Example"

MOVEMENT_SPEED = 5

class rooms():
    def setup_room_1(self):
        """
        Create and return room 1.
        If your program gets large, you may want to separate this into different
        files.
        """
        room = Room()

        """ Set up the game and initialize the variables. """
        # Sprite lists
        room.wall_list = arcade.SpriteList()

        # -- Set up the walls
        # Create bottom and top row of boxes
        # This y loops a list of two, the coordinate 0, and just under the top of window
        for x in range(0, 800, 32):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x+17
            wall.center_y = 794
            room.wall_list.append(wall)

        for x in range(0, 800, 32):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x+17
            wall.center_y = 7
            room.wall_list.append(wall)

        for y in range(80, 800, 32):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 795
            wall.center_y = y+20
            room.wall_list.append(wall)
            
        for y in range(0, 800, 32):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 4
            wall.center_y = y+17
            room.wall_list.append(wall)
        
        for x in range(0, 350, 32): #1
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x+15
            wall.center_y = 700
            room.wall_list.append(wall)

        for x in range(0, 350, 32): #2
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x+500
            wall.center_y = 700
            room.wall_list.append(wall)
        
        for y in range(0, 100, 32): #3
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 350
            wall.center_y = y+605
            room.wall_list.append(wall)

        for y in range(0, 125, 32): #4
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 500
            wall.center_y = y+605
            room.wall_list.append(wall)
        
        for x in range(0, 170, 32): #5
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x+500
            wall.center_y = 580
            room.wall_list.append(wall)
        
        for y in range(450, 640, 32): #6
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 670
            wall.center_y = y-35
            room.wall_list.append(wall)
        
        for y in range(400, 490, 32): #9
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 297
            wall.center_y = y+15
            room.wall_list.append(wall)
        
        for x in range(370, 500, 32): #8
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x-60
            wall.center_y = 415
            room.wall_list.append(wall)
        
        for x in range(300, 450, 32): #7
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x+238
            wall.center_y = 415
            room.wall_list.append(wall)
        
        for x in range(180, 330, 32): #10
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x-10
            wall.center_y = 500
            room.wall_list.append(wall)
        
        for x in range(150, 250, 32): #11
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x-70
            wall.center_y = 585
            room.wall_list.append(wall)
        
        for y in range(0, 580, 32): #12
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 80
            wall.center_y = y
            room.wall_list.append(wall)
        
        for y in range(150, 500, 32): #13
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 170
            wall.center_y = y+10
            room.wall_list.append(wall)
        
        for x in range(170, 220, 32): #14
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 130
            room.wall_list.append(wall)
        
        for y in range(0, 800, 32): #15
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 4
            wall.center_y = y+17
            room.wall_list.append(wall)
        
        for x in range(330, 500, 32): #17
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 290
            room.wall_list.append(wall)
        
        for y in range(100, 290, 32): #18
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 490
            wall.center_y = y
            room.wall_list.append(wall)
        #
        for x in range(500, 630, 32): #19
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 100
            room.wall_list.append(wall)
        #martin
        for y in range(100, 250, 32): #20
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 630
            wall.center_y = y
            room.wall_list.append(wall)
        #martin
        for y in range(100, 250, 32): #21
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 710
            wall.center_y = y
            room.wall_list.append(wall)
        #martin
        for x in range(710, 800, 32): #22
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 100
            room.wall_list.append(wall)
        #martin
        for y in range(0, 290, 32): #23
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 315
            wall.center_y = y
            room.wall_list.append(wall)

        room.wall_list.append(wall)

        # If you want coins or monsters in a level, then add that code here.

        # Load the background image for this level.
        room.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")

        return room


    def setup_room_2(self):
        """
        Create and return room 2.
        """
        room = Room()

        """ Set up the game and initialize the variables. """
        # Sprite lists
        room.wall_list = arcade.SpriteList()

        # -- Set up the walls
        # Create bottom and top row of boxes
        # This y loops a list of two, the coordinate 0, and just under the top of window
        for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
            # Loop for each box going across
            for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
                wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

        # Create left and right column of boxes
        for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
            # Loop for each box going across
            for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
                # Skip making a block 4 and 5 blocks up
                if (y != SPRITE_SIZE * 1 and y != SPRITE_SIZE * 2) or x != 0:
                    wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
                    wall.left = x
                    wall.bottom = y
                    room.wall_list.append(wall)


        room.wall_list.append(wall)
        room.background = arcade.load_texture(":resources:images/backgrounds/abstract_2.jpg")

        return room