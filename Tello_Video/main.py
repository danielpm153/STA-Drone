import tello
from tello_control_ui import TelloUI

import threading
import Tkinter as tk
#from Tkinter import Toplevel, Scale
#import curses
#from time import sleep
import socket

from PIL import Image
from PIL import ImageTk

INTERVAL = 0.001

class Interface:
    def __init__(self, tello, controle):
        self.tello = tello
        self.root = tk.Toplevel()
        self.root.wm_title("Data Drone")
        self.text = str(self.tello.response)
        self.root.geometry("700x500")
        self.controle = controle
        #self.root.configure(bg = "yellow")

        self.list_capt = ['mid', 'x', 'y', 'z', 'mpry', 'pitch', 'roll', 'yaw', 'vgx', 'vgy', 'vgz', 'templ', 'temph', 'tof', 'h', 'bat', 'baro', 'time', 'agx', 'agy', 'agz']

        self.list_label = []
        for i in range(21):
            self.list_label.append(tk.Label(self.root))
            self.list_label[i].grid()
        self.imagem = ImageTk.PhotoImage(Image.open("Drone.png"))
        FILENAME = "Drone.png"
        self.canvas = tk.Canvas(self.root, bg="blue", height=400, width=500)
        self.canvas.place(x = 100,y = 0)
        self.tk_img = ImageTk.PhotoImage(file=FILENAME)
        self.canvas.create_image(200, 300, image=self.tk_img)
        self.control_button = tk.Button(self.root, text="Control", command=self.controle, anchor="w",
                                width=10, activebackground="#33B5E5")
        self.quit_button_window = self.canvas.create_window(200, 360, anchor="nw", window=self.control_button)

        self.control_script = tk.Button(self.root, width= 10, text = "Script")
        self.control_script.place(x = 300, y=320)
        #self.control_script = tk.Button(self.root, text="Script", achor="w", width=10, activebackground="#33B5E5")
        #self.controle_button_window = self.canvas.create_window(200, 340, anchor="nw", window=self.control_script)

        #self.canvas.create_image((0,0), image = imagem)

        #self.aux = tk.Label(self.root, image=imagem)
        #self.aux.image = imagem
        #self.aux.pack(side="left", padx=10, pady=10)
        #self.canvas = tk.Canvas(self.root, bg="blue", height=250, width=300)

        #self.canvas.create_image(0, 0, image = image_)
        #self.canvas.pack()
        #background_image = tk.PhotoImage(file = "Drone.png")
        #background_label = tk.Label(self.root, image=background_image)
        #background_label.place(x=0, y=0, relwidth=1, relheight=1)

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
    vplayer = TelloUI(drone,"./img/")b

    root_interface = Interface(drone, vplayer.openCmdWindow)
    # start the Tkinter mainloop
    root_thread = threading.Thread(target=loop(vplayer))

    root_thread.daemon = True
    root_thread.start()

    canvas_thread = threading.Thread(target=root_interface.mainloop())
    canvas_thread.daemon = True
    canvas_thread.start()



if __name__ == "__main__":
    main()
