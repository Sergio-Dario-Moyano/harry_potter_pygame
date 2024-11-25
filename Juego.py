import pygame 
import random
from Funciones import *
from Preguntas import *

pygame.init()
cuadro_pregunta = {}
#cuadro_pregunta["superficie"] = pygame.Surface(TAMAÑO_PREGUNTA)
cuadro_pregunta["superficie"] = pygame.image.load("fondo.jpg")
cuadro_pregunta["superficie"] = pygame.transform.scale(cuadro_pregunta["superficie"],TAMAÑO_PREGUNTA)
cuadro_pregunta["rectangulo"] = cuadro_pregunta["superficie"].get_rect()
#cuadro_pregunta["superficie"].fill(COLOR_ROJO)

lista_respuestas = []

# for i in range(3): --> original
for i in range(4):
    cuadro_respuesta = {}
    cuadro_respuesta["superficie"] = pygame.Surface(TAMAÑO_RESPUESTA)
    cuadro_respuesta["rectangulo"] = cuadro_respuesta["superficie"].get_rect()
    cuadro_respuesta["superficie"].fill(COLOR_AZUL)
    lista_respuestas.append(cuadro_respuesta)

indice = 0 #Son inmutables
bandera_respuesta = False #Son inmutables
acumula_puntos = 0
random.shuffle(lista_preguntas)

def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    global indice
    global bandera_respuesta
    global acumula_puntos

    print(f"DATOS DEL JUEGO: {len(lista_respuestas)}")
    
    retorno = "juego"
    if bandera_respuesta:
        pygame.time.delay(250)
        #cuadro_pregunta["superficie"].fill(COLOR_ROJO)
        #Limpio la superficie
        cuadro_pregunta["superficie"] = pygame.image.load("fondo.jpg")
        cuadro_pregunta["superficie"] = pygame.transform.scale(cuadro_pregunta["superficie"],TAMAÑO_PREGUNTA)
        for i in range(len(lista_respuestas)):
            lista_respuestas[i]["superficie"].fill(COLOR_AZUL)
        bandera_respuesta = False
    
    pregunta_actual = lista_preguntas[indice]
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(lista_respuestas)):
                if lista_respuestas[i]["rectangulo"].collidepoint(evento.pos):
                    respuesta_seleccionada = (i + 1)

                    print(f"Respuesta correcta: {pregunta_actual["respuesta_correcta"]}")
                    print(f"Respuesta seleccionada: {respuesta_seleccionada}")
                   
                    if respuesta_seleccionada == int(pregunta_actual["respuesta_correcta"]):
                    
                        ACIERTO_SONIDO.play()
                        print("RESPUESTA CORRECTA")
                        lista_respuestas[i]["superficie"].fill(COLOR_VERDE_OSCURO)
                        datos_juego["puntuacion"] += PUNTUACION_ACIERTO
                        acumula_puntos += 1

                        if acumula_puntos == 5:
                            datos_juego["cantidad_vidas"] += 1
                            acumula_puntos = 0
                    else:
                        ERROR_SONIDO.play()
                        lista_respuestas[i]["superficie"].fill(COLOR_ROJO)
                        acumula_puntos = 0

                        
                        if datos_juego["cantidad_vidas"] > 1:
                            datos_juego["cantidad_vidas"] -= 1

                            if datos_juego["puntuacion"] > 0:
                                datos_juego["puntuacion"] -= PUNTUACION_ERROR
                            retorno = "juego"
                            print(f"RESPUESTA INCORRECTA! Te quedan {datos_juego['cantidad_vidas']} vidas")

                        else:
                            retorno = "terminado"
                            
                    indice += 1
                    
                    if indice == len(lista_preguntas):
                        indice = 0
                        random.shuffle(lista_preguntas)
                        
                    bandera_respuesta = True

    
    pantalla.fill(COLOR_VIOLETA)
    #pantalla.blit(fondo,(0,0))
    
    mostrar_texto(cuadro_pregunta["superficie"],f"{pregunta_actual["pregunta"]}",(20,20),FUENTE_27,COLOR_NEGRO)
    mostrar_texto(lista_respuestas[0]["superficie"],f"{pregunta_actual["respuesta_1"]}",(20,20),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[1]["superficie"],f"{pregunta_actual["respuesta_2"]}",(20,20),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[2]["superficie"],f"{pregunta_actual["respuesta_3"]}",(20,20),FUENTE_22,COLOR_BLANCO)

    mostrar_texto(lista_respuestas[3]["superficie"],f"{pregunta_actual["respuesta_4"]}",(20,20),FUENTE_22,COLOR_BLANCO)
    

    
    cuadro_pregunta["rectangulo"] = pantalla.blit(cuadro_pregunta["superficie"],(80,80))
    lista_respuestas[0]["rectangulo"] = pantalla.blit(lista_respuestas[0]["superficie"],(125,245))#r1
    lista_respuestas[1]["rectangulo"] = pantalla.blit(lista_respuestas[1]["superficie"],(125,315))#r2
    lista_respuestas[2]["rectangulo"] = pantalla.blit(lista_respuestas[2]["superficie"],(125,385))#r3

    lista_respuestas[3]["rectangulo"] = pantalla.blit(lista_respuestas[3]["superficie"],(125,455))#r4


    

    pygame.draw.rect(pantalla,COLOR_NEGRO,cuadro_pregunta["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[0]["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[1]["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[2]["rectangulo"],2)

    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[3]["rectangulo"],2)
    
    mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(10,10),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,f"VIDAS: {datos_juego['cantidad_vidas']}",(10,40),FUENTE_25,COLOR_NEGRO)
    
    return retorno