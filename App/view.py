"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

listType= "ARRAY_LIST"
def new_controller(size, map_type, charge_factor):
    control= controller.new_controller(size, map_type, charge_factor)
    return control 
    """

        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")
    
    



def load_data(control, size):
    
    """
    Carga los datos
    """
    
    return controller.load_data(control, size)


def map_type():
    
    print("Escoja el tipo de mapa que desea usar")
    print("1. Separate chaining")
    print("2. Linear Probing")
    
    input_type = int(input("Ingrese el valor: "))
    
    if input_type == 1:
        map_type =  "CHAINING"
    else:
        map_type = "PROBING"
        
    if map_type == "CHAINING":
        print("Seleccione factor de carga")
        print("1. 2")
        print("2. 4")
        print("3. 6")
        print("4. 8")
        charge_factor = int(input("Ingrese el valor: "))
        if charge_factor == 1:
            charge_factor = 2
        elif charge_factor == 2:
            charge_factor = 4
        elif charge_factor == 3:
            charge_factor = 6
        else:
            charge_factor = 8
    
    if map_type == "PROBING":
        print("Seleccione factor de carga")
        print("1. 0.5")
        print("2. 0.75")
        print("3. 0.9")
        print("4. 0.95")
        charge_factor = int(input("Ingrese el valor: "))
        if charge_factor == 1:
            charge_factor = 0.5
        elif charge_factor == 2:
            charge_factor = 0.75
        elif charge_factor == 3:
            charge_factor = 0.9
        else:
            charge_factor = 0.95
    
    return map_type, charge_factor
        

def choose_size():

    print("Escoja el tamanio de los datos")
    print("1. small")
    print("2. medium")
    print("3. large")
    print("4. 10 porciento")
    print("5. 20 porciento")
    print("6. 30 porciento")
    print("7. 40 porciento")
    print("8. 50 porciento")
    print("9. 60 porciento")
    print("10. 70 porciento")
    print("11. 80 porciento")
    print("12. 90 porciento")
    
    value = int(input("Ingrese el valor: "))
    
    if value == 1:
        return "small-"
    elif value == 2:
        return "medium-"
    elif value == 3:
        return "large-"
    elif value == 4:
        return "10-por-"
    elif value == 5:
        return "20-por-"
    elif value == 6:
        return "30-por-"
    elif value == 7:
        return "40-por-"
    elif value == 8:
        return "50-por-"
    elif value == 9:
        return "60-por-"
    elif value == 10:
        return "70-por-"
    elif value == 11:
        return "80-por-"
    elif value == 12:
        return "90-por-"
    else:
        return "large-"

# def print_data(control, id):
#     """
#         Función que imprime un dato dado su ID
#     """
#     print("Los primeros tres elementos de ", csv, "son: ")

#     for elements in lt.iterator(lista_inicial):
#         print("Title: ", elements["title"],", ","Street: ", elements["street"], ", ","City: ", elements["city"],", ", "Country_code: ", elements["country_code"],", ","Address_text ", elements["address_text"], ", ","Marker_icon", elements["marker_icon"], ", ","Workplace_type", elements["workplace_type"], ", ","Company_name ",elements["company_name"],", "," Company_url", elements["company_url"],  ", ", "Company_size ", elements["company_size"],", ", " Experience_level ", elements["experience_level"],", ","Published_at ", elements["published_at"],", ", "Remote_interview",elements["remote_interview"],", ","Open_to_hire_ukrainians", elements["open_to_hire_ukrainians"],", ","Id",elements["id"],"Display_offer",elements["display_offer"],"\n")
        
#     print("Los ultimos tres elementos de ", csv, "son: ")

