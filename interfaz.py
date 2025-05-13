# -*- coding: utf-8 -*-
"""
@file interfaz.py
@brief Módulo de interfaz del sistema
@details  Este archivo se corresponde con la interfaz del sistema, en el que interactúan el resto de módulos y métodos
"""
import huella
import bd
import grabadora
import entrenador
import comparador
import os
import hashlib
import time                                                                                        


hash_db = {"algoritmo": None}

def seleccionar_algoritmo():
    """
    @brief Breve función para seleccionar el algoritmo dentro de la interfaz
    @return El nombre del algoritmo seleccionado o None si no es válido.
    """
    print("\n--- Selección de Algoritmo de Hash ---\n")
    print("1. MD5")
    print("2. SHA-1")
    print("3. SHA-256\n")

    algoritmo_opcion = input("Introduce el número de la opción: ").strip()

    if algoritmo_opcion == "1":
        return "MD5"
    elif algoritmo_opcion == "2":
        return "SHA-1"
    elif algoritmo_opcion == "3":
        return "SHA-256"
    else:
        print("Error 007: Opción de hash no válida.")
        return None

def main():
    while True:
        print("\n--- Menú Principal ---\n")
        print("¿Qué quieres hacer?")
        print("1. Entrenar")
        print("2. Comparar")
        print("0. Salir\n")

        opcion = input("Introduce el número de la opción: ").strip()
        if opcion == "0":
            print("Saliendo del programa.")
            break

        algoritmo = seleccionar_algoritmo()
        if algoritmo is None:
            if not reintentar():
                break
            continue

        if opcion == "2":  # Comparar
            print("\n--- Modo de Comparación ---\n")
            print("1. Usar archivo")
            print("2. Usar grabadora")
            print("0. Volver al menú principal\n")

            modo_comparacion = input("Introduce el número de la opción: ").strip()
            if modo_comparacion == "1":
                ruta_archivo = input("Introduce la ruta del archivo para comparar: ").strip()
                
                if not os.path.exists(ruta_archivo):
                    print("\nError 001: No se encuentra el archivo.\n")
                elif not ruta_archivo.lower().endswith(".mp3"):
                    print("\nError 002: El archivo no es de tipo MP3.\n")
                else:
                    comparador.comparador(ruta_archivo, algoritmo)
            
            elif modo_comparacion == "2":
                comparador.comparador_al_menos_una_coincidencia(algoritmo)
            
            elif modo_comparacion == "0":
                continue

            else:
                print("\nError 005: Modo de comparación no válido.")
                if not reintentar():
                    break
                continue

            if not finalizar_o_volver():
                break

        elif opcion == "1":  # Entrenar
            print("\n--- Modo de Entrenamiento ---\n")
            if hash_db["algoritmo"] == algoritmo:
                print(f"Algoritmo {algoritmo} ya configurado. Eligiendo modo de entrenamiento.\n")
            else:
                print(f"Algoritmo {algoritmo} no coincide con el actual. Limpiando y reconfigurando.\n")
                hash_db["algoritmo"] = algoritmo

            print("1. Entrenar un directorio específico")
            print("2. Entrenar una sola canción")
            print("3. Entrenar el directorio de pruebas")
            print("0. Volver al menú principal\n")

            modo_entrenamiento = input("Introduce el número de la opción: ").strip()
            if modo_entrenamiento == "1":
                ruta_directorio = input("Introduce la ruta del directorio: ").strip()
                if not os.path.isdir(ruta_directorio):
                    print("\nError 006: No se encuentra el directorio.\n")
                else:
                    print(f"Entrenamiento en directorio {ruta_directorio} completado.")

            elif modo_entrenamiento == "2":
                ruta_cancion = input("Introduce la ruta del archivo MP3: ").strip()
                if not os.path.exists(ruta_cancion):
                    print("\nError 001: No se encuentra el archivo.\n")
                elif not ruta_cancion.lower().endswith(".mp3"):
                    print("\nError 002: El archivo no es de tipo MP3.\n")
                else:
                    #bd.limpiar_bd()
                    tiempo0 = time.time()
                    entrenador.entrenar_archivo(ruta_cancion, algoritmo)
                    tiempo1 = time.time()
                    print(f"\nEntrenamiento completado en el directorio de pruebas. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")

            elif modo_entrenamiento == "3":
                tiempo0 = time.time()
                entrenador.entrenar_directorio_pruebas(algoritmo)
                tiempo1 = time.time()
                print(f"\nEntrenamiento completado en el directorio de pruebas. Tiempo transcurrido: {tiempo1 - tiempo0:.2f} segundos.")

            elif modo_entrenamiento == "0":
                continue
            else:
                print("Error 004: Modo de entrenamiento no válido.")
                if not reintentar():
                    break
                continue

            if not finalizar_o_volver():
                break

        else:
            print("Error 003:Opción no válida. Por favor, elige '1' o '2'.")

def reintentar():
    """
    Ofrece la opción de volver al menú principal o salir en caso de error.
    """
    print("\n¿Deseas intentar de nuevo? (s/n)")
    return input().strip().lower() == "s"

def finalizar_o_volver():
    """
    Ofrece la opción de volver al menú principal o salir después de completar una operación.
    """
    print("\n¿Deseas volver al menú principal o salir? (m/s)")
    return input().strip().lower() == "m"

if __name__ == "__main__":
    main()
