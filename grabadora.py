# -*- coding: utf-8 -*-
"""
@file grabadora.py
@brief Módulo de conversión a bytes de audio
@details Este archivo contiene las funciones necesarias para la grabación de audio 
vía micrófono y la obtención de bytes a aprtir de archivos MP3
"""
from pydub import AudioSegment
import sounddevice as sd
import numpy as np
from scipy.fft import fft
from io import BytesIO
from scipy.io.wavfile import write



def grabadora(duracion=40):
    """
    @brief Esta función accede al micrófono del sistema y realiza una 
    grabación de la duración indicada.
    

    @param duracion  Entero indicador del tiempo que se quiere grabar, por defecto 10
    @return Array de bytes de audio
    """
    print("Grabando...")
    fs = 44100
    frames = int(duracion * fs)
    audio = sd.rec(frames, samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    print("Se ha terminado la grabacion...")
    write("audio_grabado.wav", fs, audio)
    print("Audio guardado como 'audio_grabado.wav'")
    return audio.flatten()

def capturadora(ruta):
    """
    @brief Esta función pasa directamente un archivo a bytes
    

    @param ruta  string con la ruta de un archivo
    @return Array de bytes de audio
    """
    with open(ruta, 'rb') as f:
        audio=f.read()
    return audio

 
def capturadora_mp3(ruta):
        """
        @brief Esta función captura el array de bytes de un archivo MP3 usando AudioSegment
    
        
        @param ruta  string con la ruta de un archivo
        @return Array de bytes de audio
        """    
        
        archivo= AudioSegment.from_mp3(ruta)
        
        audio=np.array(archivo.get_array_of_samples())
        return audio

