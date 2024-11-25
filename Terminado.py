import pygame 
from Constantes import *
from Funciones import *

pygame.init()

cuadro_texto = {}
#cuadro_texto ["superficie"] = pygame.Surface(CUADRO_TEXTO)
cuadro_texto["superficie"] = pygame.image.load("fondo.jpg")
cuadro_texto["superficie"] = pygame.transform.scale(cuadro_texto["superficie"],CUADRO_TEXTO)
cuadro_texto["rectangulo"] = cuadro_texto["superficie"].get_rect()
#cuadro_texto["superficie"].fill(COLOR_AZUL)
nombre = ""

def mostrar_fin_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    global nombre
    retorno = "terminado"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pass
        elif evento.type == pygame.KEYDOWN:
            #caracter = chr(evento.key)
            tecla_presionada = pygame.key.name(evento.key)
            bloc_mayus = pygame.key.get_mods() and pygame.KMOD_CAPS
            print(tecla_presionada)
            # print(evento.key)
            
            if tecla_presionada == "backspace" and len(nombre) > 0:
                #nombre = 'Mariano' -> 'Marian'
                nombre = nombre[0:-1]
                cuadro_texto["superficie"] = pygame.image.load("fondo.jpg")
                cuadro_texto["superficie"] = pygame.transform.scale(cuadro_texto["superficie"],CUADRO_TEXTO)
                #cuadro_texto["superficie"].fill(COLOR_AZUL)
                #Si su superficie parte de una imagen
                #Tienen que cargar la imagen de nuevo y reescalarla
            
            if tecla_presionada == "space":
                nombre += " "
            
            if len(tecla_presionada) == 1:
                if bloc_mayus != 0:
                    nombre += tecla_presionada.upper()
                else:
                    nombre += tecla_presionada
        
    
    pantalla.fill(COLOR_BLANCO)
    cuadro_texto["rectangulo"] = pantalla.blit(cuadro_texto["superficie"],(200,200))
    mostrar_texto(cuadro_texto["superficie"],nombre,(10,0),FUENTE_40,COLOR_BLANCO)
    mostrar_texto(pantalla,f"USTED OBTUVO {datos_juego["puntuacion"]} PUNTOS",(250,50),FUENTE_32,COLOR_NEGRO)
    
    return retorno