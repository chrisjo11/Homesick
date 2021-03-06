import arcade
import os

SPRITE_SCALING = 0.25

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Home Sick"

MOVEMENT_SPEED = 5

class Homesick(arcade.Window):
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
        self.coin_list = None
        self.wall_list = None
        self.player_list = None

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None

        self.stage1 = True
        self.stage2 = False
        self.stage3 = False

    def createMaze(self):
        for x in range(0, 800, 32):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x+17
            wall.center_y = 794
            self.wall_list.append(wall)

        for x in range(0, 800, 32):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x+17
            wall.center_y = 7
            self.wall_list.append(wall)

        for y in range(80, 800, 32):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 795
            wall.center_y = y+20
            self.wall_list.append(wall)
            
        for y in range(0, 800, 32):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 4
            wall.center_y = y+17
            self.wall_list.append(wall)
        
        for x in range(0, 350, 32): #1
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x+15
            wall.center_y = 700
            self.wall_list.append(wall)

        for x in range(0, 350, 32): #2
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x+500
            wall.center_y = 700
            self.wall_list.append(wall)
        
        for y in range(0, 100, 32): #3
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 350
            wall.center_y = y+605
            self.wall_list.append(wall)

        for y in range(0, 125, 32): #4
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 500
            wall.center_y = y+605
            self.wall_list.append(wall)
        
        for x in range(0, 170, 32): #5
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x+500
            wall.center_y = 580
            self.wall_list.append(wall)
        
        for y in range(450, 640, 32): #6
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 670
            wall.center_y = y-35
            self.wall_list.append(wall)
        
        for y in range(400, 490, 32): #9
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 297
            wall.center_y = y+15
            self.wall_list.append(wall)
        
        for x in range(370, 500, 32): #8
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x-60
            wall.center_y = 415
            self.wall_list.append(wall)
        
        for x in range(300, 450, 32): #7
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x+238
            wall.center_y = 415
            self.wall_list.append(wall)
        
        for x in range(180, 330, 32): #10
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x-10
            wall.center_y = 500
            self.wall_list.append(wall)
        
        for x in range(150, 250, 32): #11
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x-70
            wall.center_y = 585
            self.wall_list.append(wall)
        
        for y in range(0, 580, 32): #12
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 80
            wall.center_y = y
            self.wall_list.append(wall)
        
        for y in range(150, 500, 32): #13
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 170
            wall.center_y = y+10
            self.wall_list.append(wall)
        
        for x in range(170, 220, 32): #14
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 130
            self.wall_list.append(wall)
        
        for y in range(0, 800, 32): #15
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 4
            wall.center_y = y+17
            self.wall_list.append(wall)
        
        for x in range(330, 500, 32): #17
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 290
            self.wall_list.append(wall)
        #martin
        for y in range(100, 290, 32): #18
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 490
            wall.center_y = y
            self.wall_list.append(wall)
        #martin
        for x in range(500, 630, 32): #19
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 100
            self.wall_list.append(wall)
        #martin
        for y in range(100, 250, 32): #20
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 630
            wall.center_y = y
            self.wall_list.append(wall)
        #martin
        for y in range(100, 250, 32): #21
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 710
            wall.center_y = y
            self.wall_list.append(wall)
        #martin
        for x in range(710, 800, 32): #22
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 100
            self.wall_list.append(wall)
        #martin
        for y in range(0, 290, 32): #23
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 315
            wall.center_y = y
            self.wall_list.append(wall)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/alien/alienBlue_front.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # -- Set up the maze
        self.createMaze()

        #:resources:images/topdown_tanks/treeGreen_large.png
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """ Renders the screen. """
        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
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

        if self.player_sprite.center_x > 800:
            self.stage2 = True
            print(self.stage2)
        
        # Call update on all sprites
        self.physics_engine.update()