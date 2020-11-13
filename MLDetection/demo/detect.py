#Definir la fonction de detection d'image

import time
import os
import sys
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

coordonnees = "23, 56, 12"
midNum = "2"

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
from ssd import build_ssd
import torch #https://pytorch.org/get-started/locally/
import torch.nn as nn
import torch.backends.cudnn as cudnn
from torch.autograd import Variable
import numpy as np
import cv2
if torch.cuda.is_available():
    torch.set_default_tensor_type('torch.cuda.FloatTensor')
from data import VOCDetection, VOC_ROOT, VOCAnnotationTransform
from data import VOC_CLASSES as labels

def mail(coordonnees, midNum, path_img):
    From = "drone.sncf@gmail.com"
    To = "drone.sncf@gmail.com"
    cc = ["leo.gresillon@gmail.com"]
    message = MIMEMultipart()
    message['From'] = From
    message['To'] = To
    message['CC'] = ",".join(cc)
    message['Subject'] = "Obstacle detecte"
    msg = "Attention, un obstacle a ete detecte. Au moment ou l'obstacle a ete detecte, le drone etait aux positions : " + coordonnees + " et au dessus du mid : " + midNum  # Message a envoyer
    message.attach(MIMEText(msg.encode('utf-8'), 'plain', 'utf-8'))  # Attache du message a l'objet "message", et encodage en UTF-8

    nom_fichier = "Photo Obstacle"  # Spécification du nom de la pièce jointe
    piece = open(path_img, "rb")  ## Ouverture du fichier
    part = MIMEBase('application', 'octet-stream')  ## Encodage de la pièce jointe en Base64
    part.set_payload((piece).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "piece; filename= %s" % nom_fichier)
    message.attach(part)  ## Attache de la pièce jointe à l'objet "message"

    serveur = smtplib.SMTP('smtp.gmail.com', 587)  # Connexion au serveur sortant (en precisant son nom et son port)
    serveur.starttls()  # Specification de la securisation
    serveur.login(From, "droneSTA20")  # Authentification
    texte = message.as_string().encode('utf-8')  # Conversion de l'objet "message" en chaine de caractere et encodage en UTF-8
    Tos = [To] + cc
    serveur.sendmail(From, Tos, texte)  # Envoi du mail
    serveur.quit()  # Deconnexion du serveur

def detect_image(dir_path, net):
    while (1):

        path = os.listdir(dir_path)
        # print(path)
        if len(path) == 0:
            continue
        print("Read image...")
        image_path = os.path.join(dir_path, path[0])
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        x = cv2.resize(image, (300, 300)).astype(np.float32)
        x -= (104.0, 117.0, 123.0)
        x = x.astype(np.float32)
        x = x[:, :, ::-1].copy()
        x = torch.from_numpy(x).permute(2, 0, 1)
        xx = Variable(x.unsqueeze(0))  # wrap tensor in Variable
        if torch.cuda.is_available():
            xx = xx.cuda()
        y = net(xx)
        detections = y.data
        result = []
        scale = torch.Tensor(rgb_image.shape[1::-1]).repeat(2)
        for i in range(detections.size(1)):
            j = 0
            while detections[0, i, j, 0] >= 0.6:
                score = detections[0, i, j, 0]
                label_name = labels[i - 1]

                pt = (detections[0, i, j, 1:] * scale).cpu().numpy()
                if label_name != 'train':
                    result.append(label_name)
                coords = (pt[0], pt[1]), pt[2] - pt[0] + 1, pt[3] - pt[1] + 1
                j += 1
        print(is_detected(result))
        if(is_detected(result)):
            print(result)
            mail(coordonnees, midNum, image_path)
        os.remove(image_path)
        time.sleep(10)

def is_detected(result):
    if len(result) != 0:
        return True
    else:
        return False
#si le resultat est vide, il ne detecte pas d'objet sauf le train.

if __name__ == '__main__':

    net = build_ssd('test', 300, 21)  # initialize SSD
    net.load_weights('../weights/ssd300_COCO_15000.pth')
    filePath = 'img'
    # f1 = threading.Thread(target = detect_image(filePath, net))

    detect_image(filePath, net)
