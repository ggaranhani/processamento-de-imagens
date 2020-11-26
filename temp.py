import numpy as np
import matplotlib.pyplot as plt

def checa_vizinhos(img, i, j):
    if(img[i][j+1][3] == 255 or img[i][j-1][3] == 255 or img[i-1][j][3] == 255 or img[i+1][j][3]):
        return True
    else:
        return False
            

img = quad
#plt.imshow(img, cmap='gray')



m = img.shape[0]
n = img.shape[1]

bordas = np.zeros([100,100,3],dtype=np.uint8)
bordas.fill(255)

#plt.imshow(bordas, cmap='gray')

for i in range(m-1):
    for j in range(n-1):
        if(img[i][j][3] == 0):
            if(checa_vizinhos(img, i, j)):
                bordas[i][j] = 0
                bordas[i+1][j] = 0
                bordas[i-1][j] = 0
                bordas[i][j+1] = 0
                bordas[i][j-1] = 0
                
plt.imshow(bordas, cmap='gray')
  
                