#     for ele in lt.iterator(lista_final):
#         print("Title: ", ele["title"],", ","Street: ", ele["street"], ", ","City: ", ele["city"],", ", "Country_code: ", ele["country_code"],", ","Address_text ", ele["address_text"], ", ","Marker_icon", ele["marker_icon"], ", ","Workplace_type", ele["workplace_type"], ", ","Company_name ",ele["company_name"],", "," Company_url", ele["company_url"],  ", ", "Company_size ", ele["company_size"],", ", " Experience_level ", ele["experience_level"],", ","Published_at ", ele["published_at"],", ", "Remote_interview",ele["remote_interview"],", ","Open_to_hire_ukrainians", ele["open_to_hire_ukrainians"],", ","Id",ele["id"],"Display_offer",ele["display_offer"],"\n")

#     #TODO: Realizar la función para imprimir un elemento
    
def print_lista(lista):
    print("las ofertas cargadas son:")
    for elements in lt.iterator(lista):
        print("Title: ", elements["title"],", ","Street: ", elements["street"], ", ","City: ", elements["city"],", ", "Country_code: ", elements["country_code"],", ","Address_text ", elements["address_text"], ", ","Marker_icon", elements["marker_icon"], ", ","Workplace_type", elements["workplace_type"], ", ","Company_name ",elements["company_name"],", "," Company_url", elements["company_url"],  ", ", "Company_size ", elements["company_size"],", ", " Experience_level ", elements["experience_level"],", ","Published_at ", elements["published_at"],", ", "Remote_interview",elements["remote_interview"],", ","Open_to_hire_ukrainians", elements["open_to_hire_ukrainians"],", ","Id",elements["id"],"Display_offer",elements["display_offer"],"\n")
   
def print_req_1(control, country_code, experience_level, amount):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    
    answer = controller.req_1(control, country_code, experience_level, amount)

    
    if answer is not None:
        amount_jobs_country = answer[0]
        amount_jobs_by_experience = answer[1]
        table_jobs = answer[2]

        print("======== Requerimiento 1: Respuesta ========")
        print(f"\nLa cantidad de ofertas de trabajo en el pais {country_code} son {amount_jobs_country}")
        print(f"La cantidad de ofertas de trabajo en el nivel de experiencia {experience_level} son {amount_jobs_by_experience}")
        
        print(f"\nLas {amount} ofertas de trabajo mas recientes en el pais {country_code} y nivel de experiencia {experience_level} son:")
        print(table_jobs)
    else:
        print("======== Requerimiento 1: Respuesta ========")
        print("No se encontraron ofertas de trabajo con los parametros ingresados")



def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control, company_name, start_date, final_date):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    
    answer = controller.req_3(control, company_name, start_date, final_date)
    
    if answer is not None:
        table = answer[0]
        amount_offers = answer[1]
        amount_senior = answer[2]
        amount_junior = answer[3]
        amount_mid = answer[4]
        
        print("======== Requerimiento 3: Respuesta ========")
        print(f"La cantidad de ofertas de trabajo de la empresa {company_name} son {amount_offers}")
        print(f"La cantidad de ofertas de trabajo de nivel senior son {amount_senior}")
        print(f"La cantidad de ofertas de trabajo de nivel junior son {amount_junior}")
        print(f"La cantidad de ofertas de trabajo de nivel mid son {amount_mid}")
        print(f"El listado de ofertas de trabajo ordenadas por fecha y pais de la empresa {company_name} son los siguientes:")
        print(table)
        
        
    else:
        print("======== Requerimiento 3: Respuesta ========")
        print("No se encontraron ofertas de trabajo con los parametros ingresados")


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control, amount_cities, level, year):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    
    answer = controller.req_6(control, amount_cities, level, year)
    
    if answer is not None:
        total_ciudades, total_empresas, total_ofertas, best_city, worst_city, tabulate_cities = answer
        print("======== Requerimiento 6: Respuesta ========")
        print(f"El total de ciudades con ofertas de trabajo en el año {year} y nivel de experiencia {level} son {total_ciudades}")
        print(f"El total de empresas con ofertas de trabajo en el año {year} y nivel de experiencia {level} son {total_empresas}")
        print(f"El total de ofertas de trabajo en el año {year} y nivel de experiencia {level} son {total_ofertas}")
        print(f"La ciudad con mayor cantidad de ofertas de trabajo en el año {year} y nivel de experiencia {level} es {best_city['city']} con {best_city['amount_jobs']} ofertas")
        print(f"La ciudad con menor cantidad de ofertas de trabajo en el año {year} y nivel de experiencia {level} es {worst_city['city']} con {worst_city['amount_jobs']} ofertas")
        print(f"Las {amount_cities} ciudades con mayor cantidad de ofertas de trabajo en el año {year} y nivel de experiencia {level} son:")
        print(tabulate_cities)
        
    else:
        print("======== Requerimiento 6: Respuesta ========")
        print("No se encontraron ofertas de trabajo con los parametros ingresados")


