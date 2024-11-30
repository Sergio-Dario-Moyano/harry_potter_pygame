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

comodin = {}
comodin["superficie"] = pygame.Surface(TAMAÑO_RESPUESTA)
comodin["rectangulo"] = comodin["superficie"].get_rect()
# comodin["superficie"].fill(255,255,255)

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
acumula_puntos = 0 #acumula aciertos y da una vida cuando hay 5 seguidos
random.shuffle(lista_preguntas)

def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    global indice
    global bandera_respuesta
    # global acumula_puntos


       #TEMPORIZADOR
    #-------------
    superficie_reloj = {}
    superficie_reloj["superficie"] = pygame.Surface((180,50))
    superficie_reloj["rectangulo"] = superficie_reloj["superficie"].get_rect()
    

    
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
                   
                   
                    if respuesta_seleccionada == int(pregunta_actual["respuesta_correcta"]):
                    
                        respuesta_correcta(datos_juego, lista_respuestas, i)
                    #     ACIERTO_SONIDO.play()
                    #     print("RESPUESTA CORRECTA")
                    #     lista_respuestas[i]["superficie"].fill(COLOR_VERDE_OSCURO)
                    #     datos_juego["puntuacion"] += PUNTUACION_ACIERTO
                    #     acumula_puntos += 1

                    #     if acumula_puntos == 5:
                    #         datos_juego["cantidad_vidas"] += 1
                    #         acumula_puntos = 0
                    # else:
                    #     ERROR_SONIDO.play()
                    #     lista_respuestas[i]["superficie"].fill(COLOR_ROJO)
                    #     acumula_puntos = 0
                    else:
                        respuesta_incorrecta(datos_juego, lista_respuestas, i, retorno)
                        
                        # if datos_juego["cantidad_vidas"] > 0:
                        #     datos_juego["cantidad_vidas"] -= 1

                        #     if datos_juego["puntuacion"] > 0:
                        #         datos_juego["puntuacion"] -= PUNTUACION_ERROR

                        #     retorno = "juego"
                            
                        # else:
                         
                        #     retorno = "terminado"
                        #     pedir_nombre(
                        #         "Ingrese su nombre para el ranking: ",
                        #         "!ERROR¡ Nombre demasiado corto, debe tener al menos 3 caracteres. Reingrese un nombre: ",
                        #         datos_juego["puntuacion"]
                        #     )
                            
                    indice += 1
                    
                    if indice == len(lista_preguntas):
                        indice = 0
                        random.shuffle(lista_preguntas)
                        
                    bandera_respuesta = True

    
    pantalla.fill(COLOR_VIOLETA)

    tiempo = dibujar_reloj(pantalla, superficie_reloj, 10, 5000)
    #dibuja las preguntas
    dibujar_preguntas(pantalla,cuadro_pregunta,pregunta_actual)

    dibujar_respuestas(pantalla, lista_respuestas,pregunta_actual)
    
    mostrar_texto(comodin["superficie"], "USAR COMODIN", (20,20), FUENTE_22, COLOR_NEGRO) #-->comodin
    comodin["rectangulo"] = pantalla.blit(comodin["superficie"],(125,535))
    comodin["superficie"].fill(COLOR_VERDE_OSCURO)
    
    mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(10,10),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,f"VIDAS: {datos_juego['cantidad_vidas']}",(10,40),FUENTE_25,COLOR_NEGRO)
    
    return retorno

   