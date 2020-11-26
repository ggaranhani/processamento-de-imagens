import numpy as np
from scipy import misc
#import imageio
import matplotlib.pyplot as plt

def DetectarPontos(npImage, T, size):     
    ''' Nova imagem, que será preenchida pela detecção de pontos discrepantes na imagem atual '''
    newnpImage = np.zeros(size, dtype = np.float)  # Imagem inicial com fundo preto
    
    ''' Definição da máscara '''
    windowSize = 3       
    xpiso, ypiso = int(np.floor(windowSize/2)), int(np.floor(windowSize/2))
    u, v, verificaLimiar= -xpiso, -ypiso, 0
    
    ''' Aplicação da máscara para detecção de pontos '''
    for i in range(xpiso, size[0] - xpiso):
        for j in range(ypiso, size[1] - ypiso):
            for nivel in range(size[2]):
                while u <= xpiso:
                    while v <= ypiso:
                        if u == 0 and v == 0:
                            verificaLimiar += 8 * npImage[i+u, v+j, nivel]
                        else:
                            verificaLimiar += (-1) * npImage[i+u, v+j, nivel]                        
                        v += 1
                    u += 1
                    v = -ypiso
                    
                if np.abs(verificaLimiar) > T:
                    newnpImage[i, j, nivel] = 255                
                u, v, verificaLimiar = -xpiso, -ypiso, 0
    
    plt.figure(1)
    plt.subplot(1,2,1)
    plt.title('Imagem Normal \n(Gray Scale Red)')
    plt.imshow(npImage[:, :, 0], cmap = 'gray', vmin = 0, vmax = 255)
    plt.subplot(1,2,2)               
    plt.title('Deteccao de Pontos \n(Gray Scale Red)')
    plt.imshow(newnpImage[:, :, 0], cmap = 'gray', vmin = 0, vmax = 255)
    
    plt.figure(2)
    plt.subplot(1,2,1)
    plt.title('Imagem Normal \n(Gray Scale Green)')
    plt.imshow(npImage[:, :, 1], cmap = 'gray', vmin = 0, vmax = 255)
    plt.subplot(1,2,2)               
    plt.title('Deteccao de Pontos \n(Gray Scale Green)')
    plt.imshow(newnpImage[:, :, 1], cmap = 'gray', vmin = 0, vmax = 255)
    
    plt.figure(3)
    plt.subplot(1,2,1)
    plt.title('Imagem Normal \n(Gray Scale Blue)')
    plt.imshow(npImage[:, :, 2], cmap = 'gray', vmin = 0, vmax = 255)
    plt.subplot(1,2,2)               
    plt.title('Deteccao de Pontos \n(Gray Scale Blue)')
    plt.imshow(newnpImage[:, :, 2], cmap = 'gray', vmin = 0, vmax = 255)
    
    plt.figure(4)
    plt.subplot(1,2,1)
    plt.title('Imagem Normal')
    plt.imshow(npImage, cmap = 'gray', vmin = 0, vmax = 255)
    plt.title('Deteccao de Pontos')
    plt.subplot(1,2,2)               
    plt.imshow(newnpImage, cmap = 'gray', vmin = 0, vmax = 255)
    
def DetectarRetas(npImage, T, size):
    ''' Nova imagem, que será preenchida pela detecção de retas na imagem atual '''
    newnpImage = np.zeros(size, dtype = np.float)  # Imagem inicial com fundo preto
    
    ''' Definição da máscara '''
    windowSize = 3       
    xpiso, ypiso = int(np.floor(windowSize/2)), int(np.floor(windowSize/2))
    u, v = -xpiso, -ypiso
    verificaLimiar = 0 
    
    ''' Definir qual tipo de máscara a ser utilizada na detecção de retas '''
    opcao = None
    while opcao not in (1, 2, 3, 4):
        valorEntrada = input("Entre com as seguintes opções de detecção de retas: \n1 - " +
                             "Horizontais \n2 - Verticais \n3 - 45 Graus \n4 - 135 Graus: \n")
        try: 
            opcao = int(valorEntrada)
        except ValueError:
            print("\n>> Por favor, entre com um inteiro e, de preferência, válido!".format(input = valorEntrada))
            
    if opcao == 1:
        
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
    
