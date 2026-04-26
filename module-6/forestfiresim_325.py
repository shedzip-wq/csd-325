# Sheridan Dela Cruz
# Sebastian Siqueiros
# Samuel Dirr
# Desarai Lofton
# April 26, 2026
# Module 6.2

"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/

MODULE 6 MODIFICATIONS 
------------------------------------------------
1. Added WATER constant and blue display color.
2. Inserted a lake in the center of the forest inside createNewForest().
3. Ensured water never changes state (cannot grow trees, burn, or become empty).
4. Updated fire-spread logic so fire cannot cross water (lake acts as firebreak).
5. Documented all changes clearly for assignment requirements.

** use spaces, not indentation to modify **
Tags: short, bext, simulation
"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '

# MODULE 6 ADDITION — WATER CONSTANT
WATER = '~'   # New water feature symbol (must not be A or @)

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):

                # MODULE 6 ADDITION — WATER NEVER CHANGES
                if forest[(x, y)] == WATER:
                    nextForest[(x, y)] = WATER
                    continue

                if (x, y) in nextForest:
                    continue

                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    nextForest[(x, y)] = TREE

                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    nextForest[(x, y)] = FIRE

                elif forest[(x, y)] == FIRE:
                    # This tree is currently burning.
                    # Loop through all the neighboring spaces:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):

                            # MODULE 6 ADDITION — FIRE CANNOT SPREAD INTO WATER
                            if forest.get((x + ix, y + iy)) == TREE:
                                if forest.get((x + ix, y + iy)) != WATER:
                                    nextForest[(x + ix, y + iy)] = FIRE

                    nextForest[(x, y)] = EMPTY

                else:
                    nextForest[(x, y)] = forest[(x, y)]

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY

    # MODULE 6 ADDITION — INSERT LAKE IN CENTER OF GRID
    lake_width = 15
    lake_height = 6
    start_x = (WIDTH - lake_width) // 2
    start_y = (HEIGHT - lake_height) // 2

    for x in range(start_x, start_x + lake_width):
        for y in range(start_y, start_y + lake_height):
            forest[(x, y)] = WATER  # Water overwrites trees/empty

    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):

            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')

            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')

            # MODULE 6 ADDITION — BLUE WATER DISPLAY
            elif forest[(x, y)] == WATER:
                bext.fg('blue')
                print(WATER, end='')

            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')

        print()

    bext.fg('reset')
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
