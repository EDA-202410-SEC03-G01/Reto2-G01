"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
from datetime import datetime # importar para las fechas 
from datetime import timedelta
from tabulate import tabulate 
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_catalog():
    catalog = {'jobs': None,
               'skills': None,
               'employment_type': None,
               "multilocation": None } 
    catalog["jobs"]= lt.newList("ARRAY_LIST")
    catalog["skills"]=lt.newList("ARRAY_LIST")
    catalog["employment_type"]=lt.newList("ARRAY_LIST")
    catalog["multilocation"]=lt.newList("ARRAY_LIST")
    #mapa_ofertas 
    return catalog
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    # Crea y devuelve un diccionario vacio con las claves para despues almacenar la información 
    


# Funciones para agregar informacion al modelo
# JOBS, con esta función obtenemos el total de ofertas de trabajo publicadas 

def add_job(catalog, job):
    lt.addLast(catalog, job)
    return catalog
def jobs_size(catalog):
    return lt.size(catalog)

#def add_mapa_job(catalog,job):
    #si esta o no 
    # si esta, se actualiza, si no se crea 
    #utilizar las llaves de city ,company name 

# SKILLS total de habilidades 
def add_skill(catalog, skill):
    lt.addLast(catalog, skill)
    return catalog
def skills_size(catalog):
    return lt.size(catalog)

# EMPLOYMENT TYPE, total de tipos de contratacion disponibles 
def add_employment_type(catalog, employment_type):
    lt.addLast(catalog, employment_type)
    return catalog
def employment_type_size(catalog):
    return lt.size(catalog)

# MULTILOCATIONS, total ubicaciones de la empresa que publica la oferta de trabajo. 
def add_multilocation(catalog ,multilocation):
    lt.addLast(catalog, multilocation)
    return catalog 
def multilocation_size(catalog):
    return lt.size(catalog)

#Funciones primeros y ultimos 3
def primeros_tres(catalog):
    job_Newlist= lt.subList(sa.sort(catalog["jobs"],compare_by_fecha),1,3)
    skills_Newlist= lt.subList(catalog["skills"],1,3)
    employment_type_Newlist= lt.subList(catalog["employment_type"],1,3)
    return job_Newlist,skills_Newlist,employment_type_Newlist

def ultimos_tres(catalog):
    job_Newlist= lt.subList(catalog["jobs"],lt.size(catalog["jobs"])-2,3)
    skills_Newlist= lt.subList(catalog["skills"],lt.size(catalog["skills"])-2,3)
    employment_type_Newlist= lt.subList(catalog["employment_types"],lt.size(catalog["employment_type"])-2,3)
    return job_Newlist,skills_Newlist,employment_type_Newlist




def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    pass


# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
