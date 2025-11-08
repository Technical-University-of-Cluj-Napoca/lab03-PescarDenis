import pygame

# some global constants
WIDTH = 800
HEIGHT = 800

# colors.
# if you find it more suitable, change this dictionary to standalone constants like: RED = (255, 0, 0)
COLORS = {
    "WHITE": (46, 46, 51),        # default cell background
    "BLACK": (13, 13, 15),        # barriers
    "RED": (90, 24, 154),         # closed set
    "GREEN": (157, 78, 221),      # open set
    "ORANGE": (247, 37, 133),     # start node
    "YELLOW": (76, 201, 240),     # end node
    "PURPLE": (199, 125, 255),    # final path highlight
}

BACKGROUND_COLOR = (26, 26, 29)   
GRID_LINE_COLOR = (68, 68, 68)    
