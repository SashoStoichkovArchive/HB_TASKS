import os, sys, pyautogui
from Xlib import display 

def mousepos():
    while True:
        return pyautogui.position()

def is_in_corner():
    try:
        if mousepos() == (0, 0):
            os.system('play -nq -t alsa synth {} sine {}'.format(0.1, 1000)) # beep
    except KeyboardInterrupt:
        sys.exit(0)

while True:
    is_in_corner()