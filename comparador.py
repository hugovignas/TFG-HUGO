# -*- coding: utf-8 -*-
"""
@file comparador.py
@brief Módulo de comparativa de conjuntos
@details Este archivo contiene las funciones necesarias para la obtención de datos 
por parte de la base de datos para realizar la comparativa con fragmentos de audio
"""
import numpy as np
import bd
import huella
import grabadora
import array


def buscar_coincidencias_hashes(array1, array2):
    """
    @brief Esta función obtiene la intersección entre dos arrays de datos.
    

    @param array1 Primer array a comparar
    @param array2 Segundo array a comparar
    @return Array de bytes de audio
    """
    arr1 = np.array(array1)
    arr2 = np.array(array2)

    # Encontrar la intersección entre ambos arrays
    coincidencias = np.intersect1d(arr1, arr2)
    
    
    return coincidencias


def comparador(cancion, tipoalgoritmo, porcentaje=10):
    """
    @brief Esta función obtiene una muestra, llama a la creación de huella y la compara con la Base de Datos,
    mostrando en pantalla los resultados. Sólo carga en memoria aquellas huellas 
    que tienen un porcentaje de similitud.
    

    @param cancion Muestra a comparar
    @param tipoalgoritmo Hash que se quiere aplicar a la comparación
    @param porcentaje Porcentaje mínimo de similitud para extraer de la base de datos
    @return None
    """
    
    audio=grabadora.capturadora_mp3(cancion)
    h=huella.huella(audio,tipoalgoritmo)

    array_huella=np.array(list(h))
    array_huella=array_huella.tolist()


    huellas_bd=bd.cargar_huellas_restringido_a_porcentaje(array_huella)
    if not huellas_bd:
        print("No se han encontrado coincidencias en la base de datos.")
        
    for objeto in huellas_bd:
        aux=buscar_coincidencias_hashes(array_huella, objeto['huella'])
        
        porcentaje=len(aux)/len(array_huella)
        if porcentaje>0.1:
            print("\n-------------")
            bd.obtener_metadatos(objeto['nombre'])
            print(f"Hashes coincidentes: {len(aux)}")
            print(f"Tasa de coincidencia:{porcentaje}")
  
def comparador_al_menos_una_coincidencia(tipoalgoritmo, cancion=None):
    """
    @brief Esta función obtiene una muestra, llama a la creación de huella y la compara 
    con la Base de Datos, mostrando en pantalla los resultados. Sólo carga en memoria 
    aquellas huellas que tienen al menos una coincidencia con la muestra.
    

    @param cancion Muestra a comparar
    @param tipoalgoritmo Hash que se quiere aplicar a la comparación
    @return None
    """
        
    audio=grabadora.grabadora()
    h=huella.huella_grabadora(audio,tipoalgoritmo)

    array_huella=np.array(list(h))
    array_huella=array_huella.tolist()

    huellas_bd=bd.cargar_huellas_restringida(array_huella)
    print("Se han encontrado las siguientes coincidencias de base de datos:")
    for objeto in huellas_bd:
        aux=buscar_coincidencias_hashes(array_huella, objeto['huella'])
        
        porcentaje=len(aux)/len(array_huella)
        if porcentaje>0.001:
            bd.obtener_metadatos(objeto['nombre'])
            print(f"Hashes coincidentes: {len(aux)}")
            print(f"Tasa de coincidencia:{porcentaje}")

def comparador_bd_completa(cancion, tipoalgoritmo):
    """
    @brief Esta función obtiene una muestra, llama a la creación de huella y la compara
    con la Base de Datos, mostrando en pantalla los resultados. Se carga toda la base de 
    datos en memoria. Solo recomendable para entorno de pruebas con poca cantidad de huellas.
    

    @param cancion Muestra a comparar
    @param tipoalgoritmo Hash que se quiere aplicar a la comparación
    @return None
    """
    
    audio=grabadora.capturadora_mp3(cancion)
    h=huella.huella(audio,tipoalgoritmo)

    array_huella=np.array(list(h))
    array_huella=array_huella.tolist()

    huellas_bd=bd.cargar_huellas()
    
    for objeto in huellas_bd:
        aux=buscar_coincidencias_hashes(array_huella, objeto['huella'])
        
        porcentaje=len(aux)/len(array_huella)
        if porcentaje>0.05:
            print("\n-------------")
            bd.obtener_metadatos(objeto['nombre'])
            print(f"Hashes coincidentes: {len(aux)}")
            print(f"Tasa de coincidencia:{porcentaje}")