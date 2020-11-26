import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

def RGB(figureRGB):     
    figureGB = np.copy(figureRGB)
    figureGB[:,:,0] = 0
    
    figureRB = np.copy(figureRGB)
    figureRB[:,:,1] = 0
    
    figureRG = np.copy(figureRGB)
    figureRG[:,:,2] = 0
    
    plt.figure()    
    plt.subplot(1,4,1)
    plt.title('RGB')
    plt.imshow(figureRGB)    
    plt.subplot(1,4,2)
    plt.title('R = 0')
    plt.imshow(figureGB)
    plt.subplot(1,4,3)
    plt.title('G = 0')
    plt.imshow(figureRB)
    plt.subplot(1,4,4)
    plt.title('B = 0')
    plt.imshow(figureRG)
    
    plt.figure()    
    plt.subplot(1,4,1)
    plt.title('RGB')
    plt.imshow(figureRGB, vmin=0, vmax=1)
    plt.subplot(1,4,2)
    plt.title('Red')
    plt.imshow(figureRGB[:,:,0], cmap='gray', vmin=0, vmax=1)
    plt.subplot(1,4,3)
    plt.title('Green')
    plt.imshow(figureRGB[:,:,1], cmap='gray', vmin=0, vmax=1)
    plt.subplot(1,4,4)
    plt.title('Blue')
    plt.imshow(figureRGB[:,:,2], cmap='gray', vmin=0, vmax=1)   
    
    
    ''' RGB com Mediana '''       
#    figureRGBcomMediana = np.copy(figureRGB)    
#    windowSize = 3       
#    matrizWindowSize = []
#    xpiso, ypiso = np.floor(windowSize/2), np.floor(windowSize/2) 
#    u, v = (int)(-xpiso), (int)(-ypiso)        
#    
#    for i in range(size[0] - windowSize//2):
#        for j in range(size[1] - windowSize//2):
#            for nivel in range(3):
#                while u <= xpiso:
#                    while v <= ypiso:
#                        if i >= windowSize//2 and j >= windowSize//2:
#                            matrizWindowSize.append(figureRGB[i + u, j + v, nivel]) 
#                        v += 1
#                    u += 1
#                    v = (int)(-ypiso)
#                
#                mediana = np.median(matrizWindowSize)            
#                
#                figureRGBcomMediana[i, j, nivel] = mediana        
#                u, v = (int)(-xpiso), (int)(-ypiso)
#                matrizWindowSize = []
#                 
#    plt.figure()    
#    plt.subplot(1,4,1)
#    plt.title('RGB com Mediana')
#    plt.imshow(figureRGBcomMediana, vmin=0, vmax=1)     
#    plt.subplot(1,4,2)
#    plt.title('Red')
#    plt.imshow(figureRGBcomMediana[:,:,0], cmap='gray', vmin=0, vmax=1)
#    plt.subplot(1,4,3)
#    plt.title('Green')
#    plt.imshow(figureRGBcomMediana[:,:,1], cmap='gray', vmin=0, vmax=1)
#    plt.subplot(1,4,4)
#    plt.title('Blue')
#    plt.imshow(figureRGBcomMediana[:,:,2], cmap='gray', vmin=0, vmax=1)    

