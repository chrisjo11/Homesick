import arcade

import arcade.gui
from arcade.gui import UIManager

music = False

class MusicButton(arcade.gui.UIFlatButton):
    def on_click(self):
        music == True

class PlayButton(arcade.gui.UIFlatButton):
    def on_click(self):
        """ Called when user lets off button """
        print("Play")

class MyView(arcade.View):
    """
    Main view. Really the only view in this example. """
    def __init__(self):
        super().__init__()

        self.ui_manager = UIManager()

    def on_draw(self):
        """ Draw this view. GUI elements are automatically drawn. """
        arcade.start_render()

        if music == True:
            arcade.draw_text("Music: 4'33'' by John Cage", 200, 200, arcade.color.WHITE, 12)

    def on_show_view(self):
        """ Called once when view is activated. """
        self.setup()
        arcade.set_background_color(arcade.color.BLACK)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        """ Set up this view. """
        self.ui_manager.purge_ui_elements()

        y_slot = self.window.height//2
        left_column_x = self.window.width
        right_column_x = self.window.width//4

        button = PlayButton(
            'Play',
            center_x=right_column_x,
            center_y=y_slot * 1,
            width=250,
            # height=20
        )
        self.ui_manager.add_ui_element(button)

        button2 = MusicButton(
            "Music",
            center_x=right_column_x*2.9,
            center_y=y_slot,
            width=250
        )
        self.ui_manager.add_ui_element(button2)


if __name__ == '__main__':
    window = arcade.Window(title='ARCADE_GUI')
    view = MyView()
    window.show_view(view)
    arcade.run()