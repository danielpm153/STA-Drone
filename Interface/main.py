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
window.iconbitmap("logo.ico")
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
    labelAltitude1 = Label(top, text = "Altitude : " + "infos") #Drone 1
    labelAltitude1.place(x = 50, y = 100, width = 100, height = 30)
    labelAltitude2 = Label(top, text="Altitude : " + "infos")  # Drone 2
    labelAltitude2.place(x=310, y=100, width=100, height=30)
    labelAltitude3 = Label(top, text="Altitude : " + "infos")  # Drone 3
    labelAltitude3.place(x=570, y=100, width=100, height=30)
    labelEnVol1 = Label(top, text="En Vol : " + "Oui")  # Drone 1
    labelEnVol1.place(x=50, y=150, width=100, height=30)
    labelEnVol2 = Label(top, text="En Vol : " + "Non")  # Drone 2
    labelEnVol2.place(x=310, y=150, width=100, height=30)
    labelEnVol3 = Label(top, text="En Vol : " + "Oui")  # Drone 3
    labelEnVol3.place(x=570, y=150, width=100, height=30)



# Rajout des boutons
# Acceder a la vraie interface graphique de supervision
btn1 = Button(window, text = "Supervision des Drones", fg = '#336699', command = open)
# Lancer le drone
btn2 = Button(window, text = "Demarrer les Drones", fg = '#336699')
# Quitter la fenetre
btn3 = Button(window, text = "Fermer l'Interface", fg = '#336699', command = destruction)

# On positionne ces boutons
""""
btn1.pack(fill=X, ipady=15, padx=200,pady=40)
btn2.pack(fill=X, ipady=15, padx=200,pady=40)
btn3.pack(fill=X, ipady=15, padx=200,pady=40)
"""
btn1.place(x = 100, y=100, width = 300, height = 50)
btn2.place(x = 100, y=200, width = 300, height = 50)
btn3.place(x = 100, y=300, width = 300, height = 50)

# Afficher la fenetre
window.mainloop()

