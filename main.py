# EVERY NEW CMD IS EXPALINED IN THE 'DRAFT' CODE.
import curses
from curses import wrapper

def start_screen(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    stdscr.clear()
    stdscr.addstr(0,0,"THIS IS A SPEED TYPING TEST.")
    stdscr.addstr(1,2, "PRESS ANY KEY TO START.") # 1,2 is the coordinates for the text.
    # FORMAT: stdscr.addstr(COL_NUM, ROW_NUM, "text") 
    stdscr.refresh()
    stdscr.getkey()
    wpm_text(stdscr)

def wpm_text(stdscr):
    target_text = "This is some random text for testing the app."
    current_text = []
    
    while True:                    # since the user has to keep entering the letters.
        stdscr.clear()  
        # clearing the screen at every loop is imp as this will prevent reprinting of the target_text and current_text.                                           
        stdscr.addstr(target_text)
        for char in current_text:
            stdscr.addstr(char, curses.color_pair(2))
        stdscr.refresh()
        key = stdscr.getkey()
        if ord(key) == 27:         # 'ord' is for ordianal/ASCII value. 27 is the ASCII value for 'esc' key.
            break
        if ord(key) == 8:          # 8 is the ASCII value of the 'backspace' key.
            if len(current_text) > 0:
                current_text.pop() # pops the last item in the list.
        else: current_text.append(key)

def main(stdscr):  
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    start_screen(stdscr)

wrapper(main)



