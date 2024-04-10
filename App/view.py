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
def new_controller():
    control= controller.new_controller()
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



def load_data(control):
    """
    Carga los datos
    """
    percent= input("ingrese el porcentaje:")
    jobs_size, skills_size, employment_types_size, multilocations_size = controller.load_data(control,percent)
    
    print('Ofertas cargadas:', jobs_size)
    print('Habilidades cargadas:', skills_size)
    print('Tipos de contratacion:', employment_types_size)
    print('Ubicaciones:', multilocations_size)
    return jobs_size, skills_size, employment_types_size, multilocations_size

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    print("Los primeros tres elementos de ", csv, "son: ")

    for elements in lt.iterator(lista_inicial):
        print("Title: ", elements["title"],", ","Street: ", elements["street"], ", ","City: ", elements["city"],", ", "Country_code: ", elements["country_code"],", ","Address_text ", elements["address_text"], ", ","Marker_icon", elements["marker_icon"], ", ","Workplace_type", elements["workplace_type"], ", ","Company_name ",elements["company_name"],", "," Company_url", elements["company_url"],  ", ", "Company_size ", elements["company_size"],", ", " Experience_level ", elements["experience_level"],", ","Published_at ", elements["published_at"],", ", "Remote_interview",elements["remote_interview"],", ","Open_to_hire_ukrainians", elements["open_to_hire_ukrainians"],", ","Id",elements["id"],"Display_offer",elements["display_offer"],"\n")
        
    print("Los ultimos tres elementos de ", csv, "son: ")

    for ele in lt.iterator(lista_final):
        print("Title: ", ele["title"],", ","Street: ", ele["street"], ", ","City: ", ele["city"],", ", "Country_code: ", ele["country_code"],", ","Address_text ", ele["address_text"], ", ","Marker_icon", ele["marker_icon"], ", ","Workplace_type", ele["workplace_type"], ", ","Company_name ",ele["company_name"],", "," Company_url", ele["company_url"],  ", ", "Company_size ", ele["company_size"],", ", " Experience_level ", ele["experience_level"],", ","Published_at ", ele["published_at"],", ", "Remote_interview",ele["remote_interview"],", ","Open_to_hire_ukrainians", ele["open_to_hire_ukrainians"],", ","Id",ele["id"],"Display_offer",ele["display_offer"],"\n")

    #TODO: Realizar la función para imprimir un elemento
    
def print_lista(lista):
    print("las ofertas cargadas son:")
    for elements in lt.iterator(lista):
        print("Title: ", elements["title"],", ","Street: ", elements["street"], ", ","City: ", elements["city"],", ", "Country_code: ", elements["country_code"],", ","Address_text ", elements["address_text"], ", ","Marker_icon", elements["marker_icon"], ", ","Workplace_type", elements["workplace_type"], ", ","Company_name ",elements["company_name"],", "," Company_url", elements["company_url"],  ", ", "Company_size ", elements["company_size"],", ", " Experience_level ", elements["experience_level"],", ","Published_at ", elements["published_at"],", ", "Remote_interview",elements["remote_interview"],", ","Open_to_hire_ukrainians", elements["open_to_hire_ukrainians"],", ","Id",elements["id"],"Display_offer",elements["display_offer"],"\n")
   
def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


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


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

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
            print("Cargando información de los archivos ....\n")
            jobs_size, skills_size, employment_types_size, multilocations_size = load_data(control)
            # Imprimir los mensajes con la información cargada
            print('Ofertas cargadas:', jobs_size)
            print('Habilidades cargadas:', skills_size)
            print('Tipos de contratación:', employment_types_size)
            print('Ubicaciones:', multilocations_size)
            
            
        
            
        
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
