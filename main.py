# EVERY NEW CMD IS EXPALINED IN THE 'DRAFT' CODE.

import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    stdscr.clear()
    stdscr.addstr(0,0,"THIS IS A SPEED TYPING TEST.")
    stdscr.addstr(1,2, "PRESS ANY KEY TO START.") # 1,2 is the coordinates for the text.
    # FORMAT: stdscr.addstr(COL_NUM, ROW_NUM, "text") 
    stdscr.refresh()
    key = stdscr.getkey()
    if ord(key) == 27:
        quit()
    while True:                    # TEST END.
        wpm = wpm_text(stdscr)
        stdscr.clear()
        stdscr.addstr(f"The test is complete. Your typing speed is {wpm} WPM.", curses.color_pair(2))
        stdscr.addstr("\nPress 'Esc' to exit the test. Press any key to try again.")
        key1 = stdscr.getkey()
        if ord(key1) == 27:
            quit()

def load_text():
    with open('typing_text.txt', 'r') as f:
        lines = f.readlines()                     # this will store all the lines of the txt as a list.
        return random.choice(lines).strip()   # choosing one of the line and striping the blank spaces.

def wpm_text(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()                                         # stores the current time in seconds.
    stdscr.nodelay(True)                                              
    # this is to continue to reduce the wpm while the user is not typing, by bypassing the 35th line.
    while True:                                                      # since the user has to keep entering the letters.
        elasped_time = max(time.time() - start_time, 1)              
        # max is taken because for the first time the elasped time will be 0. And this will give 'dividing by 0' error ahead.
        wpm = round((len(current_text) / (elasped_time / 60) / 5)) # average word size is 5

        # checking if the text is completed.
        if "".join(current_text) == target_text:
        # this "*seperator*".join(*list*) converts a list into a string with the desired seperator.
            stdscr.nodelay(False) # turning of the the nodelay as it will keep.
            return wpm
            
        stdscr.clear()  
        # clearing the screen at every loop is imp as this will prevent reprinting of the target_text and current_text.
        overlaying_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()
        try:                       # since this piece of code will force bypass (line 37) rest of the code containing 'key' will
            key = stdscr.getkey()  # crash. So, 'try' will try the code and if the user won't enter anything it will continue to 
        except: continue           # run the loop
        if ord(key) == 27:         # 'ord' is for ordianal/ASCII value. 27 is the ASCII value for 'esc' key.
            quit()
        if ord(key) == 8:          # 8 is the ASCII value of the 'backspace' key.
            if len(current_text) > 0:
                current_text.pop() # pops the last item in the list.
        elif len(current_text) < len(target_text): 
            current_text.append(key)


def overlaying_text(stdscr, target, current, wpm): # equalising a parameter to 0 makes it a optional parameter
    stdscr.addstr(target)
    stdscr.addstr(3,0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        if correct_char == char:
            color = curses.color_pair(2)
        else: color = curses.color_pair(3)
        stdscr.addstr(0, i, char, color)

def main(stdscr):  
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    start_screen(stdscr)
        
wrapper(main)




