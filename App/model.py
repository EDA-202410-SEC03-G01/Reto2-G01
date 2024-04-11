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
from tabulate import tabulate 
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_catalog(size, maptype, chargefactor):
    catalog = {'map_countries': None,
               'jobs' : None,}
    
    catalog['map_countries'] = mp.newMap(200, maptype=maptype, loadfactor=chargefactor,
                                         cmpfunction=compare_countries)
    
    catalog['jobs'] = lt.newList(datastructure='ARRAY_LIST')
    
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
    list_jobs = catalog['jobs']
    
    lt.addLast(list_jobs, job)
    return catalog
def jobs_size(catalog):
    return lt.size(catalog)

def add_map_countries(catalog,job):

    mapa = catalog['map_countries']
    
    #Verificar si existe la llave en el mapa
    
    if mp.contains(mapa, job["country_code"]):
        entry = mp.get(mapa, job["country_code"]) # Retorna la pareja llave valor con la llave dada
        country_info = me.getValue(entry) # Me obtiene la estructura de datos de la pareja llave valor
        update_country_info(country_info, job)
    else:
        country_info = new_country_info(job["country_code"])
        update_country_info(country_info, job)
        mp.put(mapa, job["country_code"], country_info)
        
    return catalog

def update_country_info(country_info, job):
    list_jobs = country_info['list_jobs']
    map_by_experience = country_info['map_by_experience']
    
    #Agregar la oferta de trabajo a la lista de trabajos
    lt.addLast(list_jobs, job)
    
    #Agregar la oferta de trabajo al mapa de trabajos por experiencia
    if mp.contains(map_by_experience, job['experience_level']):
        entry = mp.get(map_by_experience, job['experience_level'])
        jobs_by_experience = me.getValue(entry)
        lt.addLast(jobs_by_experience, job)

    else:
        jobs_by_experience = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(jobs_by_experience, job)
        mp.put(map_by_experience, job['experience_level'], jobs_by_experience)
        
    return country_info

def new_country_info(country_code):
    
    country_info = {
        'country_code' : country_code,
        'list_jobs' : None, # Lista con  las ofertas de trabajo publicadas en el pais
        'map_by_experience' : None,
    }
    
    country_info['list_jobs'] = lt.newList(datastructure='ARRAY_LIST')
    country_info['map_by_experience'] = mp.newMap(3, maptype='PROBING', loadfactor=0.5)
    
    return country_info
    

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


def req_1(catalog, country_code, experience_level, amount):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    
    answer = obtain_list_jobs_by_countryandexperience(catalog, country_code, experience_level)  # O(1) -> Obtenemos la lista
    
    if answer is None:
        return None
    
    amount_jobs_country = answer[0]
    amount_jobs_by_experience = answer[1]
    list_jobs_by_experience = answer[2]
    
    merg.sort(list_jobs_by_experience, compare_by_date) # O(nlogn) -> Ordenamos la lista de ofertas de trabajo por fecha de publicación siendo n 1
    
    if amount > amount_jobs_by_experience:
        amount = amount_jobs_by_experience

    answer_list = lt.subList(list_jobs_by_experience, 1, amount)
    
    table_jobs = tabulate_jobs_rq1(answer_list)
    
    return amount_jobs_country, amount_jobs_by_experience, table_jobs

def obtain_list_jobs_by_countryandexperience(catalog, country_code, experience_level):
    
    map_countries = catalog['map_countries']
    amount_jobs_country = 0
    amount_jobs_by_experience = 0
    
    if mp.contains(map_countries, country_code):
        entry = mp.get(map_countries, country_code)
        country_info = me.getValue(entry)
    else:
        return None
    
    amount_jobs_country = lt.size(country_info['list_jobs']) # Obtenemos el total de ofertas de trabajo publicadas en el pais
    map_by_experience = country_info['map_by_experience']
    
    if mp.contains(map_by_experience, experience_level):
        entry = mp.get(map_by_experience, experience_level)
        list_jobs_by_experience = me.getValue(entry)
    else:
        return None
    
    amount_jobs_by_experience = lt.size(list_jobs_by_experience) # Obtenemos el total de ofertas de trabajo publicadas en el pais por nivel de experiencia
    
    
    return amount_jobs_country, amount_jobs_by_experience, list_jobs_by_experience
    
        
def tabulate_jobs_rq1(list_jobs):
    
    headers = ['Fecha', 'Titulo', 'Empresa', 'Nivel', 'Pais', 'Ciudad', 'Tamanio Empresa', 'Ubicacion', 'Ukranians']
    
    table = []
    
    for job in lt.iterator(list_jobs):
        row = [job['published_at'], job['title'], job['company_name'], job['experience_level'], job['country_code'], job['city'], job['company_size'], job['workplace_type'], job['open_to_hire_ukrainians']
              ]
        table.append(row)
        
    return tabulate(table, headers, tablefmt='grid')
    
    
    


def req_2(catalog,N,empresa,ciudad):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    mapa_ofertas= mp.newMap(7000000,
                            maptype="CHAINING",
                            loadfactor=0.8,
                            cmpfunction=mp.compare_elements)
    
    def agregar_oferta(mapa,oferta):
        llave=(oferta["company_name"],oferta["city"])
        if llave not in mapa:
            mapa[llave]=[]
            lt.addLast(mapa,oferta)
            
    def filtrar_ofertas(mapa, empresa, ciudad):
        llave=(empresa,ciudad)
        if llave in mapa:
            return mapa[llave]
        else:
            return[]
    def ordenar_ofertas(ofertas):
        return sorted(ofertas, key=lambda x: datetime.strptime(x["published_at"],"%Y-%m-%d"),reverse=True)
    def limitar_ofertas(ofertas):
        if len(ofertas)>10:
            return ofertas[:5]+ ofertas[-5:]
        else:
            return ofertas 


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


# Funciones utilizadas para comparar elementos dentro de un TAD

def compare_countries(country1, entry):
    
    if country1 == me.getKey(entry):
        return 0
    elif country1 < me.getKey(entry):
        return -1
    else:
        return 1


def compare_elements(job1, job2):
    """
    Compara dos ofertas de trabajo por fecha de publicación.
    """
    print(job1,job2)

    if job1["published_at"] == job2["published_at"]:
        return 0

    elif job1["published_at"] < job2["published_at"]:
        return -1
    else:
        return 1
    
# Funciones de ordenamiento

def compare_by_date(job1, job2):
    """
    Compara dos ofertas de trabajo por fecha de publicación.
    """
    return job1["published_at"] > job2["published_at"]

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
