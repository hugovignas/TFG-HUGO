# -*- coding: utf-8 -*-

"""
@file huella.py
@brief Módulo de creación de huellas digitales
@details Este archivo contiene las funciones necesarias para la creación de una 
huella digital a partir de un array de bytes que compongan la muestra de una señal. 
Dispone de tres funcionalidades principales
,creación de espectogramas, búsqueda de máximos, y creación de hashes.
"""
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plot
from operator import itemgetter
from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import (generate_binary_structure, iterate_structure, binary_erosion)
import hashlib
import warnings
warnings.filterwarnings("ignore")

def picos(espectograma):
    """
    @brief Esta función detecta los picos máximos en un espectograma utilizando filtros de máximos locales. 
    De dichos máximos, la función se queda con aquellosque superen un umbral específico de amplitud. 
    Hay que definir en la función el valor de vecindad a para el que vamos a tener en cuenta 
    comparación de cercanía.
    

    @param espectograma  Array 2D  de numpy que representa el espectograma del muestreo
    @return Listas asociadas a picos de frecuencia y 
    """
    amplitud_referencia=10 #Amplitud mínima para ser un pico

    vecindad=15 #Cuántas celdas entran dentro de los valores comparables por cercanía de los picos

    matriz_vecindad=iterate_structure(generate_binary_structure(2,1), vecindad) #Se genera matriz de vecindad a partir de la cual se va aplicar el filtro
   

    filtro_maximo= maximum_filter(espectograma, footprint=matriz_vecindad) #Se aplica el filtro del maximo con la estructura de vecindad creada, se genera una matriz en la que esas 10 casillas son sustituidas por su máximo local
    maximos_local=filtro_maximo==espectograma #Se genera array booleano en la que tendrá valor 1 si se trata de un máximo



    j,i=np.where(maximos_local)   #Buscamos las coordenadas en las que tenemos los picos
    espectograma_reducido_a_maximos =espectograma[maximos_local] #Nos quedamos solo con los picos dentro del espectograma
    
    
    espectograma_reducido_a_maximos=espectograma_reducido_a_maximos.flatten() #Pasamos a 1D
    
    picos=zip(espectograma_reducido_a_maximos,i,j) #Guardamos cada máximo con sus coordenadas de tiempo y frecuencia
    
    #De los picos nos quedamos con todos aquellos que superen la amplitud mínima
    aux_picos=[]
    for pico in picos:
        if pico[0]>amplitud_referencia:  
            aux_picos.append(pico)
    
     #De los que la superan almacenamos su tiempo       
    tiempos=[]
    for pico in aux_picos:
        tiempos.append(pico[1])
    
    #De los que la superan almacenamos su frecuencia    
    frecuencias=[]        
    for pico in aux_picos:
        frecuencias.append(pico[2])
        
    return frecuencias, tiempos #Se devuelven las listas de frecuencia y tiempos de los picos


def hashes(frecuencias,tiempos, tipohash):
    """
    @brief Esta función compara picos de frecuencia encontrados, y si se encuentran a la distancia 
    necesaria, se genera un hash asociado al par.
    

    @param frecuencias lista de picos de frecuencias
    @param tiempos lista de tiempos asociados a los picos de frecuencias
    @param tipohash Algoritmo que se quiere aplicar al hashing
    
    @return Array de picos de frecuencia hasheados para definir la huella digital
    """
    longitud=len(frecuencias)
    vecindad=50 #Radio de búsqueda por cercanía entre hashes
    distancia_permitida=300 #Distancia temporal máxima entre picos para sellar en un hash
    
    
    hashes=[]  #Array de acumulacion de hashes
    for i in range(longitud):   #Se comienzan a recorrer los picos
        
        pos_relativa=1         #Iterador de posición relativa a picos
        
        while pos_relativa<vecindad: #Para cada pico se le hace comparación a sus picos cercanos por vecindad
            

            if(i+pos_relativa)<longitud:   #Control para no salir de memoria
                
                frecuencia1=frecuencias[i]                #Se almacenan las frecuencias
                frecuencia2=frecuencias[pos_relativa]     
   
                distancia=tiempos[i]-tiempos[pos_relativa]      #Calculamos la distancia temporal entre ambos picos de frecuencia
                distancia = abs(distancia)                      #Valor absoluto para no tener valores temporales negativos
                

                
                if distancia<=distancia_permitida:            #Si se encuentra dentro del apetito de distancia, se sellan ambos picos en un hash

                    cadena = "%s|%s|%s" % (str(distancia),str(frecuencia1), str(frecuencia2))    #Se genera un string dependiente de ambas frecuencias y del tiempo, al que se le hace un hash
                    
                    #Según el algoritmo de hash utilizado se procede con uno u otro
                    match tipohash:
                           case "MD5":
                             hash_pico = hashlib.md5(cadena.encode('utf-8'))
                 
                           case "SHA-1":
                             hash_pico = hashlib.sha1(cadena.encode('utf-8'))                       
                
                           case "SHA-256":
                             hash_pico = hashlib.sha256(cadena.encode('utf-8'))
                            
                    hashes.append(hash_pico.hexdigest())  #Se van añadiendo al array de hashes
            pos_relativa+=1
    return hashes #Se retorna la huella ya conformada
    