def DetectarBordas(npImage, T, size):
    ''' Nova imagem, que será preenchida pela detecção de bordas na imagem atual '''
    newnpImage = np.zeros(size, dtype = np.float) 
    
    ''' Definir qual tipo de máscara a ser utilizada na detecção de bordas '''
    opcao = None
    while opcao not in (1, 2, 3, 4):
        valorEntrada = input("Entre com as seguintes opções de método de detecção de bordas: \n1 - " +
                             "Roberts \n2 - Prewitt \n3 - Sobel \n4 - Kirsch: \n")
        try: 
            opcao = int(valorEntrada)
        except ValueError:
            print("\n>> Por favor, entre com um inteiro e, de preferência, válido!".format(input = valorEntrada))
            
    if opcao == 1:
        
        nomeBordas = 'Roberts'
        ''' Aplicação da máscara de Roberts para detecção de bordas '''
        for i in range(0, size[0] - 1):
            for j in range(0, size[1] - 1):
                for nivel in range(3):
                    Gx = 1 * npImage[i, j, nivel] + (-1) * npImage[i+1, j+1, nivel]
                    Gy = (-1) * npImage[i, j+1, nivel]  + 1 * npImage[i+1, j, nivel]     
                        
                    if np.abs(Gx) + np.abs(Gy) > T:
                        newnpImage[i, j, nivel] = 255 
                    Gx, Gy, = 0, 0
    
    elif opcao == 2: 
        
        nomeBordas = 'Prewitt'
        ''' Aplicação da máscara de Prewitt para detecção de bordas '''
        for i in range(1, size[0] - 1):
            for j in range(1, size[1] - 1):
                for nivel in range(3):
                    Gx = ((-1) * npImage[i-1, j-1, nivel] + (-1) * npImage[i, j-1, nivel] + 
                          (-1) * npImage[i+1, j-1, nivel] + 1 * npImage[i-1, j+1, nivel] + 
                          1 * npImage[i, j+1, nivel] + 1 * npImage[i+1, j+1, nivel]) 
                    Gy = ((-1) * npImage[i-1, j-1, nivel] + (-1) * npImage[i-1, j, nivel] + 
                          (-1) * npImage[i-1, j+1, nivel] + 1 * npImage[i+1, j-1, nivel] + 
                          1 * npImage[i+1, j, nivel] + 1 * npImage[i+1, j+1, nivel])   
                        
                    if np.abs(Gx) + np.abs(Gy) > T:
                        newnpImage[i, j, nivel] = 255 
                    Gx, Gy, = 0, 0   
                
    elif opcao == 3: 
    
        nomeBordas = 'Sobel'
        ''' Aplicação da máscara de Sobel para detecção de bordas '''
        for i in range(1, size[0] - 1):
            for j in range(1, size[1] - 1):
                for nivel in range(3):
                    Gx = ((-1) * npImage[i-1, j-1, nivel] + (-2) * npImage[i, j-1, nivel] + 
                          (-1) * npImage[i+1, j-1, nivel] + 1 * npImage[i-1, j+1, nivel] + 
                          2 * npImage[i, j+1, nivel] + 1 * npImage[i+1, j+1, nivel]) 
                    Gy = ((-1) * npImage[i-1, j-1, nivel] + (-2) * npImage[i-1, j, nivel] + 
                          (-1) * npImage[i-1, j+1, nivel] + 1 * npImage[i+1, j-1, nivel] + 
                          2 * npImage[i+1, j, nivel] + 1 * npImage[i+1, j+1, nivel])  
                        
                    if np.abs(Gx) + np.abs(Gy) > T:
                        newnpImage[i, j, nivel] = 255 
                    Gx, Gy, = 0, 0   
                
    elif opcao == 4: 
    
        nomeBordas = 'Kirsch'
        ''' Aplicação da máscara de Kirsch para detecção de bordas '''
        for i in range(1, size[0] - 1):
            for j in range(1, size[1] - 1):
                for nivel in range(3):
                    m1 = 5 * npImage[i-1, j-1, nivel] + 5 * npImage[i, j-1, nivel] + 5 * npImage[i+1, j-1, nivel] + (-3) * npImage[i+1, j, nivel] + (-3) * npImage[i+1, j+1, nivel] + (-3) * npImage[i, j+1, nivel] + (-3) * npImage[i-1, j, nivel] + (-3) * npImage[i-1, j, nivel] 
                    m2 = (-3) * npImage[i-1, j-1, nivel] + 5 * npImage[i, j-1, nivel] + 5 * npImage[i+1, j-1, nivel] + 5 * npImage[i+1, j, nivel] + (-3) * npImage[i+1, j+1, nivel] + (-3) * npImage[i, j+1, nivel] + (-3) * npImage[i-1, j, nivel] + (-3) * npImage[i-1, j, nivel] 
                    m3 = (-3) * npImage[i-1, j-1, nivel] + (-3) * npImage[i, j-1, nivel] + 5 * npImage[i+1, j-1, nivel] + 5 * npImage[i-1, j+1, nivel] + 5 * npImage[i-1, j+1, nivel] + (-3) * npImage[i-1, j+1, nivel] + (-3) * npImage[i-1, j+1, nivel] + (-3) * npImage[i-1, j+1, nivel]
                    m4 = (-3) * npImage[i-1, j-1, nivel] + (-3) * npImage[i, j-1, nivel] + (-3) * npImage[i+1, j-1, nivel] + 5 * npImage[i-1, j+1, nivel] + 5 * npImage[i-1, j+1, nivel] + 5 * npImage[i-1, j+1, nivel] + (-3) * npImage[i-1, j+1, nivel] + (-3) * npImage[i-1, j+1, nivel]
                    m5 = (-3) * npImage[i-1, j-1, nivel] + (-3) * npImage[i, j-1, nivel] + (-3) * npImage[i+1, j-1, nivel] + (-3) * npImage[i-1, j+1, nivel] + 5 * npImage[i-1, j+1, nivel] + 5 * npImage[i-1, j+1, nivel] + 5 * npImage[i-1, j+1, nivel] + (-3) * npImage[i-1, j+1, nivel]
                    m6 = (-3) * npImage[i-1, j-1, nivel] + (-3) * npImage[i, j-1, nivel] + (-3) * npImage[i+1, j-1, nivel] + (-3) * npImage[i-1, j+1, nivel] + (-3) * npImage[i-1, j+1, nivel] + 5 * npImage[i-1, j+1, nivel] + 5 * npImage[i-1, j+1, nivel] + 5 * npImage[i-1, j+1, nivel]
                    m7 = 5 * npImage[i-1, j-1, nivel] + (-3) * npImage[i, j-1, nivel] + (-3) * npImage[i+1, j-1, nivel] + (-3) * npImage[i-1, j+1, nivel] + (-3) * npImage[i-1, j+1, nivel] + (-3) * npImage[i-1, j+1, nivel] + 5 * npImage[i-1, j+1, nivel] + 5 * npImage[i-1, j+1, nivel]
                    m8 = 5 * npImage[i-1, j-1, nivel] + 5 * npImage[i, j-1, nivel] + (-3) * npImage[i+1, j-1, nivel] + (-3) * npImage[i-1, j+1, nivel] + (-3) * npImage[i-1, j+1, nivel] + (-3) * npImage[i-1, j+1, nivel] + (-3) * npImage[i-1, j+1, nivel] + 5 * npImage[i-1, j+1, nivel]
                    
                    valorMaximoMascara = max(m1, m2, m3, m4, m5, m6, m7, m8)
                    if valorMaximoMascara > T:
                        newnpImage[i, j, nivel] = 255 
                    valorMaximoMascara = 0   
                
    plt.figure(1)
    plt.subplot(1,2,1)
    plt.title('Imagem Normal \n(Gray Scale Red)')
    plt.imshow(npImage[:, :, 0], cmap = 'gray', vmin = 0, vmax = 255)
    plt.subplot(1,2,2)               
    plt.title('Deteccao de Bordas de ' + str(nomeBordas) + '\n(Gray Scale Red)')
    plt.imshow(newnpImage[:, :, 0], cmap = 'gray', vmin = 0, vmax = 255)
    
    plt.figure(2)
    plt.subplot(1,2,1)
    plt.title('Imagem Normal \n(Gray Scale Green)')
    plt.imshow(npImage[:, :, 1], cmap = 'gray', vmin = 0, vmax = 255)
    plt.subplot(1,2,2)               
    plt.title('Deteccao de Bordas de ' + str(nomeBordas) + '\n(Gray Scale Green)')
    plt.imshow(newnpImage[:, :, 1], cmap = 'gray', vmin = 0, vmax = 255)
    
    plt.figure(3)
    plt.subplot(1,2,1)
    plt.title('Imagem Normal \n(Gray Scale Blue)')
    plt.imshow(npImage[:, :, 2], cmap = 'gray', vmin = 0, vmax = 255)
    plt.subplot(1,2,2)               
    plt.title('Deteccao de Bordas de ' + str(nomeBordas) + '\n(Gray Scale Blue)')
    plt.imshow(newnpImage[:, :, 2], cmap = 'gray', vmin = 0, vmax = 255)    
    
