from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        if left_is_clear():
            set_beeper()
            new_line()
        else:
            set_beeper()

def new_line():
    come_back()
    move()
    turn_about()
def come_back():
    turn_right()
    while front_is_clear():
        move()
    turn_about()
def set_beeper():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()
def turn_right():
    turn_left()
    turn_left()
def turn_about():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()