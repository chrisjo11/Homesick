from gamesetup import MyGame
import arcade

# Inititial variables for screen details
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Sprite Rooms Example"

def main():
    # Sets up the window and plays the game
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

# Runs the program
main()