def ConversionRGB2CMY(figureRGB):    
    figureCMY = np.copy(figureRGB)
    
    ''' Transformação de RGB para CMY '''
    figureCMY = 1 - figureCMY
    '''
    plt.figure()    
    plt.subplot(1,4,1)
    plt.title('CMY')
    plt.imshow(figureCMY, vmin=0, vmax=1)
    plt.subplot(1,4,2)
    plt.title('Cyan')
    plt.imshow(figureCMY[:,:,0], cmap='gray', vmin=0, vmax=1)
    plt.subplot(1,4,3)
    plt.title('Magenta')
    plt.imshow(figureCMY[:,:,1], cmap='gray', vmin=0, vmax=1)
    plt.subplot(1,4,4)
    plt.title('Yellow')
    plt.imshow(figureCMY[:,:,2], cmap='gray', vmin=0, vmax=1)'''
    
    ''' CMY com Mediana '''    
    figureCMYcomMediana = np.copy(figureCMY)    
    windowSize = 3       
    matrizWindowSize = []
    xpiso, ypiso = np.floor(windowSize/2), np.floor(windowSize/2) 
    u, v = (int)(-xpiso), (int)(-ypiso)        
    
    for i in range(size[0] - windowSize//2):
        for j in range(size[1] - windowSize//2):
            for nivel in range(3):
                while u <= xpiso:
                    while v <= ypiso:
                        if i >= windowSize//2 and j >= windowSize//2:
                            matrizWindowSize.append(figureCMY[i + u, j + v, nivel]) 
                        v += 1
                    u += 1
                    v = (int)(-ypiso)
                
                mediana = np.median(matrizWindowSize)            
                
                figureCMYcomMediana[i, j, nivel] = mediana        
                u, v = (int)(-xpiso), (int)(-ypiso)
                matrizWindowSize = []
    '''               
    plt.figure()    
    plt.subplot(1,4,1)
    plt.title('CMY com Mediana')
    plt.imshow(figureCMYcomMediana, vmin=0, vmax=1)     
    plt.subplot(1,4,2)
    plt.title('Cyan')
    plt.imshow(figureCMYcomMediana[:,:,0], cmap='gray', vmin=0, vmax=1)
    plt.subplot(1,4,3)
    plt.title('Magenta')
    plt.imshow(figureCMYcomMediana[:,:,1], cmap='gray', vmin=0, vmax=1)
    plt.subplot(1,4,4)
    plt.title('Yellow')
    plt.imshow(figureCMYcomMediana[:,:,2], cmap='gray', vmin=0, vmax=1)  '''

def ConversionRGB2HSI(figureRGB, size):
    figureHSI = np.zeros(size).astype(float)
    
    ''' Transformação de RGB para HSI '''    
    for linha in range(size[0]):
        for coluna in range(size[1]):  
            teta = np.arccos((0.5 * np.absolute(
                2 * figureRGB[linha, coluna, 0] - figureRGB[linha, coluna, 1] - figureRGB[linha, coluna, 2]
                )) / (np.sqrt(
                    np.power(figureRGB[linha, coluna, 0] -
                        figureRGB[linha, coluna, 1], 2) +
                            (figureRGB[linha, coluna, 0] -
                                figureRGB[linha, coluna, 2]) * (figureRGB[linha, coluna, 1] -
                                figureRGB[linha, coluna, 2])
                            )))       
            #print(teta)
            if (figureRGB[linha, coluna, 2] <= figureRGB[linha, coluna, 1]):
                figureHSI[linha, coluna, 0] = teta      # H
            else:
                figureHSI[linha, coluna, 0] = 6.28319 - teta     # H
            
            # S
            figureHSI[linha, coluna, 1] = 1 - (3/(figureRGB[linha, coluna, 0] +
                        figureRGB[linha, coluna, 1] +
                            figureRGB[linha, coluna, 2])) *  min(figureRGB[linha, coluna, 0], 
                                    figureRGB[linha, coluna, 1], 
                                    figureRGB[linha, coluna, 2])
            # I
            figureHSI[linha, coluna, 2] =  (1/3)*(figureRGB[linha, coluna, 0] +
                      figureRGB[linha, coluna, 1] +
                      figureRGB[linha, coluna, 2])        
            
            #if(figureHSI[linha, coluna, 0] ==' nan'):    
            #print(figureHSI[linha, coluna, 0])
            
    plt.figure()     
    plt.subplot(1,4,1)
    plt.title('HSI')
    plt.imshow(figureHSI, vmin=0, vmax=1)
    plt.subplot(1,4,2)
    plt.title('H')
    plt.imshow(figureHSI[:,:,0], cmap='gray', vmin=0, vmax=1)
    plt.subplot(1,4,3)
    plt.title('S')
    plt.imshow(figureHSI[:,:,1], cmap='gray', vmin=0, vmax=1)
    plt.subplot(1,4,4)
    plt.title('I')
    plt.imshow(figureHSI[:,:,2], cmap='gray', vmin=0, vmax=1)     
    
    ''' HSI com Mediana '''    
    figureHSIcomMediana = np.copy(figureHSI)    
    windowSize = 3       
    matrizWindowSize = []
    xpiso, ypiso = np.floor(windowSize/2), np.floor(windowSize/2) 
    u, v = (int)(-xpiso), (int)(-ypiso)        
    
    for i in range(size[0] - windowSize//2):
        for j in range(size[1] - windowSize//2):
            for nivel in range(3):
                while u <= xpiso:
                    while v <= ypiso:
                        if i >= windowSize//2 and j >= windowSize//2:
                            matrizWindowSize.append(figureHSI[i + u, j + v, nivel]) 
                        v += 1
                    u += 1
                    v = (int)(-ypiso)
                
                mediana = np.median(matrizWindowSize)            
                
                figureHSIcomMediana[i, j, nivel] = mediana        
                u, v = (int)(-xpiso), (int)(-ypiso)
                matrizWindowSize = []
                   
    plt.figure()    
    plt.subplot(1,4,1)
    plt.title('HSI com Mediana')
    plt.imshow(figureHSIcomMediana, vmin=0, vmax=1)     
    plt.subplot(1,4,2)
    plt.title('H')
    plt.imshow(figureHSIcomMediana[:,:,0], cmap='gray', vmin=0, vmax=1)
    plt.subplot(1,4,3)
    plt.title('S')
    plt.imshow(figureHSIcomMediana[:,:,1], cmap='gray', vmin=0, vmax=1)
    plt.subplot(1,4,4)
    plt.title('I')
    plt.imshow(figureHSIcomMediana[:,:,2], cmap='gray', vmin=0, vmax=1)  
    
    '''   
    plt.figure()   
    
    plt.subplot(1,4,1)
    plt.title("Histograma HSI")
    print(np.ndarray.flatten(figureHSI))
    #figureRGB *= 255
    plt.hist(np.ndarray.flatten(figureHSI), bins = 256, range = (0, 10));    
    #print(np.ndarray.flatten(figureHSI).min())
    #np.histogram(np.ndarray.flatten(figureRGB), bins = 256)
    '''

nature = misc.imread("nature.png")
figureRGB = np.copy(nature)
figureRGB = figureRGB.astype(float)/255
size = np.shape(figureRGB) 
    
RGB(figureRGB)
ConversionRGB2CMY(figureRGB)
ConversionRGB2HSI(figureRGB, size)