def print_req_7(control, amount_countries, year, month):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    
    answer = controller.req_7(control, amount_countries, year, month)
    
    if answer is not None:
        amount_jobs, amount_cities, best_country, best_city, multitable = answer
        print("======== Requerimiento 7: Respuesta ========")
        print(f"El total de ofertas de trabajo en el año {year} y mes {month} son {amount_jobs}")
        print(f"El total de ciudades con ofertas de trabajo en el año {year} y mes {month} son {amount_cities}")
        print(f"El pais con mayor cantidad de ofertas de trabajo en el año {year} y mes {month} es {best_country['country']} con {best_country['amount_jobs']} ofertas")
        print(f"La ciudad con mayor cantidad de ofertas de trabajo en el año {year} y mes {month} es {best_city['city']} con {best_city['amount']} ofertas")
        print(f"Los {amount_countries} paises con mayor cantidad de ofertas de trabajo en el año {year} y mes {month} son:")
        for table in multitable:
            print(table)
            print("\n")
    else:
        print("======== Requerimiento 7: Respuesta ========")
        print("No se encontraron ofertas de trabajo con los parametros ingresados")


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista

# main del reto
if __name__ == "__main__":
    
    """
    Menu principal
    """
    
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            size = choose_size()
            map_t, charge_f = map_type()
            control = new_controller(size, map_t, charge_f)
            print("Cargando información de los archivos ....\n")
            control = load_data(control, size)
            print("La información ha sido cargada con éxito\n")
        
        elif int(inputs) == 2:
            print("========== Requerimiento 1 - Listar las últimas N ofertas de trabajo según su país y nivel de experticia ========== ")
            country_code = input("Ingrese el código del país: ")
            experience_level = input("Ingrese el nivel de experiencia: ")
            amount = int(input("Ingrese la cantidad de ofertas que desea ver: "))
            print_req_1(control, country_code, experience_level, amount)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print("========== Requerimiento 3 - Consultar las ofertas que publicó una empresa durante un periodo especifico de tiempo ========")
            company_name = input("Ingrese el nombre de la empresa: ")
            start_date = input("Ingrese la fecha inicial de busqueda (YYYY-MM-DD)")
            final_date = input("Ingresa la fecha final del busqueda (YYYY-MM-DD)")
            print_req_3(control, company_name, start_date, final_date)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print("========== Requerimiento 6 - Clasificar las N ciudades con mayor número de ofertas de trabajo de un año por experticia ==========")
            amount_cities = int(input("Ingrese la cantidad de ciudades que desea ver: "))
            level = input("Ingrese el nivel de experiencia: ")
            year = int(input("Ingrese el año: "))
            print_req_6(control, amount_cities, level, year)

        elif int(inputs) == 8:
            print("========== Requerimiento 7 - Clasificar las N paises con mayor número de ofertas de trabajo ==========")
            amount_countries = int(input("Ingrese la cantidad de paises que desea ver: "))
            year = int(input("Ingrese el año (YYYY): "))
            month = int(input("Ingrese el mes (MM): "))
            print_req_7(control, amount_countries, year, month)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
