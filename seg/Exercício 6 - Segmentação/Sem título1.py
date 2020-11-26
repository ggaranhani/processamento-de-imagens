import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

def plot_grayscale(imagem, nova_imagem, txt):
    plt.figure(1)
    plt.subplot(1,2,1)
    plt.title('Imagem Normal - Red')
    plt.imshow(imagem[:, :, 0], cmap = 'gray', vmin = 0, vmax = 255)
    plt.subplot(1,2,2)               
    plt.title('Imagem processada' + (txt) + ' - Red')
    plt.imshow(nova_imagem[:, :, 0], cmap = 'gray', vmin = 0, vmax = 255)
    
    plt.figure(2)
    plt.subplot(1,2,1)
    plt.title('Imagem Normal - Green')
    plt.imshow(imagem[:, :, 1], cmap = 'gray', vmin = 0, vmax = 255)
    plt.subplot(1,2,2)               
    plt.title('Imagem processada' + (txt) + ' - Green')
    plt.imshow(nova_imagem[:, :, 1], cmap = 'gray', vmin = 0, vmax = 255)
    
    plt.figure(3)
    plt.subplot(1,2,1)
    plt.title('Imagem Normal - Blue')
    plt.imshow(imagem[:, :, 2], cmap = 'gray', vmin = 0, vmax = 255)
    plt.subplot(1,2,2)               
    plt.title('Imagem processada' + (txt) + ' - Blue')
    plt.imshow(nova_imagem[:, :, 2], cmap = 'gray', vmin = 0, vmax = 255)
    
    plt.figure(4)
    plt.subplot(1,2,1)
    plt.title('Imagem Normal')
    plt.imshow(imagem, cmap = 'gray', vmin = 0, vmax = 255)
    plt.title('Imagem processada ' + (txt))
    plt.subplot(1,2,2)               
    plt.imshow(nova_imagem, cmap = 'gray', vmin = 0, vmax = 255)




