## This is a learning project.
I am making this project to learn python.So, instead of learing the syntax first, I am building this project to learn while I am building this. I have made notes within the code as comments, of every new concept I get to know.
##### Source of learning: https://www.youtube.com/watch?v=NpmFbWO6HPU&list=WL
### About this project:
THIS IS A GOOD ADVANCE LEVEL PROJECT. At least for me, it is. This is WPA tester on the terminal itself, with a full on overlaying text animation, where the user is kinda typing over the text. The correct letters go green and the wrong ones go red. The main part is the WPA part, the program gives a live WPA score, as the user is typing.

### [ COMPLETED ]

## Learnings:
1) *stdscr* as input: taking the screen as input, here the terminal screen to make changes to the terminal screen.
###### *stdscr* functions:
- *stdscr.clear()* - To clear the terminal screen.
- *stdscr.addstr(0,0,"string")* - To add a string to a terminal screen, the numbers in the beginning are the coordinates for the text (R,C).
- *key = stdscr.getkey()* - To get a input from the user in the terminal screen (and here, store it in key variable).
- *stdscr.refresh()* -  To refresh the terminal screen to display the made changes.
- *stdscr.nodelay(True)* - Turning on the no delay, in this program this feature is used to still change the wpm when the user is not typing (as the getkey() cmd used to wait for the user to input a key a then the wpm was calculated).
- *stdscr.nodelay(False)* - Turn off the no delay.
2) *wrapper()* function: wrapper function is used to revert back the changes made to the terminal to its original form. This the reason the "main" function is inside a wrapper function. Cause we want the terminal to revert back to normal.
3) 

 
