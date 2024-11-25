import pygame
import random
from Funciones import *
from Preguntas import *

pygame.init()

# Configuración inicial
cuadro_pregunta = {
    "superficie": pygame.image.load("fondo.jpg"),
}
cuadro_pregunta["superficie"] = pygame.transform.scale(cuadro_pregunta["superficie"], TAMAÑO_PREGUNTA)
cuadro_pregunta["rectangulo"] = cuadro_pregunta["superficie"].get_rect()

# Crear la lista de respuestas dinámicamente
NUM_RESPUESTAS = 4  # Número de respuestas (puedes cambiarlo si es necesario)
lista_respuestas = []

for i in range(NUM_RESPUESTAS):
    cuadro_respuesta = {
        "superficie": pygame.Surface(TAMAÑO_RESPUESTA),
        "rectangulo": None,
    }
    cuadro_respuesta["superficie"].fill(COLOR_AZUL)
    lista_respuestas.append(cuadro_respuesta)

indice = 0
bandera_respuesta = False
random.shuffle(lista_preguntas)

def mostrar_juego(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict) -> str:
    global indice
    global bandera_respuesta

    retorno = "juego"

    if bandera_respuesta:
        pygame.time.delay(250)
        cuadro_pregunta["superficie"] = pygame.image.load("fondo.jpg")
        cuadro_pregunta["superficie"] = pygame.transform.scale(cuadro_pregunta["superficie"], TAMAÑO_PREGUNTA)
        for respuesta in lista_respuestas:
            respuesta["superficie"].fill(COLOR_AZUL)
        bandera_respuesta = False

    pregunta_actual = lista_preguntas[indice]

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for i, respuesta in enumerate(lista_respuestas):
                if respuesta["rectangulo"] and respuesta["rectangulo"].collidepoint(evento.pos):
                    respuesta_seleccionada = i + 1
                    if respuesta_seleccionada == pregunta_actual["respuesta_correcta"]:
                        ACIERTO_SONIDO.play()
                        respuesta["superficie"].fill(COLOR_VERDE_OSCURO)
                        datos_juego["puntuacion"] += PUNTUACION_ACIERTO
                    else:
                        ERROR_SONIDO.play()
                        respuesta["superficie"].fill(COLOR_ROJO)
                        if datos_juego["puntuacion"] > 0:
                            datos_juego["puntuacion"] -= PUNTUACION_ERROR
                        datos_juego["cantidad_vidas"] -= 1
                        print("RESPUESTA INCORRECTA")
                        retorno = "terminado"
                        # if datos_juego["cantidad_vidas"] <= 0:
                    
                    if indice == len(lista_preguntas):
                        indice = 0
                        random.shuffle(lista_preguntas)
                    
                    bandera_respuesta = True
                    break

    pantalla.fill(COLOR_VIOLETA)

    mostrar_texto(cuadro_pregunta["superficie"],f"{pregunta_actual["pregunta"]}",(20,20),FUENTE_27,COLOR_NEGRO)
    mostrar_texto(lista_respuestas[0]["superficie"],f"{pregunta_actual["respuesta_1"]}",(20,20),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[1]["superficie"],f"{pregunta_actual["respuesta_2"]}",(20,20),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[2]["superficie"],f"{pregunta_actual["respuesta_3"]}",(20,20),FUENTE_22,COLOR_BLANCO)


    cuadro_pregunta["rectangulo"] = pantalla.blit(cuadro_pregunta["superficie"],(80,80))
    lista_respuestas[0]["rectangulo"] = pantalla.blit(lista_respuestas[0]["superficie"],(125,245))#r1
    lista_respuestas[1]["rectangulo"] = pantalla.blit(lista_respuestas[1]["superficie"],(125,315))#r2
    lista_respuestas[2]["rectangulo"] = pantalla.blit(lista_respuestas[2]["superficie"],(125,385))#r3


    pygame.draw.rect(pantalla,COLOR_NEGRO,cuadro_pregunta["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[0]["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[1]["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[2]["rectangulo"],2)

    mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(10,10),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,f"VIDAS: {datos_juego['cantidad_vidas']}",(10,40),FUENTE_25,COLOR_NEGRO)


    return retorno













    # mostrar_texto(cuadro_pregunta["superficie"], pregunta_actual["pregunta"], (20, 20), FUENTE_27, COLOR_NEGRO)

    # for i, respuesta in enumerate(lista_respuestas):
    #     texto_respuesta = pregunta_actual[f"respuesta_{i + 1}"]
    #     mostrar_texto(respuesta["superficie"], texto_respuesta, (20, 20), FUENTE_22, COLOR_BLANCO)

    # cuadro_pregunta["rectangulo"] = pantalla.blit(cuadro_pregunta["superficie"], (80, 80))
    
    # Posicionar las respuestas dinámicamente
    # for i, respuesta in enumerate(lista_respuestas):
    #     x = 125
    #     y = 245 + i * 70  # Ajusta la separación entre respuestas
    #     respuesta["rectangulo"] = pantalla.blit(respuesta["superficie"], (x, y))
    #     pygame.draw.rect(pantalla, COLOR_BLANCO, respuesta["rectangulo"], 2)

    # mostrar_texto(pantalla, f"PUNTUACION: {datos_juego['puntuacion']}", (10, 10), FUENTE_25, COLOR_NEGRO)
    # mostrar_texto(pantalla, f"VIDAS: {datos_juego['cantidad_vidas']}", (10, 40), FUENTE_25, COLOR_NEGRO)

