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



    cuadro_p = {}
    for datos in ranking:
      
        cuadro_p["superficie"] = pygame.image.load("fondo.jpg")
        cuadro_p["superficie"] = pygame.transform.scale(cuadro_p["superficie"],TAMAÑO_PREGUNTA)

        mostrar_texto(cuadro_p["superficie"], datos['nombre'],(80,80),FUENTE_50, COLOR_VERDE_OSCURO)

        pantalla.blit(cuadro_p["superficie"], (200,200))
        
      

    pygame.display.flip()
    # pantalla.fill(COLOR_BLANCO)
    # boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))

   
    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_22,COLOR_BLANCO)
    # mostrar_texto(pantalla,f"ACA DEBEN MOSTRAR EL TOP 10",(20,200),FUENTE_32,COLOR_NEGRO)

    return retorno