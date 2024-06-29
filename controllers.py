import models
import os

def crear_contacto(lista_contactos, RUTA):
    lista_actualizada = models.crear_contacto(lista_contactos)
    models.guardar_contactos(lista_actualizada, RUTA)
    input("\nApreta enter para continuar")
    os.system("clear")

def mostrar_contactos(lista_contactos):
    models.mostrar_contactos(lista_contactos)
    input("\nApreta enter para continuar")
    os.system("clear")

def eliminar_contacto(lista_contactos, RUTA):
    models.mostrar_contactos(lista_contactos)
    lista_actualizada = models.eliminar_contacto(lista_contactos)
    models.guardar_contactos(lista_actualizada, RUTA)
    input("\nApreta enter para continuar")
    os.system("clear")

def actualizar_contacto(lista_contactos, RUTA):
    models.mostrar_contactos(lista_contactos)
    models.actualizar_contacto(lista_contactos, RUTA)
    models.guardar_contactos(lista_contactos,RUTA)