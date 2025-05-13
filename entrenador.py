# -*- coding: utf-8 -*-
"""
@file entrenador.py
@brief Módulo de entrenamiento de la BD del sistema
@details Este archivo contiene las funciones necesarias para la obtención de metadatos y 
huellas digitales de archivos de audio con el objetivo de alimentar la base de datos del proyecto.
"""
import hashlib
import os
from pydub import AudioSegment
from pydub.utils import audioop
import numpy as np
from grabadora import capturadora_mp3, grabadora
import huella
import bd
import comparador
import array
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TDRC, TALB

#nombre_cancion='musica/Camaron de la Isla-Potro de Rabia y Miel.mp3'


def almacenar_cancion_entrenador(ruta,tipohash):
    """
    @brief Esta función obtiene los metadatos de un archivo esepecificado y realiza la llamada al 
    generador de huellas según el tipo de hash especificado.Seguidamente los almacena en su correspondiente 
    colección de datos de la base de datos.
    

    @param ruta String correspondiente a la ruta de un archivo  
    @param tipohash Algoritmo que se quiere aplicar al hashing
    @return None 
    """
    
    cancion=capturadora_mp3(ruta)  #Se obtiene el muestreo del archivo MP3
    h=huella.huella(cancion,tipohash) #Se calcula la huella del archivo
    
    try:
        # Intenta leer los metadatos
        metadatos = MP3(ruta, ID3=ID3)
        titulo = str(metadatos["TIT2"].text[0])  # Título
        artista = str(metadatos["TPE1"].text[0])  # Artista
        anyo = str(metadatos["TDRC"].text[0])    # Año
        album = str(metadatos["TALB"].text[0])  # Álbum
    except:
        print("Error 008: Metadatos de archivo erróneo.")

    
    bd.almacenar_metadatos(titulo,artista,anyo,album)  #Se almacenan los metadatos 

    array_huella=np.array(list(h))
    array_huella=array_huella.tolist()
    bd.almacenar_huellas(titulo, array_huella) #Se almacena la huella como una lista de datos
  


#bd.limpiar_bd()

def entrenar_directorio_pruebas(tipohash):
    """
    @brief Esta función automatiza la llamada de la función de entrenamiento para un 
    directorio de pruebas predefinido.
    

    @param tipohash Algoritmo que se quiere aplicar al hashing
    @return None 
    """

    pwd = os.getcwd() 
    directorio = os.path.join(pwd, 'musica') 

    if os.path.exists(directorio):
        for nombre_archivo in os.listdir(directorio):
       
           ruta_archivo = os.path.join(directorio, nombre_archivo)
       
        
           almacenar_cancion_entrenador(ruta_archivo,tipohash)
    else:
       print("La carpeta 'musica' no existe en el directorio del proyecto.")


def entrenar_directorio(directorio, tipohash):
    """
    @brief Esta función automatiza la llamada de la función de entrenamiento 
    para un directorio especificado.
    

    @param directorio String correspondiente a la ruta del directorio que se quiere procesar
    @param tipohash Algoritmo que se quiere aplicar al hashing
    @return None 
    """
    if os.path.exists(directorio):
        for nombre_archivo in os.listdir(directorio):
       
           ruta_archivo = os.path.join(directorio, nombre_archivo)
       
        
           almacenar_cancion_entrenador(ruta_archivo,tipohash)
    else:
       print("La carpeta especificada no se encuentra")

def entrenar_archivo(ruta_archivo,tipohash):
    """
    @brief Esta función automatiza la llamada de la función de entrenamiento para un archivo 
    específico. Se realiza la comprobación de existencia del archivo.
    

    @param ruta_archivo String correspondiente a la ruta del archivo que se quiere procesar; 
    @param tipohash Algoritmo que se quiere aplicar al hashing
    @return None 
    """
    if os.path.exists(ruta_archivo):
        almacenar_cancion_entrenador(ruta_archivo,tipohash)
    else:
        print("No se encuentra el archivo especificado.")
