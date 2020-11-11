#import tello
#from tello_control_ui import TelloUI

import threading
from tkinter import *
# from Tkinter import Toplevel, Scale
# import curses
# from time import sleep
import socket

#from PIL import Image
#from PIL import ImageTk

INTERVAL = 0.001


class Interface:

    def __init__(self):
        global imagePremiere
        # Creation de la fenetre d'accueil
        self.window = Tk()

        self.window.title("interface graphique pour les drones")
        self.window.geometry("720x480")

        self.window.config(background='white')

        # Creation de l'image pour fond d'ecran

        imagePremiere = PhotoImage(file="FondInterface.png").zoom(35).subsample(32)
        self.background_label = Label(self.window, image=imagePremiere)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Rajout des boutons
        # Acceder a la vraie interface graphique de supervision
        self.btn1 = Button(self.window, text="Supervision des Drones", fg='#336699', command=self.open)
        # Arreter les drones
        self.btn5 = Button(self.window, text="Arreter tous les drones", fg='#336699')
        # Quitter la fenetre
        self.btn6 = Button(self.window, text="Fermer l'Interface", fg='#336699', command=self.destruction)

        # On positionne ces boutons
        self.btn1.place(x=80, y=40, width=300, height=50)
        self.btn5.place(x=80, y=320, width=300, height=50)
        self.btn6.place(x=80, y=390, width=300, height=50)

        # Commander le Drone numero 1        
        self.control_button1 = Button(self.window, text="Commander Drone 1", fg='#336699')
        self.control_button1.place(x=445, y=220, width=200, height=50)

        # Commander le Drone numero 2        
        self.control_button2 = Button(self.window, text="Commander Drone 2", fg='#336699')
        self.control_button2.place(x=445, y=300, width=200, height=50)

        # Lancer les deux drones
        self.control_script = Button(self.window, width=10, text="Demarrer les deux Drones", fg='#336699')
        self.control_script.place(x=80, y=110, width=300, height=50)

        # Lancer la trajectoire du Drone 1
        self.control_script1 = Button(self.window, width=10, text="Demarrer Drone numero 1", fg='#336699')
        self.control_script1.place(x=80, y=180, width=300, height=50)

        # Lancer la trajectoire du Drone 2
        self.control_script2 = Button(self.window, width=10, text="Demarrer Drone numero 2", fg='#336699')
        self.control_script2.place(x=80, y=250, width=300, height=50)

        self.window.mainloop()

    def open(self):
        global imageSeconde
        self.root = Toplevel()
        self.root.title("Supervision des Drones")
        self.root.geometry("800x500")
        self.root.iconbitmap("logo.ico")
        self.root.config(background='white')
        imageSeconde = PhotoImage(file="DRONESUPERVISION.png").zoom(35).subsample(32)
        self.background_label = Label(self.root, image=imageSeconde)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        # self.tello = tello
        # self.text = str(self.tello.response)
        # self.controle = controle
        # self.root.configure(bg = "yellow")

        # self.list_capt = ['mid', 'x', 'y', 'z', 'vgx', 'vgy', 'vgz', 'bat', 'time']

        # Quitter la fenetre
        self.buttonQuit = Button(self.root, text="Fermer la fenetre Supervision des Drones", fg='#336699',
                                 command=self.root.destroy)
        self.buttonQuit.pack()

        # Informations Drone 1
        self.labelAltitude1 = Label(self.root, text="Altitude : " + "infos")
        self.labelAltitude1.place(x=40, y=220, width=100, height=30)
        self.labelX1 = Label(self.root, text="x : " + "34")
        self.labelX1.place(x=40, y=120, width=100, height=30)
        self.labelY1 = Label(self.root, text="y : " + "")
        self.labelY1.place(x=40, y=170, width=100, height=30)
        self.labelMid1 = Label(self.root, text="Mid : " + "1")
        self.labelMid1.place(x=270, y=120, width=100, height=30)
        self.labelVgx1 = Label(self.root, text="Vgx : " + "56")
        self.labelVgx1.place(x=155, y=120, width=100, height=30)
        self.labelVgy1 = Label(self.root, text="Vgy : " + "2")
        self.labelVgy1.place(x=155, y=170, width=100, height=30)
        self.labelVgz1 = Label(self.root, text="Vgz : " + "12")
        self.labelVgz1.place(x=155, y=220, width=100, height=30)
        self.labelBat1 = Label(self.root, text="Batterie : " + "7")
        self.labelBat1.place(x=270, y=170, width=100, height=30)
        self.labelTime1 = Label(self.root, text="Temps : " + "76")
        self.labelTime1.place(x=270, y=220, width=100, height=30)

        # Supervision Obstacle Drone 1
        self.labelObstacle1Presence = Label(self.root, text="Obstacle : " + "Oui", fg='red')
        self.labelObstacle1Presence.place(x=130, y=270, width=150, height=40)
        self.labelCoordonnees1 = Label(self.root, text="Coordonnees : " + "87 " + "32 " + "78", fg='red')
        self.labelCoordonnees1.place(x=105, y=330, width=200, height=40)
        self.labelMidObstacle1 = Label(self.root, text="Mid Obstacle : " + "2", fg='red')
        self.labelMidObstacle1.place(x=130, y=390, width=150, height=40)

        # Drone 2
        self.labelAltitude2 = Label(self.root, text="Altitude : " + "infos")
        self.labelAltitude2.place(x=430, y=220, width=100, height=30)
        self.labelX2 = Label(self.root, text="x : " + "23")
        self.labelX2.place(x=430, y=120, width=100, height=30)
        self.labelY2 = Label(self.root, text="y : " + "11")
        self.labelY2.place(x=430, y=170, width=100, height=30)
        self.labelMid2 = Label(self.root, text="Mid : " + "1")
        self.labelMid2.place(x=660, y=120, width=100, height=30)
        self.labelVgx2 = Label(self.root, text="Vgx : " + "56")
        self.labelVgx2.place(x=545, y=120, width=100, height=30)
        self.labelVgy2 = Label(self.root, text="Vgy : " + "2")
        self.labelVgy2.place(x=545, y=170, width=100, height=30)
        self.labelVgz2 = Label(self.root, text="Vgz : " + "12")
        self.labelVgz2.place(x=545, y=220, width=100, height=30)
        self.labelBat2 = Label(self.root, text="Batterie : " + "7")
        self.labelBat2.place(x=660, y=170, width=100, height=30)
        self.labelTime2 = Label(self.root, text="Temps : " + "76")
        self.labelTime2.place(x=660, y=220, width=100, height=30)

        # Supervision Obstacle Drone 2
        self.labelObstacle2Presence = Label(self.root, text="Obstacle : " + "Oui", fg='red')
        self.labelObstacle2Presence.place(x=520, y=270, width=150, height=40)
        self.labelCoordonnees2 = Label(self.root, text="Coordonnees : " + "76 " + "45 " + "06", fg='red')
        self.labelCoordonnees2.place(x=495, y=330, width=200, height=40)
        self.labelMidObstacle2 = Label(self.root, text="Mid Obstacle : " + "4", fg='red')
        self.labelMidObstacle2.place(x=520, y=390, width=150, height=40)

    def destruction(self):  # fonction pour fermer la fenetre si jamais
        self.window.destroy()

        # self.control_script = tk.Button(self.root, text="Script", achor="w", width=10, activebackground="#33B5E5")
        # self.controle_button_window = self.canvas.create_window(200, 340, anchor="nw", window=self.control_script)

        # self.canvas.create_image((0,0), image = imagem)

        # self.aux = tk.Label(self.root, image=imagem)
        # self.aux.image = imagem
        # self.aux.pack(side="left", padx=10, pady=10)
        # self.canvas = tk.Canvas(self.root, bg="blue", height=250, width=300)

        # self.canvas.create_image(0, 0, image = image_)
        # self.canvas.pack()
        # background_image = tk.PhotoImage(file = "Drone.png")
        # background_label = tk.Label(self.root, image=background_image)
        # background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # communitation
        # self.stdscr = curses.initscr()
        # curses.noecho()
        # curses.cbreak()

"""
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
"""
Interface()
