import pygame
import random
pygame.init()
pygame.mixer.init()
ANCHO = 800
ALTO = 600
FPS = 60
COLOR_ROSA = "#ff00bb"
COLOR_NEGRO = "#000000"
COLOR_AZUL = "#3333FF" 
VENTANA = (ANCHO,ALTO)

pygame.display.set_caption("MI TITULO DEL JUEGO")
icono = pygame.image.load("icono.png")
pygame.display.set_icon(icono)


# 1 Configurar pantalla
pantalla = pygame.display.set_mode(VENTANA)
corriendo =  True
#Creo un reloj para medir el tiempo en nuestro juego
clock = pygame.time.Clock()

fondo = pygame.image.load("fondo.jpg")
fondo = pygame.transform.scale(fondo,VENTANA)

# cargar imagen
homero = pygame.image.load("homero.png")
# redimensionar imagen
homero = pygame.transform.scale(homero,(100,150))

# El rectangulo permite el movimiento (toma las medidas del emento que represente, en este caso, homero 100x150)
# Con este elemento ahora podemos darle movimiento a la imagen de homero
rectangulo_homero = homero.get_rect()
rectangulo_homero.x = 100
rectangulo_homero.y = 450



contador_tiempo = 5
# generar texto
fuente = pygame.font.SysFont("Arial",25)
texto = fuente.render(f"TIEMPO PASADO : {contador_tiempo} SEGUNDOS",False, COLOR_NEGRO)

# crear superficie
mi_superficie = pygame.Surface((100,150))
mi_superficie.fill("#3333FF")

#Sonidos
# guaradrlo en la variable
sonido_click = pygame.mixer.Sound("click.mp3")
sonido_click.set_volume(0.5)

# Sonido de fondo
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1) #con -1 se ejecuta el loop

#Eventos propios (ocurren cuando pasa un X tiempo)
evento_tiempo_1s = pygame.USEREVENT #devuelve el numero 32866
pygame.time.set_timer(evento_tiempo_1s,1000)

evento_tiempo_5s = pygame.USEREVENT + 1 
pygame.time.set_timer(evento_tiempo_5s,5000,1) #El 1 hace que se ejecute solo 1 vez


pared = pygame.Surface((150,250))
pared.fill(COLOR_AZUL)
#construimos un rectangulo que contenga a pared para poder darle movimiento
#ES ENCESARIO CREAR UN RECTANGULO PARA TOOODO LO QUE QUERRAMOS MOVER
pared_rectangulo = pared.get_rect()
pared_rectangulo.x = 400
pared_rectangulo.y = 300



# 2 Bucle principal
while corriendo:

  # if contador_tiempo == 0:
  #   corriendo = False
  # 3 manejo de eventos
  for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
      print("SALIENDO")
      corriendo = False
    if evento.type == pygame.MOUSEBUTTONDOWN:
      print(evento.pos)
      sonido_click.play()
      #mueve el rectangulo al lugar donde hacemos click
      # rectangulo_homero.x = evento.pos[0] #evento.pos --> devuelve una tupla con las coordenadas de movimiento
      # rectangulo_homero.y = evento.pos[1] #devuelve una tupla con las coordenadas de movimiento

      #colision de elementos (Los elementos reaccionan al Click)
      # if rectangulo_homero.collidepoint(evento.pos):
        # print("Se le dio click a homero")
        # rectangulo_homero.x = random.randint(0,400)
        # rectangulo_homero.y = random.randint(100,500)
    if evento.type == pygame.KEYDOWN:
      # print("Se toco una tecla")
      if evento.key == pygame.K_SPACE: #K_SPACE se puede cambiar por el numero en codigo ASCII
        # print("Se toco la tecla espacio")
        rectangulo_homero.y -= 10

      # if evento.key == pygame.K_LEFT:
      #    if rectangulo_homero.left > 0:
      #     rectangulo_homero.left -= 5 # ---> mueve la imagen a la izquierda

      # if evento.key == pygame.K_RIGHT:
      #    if rectangulo_homero.right < 495:
      #     rectangulo_homero.right += 5 # ---> mueve la imagen a la derecha


    # if evento.type == evento_tiempo_1s:
    #   print("PASO 1 SEGUNDO")
      # contador_tiempo -= 1
    #   texto = fuente.render(f"TIEMPO PASADO : {contador_tiempo} SEGUNDOS",False, COLOR_NEGRO)
    # if evento.type == evento_tiempo_5s:
    #   print("PASO 5 SEGUNDO")

    #gardamos tods las teclas en esta variable telas
  teclas = pygame.key.get_pressed()
    # preguntamos si la tecla seleccionada es <- flecha izquierda
  if teclas[pygame.K_LEFT]:
    # lo que pasa al tocar la pared
    # if rectangulo_homero.colliderect(pared_rectangulo):
    #   print("CHOCO")
    # else:
      if rectangulo_homero.left >= 0:
        rectangulo_homero.left -= 2
      else:
        rectangulo_homero.right +=2

  # preguntamos si la tecla seleccionada es -> flecha derecha
  if teclas[pygame.K_RIGHT]:
    if rectangulo_homero.colliderect(pared_rectangulo):
      rectangulo_homero.left -= 5
    else:
      if rectangulo_homero.right <= 450:
        rectangulo_homero.right += 2
      else:
        rectangulo_homero.right -=2



  # 4 Actualizar juego
  #El bucle se va a repetir X veces (fotogramas) por segundo
  clock.tick(FPS)

  # 5 Dibujar los elementos en pantalla
  pantalla.fill(COLOR_ROSA)

  # colocar fondo/imagen
  pantalla.blit(fondo,(0,0))
  # colocar nuevo fondo sobre el ya existente
  pantalla.blit(mi_superficie,(550,50))
  # coloco la imagen de homero sobre el fondo
  # pantalla.blit(homero,(100,450)) # ---> imagen fija de homero
  pantalla.blit(homero,(rectangulo_homero.x,rectangulo_homero.y)) # ---> imagen que se mueve junto al rectangulo creado
  # coloco texto
  pantalla.blit(texto,(20,20))

  # coloco "pared"
  # pantalla.blit(pared,(400,300))

  # pared con comportamiento
  pantalla.blit(pared,(pared_rectangulo.x,pared_rectangulo.y))



  #Este rectangulo solo se muestra en modo desarrollo, una vez que tenemos el
  #comportamiento que deseamos, tenemos que ocultarlo/borrarlo/comentarlo.
  # pygame.draw.rect(pantalla,"#FF0000",rectangulo_homero,2)

  # dibujar un circulo
  # pygame.draw.circle(pantalla,COLOR_ROSA,(100,250),200)
  # dibujar un rectangulo
  # pygame.draw.rect(pantalla,COLOR_ROSA,(300,300,300,300))


  # 6 cttalizar la pantalla
  pygame.display.flip()




# 7 Terminar juego
pygame.quit()