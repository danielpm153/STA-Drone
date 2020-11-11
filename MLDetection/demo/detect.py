#Definir la fonction de detection d'image


import os
import sys
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


def detect_image(image_path, net):
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
                result.append([label_name, pt])
            coords = (pt[0], pt[1]), pt[2] - pt[0] + 1, pt[3] - pt[1] + 1
            print(coords)
            j += 1
    return result
#si le resultat est vide, il ne detecte pas d'objet sauf le train.

if __name__ == '__main__':
    net = build_ssd('test', 300, 21)  # initialize SSD
    net.load_weights('../weights/ssd300_COCO_15000.pth')
    result = detect_image('IMG_2499.jpg', net)
    print(result)
