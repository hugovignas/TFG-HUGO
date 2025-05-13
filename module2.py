import huella
import bd
import grabadora
import entrenador
import comparador
import os
import hashlib
import time     

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta15","MD5")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 15 elementos para MD5. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")

