import os
import json
from Constantes import *
import random
import pygame
from datetime import datetime
import time
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


#Dibujar preguntas
def dibujar_preguntas(pantalla:pygame.Surface, cuadro_pregunta:dict, pregunta_actual:dict) -> None:
   
   mostrar_texto(cuadro_pregunta["superficie"],f"{pregunta_actual['pregunta']}", (20,20),FUENTE_22,COLOR_BLANCO)
   cuadro_pregunta["rectangulo"] = pantalla.blit(cuadro_pregunta["superficie"],(80,80))
   pygame.draw.rect(pantalla,COLOR_NEGRO,cuadro_pregunta["rectangulo"],2)



#Dibujar respuestas
def dibujar_respuestas(pantalla:pygame.Surface, lista_respuestas:dict, pregunta_actual:dict) -> dict:
    
    posiciones_respuestas = [(125, 245), (125, 315), (125, 385), (125, 455)]

    for i in range(len(lista_respuestas)):
        mostrar_texto(lista_respuestas[i]["superficie"],f"{pregunta_actual[f"respuesta_{i+1}"]}",(20,20),FUENTE_22,COLOR_BLANCO)
        lista_respuestas[i]["rectangulo"] = pantalla.blit(lista_respuestas[i]["superficie"],posiciones_respuestas[i])
        pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[i]["rectangulo"],2)


def dibujar_reloj(pantalla: pygame.Surface, superficie_reloj: dict, tiempo_inicial: int, tiempo_inicio: int):
    """
    Dibuja un reloj regresivo en la pantalla.

    Args:
        pantalla: La superficie principal donde se dibuja.
        superficie_reloj: Diccionario con la superficie y rectángulo del reloj.
        tiempo_inicial: Tiempo total del contador en segundos.
        tiempo_inicio: Marca de tiempo inicial en milisegundos.
    """
    # Calcular tiempo restante
    tiempo_actual = pygame.time.get_ticks()
    tiempo_restante = tiempo_inicial - (tiempo_actual - tiempo_inicio) // 1000

    if tiempo_restante < 0:
        tiempo_restante = 0

    # Dibujar fondo y texto
    superficie_reloj["superficie"].fill(COLOR_BLANCO)  # Fondo (opcional, depende del diseño)
    texto_tiempo = f"Tiempo: {tiempo_restante}"
    mostrar_texto(
        superficie_reloj["superficie"],
        texto_tiempo,
        (60, 7),
        FUENTE_27,
        COLOR_NEGRO
    )
    pantalla.blit(superficie_reloj["superficie"], (410, 10))
    return tiempo_restante

acumula_puntos = 0
def respuesta_correcta(datos_juego, lista_respuestas, i):
    global acumula_puntos
   
    ACIERTO_SONIDO.play()
    print("RESPUESTA CORRECTA")
    acumula_puntos += 1
    pintar = True
    pintar_respuesta(lista_respuestas, pintar, i)
    sumar_puntos(datos_juego)

    if acumula_puntos == 5:
        acumula_puntos = 0
        sumar_vida(datos_juego)


def respuesta_incorrecta(datos_juego, lista_respuestas, i, retorno):
    ERROR_SONIDO.play()
    pintar = False
    pintar_respuesta(lista_respuestas, pintar, i)
    verificar_vidas(datos_juego, retorno)


def pintar_respuesta(lista_respuestas:dict, pintar:bool, i):
    if pintar:
        lista_respuestas[i]["superficie"].fill(COLOR_VERDE_OSCURO)
    else:
        lista_respuestas[i]["superficie"].fill(COLOR_ROJO)


def sumar_puntos(datos_juego:dict):
    datos_juego["puntuacion"] += PUNTUACION_ACIERTO


def restar_puntos(datos_juego:dict):
    datos_juego["puntuacion"] -= PUNTUACION_ERROR


def sumar_vida(datos_juego):
        datos_juego["cantidad_vidas"] += 1
        
def restar_vida(datos_juego):
        datos_juego["cantidad_vidas"] -= 1

def verificar_vidas( datos_juego, retorno ) -> bool:
    if datos_juego["cantidad_vidas"] > 0:
        restar_vida(datos_juego)
        restar_puntos(datos_juego)
        retorno = "juego"
    else:
        retorno = "terminado"
        pedir_nombre(
            "Ingrese su nombre para el ranking: ",
            "!ERROR¡ Nombre demasiado corto, debe tener al menos 3 caracteres. Reingrese un nombre: ",
            datos_juego["puntuacion"]
        )
