from Constantes import *
import random
import pygame
from datetime import datetime

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







# def pedir_nombre(mensaje, mensaje_error) -> str:
   
#     nombre = input(mensaje)
#     while True:
#         if len(nombre) >= 3:
#             fecha_actual = datetime.now()
#             solo_fecha = fecha_actual.strftime("%d/%m/%y")
#             break
#         else:
#             nombre = input(mensaje_error)

#     print("Nombre validado exitosamente!!!")
#     datos = [nombre,solo_fecha]
#     return datos

# res = pedir_nombre("Ingrese su nombre para el ranking: ", "!ERROR¡ Nombre demasiado corto, debe tener al menos 3 caracteres. Reingrese un nombre: ")
# print(res)
