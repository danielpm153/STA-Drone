import tello
from tello_control_ui import TelloUI

import threading
import Tkinter as tk
import curses
from time import sleep
import socket

INTERVAL = 0.001

class Interface:
    def __init__(self, tello):
        self.tello = tello
        self.root = tk.Tk()


def loop(vplayer):
    vplayer.root.mainloop()

def main():

    drone = tello.Tello('', 8889)  
    vplayer = TelloUI(drone,"./img/")

    root_interface = Interface(drone)
    
	# start the Tkinter mainloop
    root_thread = threading.Thread(target=loop(vplayer))
    root_thread.daemon = True
    root_thread.start()

    canvas_thread = threading.Thread(target=root_interface.mainloop())
    canvas_thread.daemon = True
    canvas_thread.start()



if __name__ == "__main__":
    main()
