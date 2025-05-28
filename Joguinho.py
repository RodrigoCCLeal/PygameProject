# Exemplo 5 - Mapa com imagens
import pygame
hero_animation_frame = 0
hero_start_frame = 0
hero_pos_x = 1000
hero_pos_y = 225
hero_anim_time = 0
part_animation_frame = 0
part_start_frame = 0
part_pos_x = 400
part_pos_y = 225
part_anim_time = 0
width = 24 * 60
height = 24 * 40
vel = 0.1
mapa = []

def load_mapa(filename):    #Lê o conteúdo do arquivo para a matriz
    global mapa
    file = open(filename,"r")
    for line in file.readlines():
        mapa.append(line)
    file.close()

def load():
    global clock, playerChar, tileset, tile_wdt, clock, spt_hgt,spt_wdt, partChar,part_wdt,part_hgt
    global collider_hero, collider_part, collider_paredeL, collider_paredeU, collider_paredeR, collider_paredeD
    clock = pygame.time.Clock() 
    load_mapa("mapa.txt")
    tileset = pygame.image.load("tilesetMD.png")
    playerChar = pygame.image.load("Mudkip-Idle-Anim.png")
    partChar = pygame.image.load("Chimchar-Idle-Anim.png")
    tile_wdt = tileset.get_width()/16

    spt_wdt = playerChar.get_width()/7
    spt_hgt = playerChar.get_height()/8
    part_wdt = partChar.get_width()/5
    part_hgt = partChar.get_width()/8

    collider_paredeL = pygame.Rect(0, 0, 24, 960)
    collider_paredeU = pygame.Rect(0, 0, 1440, 24)
    collider_paredeR = pygame.Rect(1416, 0, 24, 960)
    collider_paredeD = pygame.Rect(0, 936, 1440, 960)

