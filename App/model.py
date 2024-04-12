""" 
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
               'jobs' : None,
               'map_companies' : None,
               'map_cities': None}
    
    catalog['map_countries'] = mp.newMap(85, maptype=maptype, loadfactor=chargefactor,
                                         cmpfunction=compare_countries)
    
    catalog['map_companies'] = mp.newMap(6500, maptype=maptype, loadfactor=chargefactor, cmpfunction=compare_countries)
    
    catalog['map_cities'] = mp.newMap(1500, maptype=maptype, loadfactor=chargefactor, cmpfunction=compare_countries)
    catalog['map_employments'] = mp.newMap(204000, maptype=maptype, loadfactor=chargefactor, cmpfunction=compare_countries)
    catalog['map_skills'] = mp.newMap(204000, maptype=maptype, loadfactor=chargefactor, cmpfunction=compare_countries)
    catalog['jobs'] = lt.newList(datastructure='ARRAY_LIST')
    
    return catalog
    
def add_job(catalog, job):
    
    list_josbs = catalog['jobs']
    lt.addLast(list_josbs, job)
    return catalog

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
    
def add_map_companies(catalog, job):
    """
    Agrega una oferta de trabajo al mapa de paises
    """
    
    mapa = catalog['map_companies']
    
    if mp.contains(mapa, job['company_name']):
        entry = mp.get(mapa, job['company_name'])
        company_info = me.getValue(entry)
        update_company_info(company_info, job)
    else:
        company_info = new_company_info(job['company_name'])
        update_company_info(company_info, job)
        mp.put(mapa, job['company_name'], company_info)
        
    return catalog

def update_company_info(company_info, job):
    list_jobs = company_info['list_jobs']
    map_by_experience = company_info['map_by_experience']
    
    lt.addLast(list_jobs, job)
    
    if mp.contains(map_by_experience, job['experience_level']):
        entry = mp.get(map_by_experience, job['experience_level'])
        jobs_by_experience = me.getValue(entry)
        lt.addLast(jobs_by_experience, job)
    else:
        jobs_by_experience = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(jobs_by_experience, job)
        mp.put(map_by_experience, job['experience_level'], jobs_by_experience)
        
    return company_info

def new_company_info(company_name):
    company_info = {
        'company_name' : company_name,
        'list_jobs' : None, # Lista con  las ofertas de trabajo publicadas en la compañia
        'map_by_experience' : None,
    }
    
    company_info['list_jobs'] = lt.newList(datastructure='ARRAY_LIST')
    company_info['map_by_experience'] = mp.newMap(3, maptype='PROBING', loadfactor=0.5)
    
    return company_info
# EMPLOYMENT TYPE, total de tipos de contratacion disponibles 
def add_employment(catalog, employment):
    employment['salary_from'] = int(employment['salary_from']) if employment['salary_from'] != '' else ''
    employment['salary_to'] = int(employment['salary_to']) if employment['salary_to'] != '' else ''
    map_employments = catalog['map_employments']
    
    if mp.contains(map_employments, employment['id']):
        entry = me.getValue(mp.get(map_employments, employment['id']))
        entry[employment['type']] = employment
        mp.put(map_employments, employment['id'], entry)
    else:
        entry = {}
        entry[employment['type']] = employment
        mp.put(map_employments, employment['id'], entry)
    return catalog

def add_map_cities(catalog, job):
    """
    Agrega una oferta de trabajo al mapa de ciudades
    """
    mapa = catalog['map_cities']
    
    if mp.contains(mapa, job['city']):
        entry = mp.get(mapa, job['city'])
        city_info = me.getValue(entry)
        update_city_info(city_info, job)
    else:
        city_info = new_city_info(job['city'])
        update_city_info(city_info, job)
        mp.put(mapa, job['city'], city_info)
        
    return catalog

def update_city_info(city_info, job):
    list_jobs = city_info['list_jobs']
    map_by_year = city_info['map_by_year']
    
    lt.addLast(list_jobs, job)
    
    if mp.contains(map_by_year, job['published_at'].year):
        entry = mp.get(map_by_year, job['published_at'].year)
        year_info = me.getValue(entry)
        update_year_info(year_info, job)
    else:
        year_info = new_year_info(job['published_at'].year)
        update_year_info(year_info, job)
        mp.put(map_by_year, job['published_at'].year, year_info)
        
    return city_info

def update_year_info(year_info, job):
    list_jobs = year_info['list_jobs']
    map_by_experience = year_info['map_by_experience']
    
    lt.addLast(list_jobs, job)
    
    if mp.contains(map_by_experience, job['experience_level']):
        entry = mp.get(map_by_experience, job['experience_level'])
        jobs_by_experience = me.getValue(entry)
        lt.addLast(jobs_by_experience, job)
    else:
        jobs_by_experience = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(jobs_by_experience, job)
        mp.put(map_by_experience, job['experience_level'], jobs_by_experience)
        
    return year_info


def new_city_info(city):
    
    city_info = {
        'city' : city,
        'list_jobs' : None, # Lista con  las ofertas de trabajo publicadas en la ciudad
        'map_by_year' : None,
    }
    
    city_info['list_jobs'] = lt.newList(datastructure='ARRAY_LIST')
    city_info['map_by_year'] = mp.newMap(2, maptype='PROBING', loadfactor=0.5)
    
    return city_info

def new_year_info(year):
    
    year_info = {
        'year' : year,
        'list_jobs' : None,
        'map_by_experience' : None,
    }
    
    year_info['list_jobs'] = lt.newList(datastructure='ARRAY_LIST')
    year_info['map_by_experience'] = mp.newMap(3, maptype='PROBING', loadfactor=0.5)
    
    return year_info

def add_skill(catalog, skill):
    
    map_skills = catalog['map_skills']
    
    if mp.contains(map_skills, skill['id']):
        entry = mp.get(map_skills, skill['id'])
        list_skills = me.getValue(entry)
        lt.addLast(list_skills, skill)
    else:
        list_skills = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(list_skills, skill)
        mp.put(map_skills, skill['id'], list_skills)
        
    return catalog

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
    
    answer = obtain_list_jobs_by_countryandexperience(catalog, country_code, experience_level)  # O(1) -> Obtenemos la lista de trabajos según el país y nivel de experiencia dados.
    
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
    

def req_3(catalog, company_name, start_date, final_date):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    
    
    map_companies = catalog['map_companies']
    company_info = obtain_info_company(map_companies, company_name)
    
    if company_info is not None:
        
        filter_jobs, senior_amount, junior_amount, mid_amount = obtain_jobs_and_counters(company_info, start_date, final_date)
        
        if lt.size(filter_jobs) == 0:
            return None
        else:
            amount_offers = senior_amount + junior_amount + mid_amount
            
            merg.sort(filter_jobs, compare_by_date_and_country)
            
            if lt.size(filter_jobs) > 10:
                first_jobs, last_jobs = obtain_first_and_last(filter_jobs, 5)
                filter_jobs = lt.newList(datastructure='ARRAY_LIST')
                for job in lt.iterator(first_jobs):
                    lt.addLast(filter_jobs, job)
                for job in lt.iterator(last_jobs):
                    lt.addLast(filter_jobs, job)
            
            table_jobs = tabulate_jobs_rq3(filter_jobs)
    else:
        return None
                
    return table_jobs, amount_offers, senior_amount, junior_amount, mid_amount
        
    
def obtain_info_company(map_companies, company_name):
    
    if mp.contains(map_companies, company_name):
        entry = mp.get(map_companies, company_name)
        company_info = me.getValue(entry)
    else:
        return None
    
    return company_info

def obtain_jobs_and_counters(company_info, start_date, final_date):
    filter_jobs = lt.newList(datastructure='ARRAY_LIST')
    jobs_experience = company_info['map_by_experience']
    list_experiences = mp.keySet(jobs_experience) # Lista de listas para evaluar si cumple los rangos de fecha
    senior_amount = 0
    junior_amount = 0
    mid_amount = 0
    
    for experience in lt.iterator(list_experiences):
        
        list_jobs = me.getValue(mp.get(jobs_experience, experience))
        
        for job in lt.iterator(list_jobs):
            
            job = examine_jobsito(job, start_date, final_date)
            
            if job is not None:
                if experience == 'senior':
                    senior_amount += 1
                elif experience == 'junior':
                    junior_amount += 1
                elif experience == 'mid':
                    mid_amount += 1
                lt.addLast(filter_jobs, job)
    
    return filter_jobs, senior_amount, junior_amount, mid_amount

def examine_jobsito(job, start_date, final_date):
    
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    final_date = datetime.strptime(final_date, "%Y-%m-%d")
    
    if start_date <= job['published_at'] <= final_date:
        return job
    else:
        return None

def tabulate_jobs_rq3(list_jobs):
    
    headers = ['Fecha', 'Titulo', 'Nivel', 'Ciudad', 'Pais', 'Tamanio Empresa','Ubicacion', 'Ukranians']
    
    table = []
    
    for job in lt.iterator(list_jobs):
        row = [job['published_at'], job['title'], job['experience_level'], job['city'], job['country_code'], job['company_size'], job['workplace_type'], job['open_to_hire_ukrainians']]
        table.append(row)
    
    return tabulate(tabular_data=table, headers=headers, tablefmt='fancy_grid')
    

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


def req_6(catalog, amount_cities, level, year):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    total_ofertas = 0
    map_cities = catalog['map_cities'] # Mapa Ciudades
    map_companies = mp.newMap(1000, maptype='PROBING', loadfactor=0.5) # Mapa Compañias
    
    filtered_cities = filter_cities(map_cities,level, year) #? O(n) siendo n la cantida de ciudades que hay en el mapa | Se filtran los datos de las ciudades
    
    if filtered_cities is None:
        return None
    
    merg.sort(filtered_cities, compare_city_by_size) #? O(nlogn) siendo n la cantidad de ciudades que hay  en la lista despues del filtro | Se ordenan las ciudades por la cantidad de ofertas de trabajo publicadas
    
    if amount_cities > lt.size(filtered_cities):
        amount_cities = lt.size(filtered_cities)
    
    sublist_cities = lt.subList(filtered_cities, 1, amount_cities) #? O(H) siendo H la cantidad de ciudades que se quieren mostrar | Se obtiene la sublista con las ciudades que se van a mostrar
    cities_updated, total_ofertas = update_cities_and_companies(catalog, sublist_cities, map_companies, total_ofertas) #? O(n) siendo n la cantidad de ciudades que se van a mostrar | Se actualizan las ciudades y las compañias
    tabulate_cities = tabulate_cities_rq6(cities_updated) #? O(n) siendo n la cantidad de ciudades que se van a mostrar | Se tabulan las ciudades
    total_ciudades = amount_cities
    total_empresas = mp.size(map_companies)
    best_city, worst_city = obtain_best_worst_city(cities_updated)
        
    return total_ciudades, total_empresas, total_ofertas, best_city, worst_city, tabulate_cities
def obtain_best_worst_city(cities_updated):
    
    best_city = lt.firstElement(cities_updated)
    best_city_name = me.getValue(mp.get(best_city, 'city'))
    best_city_jobs = lt.size(me.getValue(mp.get(best_city, 'list_jobs')))
    best_city = {'city': best_city_name, 'amount_jobs': best_city_jobs}
    
    worst_city = lt.lastElement(cities_updated)
    worst_city_name = me.getValue(mp.get(worst_city, 'city'))
    worst_city_jobs = lt.size(me.getValue(mp.get(worst_city, 'list_jobs')))
    worst_city = {'city': worst_city_name, 'amount_jobs': worst_city_jobs}
    
    return best_city, worst_city
def filter_cities(map_cities, level, year):
    filtered_cities = lt.newList(datastructure='ARRAY_LIST') # Lista vacia con la inforamcion que nos sirve
    keys_cities = mp.keySet(map_cities) # LIsta con las llaves de las ciudades
    
    for city in lt.iterator(keys_cities):
        city_info = (mp.get(map_cities, city)) # Obtiene la informacion de la ciudad
        if city_info is not None: 
            city_info = me.getValue(city_info)
            year_info = filter_year(city_info, year) # Filtra la informacion de la ciudad por año
            if year_info is not None:
                level_info = filter_level(year_info, level)
                if level_info is not None:
                    lt.addLast(filtered_cities, level_info) # Se agrega la informacion de la ciudad a la lista de ciudades filtradas
    
    if lt.size(filtered_cities) == 0:
        return None
    
    return filtered_cities
def filter_year(city_info, year):
    
    map_by_year = city_info['map_by_year']
    
    if mp.contains(map_by_year, year):
        year_info = me.getValue(mp.get(map_by_year, year))
    else:
        return None
    
    return year_info
def filter_level(year_info, level):
    
    map_by_experience = year_info['map_by_experience']
    
    if mp.contains(map_by_experience, level):
        level_info = me.getValue(mp.get(map_by_experience, level))
    else:
        return None
    
    return level_info
def new_city_map(city):
    
    city_map = mp.newMap(10, maptype='PROBING', loadfactor=0.5)
    
    mp.put(city_map, 'city', city)
    mp.put(city_map, 'list_jobs', lt.newList(datastructure='ARRAY_LIST'))
    mp.put(city_map, 'sumatoria',  0)
    mp.put(city_map, 'contador', 0)
    mp.put(city_map, 'best_job', None)
    mp.put(city_map, 'worst_job', None)
    mp.put(city_map, 'map_by_companies', mp.newMap(20, maptype='PROBING', loadfactor=0.5))

    return city_map
def update_cities_and_companies(control, sublist_cities, map_companies, total_ofertas):
    
    list_cities = lt.newList(datastructure='ARRAY_LIST')
    
    for city_list in lt.iterator(sublist_cities):
        city_name = lt.firstElement(city_list)['city']
        city_map = new_city_map(city_name)
        
        for job in lt.iterator(city_list):
            total_ofertas += 1
            update_city_map(control, city_map, job)
            update_companies(control, map_companies, job)
        
        lt.addLast(list_cities, city_map)
    
    return list_cities, total_ofertas
def update_city_map(control, city_map, job):
    
    list_jobs = me.getValue(mp.get(city_map, 'list_jobs'))
    sumatoria = me.getValue(mp.get(city_map, 'sumatoria'))
    contador = me.getValue(mp.get(city_map, 'contador'))
    best_job = me.getValue(mp.get(city_map, 'best_job'))
    worst_job = me.getValue(mp.get(city_map, 'worst_job'))
    map_by_companies = me.getValue(mp.get(city_map, 'map_by_companies'))
    
    lt.addLast(list_jobs, job) # Se agrega la oferta de trabajo a la lista de trabajos de la ciudad
    
    salaries = search_salary(control, job) # Se busca el mejor y peor salario de la oferta de trabajo
    
    if salaries is not None:
        best_offer, worst_offer = salaries
        average = (float(best_offer['salary_from']) + float(worst_offer['salary_to'])) / 2
        contador += 1
        sumatoria += average
        
        mp.put(city_map, 'sumatoria', sumatoria) # Se actualiza la sumatoria de los salarios
        mp.put(city_map, 'contador', contador) # Se actualiza el contador de ofertas de trabajo
            
        if best_job is None: # Se actualiza la mejor y peor oferta de trabajo
            best_job = {'Oferta': job['title'], 'salary_to': best_offer['salary_to']} # Se actualiza la mejor oferta de trabajo
            mp.put(city_map, 'best_job', best_job) # Se actualiza la mejor oferta de trabajo
        elif best_offer['salary_to'] > best_job['salary_to']:
            best_job = {'Oferta': job['title'], 'salary_to': best_offer['salary_to']}
            mp.put(city_map, 'best_job', best_job)
        
        if worst_job is None:
            worst_job = {'Oferta': job['title'], 'salary_from': worst_offer['salary_from']}
            mp.put(city_map, 'worst_job', worst_job)
        elif worst_offer['salary_from'] < worst_job['salary_from']:
            worst_job = {'Oferta': job['title'], 'salary_from': worst_offer['salary_from']}
            mp.put(city_map, 'worst_job', worst_job)
    
    update_companies(control, map_by_companies, job)
    
    return city_map   
def update_companies(control, map_companies, job):
    
    if mp.contains(map_companies, job['company_name']):
        company_info = me.getValue(mp.get(map_companies, job['company_name']))
        lt.addLast(company_info, job)
    else:
        company_info = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(company_info, job)
        mp.put(map_companies, job['company_name'], company_info)
    
    return control      
def search_salary(control, job):
    
    id_job = job['id'] # Extrae el id del trabajo
    map_employments = control['map_employments'] # Catalogo el mapa de empleos
    if mp.contains(map_employments, id_job): # Verifica si el id del trabajo esta en el mapa de empleos
        employment_type = me.getValue(mp.get(map_employments, id_job))
        if len(employment_type) > 1: # Si el mismo empleo tiene mas de un tipo de contratacion
            offers = employment_type.values() # Se extraen las ofertas de trabajo
            offers = list(offers) # Se convierte en lista
            answer = examine_salaries(control, offers)  # Se examinan los salarios de las ofertas de trabajo
            if answer is not None: # Si la respuesta no es nula
                best_offer, worst_offer = answer
            else:
                return None
        else: # Si el mismo empleo tiene un solo tipo de contratacion
            offers = employment_type.values() 
            offers = list(offers)
            best_offer = offers[0]
            worst_offer = offers[0]
            if best_offer['salary_to'] == '' and worst_offer['salary_from'] == '':
                return None
    else: # Si no esta en el mapa de empleos
        return None
    
    return best_offer, worst_offer  
def examine_salaries(control, offers):
    
    best_offer = offers[0]
    worst_offer = offers[0]
    
    for offer in offers:
        if offer['salary_from'] != '' and offer['salary_to'] != '':
            if offer['salary_from'] < worst_offer['salary_from']:
                worst_offer = offer
            if offer['salary_to'] > best_offer['salary_to']:
                best_offer = offer
    
    if best_offer['salary_to'] == '' and worst_offer['salary_from'] == '':
        return None
    
    return best_offer, worst_offer   
def tabulate_cities_rq6(list_cities):
    
    headers = ['Ciudad', 'Pais', 'Total Ofertas', 'Promedio Salario', '# Empresas', 'Mejor Empresa' ,'Mejor Oferta', 'Peor Oferta']
    
    table = []
    
    for city in lt.iterator(list_cities):
        name_city = me.getValue(mp.get(city, 'city'))
        country = lt.firstElement(me.getValue(mp.get(city, 'list_jobs')))['country_code']
        amount_offers = lt.size(me.getValue(mp.get(city, 'list_jobs')))
        
        sumatoria = me.getValue(mp.get(city, 'sumatoria'))
        contador = me.getValue(mp.get(city, 'contador'))
        
        if not(sumatoria == 0 or contador == 0):
            average_salary = sumatoria / contador
        
        amount_companies = mp.size(me.getValue(mp.get(city, 'map_by_companies')))
        best_company = obtain_best_company(city)
        best_offer = me.getValue(mp.get(city, 'best_job'))
        worst_offer = me.getValue(mp.get(city, 'worst_job'))
        row = [name_city, country, amount_offers, average_salary, amount_companies, best_company, best_offer, worst_offer]
        table.append(row)
    
    return tabulate(table, headers, tablefmt='grid')
def obtain_best_company(city):
    
    map_by_companies = me.getValue(mp.get(city, 'map_by_companies'))
    
    list_companies = mp.valueSet(map_by_companies)
    
    merg.sort(list_companies, compare_city_by_size)
    
    best_company = {
        'company_name' : lt.firstElement(lt.firstElement(list_companies))['company_name'],
        'amount_jobs' : lt.size(lt.firstElement(list_companies))
    }
    
    return best_company 
def req_7(catalog, amount_countries, year, month):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    
    map_countries = catalog['map_countries']
    map_cities = mp.newMap(500, maptype='PROBING', loadfactor=0.5)
    
    
    list_countries, amount_countries = sort_countries(map_countries, amount_countries)
    
    
    return False
 
def obtain_data_rq7(control, list_countries, year, month):
    
    filtered_countries = lt.newList(datastructure='ARRAY_LIST')
    
    for country in lt.iterator(list_countries):
        filter_country = lt.newList(datastructure='ARRAY_LIST')

def filter_levels(control ,country, filter_country, year, month):
    
    map_by_experience = me.getValue(mp.get(country, 'map_by_experience'))
    
    for experience in lt.iterator(mp.keySet(map_by_experience)):
        experience_map = new_experience_filtered(experience)
        list_jobs = me.getValue(mp.get(map_by_experience, experience))
        
        for job in lt.iterator(list_jobs):
            job = examine_job(job, year, month)
            
            if job is not None:
                pass

def update_info_experience(control, experience_map, job):
        
    amount_jobs = me.getValue(mp.get(experience_map, 'amount_jobs'))
    map_companies = me.getValue(mp.get(experience_map, 'map_companies'))
    map_skills = me.getValue(mp.get(experience_map, 'map_skills'))
    summation = me.getValue(mp.get(experience_map, 'summation'))
    counter = me.getValue(mp.get(experience_map, 'counter'))
        
    amount_jobs += 1
        
    mp.put(experience_map, 'amount_jobs', amount_jobs)
        
    update_companies(map_companies, job)
    update_skills(map_skills, job)
        
    return experience_map

def update_skills(control, map_skills, job):
    pass
    

def examine_job(job, year, month):
    
    if job['published_at'].year == year and job['published_at'].month == month:
        return job
    else:
        return None

def new_experience_filtered(experience_level):
    
    experience_map = mp.newMap(10, maptype='PROBING', loadfactor=0.5)
    
    mp.put(experience_map, 'experience_level', experience_level)
    mp.put(experience_map, 'amount_jobs', 0)
    mp.put(experience_map, 'map_companies', mp.newMap(100, maptype='PROBING', loadfactor=0.5))
    mp.put(experience_map, 'map_skills', mp.newMap(100, maptype='PROBING', loadfactor=0.5))
    mp.put(experience_map, 'summation', 0)
    mp.put(experience_map, 'counter', 0)
    
    return experience_map
    
def sort_countries(map_countries, amount_countries):
    
    list_countries = mp.valueSet(map_countries)
    
    merg.sort(list_countries, compare_countries_by_size)
    
    if amount_countries > lt.size(list_countries):
        amount_countries = lt.size(list_countries)
    
    sublist_countries = lt.subList(list_countries, 1, amount_countries)
    
    return sublist_countries, amount_countries
    

def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


def obtain_first_and_last(list, N):
    
    if lt.size(list) < N*2:
        return list
    
    first_elements = lt.subList(list, 1, N)
    last_elements = lt.subList(list, lt.size(list)-N, N)
    
    return first_elements, last_elements
    
    # 5 primeras y las 5 ultimas 
    # Lista 9 elementos?
    
    
    
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

def compare_countries_by_size(country1, country2):
    """
    Compara dos países por la cantidad de ofertas de trabajo publicadas.
    """
    country1_size = lt.size(me.getValue(mp.get(country1, 'list_jobs')))
    country2_size = lt.size(me.getValue(mp.get(country2, 'list_jobs')))
    
    return country1_size > country2_size

def compare_by_date_and_country(job1, job2):
    
    if job1['published_at'] == job2['published_at']:
        return job1['country_code'] > job2['country_code']
    else:
        return job1['published_at'] > job2['published_at']

def compare_city_by_size(city1, city2):
    """
    Compara dos ciudades por la cantidad de ofertas de trabajo publicadas.
    """
    return lt.size(city1) > lt.size(city2)


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
