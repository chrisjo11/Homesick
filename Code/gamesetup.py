import random
import arcade
import os
from roomsetup import Room
from rooms import rooms
import math

# ONLY SET TRUE IF DEBUGGING
DEBUG = False

# Scaling variables
SPRITE_SCALING = 0.25
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)
SPRITE_SCALING_PART_2 = 0

# Inititial variables for screen details
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Sprite Rooms Example"

# Initial Variables for speed attributes
MOVEMENT_SPEED = 5
BULLET_SPEED = 4

# Initial variables for sound
MUSIC_VOLUME = 0.5

# Initial variables for object sprites
playerUp = ":resources:images/alien/alienBlue_climb2.png"
playerDown = ":resources:images/alien/alienBlue_front.png"
playerRight = ":resources:images/alien/alienBlue_walk1.png"
playerLeft = ":resources:images/alien/alienBlue_jump.png"

# Initial variables for difficulty
isEasy = False
isNormal = True
isHard = False

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sets a variable for the "current room"; holds sprite objects
        self.current_room = 0

        # WIP CODE FOR PUTTING LOCAL PNG SPRITES INTO ARCADE
        # self.sprite1 = arcade.Sprite("playerDown.png", SPRITE_SCALING)
        
        # Initialize a variable housing the rooms in the room object
        self.rooms = None
        
        # Initialize variables for sprites and lists
        self.player_sprite = None
        self.enemy_sprite = None
        self.player_list = None
        self.enemy_list = None
        self.background_list = None
        self.bullet_list = None
        self.killcount = 0
        self.total_time = 0
        self.timeEnd = 0

        # Initialize a variable for frame count
        self.frame_count = 0

        # Initialize a variable for the physics engine
        self.physics_engine = None

    def setup(self): # Sets up the game and initializes the variables
        # Set up the player
        self.player_sprite = arcade.Sprite(playerDown, SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
    
        # List of rooms
        self.rooms = []

        # Append the rooms into a list
        room = rooms.setup_room_1()
        self.rooms.append(room)

        room = rooms.setup_room_2()
        self.rooms.append(room)
        
        room = rooms.setup_room_3()
        self.rooms.append(room)

        room = rooms.setup_room_4()
        self.rooms.append(room)

        # Our starting room number
        self.current_room = 0

        # Create a physics engine for this room (only for the wall objects)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

    def on_draw(self): # Renders the screen
        arcade.start_render()

        # Draws the background texture for each room
        if self.current_room == 0:
            arcade.set_background_color((101, 67, 33))
        elif self.current_room == 1:
            arcade.set_background_color((0,154,23))
            arcade.draw_lrwh_rectangle_textured(0, 0,
                                                SCREEN_WIDTH, SCREEN_HEIGHT,
                                                self.rooms[self.current_room].background)
        elif self.current_room == 2:
            arcade.set_background_color((0,154,23))
        else:
            arcade.set_background_color((0, 0, 0))
            arcade.draw_lrwh_rectangle_textured(0, 0,
                                                SCREEN_WIDTH, SCREEN_HEIGHT,
                                                self.rooms[self.current_room].background)

        # Draws every "decoration" object
        self.rooms[self.current_room].background_list.draw()

        if self.current_room == 1:
            # Draws the enemies for each stage (only stages with enemies)
            if self.current_room in [1, 2]:
                self.rooms[self.current_room].enemy_list.draw()

            # Draw the walls for each room
            self.rooms[self.current_room].wall_list.draw()
        else:
            # Draw the walls for each room
            self.rooms[self.current_room].wall_list.draw()

            # Draws the enemies for each stage (only stages with enemies)
            if self.current_room in [1, 2]:
                self.rooms[self.current_room].enemy_list.draw()

        # Draws the bullets for the third stage
        if self.current_room == 2:
            self.rooms[self.current_room].bullet_list.draw()
        
        # Draws the player sprite
        self.player_list.draw()

        if self.current_room == 3:
            # Calculate minutes
            minutes = int(self.timeEnd) // 60

            # Calculate seconds
            seconds = int(self.timeEnd) % 60

            # Output timer
            if seconds >= 10:
                arcade.draw_text("Time: " + str(minutes) + ":" + str(seconds) + " Death Count: " + str(self.killcount),
                                400, 600, arcade.color.WHITE, 30, width=800, align="center",
                                anchor_x="center", anchor_y="center")
            else:
                arcade.draw_text("Time: " + str(minutes) + ":0" + str(seconds) + " Death Count: " + str(self.killcount),
                                    400, 600, arcade.color.WHITE, 30, width=800, align="center",
                                    anchor_x="center", anchor_y="center")

            # Output winning message
            arcade.draw_text("YOU WON!",
                            400, 700, arcade.color.WHITE, 50, width=800, align="center",
                            anchor_x="center", anchor_y="center")

            # Output exit message
            arcade.draw_text("Move into the spaceship\nto exit the program",
                            400, 200, arcade.color.WHITE, 30, width=800, align="center",
                            anchor_x="center", anchor_y="center")
        else:
            # Calculate minutes
            minutes = int(self.total_time) // 60

            # Calculate seconds
            seconds = int(self.total_time) % 60

            # Figure out our output
            output = f"Time: {minutes:02d}:{seconds:02d}"

            # Output the timer text.
            arcade.draw_text(output, 50, 750, arcade.color.WHITE, 15)

        # Debug for the player sprite's position
        if DEBUG:
            arcade.draw_text("X: " + str(self.player_sprite.center_x) + " Y: " + str(self.player_sprite.center_y),
                            100, 50, arcade.color.BLACK, 14, width=200, align="center",
                            anchor_x="center", anchor_y="center")

    def on_key_press(self, key, modifiers): # Called whenever a key is pressed
        # Moves the player based on key
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers): # Called whenever a key is released
        # Stops movement once key is released
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time): # Called continuously (continuous logic)
        self.total_time += delta_time
        self.frame_count += 1

        # Run the physics engine
        self.physics_engine.update()

        if self.player_sprite.center_x <= 0:
            self.player_sprite.center_x = 0
        if self.player_sprite.center_x >= SCREEN_WIDTH:
            self.player_sprite.center_x = 800
        if self.player_sprite.center_y <= 0:
            self.player_sprite.center_y = 0
        if self.player_sprite.center_y >= 800:
            self.player_sprite.center_y = 800


        # Figures out which room we are in, and if the "door" to the other room is passed, move to the other room
        if self.player_sprite.center_x >= SCREEN_WIDTH and self.current_room == 0:
            self.player_sprite.center_x = 5
            self.player_sprite.center_y = 50

            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)                                                
        elif self.player_sprite.center_x <= 0 and self.current_room == 1:
            self.player_sprite.center_x = 795
            self.player_sprite.center_y = 50

            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
        if self.player_sprite.center_x >= SCREEN_WIDTH and self.current_room == 1:
            self.player_sprite.center_x = 5
            self.player_sprite.center_y = 100

            self.current_room = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list) 
        elif (self.player_sprite.center_x <= 0 and self.player_sprite.center_y < 170) and self.current_room == 2:
            self.player_sprite.center_x = 795
            self.player_sprite.center_y = 50

            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
        if self.player_sprite.center_x >= SCREEN_WIDTH and self.current_room == 2:
            self.player_sprite.center_x = 5
            self.player_sprite.center_y = 100

            self.current_room = 3
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.timeEnd = self.total_time

        # Checks for collision with enemies in rooms with enemies
        if self.current_room == 1:
            colliding = arcade.check_for_collision_with_list(self.player_sprite, self.rooms[self.current_room].enemy_list)
            if len(colliding) > 0:
                self.player_sprite.center_x = 50
                self.player_sprite.center_y = 50
                music = arcade.Sound(":resources:sounds/hurt3.wav", streaming=True)
                music.play(MUSIC_VOLUME)
                self.killcount += 1

        # Moves the enemies in the second room
        if self.current_room == 1:
            for enemy in self.rooms[self.current_room].enemy_list:
                enemy.center_y += enemy.change_y
                enemy.center_x += enemy.change_x

                if enemy.center_y <= 0 or enemy.center_y >= 800:
                    enemy.change_y *= -1
        
        if self.current_room == 2:
            for enemy in self.rooms[self.current_room].enemy_list:
                # Position the start at the enemy's current location
                start_x = enemy.center_x
                start_y = enemy.center_y

                # Get the destination location for the bullet
                dest_x = self.player_sprite.center_x
                dest_y = self.player_sprite.center_y

                # Do math to calculate how to get the bullet to the destination.
                x_diff = dest_x - start_x
                y_diff = dest_y - start_y
                angle = math.atan2(y_diff, x_diff)

                # Set the enemy to face the player.
                enemy.angle = math.degrees(angle)-90

                if self.frame_count % 80 == 0: # Shoot at an interval (increasing with difficulty)
                    # Creates the sprite for the bullet
                    bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING+0.25)
                    bullet.center_x = start_x
                    bullet.center_y = start_y

                    # Angle the bullet sprite
                    bullet.angle = math.degrees(angle)

                    # Move the bullet towards the player
                    bullet.change_x = math.cos(angle) * BULLET_SPEED
                    bullet.change_y = math.sin(angle) * BULLET_SPEED

                    # PEW
                    music = arcade.Sound(":resources:sounds/laser1.mp3", streaming=True)
                    music.play(MUSIC_VOLUME)

                    self.rooms[self.current_room].bullet_list.append(bullet)

            # If the bullet is colliding with the player, move the player back to the beginning
            colliding = arcade.check_for_collision_with_list(self.player_sprite, self.rooms[self.current_room].bullet_list)
            if len(colliding) > 0:
                self.player_sprite.center_x = 50
                self.player_sprite.center_y = 50
                music = arcade.Sound(":resources:sounds/hurt3.wav", streaming=True)
                music.play(MUSIC_VOLUME)
                self.killcount += 1

            # Get rid of the bullet when it flies off-screen or if it hits a wall
            for bullet in self.rooms[self.current_room].bullet_list:
                colliding = arcade.check_for_collision_with_list(bullet, self.rooms[self.current_room].wall_list)
                if (isEasy and len(colliding) > 0) or bullet.top < 0:
                    bullet.remove_from_sprite_lists()

            self.rooms[self.current_room].bullet_list.update()
        if self.current_room == 3:
            colliding = arcade.check_for_collision_with_list(self.player_sprite, self.rooms[self.current_room].background_list)
            if len(colliding) > 0:
                collision = al;kjsdf;lsdjkflasjflskjf;lasdfj;lsadkfj;lkj # this crashes the code