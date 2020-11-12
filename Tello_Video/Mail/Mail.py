# Importation des modules
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

coordonnees = "23, 56, 12"
midNum = "2"

def mail(coordonnees, midNum):
    From = "drone.sncf@gmail.com"
    To = "drone.sncf@gmail.com"
    cc = ["leo.gresillon@gmail.com", "omeurer@yahoo.fr"]
    message = MIMEMultipart()
    message['From'] = From
    message['To'] = To
    message['CC'] = ",".join(cc)
    message['Subject'] = "Obstacle detecte"
    msg = "Attention, un obstacle a ete detecte. Au moment ou l'obstacle a ete detecte, le drone etait aux positions : " + coordonnees + " et au dessus du mid : " + midNum  # Message a envoyer
    message.attach(MIMEText(msg.encode('utf-8'), 'plain', 'utf-8'))  # Attache du message a l'objet "message", et encodage en UTF-8

    serveur = smtplib.SMTP('smtp.gmail.com', 587)  # Connexion au serveur sortant (en precisant son nom et son port)
    serveur.starttls()  # Specification de la securisation
    serveur.login(From, "droneSTA20")  # Authentification
    texte = message.as_string().encode('utf-8')  # Conversion de l'objet "message" en chaine de caractere et encodage en UTF-8
    Tos = [To] + cc
    serveur.sendmail(From, Tos, texte)  # Envoi du mail
    serveur.quit()  # Deconnexion du serveur

mail(coordonnees,midNum)