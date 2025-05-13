"""
@file bd.py
@brief Módulo de gestión de base de atos
@details Este archivo contiene las funciones necesarias para la gestión de los 
almacenes de datos del sistema y su explotación.
"""

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from huella import huella
import math

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

db= client["MusicFingerprints"]
huellas= db["Fingerprints"]
metadatos=db["Metadatos"]


def almacenar_huellas(nombre, huella):
    """
    @brief Esta función genera una entrada en la colección de huellas
    

    @param nombre String corespondiente al título de la canción
    @param huella Array de huellas de la canción indicada
    @return None 
    """
    aux={"nombre": nombre, "huella": huella}
    huellas.insert_one(aux)
    
def almacenar_metadatos(nombre, artista, anyo, album):
    """
    @brief Esta función genera una entrada en la colección de metadatos
    

    @param nombre String corespondiente al título de la canción
    @param artista String correspondiente al nombre del artista
    @param anyo String correspondiente al año
    @param album String correspondiente al album
    @return None 
    """
    aux={"nombre": nombre, "artista": artista, "anyo": anyo, "album": album}
    metadatos.insert_one(aux)

def cargar_huellas():
    """
    @brief Esta función devuelve todas las entradas de la base de datos
    
    @return Lista de huellas 
    """
    lista=list(huellas.find())
    return lista

def cargar_huellas_restringida(array):
    """
    @brief Esta función devuelve las entradas de la base de datos que tengan al menos 
    una coincidencia con un array
    
    @param array Array de huellas con el que se quiere comparar
    
    @return Lista de huellas 
    """
    lista=list(huellas.find({"huella": {"$in": array}}))
    return lista

def cargar_huellas_restringido_a_porcentaje(array, porcentaje=10):
    """
    @brief Esta función devuelve las entradas de la base de datos que tengan un porcentaje 
    de coincidencia con un array
    
    @param array Array de huellas con el que se quiere comparar
    @param porcentaje Porcentaje de coincidencia al que se quiere restringir la carga de BD,
    por defecto 0.1
    
    @return Lista de huellas 
    """
    
    #minimo_coincidencia = math.ceil(len(array)*porcentaje)
    
    lista=huellas.aggregate([{
       
            "$addFields": {
                "intersection": { "$setIntersection": ["$huella", array] },
                "originalSize": { "$size": "$huella" }
            }
        },
        {
      
            "$addFields": {
                "matchPercentage": {
                    "$multiply": [
                        { "$divide": [{ "$size": "$intersection" }, "$originalSize"] },
                        100
                    ]
                }
            }
        },
        {
        
            "$match": {
                "matchPercentage": { "$gte": porcentaje }
            }
        },
        {
        
            "$project": {
                "matchPercentage": 0 
            }
        }
            ])
    
    return lista
    
    


def obtener_metadatos(nombre):
    """
    @brief Esta función busca en la colección de metadatos el nombre indicado y 
    muestra por pantalla todos sus metadatos
    
    @param nombre String correspondiente al nombre de una canción
    
    @return None
    """
    cancion=metadatos.find_one({"nombre":nombre})
    if cancion:
        # Mostrar el artista, album y nombre de la cancion
        print(f"Nombre de la Cancion: {cancion['nombre']}")
        print(f"Artista: {cancion['artista']}")
        print(f"Album: {cancion['album']}")
        print(f"Fecha: {cancion['anyo']}")
    else:
        print("Error al obtener metadatos.")

    
def limpiar_bd():
    """
    @brief Esta función borra todas las entradas de la base de datos.
    
    @return None
    """
    metadatos.delete_many({})
    huellas.delete_many({})
    print('Se ha limpiado la base de datos de huellas y metadatos')