def update(dt):
    global hero_animation_frame, hero_start_frame, hero_pos_x, hero_pos_y, hero_anim_time, collider_hero
    global part_animation_frame, part_start_frame, part_pos_y, part_pos_x, part_anim_time, collider_part
    keys = pygame.key.get_pressed()
    old_hero_x, old_hero_y = hero_pos_x, hero_pos_y
    old_part_x, old_part_y = part_pos_x, part_pos_y

    #Move Mudkip
    if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        hero_start_frame = 5
        hero_pos_y = hero_pos_y - (vel * dt) # movimenta o personagem
        hero_pos_x = hero_pos_x - (vel * dt) # movimenta o personagem
        hero_anim_time = hero_anim_time + dt #incrementa o tempo usando dt
        if hero_anim_time > 100: #quando acumular mais de 100 ms
            hero_animation_frame = hero_animation_frame + 1 # avança para proximo frame
            if hero_animation_frame > 6: # loop da animação
                hero_animation_frame = 0
            hero_anim_time = 0 #reinicializa a contagem do tempo

    elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        hero_start_frame = 7
        hero_pos_y = hero_pos_y + (vel * dt) # movimenta o personagem
        hero_pos_x = hero_pos_x - (vel * dt) # movimenta o personagem
        hero_anim_time = hero_anim_time + dt #incrementa o tempo usando dt
        if hero_anim_time > 100: #quando acumular mais de 100 ms
            hero_animation_frame = hero_animation_frame + 1 # avança para proximo frame
            if hero_animation_frame > 6: # loop da animação
                hero_animation_frame = 0
            hero_anim_time = 0 #reinicializa a contagem do tempo
    
    elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        hero_start_frame = 3
        hero_pos_y = hero_pos_y - (vel * dt) # movimenta o personagem
        hero_pos_x = hero_pos_x + (vel * dt) # movimenta o personagem
        hero_anim_time = hero_anim_time + dt #incrementa o tempo usando dt
        if hero_anim_time > 100: #quando acumular mais de 100 ms
            hero_animation_frame = hero_animation_frame + 1 # avança para proximo frame
            if hero_animation_frame > 6: # loop da animação
                hero_animation_frame = 0
            hero_anim_time = 0 #reinicializa a contagem do tempo

    elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
        hero_start_frame = 1
        hero_pos_y = hero_pos_y + (vel * dt) # movimenta o personagem
        hero_pos_x = hero_pos_x + (vel * dt) # movimenta o personagem
        hero_anim_time = hero_anim_time + dt #incrementa o tempo usando dt
        if hero_anim_time > 100: #quando acumular mais de 100 ms
            hero_animation_frame = hero_animation_frame + 1 # avança para proximo frame
            if hero_animation_frame > 6: # loop da animação
                hero_animation_frame = 0
            hero_anim_time = 0 #reinicializa a contagem do tempo
    
    elif keys[pygame.K_RIGHT]:
        hero_start_frame = 2
        hero_pos_x = hero_pos_x + (vel * dt) # movimenta o personagem
        hero_anim_time = hero_anim_time + dt #incrementa o tempo usando dt
        if hero_anim_time > 100: #quando acumular mais de 100 ms
            hero_animation_frame = hero_animation_frame + 1 # avança para proximo frame
            if hero_animation_frame > 6: # loop da animação
                hero_animation_frame = 0
            hero_anim_time = 0 #reinicializa a contagem do tempo

    elif keys[pygame.K_LEFT]:
        hero_start_frame = 6
        hero_pos_x = hero_pos_x - (vel * dt) # movimenta o personagem
        hero_anim_time = hero_anim_time + dt #incrementa o tempo usando dt
        if hero_anim_time > 100: #quando acumular mais de 100 ms
            hero_animation_frame = hero_animation_frame + 1 # avança para proximo frame
            if hero_animation_frame > 6: # loop da animação
                hero_animation_frame = 0
            hero_anim_time = 0 #reinicializa a contagem do tempo
    
    elif keys[pygame.K_UP]:
        hero_start_frame = 4
        hero_pos_y = hero_pos_y - (vel * dt) # movimenta o personagem
        hero_anim_time = hero_anim_time + dt #incrementa o tempo usando dt
        if hero_anim_time > 100: #quando acumular mais de 100 ms
            hero_animation_frame = hero_animation_frame + 1 # avança para proximo frame
            if hero_animation_frame > 6: # loop da animação
                hero_animation_frame = 0
            hero_anim_time = 0 #reinicializa a contagem do tempo

    elif keys[pygame.K_DOWN]:
        hero_start_frame = 0
        hero_pos_y = hero_pos_y + (vel * dt) # movimenta o personagem
        hero_anim_time = hero_anim_time + dt #incrementa o tempo usando dt
        if hero_anim_time > 100: #quando acumular mais de 100 ms
            hero_animation_frame = hero_animation_frame + 1 # avança para proximo frame
            if hero_animation_frame > 6: # loop da animação
                hero_animation_frame = 0
            hero_anim_time = 0 #reinicializa a contagem do tempo

    else:
        hero_anim_time = hero_anim_time + dt #incrementa o tempo usando dt
        if hero_anim_time > 100: #quando acumular mais de 100 ms
            hero_animation_frame = hero_animation_frame + 1 # avança para proximo frame
            if hero_animation_frame > 6: # loop da animação
                hero_animation_frame = 0
            hero_anim_time = 0 #reinicializa a contagem do tempo

    #Move Chimchar
    if keys[pygame.K_w] and keys[pygame.K_a]:
        part_start_frame = 5
        part_pos_y = part_pos_y - (vel * dt) # movimenta o personagem
        part_pos_x = part_pos_x - (vel * dt) # movimenta o personagem
        part_anim_time = part_anim_time + dt #incrementa o tempo usando dt
        if part_anim_time > 100: #quando acumular mais de 100 ms
            part_animation_frame = part_animation_frame + 1 # avança para proximo frame
            if part_animation_frame > 4: # loop da animação
                part_animation_frame = 0
            part_anim_time = 0 #reinicializa a contagem do tempo

    elif keys[pygame.K_s] and keys[pygame.K_a]:
        part_start_frame = 7
        part_pos_y = part_pos_y + (vel * dt) # movimenta o personagem
        part_pos_x = part_pos_x - (vel * dt) # movimenta o personagem
        part_anim_time = part_anim_time + dt #incrementa o tempo usando dt
        if part_anim_time > 100: #quando acumular mais de 100 ms
            part_animation_frame = part_animation_frame + 1 # avança para proximo frame
            if part_animation_frame > 4: # loop da animação
                part_animation_frame = 0
            part_anim_time = 0 #reinicializa a contagem do tempo
    
    elif keys[pygame.K_w] and keys[pygame.K_d]:
        part_start_frame = 3
        part_pos_y = part_pos_y - (vel * dt) # movimenta o personagem
        part_pos_x = part_pos_x + (vel * dt) # movimenta o personagem
        part_anim_time = part_anim_time + dt #incrementa o tempo usando dt
        if part_anim_time > 100: #quando acumular mais de 100 ms
            part_animation_frame = part_animation_frame + 1 # avança para proximo frame
            if part_animation_frame > 4: # loop da animação
                part_animation_frame = 0
            part_anim_time = 0 #reinicializa a contagem do tempo

    elif keys[pygame.K_s] and keys[pygame.K_d]:
        part_start_frame = 1
        part_pos_y = part_pos_y + (vel * dt) # movimenta o personagem
        part_pos_x = part_pos_x + (vel * dt) # movimenta o personagem
        part_anim_time = part_anim_time + dt #incrementa o tempo usando dt
        if part_anim_time > 100: #quando acumular mais de 100 ms
            part_animation_frame = part_animation_frame + 1 # avança para proximo frame
            if part_animation_frame > 4: # loop da animação
                part_animation_frame = 0
            part_anim_time = 0 #reinicializa a contagem do tempo
    
    elif keys[pygame.K_d]:
        part_start_frame = 2
        part_pos_x = part_pos_x + (vel * dt) # movimenta o personagem
        part_anim_time = part_anim_time + dt #incrementa o tempo usando dt
        if part_anim_time > 100: #quando acumular mais de 100 ms
            part_animation_frame = part_animation_frame + 1 # avança para proximo frame
            if part_animation_frame > 4: # loop da animação
                part_animation_frame = 0
            part_anim_time = 0 #reinicializa a contagem do tempo

    elif keys[pygame.K_a]:
        part_start_frame = 6
        part_pos_x = part_pos_x - (vel * dt) # movimenta o personagem
        part_anim_time = part_anim_time + dt #incrementa o tempo usando dt
        if part_anim_time > 100: #quando acumular mais de 100 ms
            part_animation_frame = part_animation_frame + 1 # avança para proximo frame
            if part_animation_frame > 4: # loop da animação
                part_animation_frame = 0
            part_anim_time = 0 #reinicializa a contagem do tempo
    
    elif keys[pygame.K_w]:
        part_start_frame = 4
        part_pos_y = part_pos_y - (vel * dt) # movimenta o personagem
        part_anim_time = part_anim_time + dt #incrementa o tempo usando dt
        if part_anim_time > 100: #quando acumular mais de 100 ms
            part_animation_frame = part_animation_frame + 1 # avança para proximo frame
            if part_animation_frame > 4: # loop da animação
                part_animation_frame = 0
            part_anim_time = 0 #reinicializa a contagem do tempo

    elif keys[pygame.K_s]:
        part_start_frame = 0
        part_pos_y = part_pos_y + (vel * dt) # movimenta o personagem
        part_anim_time = part_anim_time + dt #incrementa o tempo usando dt
        if part_anim_time > 100: #quando acumular mais de 100 ms
            part_animation_frame = part_animation_frame + 1 # avança para proximo frame
            if part_animation_frame > 4: # loop da animação
                part_animation_frame = 0
            part_anim_time = 0 #reinicializa a contagem do tempo

    else:
        part_anim_time = part_anim_time + dt #incrementa o tempo usando dt
        if part_anim_time > 100: #quando acumular mais de 100 ms
            part_animation_frame = part_animation_frame + 1 # avança para proximo frame
            if part_animation_frame > 4: # loop da animação
                part_animation_frame = 0
            part_anim_time = 0 #reinicializa a contagem do tempo
    
    
    collider_hero = pygame.Rect(hero_pos_x, hero_pos_y, 24, 24)
    if collider_hero.colliderect(collider_paredeL):
        hero_pos_x = old_hero_x
        hero_pos_y = old_hero_y
    if collider_hero.colliderect(collider_paredeU):
        hero_pos_x = old_hero_x
        hero_pos_y = old_hero_y
    if collider_hero.colliderect(collider_paredeR):
        hero_pos_x = old_hero_x
        hero_pos_y = old_hero_y
    if collider_hero.colliderect(collider_paredeD):
        hero_pos_x = old_hero_x
        hero_pos_y = old_hero_y

    collider_part = pygame.Rect(part_pos_x, part_pos_y, 24, 24)
    if collider_part.colliderect(collider_paredeL):
        part_pos_x = old_part_x
        part_pos_y = old_part_y
    if collider_part.colliderect(collider_paredeU):
        part_pos_x = old_part_x
        part_pos_y = old_part_y
    if collider_part.colliderect(collider_paredeR):
        part_pos_x = old_part_x
        part_pos_y = old_part_y
    if collider_part.colliderect(collider_paredeD):
        part_pos_x = old_part_x
        part_pos_y = old_part_y


    

