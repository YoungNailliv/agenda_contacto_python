from models import *
import controllers
import os

lista_contactos = []
RUTA = "./contactos.json"


def main():
    global lista_contactos
    global RUTA

    lista_contactos = cargar_contactos(RUTA)

    while True:
        print_menu()
        choice = input("\nIngresa una opcion: ")

        match choice:
            case "1":
                controllers.crear_contacto(lista_contactos, RUTA)
            case "2":
                controllers.mostrar_contactos(lista_contactos)
            case "3":
                controllers.eliminar_contacto(lista_contactos, RUTA)
            case "4":
                controllers.actualizar_contacto(lista_contactos, RUTA)
            case "5":
                print("Adios!")
                break
                
            case _:
                print("\nIngresa una opcion valida.")
                input("Apreta enter para continuar")
                os.system("clear")


if __name__ == "__main__":
    main()
