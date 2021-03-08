from gamesetup import MyGame
import arcade

# Inititial variables for screen details
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Sprite Rooms Example"

def main():
    # # Sets up tkinter menu screen
    # root = Tk()
    # root.title("Homesick")
    # root.geometry("400x200")
    # app = Application(root)
    # root.mainloop()

    # if app.startGame:
    #     # Closes tkinter menu screen, and sets up the window and plays the game
    #     print(app.volume)
    #     print(app.isEasy)
    #     window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    #     window.setup()
    #     arcade.run()
    
    # Closes tkinter menu screen, and sets up the window and plays the game
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

# Runs the program
main()