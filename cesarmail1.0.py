import os
import time

archivo_config = "config.txt"

if not os.path.exists(archivo_config):
    input("nombre: ")
    input("correo: ")
    input("contraseña: ")

    with open(archivo_config, "w") as archivo:
        archivo.write("Preguntas iniciales realizadas")

while True:
    print("\n--- César Mail™ ---")
    print("1. Bandeja de entrada")
    print("2. Enviados")
    print("3. Enviar")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Hay mail=yo que se.")
        time.sleep(1)

    elif opcion == "2":
        print("enviaste algo=yo que se.")
        time.sleep(1)

    elif opcion == "3":
        input("A quien: ")
        input("Asunto: ")
        input("El resto del correo: ")
        print("Se envio=yo que se")
        time.sleep(1)

    elif opcion == "4":
        break

    else:
        print("Escribiste algo bien=yo que se")
