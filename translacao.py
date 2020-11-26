import matplotlib.pyplot as plt
import numpy as np
from scipy import misc
import math

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
    return img_transladada

def rotacao(img, teta):
    img_transladada = np.zeros(img.shape)
    size = img.shape
    for u in range(size[1]):
        for v in range(size[0]):
            f = u*math.cos(teta) - v*math.sin(teta)
            g = u*math.sin(teta) + v*math.cos(teta)
            x = int(np.floor(f))
            y = int(np.floor(g))
            if x>=0 and x<size[1] and y>=0 and y<size[0]:
                img_transladada[v,u] = img[y,x]
    return img_transladada

def cisalhamento(img, cv, ch):
    img_transladada = np.zeros(img.shape)
    size = img.shape
    for u in range(size[1]):
        for v in range(size[0]):
            f = u - v * cv
            g = v - u * ch
            x = int(np.floor(f))
            y = int(np.floor(g))
            if x>=0 and x<size[1] and y>=0 and y<size[0]:
                img_transladada[v,u] = img[y,x]
    return img_transladada

def afim(img, m, n, teta):
    img_transladada = np.zeros(img.shape)
    size = img.shape
    for u in range(size[1]):
        for v in range(size[0]):    
            f = u+(n/2)
            g = v+(m/2)
            
            f = f*math.cos(teta) - g*math.sin(teta)
            g = f*math.sin(teta) + g*math.cos(teta)
            
            f = f-(n/2)
            g = g-(m/2)
            if x>=0 and x<size[1] and y>=0 and y<size[0]:
                img_transladada[v,u] = img[y,x]
    return img_transladada
    
    
    
def fail_afim(img, m, n):
    img2 = translacao(img, -n/2, -m/2)
    img2 = rotacao(img2, 0.2)
    img2 = translacao(img2, n/2, m/2)
    return img2

img = lena512.astype(float)
img = img/255

size = img.shape;

dx = 20
dy = 30
teta = 45
cv = 0.25
ch = -0.25
m = img.shape[0]
n = img.shape[1]
teta2 = 0.2


plt.imshow(translacao(img, dx, dy), cmap='gray')
plt.pause(0.2)
plt.imshow(rotacao(img, teta), cmap='gray')
plt.pause(0.2)
plt.imshow(cisalhamento(img, cv, ch), cmap='gray')
plt.pause(0.2)
plt.imshow(afim(img, m, n, teta2), cmap='gray')
#3 Realizar uma opera¸c˜ao de cisalhamento cv = 0.25, ch = −0.25