# interface graphique pour les drones

from tkinter import *

# Mise en place de parametres importants
window = Tk()


# Premier objectif : Creer un portail d'accueil pour lancer le drone, ou pour superviser le drone
"""
# Creation d'image pour le fond d'ecran de la page d'accueil
width = 700
height = 500
image = PhotoImage(file = "FondInterface.png").zoom(35).subsample(32)
canvas = Canvas(window, width = width, height = height)
canvas.create_image(width/2, height/2, image = image)
canvas.pack(expand = YES)
"""

# Creation de la fenetre d'accueil

window.title("interface graphique pour les drones")
window.geometry("720x480")

window.config(background = 'white')

# Creation de l'image pour fond d'ecran

image = PhotoImage(file = "FondInterface.png").zoom(35).subsample(32)
background_label = Label(window, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Avant de definir les boutons on va creer tout ce qu'il peut se passer a l'aide de ces boutons

# Il faut creer la fonction capable de detruire une fenetre
def destruction():
    window.destroy()

# Il faut creer la fonction open afin que le bouton Supervision des Drones fonctionne

"""
# On va donc creer la fonction open, elle meme constituee de ses sousfonctions droneInfoi, i = 1,2,3

def droneInfo1(): # Recuperer les infos ET les afficher
    # Recuperer les infos une a une
    labelAltitude = Label()...
"""

def open():
    global image2
    top = Toplevel()
    top.title("Supervision des Drones")
    top.geometry("800x500")
    top.iconbitmap("logo.ico")
    top.config(background = 'white')
    image2 = PhotoImage(file = "SupervisionDrones.png").zoom(35).subsample(32)
    background_label = Label(top, image=image2)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    buttonQuit = Button(top, text = "Fermer la fenetre Supervision des Drones", fg = '#336699', command = top.destroy)
    buttonQuit.pack()

    labelAltitude1 = Label(top, text = "Altitude : " + "infos")     # Drone 1
    labelAltitude1.place(x = 40, y = 220, width = 100, height = 30)
    labelX1 = Label(top, text="x : " + "34")
    labelX1.place(x=40, y=120, width=100, height=30)
    labelY1 = Label(top, text="7 : " + "56")
    labelY1.place(x=40, y=170, width=100, height=30)
    labelMid1 = Label(top, text="Mid : " + "1")
    labelMid1.place(x=270, y=120, width=100, height=30)
    labelVgx1 = Label(top, text="Vgx : " + "56")
    labelVgx1.place(x=155, y=120, width=100, height=30)
    labelVgy1 = Label(top, text="Vgy : " + "2")
    labelVgy1.place(x=155, y=170, width=100, height=30)
    labelVgz1 = Label(top, text="Vgz : " + "12")
    labelVgz1.place(x=155, y=220, width=100, height=30)
    labelBat1 = Label(top, text="Batterie : " + "7")
    labelBat1.place(x=270, y=170, width=100, height=30)
    labelTime1 = Label(top, text="Temps : " + "76")
    labelTime1.place(x=270, y=220, width=100, height=30)

    labelObstacle1Presence = Label(top, text="Obstacle : " + "Oui", fg='red')  # Supervision Obstacle
    labelObstacle1Presence.place(x=130, y=270, width=150, height=40)
    labelCoordonnees1 = Label(top, text="Coordonnees : " + "87 " + "32 " + "78", fg='red')
    labelCoordonnees1.place(x=105, y=330, width=200, height=40)
    labelMidObstacle1 = Label(top, text="Mid Obstacle : " + "2", fg='red')
    labelMidObstacle1.place(x=130, y=390, width=150, height=40)


    labelAltitude2 = Label(top, text="Altitude : " + "infos")   # Drone 2
    labelAltitude2.place(x=430, y=220, width=100, height=30)
    labelX2 = Label(top, text="x : " + "23")
    labelX2.place(x=430, y=120, width=100, height=30)
    labelY2 = Label(top, text="y : " + "11")
    labelY2.place(x=430, y=170, width=100, height=30)
    labelMid2 = Label(top, text="Mid : " + "1")
    labelMid2.place(x=660, y=120, width=100, height=30)
    labelVgx2 = Label(top, text="Vgx : " + "56")
    labelVgx2.place(x=545, y=120, width=100, height=30)
    labelVgy2 = Label(top, text="Vgy : " + "2")
    labelVgy2.place(x=545, y=170, width=100, height=30)
    labelVgz2 = Label(top, text="Vgz : " + "12")
    labelVgz2.place(x=545, y=220, width=100, height=30)
    labelBat2 = Label(top, text="Batterie : " + "7")
    labelBat2.place(x=660, y=170, width=100, height=30)
    labelTime2 = Label(top, text="Temps : " + "76")
    labelTime2.place(x=660, y=220, width=100, height=30)

    labelObstacle2Presence = Label(top, text="Obstacle : " + "Oui", fg='red')  # Supervision Obstacle
    labelObstacle2Presence.place(x=520, y=270, width=150, height=40)
    labelCoordonnees2 = Label(top, text="Coordonnees : " + "76 " + "45 " + "06", fg='red')
    labelCoordonnees2.place(x=495, y=330, width=200, height=40)
    labelMidObstacle2 = Label(top, text="Mid Obstacle : " + "4", fg='red')
    labelMidObstacle2.place(x=520, y=390, width=150, height=40)




# Rajout des boutons

# Acceder a la vraie interface graphique de supervision
btn1 = Button(window, text="Supervision des Drones", fg='#336699', command=open)
# Lancer les deux drones
btn2 = Button(window, text="Demarrer les deux Drones", fg='#336699')
# Lancer le drone 1
btn3 = Button(window, text="Demarrer Drone numero 1", fg='#336699')
# Lancer le drone 2
btn4 = Button(window, text="Demarrer Drone numero 2", fg='#336699')
# Arreter les drones
btn5 = Button(window, text="Arreter tous les drones", fg='#336699')
# Quitter la fenetre
btn6 = Button(window, text="Fermer l'Interface", fg='#336699', command=destruction)

# Commander le drone numero 1
btn7 = Button(window, text="Commander Drone 1", fg='#336699')
# Commander le drone numero 2
btn8 = Button(window, text="Commander Drone 2", fg='#336699')

# On positionne ces boutons

btn1.place(x=80, y=40, width=300, height=50)
btn2.place(x=80, y=110, width=300, height=50)
btn3.place(x=80, y=180, width=300, height=50)
btn4.place(x=80, y=250, width=300, height=50)
btn5.place(x=80, y=320, width=300, height=50)
btn6.place(x=80, y=390, width=300, height=50)
btn7.place(x=445, y=220, width=200, height=50)
btn8.place(x=445, y=300, width=200, height=50)

# On positionne ces boutons
""""
btn1.pack(fill=X, ipady=15, padx=200,pady=40)
btn2.pack(fill=X, ipady=15, padx=200,pady=40)
btn3.pack(fill=X, ipady=15, padx=200,pady=40)
"""

# Afficher la fenetre
window.mainloop()