def Pontos(imagem, T):    
    w_size = 3
    size = np.shape(imagem)
    nova_img = np.zeros(size)
    xx = int(w_size/2)
    yy = int(w_size/2)
    u = int(-xx)
    v = int(-yy)
    px = 0
    for i in range(size[0] - w_size//2):
        for j in range(size[1] - w_size//2):
            for k in range(size[2]):
#                aux = []
                while u <= xx:
                    while v <= yy:
                        if u != 0 and v != 0:
                            px += (-1) * imagem[u+i, v+j, k]
                        else:
                            px += 8 * imagem[u+i, v+j, k]
                        v += 1
                    u += 1
                    v = int(-yy)
                                        
#                nova_imgiana = np.nova_imgian(aux)      
#                nova_img[i,j,k] = nova_imgiana
                if np.abs(px) > T:
                    nova_img[i, j, k] = 255
                u, v, px = int(-xx), int(-yy), 0
    plot_grayscale(imagem, nova_imagem, 'Detecção de pontos')
    return nova_img


def DetectarRetas(imagem, T, op):
    w_size = 3
    size = np.shape(imagem)
    nova_img = np.zeros(size)
    xx = int(w_size/2)
    yy = int(w_size/2)
    u = int(-xx)
    v = int(-yy)
    px = 0
    
    
    
    ''' Definir qual tipo de máscara a ser utilizada na detecção de retas '''
    opcao = None
    while opcao not in (1, 2, 3, 4):
        valorEntrada = input("Entre com as seguintes opções de detecção de retas: \n1 - " +
                             "Horizontais \n2 - Verticais \n3 - 45 Graus \n4 - 135 Graus: \n")
        try: 
            opcao = int(valorEntrada)
        except ValueError:
            print("\n>> Por favor, entre com um inteiro e, de preferência, válido!".format(input = valorEntrada))
            
    if op == 1:
        nomeRetas = 'Horizontais'        
        ''' Aplicação da máscara para detecção de retas horizontais '''
        for i in range(xpiso, size[0] - xpiso):
            for j in range(ypiso, size[1] - ypiso):
                for nivel in range(size[2]):
                    while u <= xpiso:
                        while v <= ypiso:
                            if u == 0:
                                verificaLimiar += 2 * npImage[i+u, v+j, nivel]
                            else:
                                verificaLimiar += -1 * npImage[i+u, v+j, nivel]                        
                            v += 1
                        u += 1
                        v = -ypiso
                        
                    if np.abs(verificaLimiar) > T:
                        newnpImage[i, j-1, nivel] = 255
                        newnpImage[i, j, nivel] = 255  
                        newnpImage[i, j+1, nivel] = 255
                    u, v, verificaLimiar = -xpiso, -ypiso, 0
                    
    elif opcao == 2:
        
        nomeRetas = 'Verticais'
        ''' Aplicação da máscara para detecção de retas verticais '''
        for i in range(xpiso, size[0] - xpiso):
            for j in range(ypiso, size[1] - ypiso):
                for nivel in range(size[2]):
                    while u <= xpiso:
                        while v <= ypiso:
                            if v == 0:
                                verificaLimiar += 2 * npImage[i+u, v+j, nivel]
                            else:
                                verificaLimiar += -1 * npImage[i+u, v+j, nivel]                        
                            v += 1
                        u += 1
                        v = -ypiso
                        
                    if np.abs(verificaLimiar) > T:
                        newnpImage[i-1, j, nivel] = 255                
                        newnpImage[i, j, nivel] = 255 
                        newnpImage[i+1, j, nivel] = 255                
                    u, v, verificaLimiar = -xpiso, -ypiso, 0
 
    elif opcao == 3:   
        
        nomeRetas = 'de 45 Graus'    
        ''' Aplicação da máscara para detecção de retas de 45 graus '''
        for i in range(xpiso, size[0] - xpiso):
            for j in range(ypiso, size[1] - ypiso):
                for nivel in range(size[2]):
                    while u <= xpiso:
                        while v <= ypiso:
                            if (u == 1 and v == -1) or (u == 0 and v == 0) or (u == -1 and v == 1):
                                verificaLimiar += 2 * npImage[i+u, v+j, nivel]
                            else:
                                verificaLimiar += -1 * npImage[i+u, v+j, nivel]                        
                            v += 1
                        u += 1
                        v = -ypiso
                        
                    if np.abs(verificaLimiar) > T:
                        newnpImage[i-1, j+1, nivel] = 255                
                        newnpImage[i, j, nivel] = 255
                        newnpImage[i+1, j-1, nivel] = 255                
                    u, v, verificaLimiar = -xpiso, -ypiso, 0
                
    elif opcao == 4:
        
        nomeRetas = 'de 135 Graus'
        ''' Aplicação da máscara para detecção de retas de 135 graus '''
        for i in range(xpiso, size[0] - xpiso):
            for j in range(ypiso, size[1] - ypiso):
                for nivel in range(size[2]):
                    while u <= xpiso:
                        while v <= ypiso:
                            if u == v:
                                verificaLimiar += 2 * npImage[i+u, v+j, nivel]
                            else:
                                verificaLimiar += -1 * npImage[i+u, v+j, nivel]                        
                            v += 1
                        u += 1
                        v = -ypiso
                        
                    if np.abs(verificaLimiar) > T:
                        newnpImage[i-1, j-1, nivel] = 255
                        newnpImage[i, j, nivel] = 255 
                        newnpImage[i+1, j+1, nivel] = 255                
                    u, v, verificaLimiar = -xpiso, -ypiso, 0
                
    plt.figure(1)
    plt.subplot(1,2,1)
    plt.title('Imagem Normal \n(Gray Scale Red)')
    plt.imshow(npImage[:, :, 0], cmap = 'gray', vmin = 0, vmax = 255)
    plt.subplot(1,2,2)               
    plt.title('Deteccao de Retas ' + str(nomeRetas) + '\n(Gray Scale Red)')
    plt.imshow(newnpImage[:, :, 0], cmap = 'gray', vmin = 0, vmax = 255)
    
    plt.figure(2)
    plt.subplot(1,2,1)
    plt.title('Imagem Normal \n(Gray Scale Green)')
    plt.imshow(npImage[:, :, 1], cmap = 'gray', vmin = 0, vmax = 255)
    plt.subplot(1,2,2)               
    plt.title('Deteccao de Retas ' + str(nomeRetas) + '\n(Gray Scale Green)')
    plt.imshow(newnpImage[:, :, 1], cmap = 'gray', vmin = 0, vmax = 255)
    
    plt.figure(3)
    plt.subplot(1,2,1)
    plt.title('Imagem Normal \n(Gray Scale Blue)')
    plt.imshow(npImage[:, :, 2], cmap = 'gray', vmin = 0, vmax = 255)
    plt.subplot(1,2,2)               
    plt.title('Deteccao de Retas ' + str(nomeRetas) + '\n(Gray Scale Blue)')
    plt.imshow(newnpImage[:, :, 2], cmap = 'gray', vmin = 0, vmax = 255)