def Comparacao(npImage, T, size):
    ''' Nova imagem, que será preenchida pela detecção de bordas na imagem atual '''
    newnpImageLaplaciano = np.zeros(size, dtype = np.float)            
    newnpImageLdG = np.zeros(size, dtype = np.float)            

    ''' Aplicação do operador Laplaciano para detecção de bordas '''
    for i in range(1, size[0] - 1):
        for j in range(1, size[1] - 1):
            for nivel in range(3):
                laplaciano = ((-1) * npImage[i-1, j-1, nivel] + (-4) * npImage[i-1, j, nivel] + 
                              (-1) * npImage[i-1, j+1, nivel] + (-4) * npImage[i, j-1, nivel] + 
                              (20) * npImage[i, j, nivel] + (-4) * npImage[i, j+1, nivel] + 
                              (-1) * npImage[i+1, j-1, nivel] + (-4) * npImage[i+1, j, nivel] + 
                              (-1) * npImage[i+1, j+1, nivel])
                    
                if np.abs(laplaciano) > T:
                    newnpImageLaplaciano[i, j, nivel] = 255 
                laplaciano = 0
                
    ''' Aplicação do operador Laplaciano do Gaussiano para detecção de bordas '''
    for i in range(2, size[0] - 2):
        for j in range(2, size[1] - 2):
            for nivel in range(3):
                ldg = ((-1) * npImage[i-2, j, nivel] + (-1) * npImage[i-1, j-1, nivel] + 
                       (-2) * npImage[i-1, j, nivel] + (-1) * npImage[i-1, j+1, nivel] + 
                       (-1) * npImage[i, j-2, nivel] + (-2) * npImage[i, j-1, nivel] + 
                       (16) * npImage[i, j, nivel] + (-2) * npImage[i, j+1, nivel] + 
                       (-1) * npImage[i, j+2, nivel] + (-1) * npImage[i+1, j-1, nivel] + 
                       (-2) * npImage[i+1, j, nivel] + (-1) * npImage[i+1, j+1, nivel] + 
                       (-1) * npImage[i+2, j, nivel])
                    
                if np.abs(ldg) > T:
                    newnpImageLdG[i, j, nivel] = 255 
                ldg = 0
    
    plt.figure(1)
    plt.subplot(1,2,1)
    plt.title('Imagem Normal')
    plt.imshow(npImage, cmap = 'gray', vmin = 0, vmax = 255)    
     
    plt.figure(2)
    plt.subplot(1,2,1)               
    plt.title('Deteccao de Bordas \nLaplaciano\n(Gray Scale Red)')
    plt.imshow(newnpImageLaplaciano[:, :, 0], cmap = 'gray', vmin = 0, vmax = 255) 
    plt.subplot(1,2,2)               
    plt.title('Deteccao de Bordas \nLaplaciano do Gaussiano\n(Gray Scale Red)')
    plt.imshow(newnpImageLdG[:, :, 0], cmap = 'gray', vmin = 0, vmax = 255) 
    
    plt.figure(3)
    plt.subplot(1,2,1)               
    plt.title('Deteccao de Bordas \nLaplaciano\n(Gray Scale Green)')
    plt.imshow(newnpImageLaplaciano[:, :, 1], cmap = 'gray', vmin = 0, vmax = 255) 
    plt.subplot(1,2,2)               
    plt.title('Deteccao de Bordas \nLaplaciano do Gaussiano\n(Gray Scale Green)')
    plt.imshow(newnpImageLdG[:, :, 1], cmap = 'gray', vmin = 0, vmax = 255) 
    
    plt.figure(4)
    plt.subplot(1,2,1)               
    plt.title('Deteccao de Bordas \nLaplaciano\n(Gray Scale Blue)')
    plt.imshow(newnpImageLaplaciano[:, :, 2], cmap = 'gray', vmin = 0, vmax = 255) 
    plt.subplot(1,2,2)               
    plt.title('Deteccao de Bordas \nLaplaciano do Gaussiano\n(Gray Scale Blue)')
    plt.imshow(newnpImageLdG[:, :, 2], cmap = 'gray', vmin = 0, vmax = 255)
                
####################      MAIN      #######################  
                                 
''' Leitura da imagem '''
#image = imageio.imread("nature.png")
image = misc.imread("Colorida.png")
''' Transforma a imagem em um formato manipulável pela biblioteca numpy '''
npImage = np.copy(image)

''' Definição do limiar '''
T = 200

''' Formato da imagem '''
size = np.shape(npImage)

''' Menu de escolha '''
opcao = None
while opcao not in (1, 2, 3, 4):
    valorEntrada = input("Entre com um valor para as seguintes opções:\n1 - Detecção de Pontos\n" +
                         "2 - Detecção de Retas\n3 - Detecção de Bordas\n4 - Comparação entre " + 
                         "detector de bordas Laplaciano e Laplaciano do Gaussiano: \n")
    try:
        opcao = int(valorEntrada)
    except ValueError:
        print("\n>> Por favor, entre com um inteiro e, de preferência, válido!".format(raw_input = valorEntrada))
    
if opcao == 1:
    DetectarPontos(npImage, T, size)
    
elif opcao == 2:
    DetectarRetas(npImage, T, size)

elif opcao == 3:
    DetectarBordas(npImage, T, size)

elif opcao == 4:
    Comparacao(npImage, T, size)
