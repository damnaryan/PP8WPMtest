import curses
# this is the module used for making that effect of writing over the text and other style elements.
# since the wpm test will take place in a terminal, this library is used to style the terminal module.
from curses import wrapper
# this module is used to initalise the terminal module, baiscally take control of the computer terminal to
# run this code on it. Wrapper also reverts back the original terminal after executing the code.

def main(strstd):  # here 'strstd' is used to take the entire screen (here, the entire terminal) as a input fucntion.
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK) # initaling text and background colours.
    # (color_index, text_color, bg_color) color_index can be set any num, it'll be used to refer this pair.
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    strstd.clear() # used to clear the entire terminal screen.
    strstd.addstr("TUMHARI MAA KI CH*T", curses.color_pair(3)) # adding a string as a text on the terminal.
    strstd.refresh() # the terminal screen needs to refreshed in order to show the output.
    strstd.getkey() # this is done to get 'any' key input function before execting further.
    # (This stops the terminal from closing, instantly.)

wrapper(main)