def draw_screen(screen):
  # Mapa plataforma
  for i, linha in enumerate(mapa):
    for j, char in enumerate(linha):
      if char == "W":
        screen.blit(tileset, (j*tile_wdt, i*tile_wdt), (tile_wdt*2, tile_wdt*0, tile_wdt, tile_wdt))
      elif char == "A":
        screen.blit(tileset, (j*tile_wdt, i*tile_wdt), (tile_wdt*11, tile_wdt, tile_wdt, tile_wdt))
      elif char == "B":
        screen.blit(tileset, (j*tile_wdt, i*tile_wdt), (tile_wdt*2, tile_wdt, tile_wdt, tile_wdt))
      elif char == "1":
        screen.blit(tileset, (j*tile_wdt, i*tile_wdt), (tile_wdt*6, tile_wdt*2, tile_wdt, tile_wdt))
      elif char == "2":
        screen.blit(tileset, (j*tile_wdt, i*tile_wdt), (tile_wdt*7, tile_wdt*2, tile_wdt, tile_wdt))
      elif char == "3":
        screen.blit(tileset, (j*tile_wdt, i*tile_wdt), (tile_wdt*9, tile_wdt*4, tile_wdt, tile_wdt))
      elif char == "4":
        screen.blit(tileset, (j*tile_wdt, i*tile_wdt), (tile_wdt*13, tile_wdt*5, tile_wdt, tile_wdt))
      elif char == "5":
        screen.blit(tileset, (j*tile_wdt, i*tile_wdt), (tile_wdt*10, tile_wdt*5, tile_wdt, tile_wdt))
      elif char == "6":
        screen.blit(tileset, (j*tile_wdt, i*tile_wdt), (tile_wdt*7, tile_wdt*3, tile_wdt, tile_wdt))
      elif char == "7":
        screen.blit(tileset, (j*tile_wdt, i*tile_wdt), (tile_wdt*9, tile_wdt*5, tile_wdt, tile_wdt))
      elif char == "8":
        screen.blit(tileset, (j*tile_wdt, i*tile_wdt), (tile_wdt*6, tile_wdt*3, tile_wdt, tile_wdt))
      elif char == "9":
        screen.blit(tileset, (j*tile_wdt, i*tile_wdt), (tile_wdt*8, tile_wdt*5, tile_wdt, tile_wdt))

  #Desenha personagens      
  screen.blit(playerChar,(hero_pos_x, hero_pos_y),(spt_wdt * hero_animation_frame, hero_start_frame*spt_hgt, spt_wdt,spt_hgt))
  screen.blit(partChar,(part_pos_x, part_pos_y),(part_wdt * part_animation_frame, part_start_frame*spt_hgt, spt_wdt,spt_hgt))
  
#####################################################
# A PRINCIPIO NÃO PRECISA ALTERAR DAQUI PRA BAIXO   #
#####################################################
def main_loop(screen):  
    global clock
    running = True
    while running:
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT: # fechamento do prog
                running = False
                break

        # Define FPS máximo
        clock.tick(60)
        # Tempo transcorrido desde a última atualização 
        dt = clock.get_time()
        # Atualiza posição dos objetos
        update(dt)
        # Desenha objetos
        draw_screen(screen)
        # Pygame atualiza a visualização da tela
        pygame.display.update()

# Programa principal
pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()