import pygame
hero_animation_frame = 0
hero_start_frame = 0
hero_pos_x = 1000
hero_pos_y = 425
hero_anim_time = 0
part_animation_frame = 0
part_start_frame = 0
part_pos_x = 400
part_pos_y = 425
part_anim_time = 0
width = 24 * 60
height = 24 * 40
velH = 0.1
velP = 0.1
mapa = []
lColliders = []
lAguaCol = []
    

def load_mapa(filename):    #Lê o conteúdo do arquivo para a matriz
    global mapa
    file = open(filename,"r")
    for line in file.readlines():
        mapa.append(line)
    file.close()

def load():
    global clock, playerChar, tileset, tile_wdt, clock, spt_hgt,spt_wdt, partChar,part_wdt,part_hgt
    global collider_hero, collider_part
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


    for (x,l) in enumerate(mapa):
        for (y,c) in enumerate(l):
            if c == "W":
                parede = pygame.Rect(y*24, x*24, 24, 24)
                lColliders.append(parede)
            elif c == "9":
                parede = pygame.Rect(y*24, x*24, 24, 24)
                lAguaCol.append(parede)
        


def update(dt):
    global hero_animation_frame, hero_start_frame, hero_pos_x, hero_pos_y, hero_anim_time, collider_hero, velH
    global part_animation_frame, part_start_frame, part_pos_y, part_pos_x, part_anim_time, collider_part, velP
    keys = pygame.key.get_pressed()
    old_hero_x, old_hero_y = hero_pos_x, hero_pos_y
    old_part_x, old_part_y = part_pos_x, part_pos_y

    # Colisão
    collider_hero = pygame.Rect(hero_pos_x, hero_pos_y, 24, 24)
    collider_part = pygame.Rect(part_pos_x, part_pos_y, 24, 24)

    if collider_hero.collidelist(lColliders) >= 0:
        hero_pos_x = old_hero_x
        hero_pos_y = old_hero_y

    if collider_hero.collidelist(lAguaCol) >= 0:
        velH = 0.15
    else:
       velH = 0.1

        
    if collider_part.collidelist(lColliders) >= 0:
        part_pos_x = old_part_x
        part_pos_y = old_part_y

    #Move Mudkip
    if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        hero_start_frame = 5
        hero_pos_y = hero_pos_y - (velH * dt)
        hero_pos_x = hero_pos_x - (velH * dt)

    elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        hero_start_frame = 7
        hero_pos_y = hero_pos_y + (velH * dt)
        hero_pos_x = hero_pos_x - (velH * dt)
    
    elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        hero_start_frame = 3
        hero_pos_y = hero_pos_y - (velH * dt)
        hero_pos_x = hero_pos_x + (velH * dt)

    elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
        hero_start_frame = 1
        hero_pos_y = hero_pos_y + (velH * dt)
        hero_pos_x = hero_pos_x + (velH * dt)
    
    elif keys[pygame.K_RIGHT]:
        hero_start_frame = 2
        hero_pos_x = hero_pos_x + (velH * dt)

    elif keys[pygame.K_LEFT]:
        hero_start_frame = 6
        hero_pos_x = hero_pos_x - (velH * dt)
    
    elif keys[pygame.K_UP]:
        hero_start_frame = 4
        hero_pos_y = hero_pos_y - (velH * dt)

    elif keys[pygame.K_DOWN]:
        hero_start_frame = 0
        hero_pos_y = hero_pos_y + (velH * dt)

    hero_anim_time = hero_anim_time + dt 
    if hero_anim_time > 100: 
        hero_animation_frame = hero_animation_frame + 1 
        if hero_animation_frame > 6: 
            hero_animation_frame = 0
        hero_anim_time = 0 

    #Move Chimchar
    if keys[pygame.K_w] and keys[pygame.K_a]:
        part_start_frame = 5
        part_pos_y = part_pos_y - (velP * dt)
        part_pos_x = part_pos_x - (velP * dt)
         

    elif keys[pygame.K_s] and keys[pygame.K_a]:
        part_start_frame = 7
        part_pos_y = part_pos_y + (velP * dt)
        part_pos_x = part_pos_x - (velP * dt)
         
    
    elif keys[pygame.K_w] and keys[pygame.K_d]:
        part_start_frame = 3
        part_pos_y = part_pos_y - (velP * dt)
        part_pos_x = part_pos_x + (velP * dt)
         

    elif keys[pygame.K_s] and keys[pygame.K_d]:
        part_start_frame = 1
        part_pos_y = part_pos_y + (velP * dt)
        part_pos_x = part_pos_x + (velP * dt)
         
    
    elif keys[pygame.K_d]:
        part_start_frame = 2
        part_pos_x = part_pos_x + (velP * dt)
         

    elif keys[pygame.K_a]:
        part_start_frame = 6
        part_pos_x = part_pos_x - (velP * dt)
         
    
    elif keys[pygame.K_w]:
        part_start_frame = 4
        part_pos_y = part_pos_y - (velP * dt)
         

    elif keys[pygame.K_s]:
        part_start_frame = 0
        part_pos_y = part_pos_y + (velP * dt)
         
    part_anim_time = part_anim_time + dt 
    if part_anim_time > 100: 
        part_animation_frame = part_animation_frame + 1 
        if part_animation_frame > 4: 
            part_animation_frame = 0
        part_anim_time = 0


    


    

def draw_screen(screen):
  
  # Mapa
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
  

# Pygame
def main_loop(screen):  
    global clock
    running = True
    while running:
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT: # fecha o jogo
                running = False
                break

        # FPS máximo
        clock.tick(60)
        # Tempo entre frames 
        dt = clock.get_time()
        # Atualiza posição dos objetos
        update(dt)
        # Desenha objetos
        draw_screen(screen)
        # Update da tela
        pygame.display.update()

# Programa principal
pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()

## Debug
