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
 """

import config as cf
import model
import time
import csv
import tracemalloc
from datetime import datetime

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def measure_time(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        total = time.time() - start
        print(total, 'segundos demorados' )
        return result

    return wrapper


def new_controller(size, map_type, charge_factor):
    control = {}# Este diccionario será utilizado para almacenar el modelo del sistema.
    control['model'] = model.new_catalog(size, map_type, charge_factor)
    return control
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos



# Funciones para la carga de datos

def load_data(control,percent):
    """
    Carga los datos del reto
    
    """
    
    
    print("Cargando información")
    
    catalog= control["model"]
    
    
    
    jobs_size = load_jobs(catalog,percent)
    
    return control
    # TODO: Realizar la carga de datos
    
def load_jobs(catalog, percent):
    jobs_file = cf.data_dir + percent +"jobs.csv" # Selecciona el archivo con el porcentaje de datos a cargar S
    
    input_file = csv.DictReader(open(jobs_file, encoding='utf-8'),delimiter=";") # Obejto Iterador que permite leer el archivo
    
    for job in input_file:
        # 2022-04-14T17:24:00.000Z
        job['published_at'] = datetime.strptime(job['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
        model.add_job(catalog, job)
        model.add_map_countries(catalog,job)
    return model.jobs_size(catalog['jobs'])

def load_skills(catalog, percent):
    skills_file = cf.data_dir + percent+'-por-skills.csv'
    input_file = csv.DictReader(open(skills_file, encoding='utf-8'))
    for skill in input_file:
        model.add_skill(catalog['skills'], skill)
    return model.skills_size(catalog['skills'])

def load_employment_types(catalog, percent):
    employment_types_file = cf.data_dir + percent+'-por-employments_types.csv'
    input_file = csv.DictReader(open(employment_types_file, encoding='utf-8'), delimiter=";")
    for employment_type in input_file:
        model.add_employment_type(catalog['employment_type'], employment_type)
    return model.employment_type_size(catalog['employment_type'])

def load_multilocations(catalog, percent):
    multilocations_file = cf.data_dir + percent+'-por-multilocations.csv'
    input_file = csv.DictReader(open(multilocations_file, encoding='utf-8'))
    for multilocation in input_file:
        model.add_employment_type(catalog['multilocation'], multilocation)
    return model.employment_type_size(catalog['multilocation'])
# tres primeros y tres ultimos 

def primeros_tres(control):
    return model.primeros_tres(control["model"])



def ultimos_tres(control):
    return model.ultimos_tres(control["model"])



# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass

@measure_time
def req_1(control, country_code, experience_level, amount):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    
    return model.req_1(control["model"], country_code, experience_level, amount)


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
