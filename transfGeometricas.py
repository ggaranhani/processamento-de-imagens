#Transformações Geométricas

import numpy as np
from scipy import misc
import matplotlib.pyplot as plt


img = lena512.astype(float)
img = img/255

img_transladada = np.zeros(img.shape)

size = img.shape;

dx = 20
dy = 30


def translacao(img,dx,dy):
    
    img_transladada = np.zeros(img.shape)
    size = img.shape
    for u in range(size[1]):
        for v in range(size[0]):
            f = u-dx
            g = v-dy
            x = int(np.floor(f))
            y = int(np.floor(g))
            if x>=0 and x<size[1] and y>=0 and y<size[0]:
                img_transladada[v,u] = img[y,x]
    plt.imshow(img_transladada, cmap='gray')
    return img_transladada
