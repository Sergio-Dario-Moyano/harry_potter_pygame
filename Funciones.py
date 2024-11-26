import os
import json
from Constantes import *
import random
import pygame
from datetime import datetime
# from Terminado import *

def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


def cargar_json(datos: dict) -> bool:
    archivo_json = "partidas.json"
    arr_datos = []

    # Si el archivo existe, cargar los datos actuales
    if os.path.exists(archivo_json):
        with open(archivo_json, "r", encoding="utf-8") as archivo:
            try:
                arr_datos = json.load(archivo)
            except json.JSONDecodeError:
                arr_datos = []  # Si el archivo está vacío o corrupto, iniciar como lista vacía

    # Agregar los nuevos datos
    arr_datos.append(datos)

    # Sobrescribir el archivo con los datos actualizados
    with open(archivo_json, "w", encoding="utf-8") as archivo:
        json.dump(arr_datos, archivo, indent=4)

    return True



def pedir_nombre(mensaje:str, mensaje_error:str, puntos:int) -> None:
    while True:
        nombre = input(mensaje)
        if len(nombre) >= 3:
            fecha_actual = datetime.now()
            solo_fecha = fecha_actual.strftime("%d/%m/%y")
            datos = {"nombre": nombre, "fecha": solo_fecha, "puntos": puntos}
            cargar_json(datos)
            print("Nombre guardado exitosamente en el ranking.")
            break
        else:
            print(mensaje_error)




