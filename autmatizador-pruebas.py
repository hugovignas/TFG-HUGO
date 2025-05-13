import huella
import bd
import grabadora
import entrenador
import comparador
import os
import hashlib
import time  

"""
tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta5", "MD5")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 5 elementos para MD5. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta5","SHA-1")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 5 elementos para SHA-1. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta5","SHA-256")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 5 elementos para SHA-256. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")
bd.limpiar_bd()

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta10","MD5")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 10 elementos para MD5. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta10","SHA-1")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 10 elementos para SHA-1. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta10","SHA-256")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 10 elementos para SHA-256. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")
bd.limpiar_bd()

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta15","MD5")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 15 elementos para MD5. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta15","SHA-1")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 15 elementos para SHA-1. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta15","SHA-256")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 15 elementos para SHA-256. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")
bd.limpiar_bd()

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta20","MD5")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 20 elementos para MD5. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta20","SHA-1")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 20 elementos para SHA-1. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta20","SHA-256")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 20 elementos para SHA-256. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")
bd.limpiar_bd
"""

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta25","MD5")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 25 elementos para MD5. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta25","SHA-1")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 25 elementos para SHA-1. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta25","SHA-256")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 25 elementos para SHA-256. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")
bd.limpiar_bd

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta30","MD5")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 30 elementos para MD5. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta30","SHA-1")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 30 elementos para SHA-1. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta30","SHA-256")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 30 elementos para SHA-256. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")
bd.limpiar_bd

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta35","MD5")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 35 elementos para MD5. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta35","SHA-1")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 35 elementos para SHA-1. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta35","SHA-256")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 35 elementos para SHA-256. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")
bd.limpiar_bd

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta50","MD5")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 50 elementos para MD5. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta50","SHA-1")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 50 elementos para SHA-1. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta50","SHA-256")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 50 elementos para SHA-256. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")
bd.limpiar_bd

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta60","MD5")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 60 elementos para MD5. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta60","SHA-1")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 60 elementos para SHA-1. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")

tiempo0 = time.time()
entrenador.entrenar_directorio("C:/Users/XV258VW/OneDrive - EY/Desktop/PROYECTO SHAZAM/PROYECTO/MusicaPruebas/Carpeta60","SHA-256")
tiempo1 = time.time()
print(f"\nEntrenamiento completado con 60 elementos para SHA-256. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")
print("\n\n\n")
bd.limpiar_bd