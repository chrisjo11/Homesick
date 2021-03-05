import arcade

"""
Create a maze using a depth-first search maze generation algorithm.
For more information on this algorithm see:
http://www.algosome.com/articles/maze-generation-depth-first.html
...or search up some other examples.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.maze_depth_first
"""
import random
import arcade
import timeit
import os

NATIVE_SPRITE_SIZE = 128
SPRITE_SCALING = 0.25
SPRITE_SIZE = NATIVE_SPRITE_SIZE * SPRITE_SCALING

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Maze Depth First Example"

MOVEMENT_SPEED = 8

TILE_EMPTY = 0
TILE_CRATE = 1

# Maze must have an ODD number of rows and columns.
# Walls go on EVEN rows/columns.
# Openings go on ODD rows/columns
MAZE_HEIGHT = 51
MAZE_WIDTH = 51

MERGE_SPRITES = True

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 200

def _create_grid_with_cells(width, height):
    """ Create a grid with empty cells on odd row/column combinations. """
    grid = []
    for row in range(height):
        grid.append([])
        for column in range(width):
            if column % 2 == 1 and row % 2 == 1:
                grid[row].append(TILE_EMPTY)
            elif column == 0 or row == 0 or column == width - 1 or row == height - 1:
                grid[row].append(TILE_CRATE)
            else:
                grid[row].append(TILE_CRATE)
    return grid