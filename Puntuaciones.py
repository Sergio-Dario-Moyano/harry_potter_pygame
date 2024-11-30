import pygame
from Constantes import *
from Funciones import *
import json
from datetime import datetime
import os


pygame.init()

boton_volver = {}
boton_volver["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()
boton_volver["superficie"].fill(COLOR_AZUL)

def mostrar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    retorno = "puntuaciones"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"


    archivo_json = "partidas.json"
    if os.path.exists(archivo_json):
        with open(archivo_json, "r", encoding="utf-8") as archivo:
            try:
                ranking = json.load(archivo)
            except json.JSONDecodeError:
                ranking = []
    else:
        ranking = []

    lista_res = []

    for i in range(len(ranking)):
        cuadro = {}
        cuadro["superficie"] = pygame.Surface(TAMAÑO_RANKING)
        cuadro["rectangulo"] = cuadro["superficie"].get_rect()
        cuadro["superficie"].fill(COLOR_AZUL)
        lista_res.append(cuadro)


    fondo_img = pygame.image.load("fondo-harry.jpg")
    fondo_img = pygame.transform.scale(fondo_img,VENTANA)

    # pantalla.fill(COLOR_BLANCO)
    pantalla.blit(fondo_img, (0,0))
    
    cuadro_error = {}
    cuadro_error["superficie"] = pygame.Surface(VENTANA)
    cuadro_error["rectangulo"] = cuadro_error["superficie"].get_rect()
    if len(ranking) == 0:
        texto_error = "¡¡¡ERROR!!! Aun no hay datos cargados en el ranking!"
        mostrar_texto(cuadro_error["superficie"],texto_error,(50,200),FUENTE_30,COLOR_ROJO)
        pantalla.fill(COLOR_BLANCO)
        cuadro_error["rectangulo"] = pantalla.blit(cuadro_error["superficie"],(0,50))

    else:
        contador = 0
        for i in range(len(ranking)):
            contador += 100

            mostrar_texto(lista_res[i]["superficie"],f"Nombre: {ranking[i]["nombre"]}",(50,0),FUENTE_18,COLOR_NEGRO) #--> muestra el texto
            mostrar_texto(lista_res[i]["superficie"],f"Fecha de juego: {ranking[i]["fecha"]}",(50,20),FUENTE_18,COLOR_NEGRO) #--> muestra el texto
            mostrar_texto(lista_res[i]["superficie"],f"Puntos: {ranking[i]["puntos"]}",(50,40),FUENTE_18,COLOR_NEGRO) #--> muestra el texto

            lista_res[i]["rectangulo"] = pantalla.blit(lista_res[i]["superficie"], (180 , contador ))#r1


            pygame.draw.rect(pantalla,COLOR_BLANCO,lista_res[i]["rectangulo"],2)


    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))
    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_22,COLOR_BLANCO)


    pygame.display.flip()
    return retorno