def espectograma(muestreo):
    """
    @brief Esta función obtiene un espectograma a partir de un muestreo de bytes. 
    El espectograma también dependerá del tamaño de ventana FFT escogido, de la tasa de muestreo
    y del valor de solapamiento que queremos para la STFT.
    

    @param muestreo  Array de bytes correspondientes a un archivo de audio
    @return espectograma  Array 2D  de numpy que representa el espectograma del muestreo
    """
    fs=44100 #Frecuencia de muestreo, Teorema de Nyquist
    ventana_fft=1024  #Tamanyo de ventana de FFT para STFT
    overlap=512 #Valor de la ventana que queremos que se "pisen" 
    
    espectograma=mlab.specgram(muestreo,NFFT=ventana_fft, Fs=fs,window=mlab.window_hanning, noverlap=512)[0]  #Calculamos el espectograma
    
    espectograma = 10*np.log10(espectograma)  #Le hacemos la transformada logarítmica 
    espectograma[espectograma==-np.inf]=0   #Cambiamos los valores a infinito por ceros
    return espectograma


def espectograma_grabadora(muestreo):
    """
    @brief Esta función obtiene un espectograma a partir de un muestreo de bytes. 
    El espectograma también dependerá del tamaño de ventana FFT escogido, de la tasa de muestreo
    y del valor de solapamiento que queremos para la STFT.
    

    @param muestreo  Array de bytes correspondientes a un archivo de audio
    @return espectograma  Array 2D  de numpy que representa el espectograma del muestreo
    """
    fs=44100 #Frecuencia de muestreo, Teorema de Nyquist
    ventana_fft=512 #Tamanyo de ventana de FFT para STFT
    overlap=512 #Valor de la ventana que queremos que se "pisen" 
    
    espectograma=mlab.specgram(muestreo,NFFT=ventana_fft, Fs=fs,window=mlab.window_hanning, noverlap=128)[0]  #Calculamos el espectograma
    
    espectograma = 10*np.log10(espectograma)  #Le hacemos la transformada logarítmica 
    espectograma[espectograma==-np.inf]=0   #Cambiamos los valores a infinito por ceros
    return espectograma
    

def huella(muestreo, tipohash):
    """
    @brief Esta función crea la huella digital utilizando el resto de métodos 
    de espectograma, picos y hashes.
    

    @param muestreo  Array de bytes correspondientes a un archivo de audio
    @param tipohash Algoritmo que se quiere aplicar al hashing
    @return Array correspondiente a la huella digital
    """
  
    esp=espectograma(muestreo)  #Se calcula el espectograma
    
    frecuencias, tiempos =picos(esp) #Se obtienen la lista de picos de frecuencia y sus tiempos
    
    huella= hashes(frecuencias,tiempos, tipohash) #Se calcula la huella aplicando hashes a los picos de frecuencia
    
    return huella #Se retorna la huella
    
def huella_grabadora(muestreo, tipohash):
    """
    @brief Esta función crea la huella digital utilizando el resto de métodos 
    de espectograma, picos y hashes.
    

    @param muestreo  Array de bytes correspondientes a un archivo de audio
    @param tipohash Algoritmo que se quiere aplicar al hashing
    @return Array correspondiente a la huella digital
    """
  
    esp=espectograma_grabadora(muestreo)  #Se calcula el espectograma
    
    frecuencias, tiempos =picos(esp) #Se obtienen la lista de picos de frecuencia y sus tiempos
    
    huella= hashes(frecuencias,tiempos, tipohash) #Se calcula la huella aplicando hashes a los picos de frecuencia
    
    return huella #Se retorna la huella
    



  #
                                #REPRESENTACION EN PANTALLA DEL ESPECTOGRAMA  
   # a,b,c=mlab.specgram(muestreo,NFFT=tamanyo_fft, Fs=freq_muestreo,window=mlab.window_hanning, noverlap=int(tamanyo_fft*ratio_overlap))
    #plot.figure(figsize=(10, 6))
    #plot.imshow(10 * np.log10(a), aspect='auto', extent=[b.min(), b.max(), c.min(), c.max()], origin='lower')
    #plot.colorbar(label="Densidad espectral de potencia (dB)")
    #plot.xlabel("Ventanas (a traves del tiempo)")
    #plot.ylabel("Frecuencia (Hz)")
    #plot.title("Espectrograma")
    #plot.show()
#