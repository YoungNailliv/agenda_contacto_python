import json
import os
from classes import *

def print_menu():
    print("""
    --- Agenda de contacto ---
    1- Agregar Contacto
    2- Mostrar Contactos
    3- Eliminar Contacto
    4- Actualizar Contacto
    5- Salir
    """)

def cargar_contactos(RUTA):
    try:
        with open(RUTA, "r") as f:
            lista_contactos = json.load(f)
            return [Contacto(**data) for data in lista_contactos]
    except:
        return []

def guardar_contactos(lista_nueva, ruta):

    json_lista = [contacto.to_dict() for contacto in lista_nueva]
    
    try:
        with open(ruta, "w") as f:
            json.dump(json_lista,f,indent=4)
    except FileNotFoundError:
        print("\nNo se ha podido guardar tu lista de contactos")
        input("Apreta enter para volver al menu")
        os.system("clear")

def crear_contacto(lista_contactos):
    nombre = input("\nNombre Contacto: ")
    telefono = input("Telefono Contacto: ")
    email = input("Email Contacto: ")
    try:
        nuevo_contacto = Contacto(nombre, telefono, email)
        lista_contactos.append(nuevo_contacto)
        return lista_contactos
    except:
        return lista_contactos

def eliminar_contacto(lista_contactos):
    while True:
        contacto_eliminado = input("Ingresa el numero del usuario que deseas eliminar: ")
        if contacto_eliminado.isdigit():
            if int(contacto_eliminado) <= len(lista_contactos):
                lista_contactos.pop((int(contacto_eliminado) - 1) )
                print(f"\nSe ha eliminado el contacto")
                input("Apreta Enter para continuar")
                os.system("clear")
                return lista_contactos
            else:
                print("Ingresa un numero valido")
        else:
            print("\nIngresa un numero")

def actualizar_contacto(lista_contactos, RUTA):
    indice = input("\nIngresa el numero de contacto que deseas actualizar: ")
    if indice.isdigit():
        if int(indice) <= len(lista_contactos):
            indice = int(indice) - 1
            print("Ingresa nuevamente los campos (deja en blanco para mantenerlo)")
            nombre = input("\nNombre Contacto: ")
            telefono = input("Telefono Contacto: ")
            email = input("Email Contacto: ")
            lista_contactos[indice].update(nombre, telefono, email)
            return lista_contactos

        else:
            print("Ese numero no corresponde a un contacto")
    else:
        print("Ingresa un numero")

def mostrar_contactos(lista_contactos):
    if len(lista_contactos) != 0:
        count=1
        lista_json = [contacto.to_dict() for contacto in lista_contactos]
        print(" ")
        for contacto in lista_json:
            print(f"{count}- Nombre: {contacto['nombre']}\tTelefono:{contacto['telefono']}\tEmail:{contacto['email']}")
            count+=1
    else:
        print("No hay contactos agregados")


