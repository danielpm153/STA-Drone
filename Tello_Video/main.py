import tello
from tello_control_ui import TelloUI

import threading
import Tkinter as tk
#import curses
#from time import sleep
import socket

INTERVAL = 0.001

class Interface:
    def __init__(self, tello):
        self.tello = tello
        self.root = tk.Tk()
        self.root.wm_title("Data Drone")
        self.text = str(self.tello.response)

        self.list_capt = ['mid', 'x', 'y', 'z', 'mpry', 'pitch', 'roll', 'yaw', 'vgx', 'vgy', 'vgz', 'templ', 'temph', 'tof', 'h', 'bat', 'baro', 'time', 'agx', 'agy', 'agz']

        self.list_label = []
        for i in range(21):
            self.list_label.append(tk.Label(self.root))
            self.list_label[i].pack()
        #communitation
        #self.stdscr = curses.initscr()
        #curses.noecho()
        #curses.cbreak()

        local_ip = ''
        local_port = 8890
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((local_ip, local_port))

        tello_ip = '192.168.10.1'
        tello_port = 8889
        tello_adderss = (tello_ip, tello_port)

        self.socket.sendto('command'.encode('utf-8'), tello_adderss)
        self.dados()
    def report(self, str):
        pass
        #self.stdscr.addstr(0, 0, str)
        #self.stdscr.refresh()
    def str2dict(self, out):
        dictionnaire = {}
        for i in out:
            if ':' in i:
                aux = i.split(':')
                dictionnaire[aux[0]] = aux[1]
            else:
                pass
        return dictionnaire

    def dados(self):
        try:
            self.response, self.ip = self.socket.recvfrom(1024)
            if self.response == "ok":
                self.root.after(100, self.dados)
            else:
                self.out = self.response.split(';')
                self.out_dict = self.str2dict(self.out)
                for i in range(21):
                    self.list_label[i]["text"] = self.list_capt[i] + "=" + self.out_dict[self.list_capt[i]]
                self.root.after(100, self.dados)
        except KeyboardInterrupt:
            pass
            #curses.echo()
            #curses.nocbreak()
            #curses.endwin()



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
