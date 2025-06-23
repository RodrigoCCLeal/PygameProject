import pygame
import random
p1_animation_frame = 0
p1_start_frame = 0
p1_pos_x = 1000
p1_pos_y = 475
p1_anim_time = 0
p2_animation_frame = 0
p2_start_frame = 0
p2_pos_x = 400
p2_pos_y = 475
p2_anim_time = 0
width = 24 * 60
height = 24 * 40
vel1 = 0.1
vel2 = 0.12
tempoRestante = 180000
cont = 0
minutos = 3
segundos = 0
mapa = []
lColliders = []
lAguaCol = []
timerItem = 0
lMacaCol = []
pontP1 = 0
pontP2 = 0

def load_mapa(filename):    #Lê o conteúdo do arquivo para a matriz
    global mapa
    file = open(filename,"r")
    for line in file.readlines():
        mapa.append(line)
    file.close()

def load():
    global clock, p1CharAnim, tileset, tile_wdt,tile_hgt, clock, p1_hgt,p1_wdt,p2_wdt,p2_hgt, p1CharAnim, p1Mon,  p2CharAnim, p2Mon, font
    global collider_p1, collider_p2, maca, item_wdt, item_hgt, tempoRestante, port1_wdt, port1_hgt, port2_wdt, port2_hgt

    clock = pygame.time.Clock() 
    load_mapa("mapas\mapadesenhado.txt")
    tileset = pygame.image.load("mapas\meadowTileset.png")

    mudkip = {"idle":{"spriteSheet": pygame.image.load("spritesMons\mudkip\Mudkip-Idle-Anim.png"), "largura": 7, "altura": 8, "frameReset": 6, "animTime": 100 }, "sleep":{"spriteSheet": pygame.image.load("spritesMons\mudkip\Mudkip-Sleep-Anim.png"), "largura": 2, "altura": 1, "frameReset": 1, "animTime": 500 }, "walk":{ "spriteSheet": pygame.image.load("spritesMons\mudkip\Mudkip-Walk-Anim.png"), "largura": 6, "altura": 8, "frameReset": 5, "animTime": 100 }, "portrait": {"spriteSheet": pygame.image.load("spritesMons\mudkip\mudkip_portrait.png"), "largura": 5, "altura": 8}}
    chimchar = {"idle":{"spriteSheet": pygame.image.load("spritesMons\chimchar\Chimchar-Idle-Anim.png"), "largura": 5, "altura": 8, "frameReset": 4, "animTime": 100 }, "sleep":{"spriteSheet": pygame.image.load("spritesMons\chimchar\Chimchar-Sleep-Anim.png"), "largura": 2, "altura": 1, "frameReset": 1, "animTime": 500 }, "walk":{ "spriteSheet": pygame.image.load("spritesMons\chimchar\Chimchar-Walk-Anim.png"), "largura": 7, "altura": 8, "frameReset": 6, "animTime": 100 },
                "strike":{"spriteSheet": pygame.image.load("spritesMons\chimchar\Chimchar-Strike-Anim.png"), "largura": 10, "altura": 8, "frameReset": 9, "animTime": 75 }, "portrait": {"spriteSheet": pygame.image.load("spritesMons\chimchar\chimchar_portrait.png"), "largura": 5, "altura": 8}}
    
    p1Mon = mudkip
    p2Mon = chimchar
    p1CharAnim = p1Mon["idle"]
    p2CharAnim = p2Mon["idle"]
    
    tile_wdt = tileset.get_width()/16
    tile_hgt = tileset.get_height()/25
    
    port1_wdt = p1Mon["portrait"]["spriteSheet"].get_width()/p1Mon["portrait"]["largura"]
    port1_hgt = p1Mon["portrait"]["spriteSheet"].get_height()/p1Mon["portrait"]["altura"]

    port2_wdt = p2Mon["portrait"]["spriteSheet"].get_width()/p2Mon["portrait"]["largura"]
    port2_hgt = p2Mon["portrait"]["spriteSheet"].get_height()/p2Mon["portrait"]["altura"]

    font = pygame.font.Font("PKMN-Mystery-Dungeon.ttf", 75)

    maca = pygame.image.load("objects\Apple.png")
    item_wdt = maca.get_width()
    item_hgt = maca.get_height()

    for (y,l) in enumerate(mapa):
        for (x,c) in enumerate(l):
            parede = pygame.Rect(x*tile_wdt, y*tile_hgt, tile_wdt, tile_hgt)            
            if c == "W":
               lColliders.append(parede)
            elif c == "9":
                lAguaCol.append(parede)


        


def update(dt):
    global p1_animation_frame, p1_start_frame, p1_pos_x, p1_pos_y, p1_anim_time, collider_p1, p1CharAnim, p1Mon, p1_wdt, p1_hgt, p1PortraitFrame
    global p2_animation_frame, p2_start_frame, p2_pos_y, p2_pos_x, p2_anim_time, collider_p2, p2CharAnim, p2Mon, p2_wdt, p2_hgt, p2PortraitFrame
    global minutos, segundos, cont, timerItem, pontP1, pontP2, cronometro, pontosP1, pontosP2, tempoRestante, tempoPercent
    keys = pygame.key.get_pressed()

    tempoRestante -= dt
    tempoPercent = tempoRestante/1800
    cont = cont + dt
    if cont >= 1000:
        cont = 0
        if segundos == 0:
            minutos -= 1
            segundos = 60
        segundos -= 1
    
    old_p1_x, old_p1_y = p1_pos_x, p1_pos_y
    old_p2_x, old_p2_y = p2_pos_x, p2_pos_y

    p1PortraitFrame = 0
    p2PortraitFrame = 0

    #Move P1
    if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        p1CharAnim = p1Mon["walk"]
        p1_start_frame = 5
        p1_pos_y = p1_pos_y - (vel1 * dt)
        p1_pos_x = p1_pos_x - (vel1 * dt)
    elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        p1CharAnim = p1Mon["walk"]
        p1_start_frame = 7
        p1_pos_y = p1_pos_y + (vel1 * dt)
        p1_pos_x = p1_pos_x - (vel1 * dt)
    elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        p1CharAnim = p1Mon["walk"]
        p1_start_frame = 3
        p1_pos_y = p1_pos_y - (vel1 * dt)
        p1_pos_x = p1_pos_x + (vel1 * dt)
    elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
        p1CharAnim = p1Mon["walk"]
        p1_start_frame = 1
        p1_pos_y = p1_pos_y + (vel1 * dt)
        p1_pos_x = p1_pos_x + (vel1 * dt)
    elif keys[pygame.K_RIGHT]:
        p1CharAnim = p1Mon["walk"]
        p1_start_frame = 2
        p1_pos_x = p1_pos_x + (vel1 * dt)
    elif keys[pygame.K_LEFT]:
        p1CharAnim = p1Mon["walk"]
        p1_start_frame = 6
        p1_pos_x = p1_pos_x - (vel1 * dt) 
    elif keys[pygame.K_UP]:
        p1CharAnim = p1Mon["walk"]
        p1_start_frame = 4
        p1_pos_y = p1_pos_y - (vel1 * dt)
    elif keys[pygame.K_DOWN]:
        p1CharAnim = p1Mon["walk"]
        p1_start_frame = 0
        p1_pos_y = p1_pos_y + (vel1 * dt)
    elif p1_animation_frame == 0:
        p1CharAnim = p1Mon["idle"]


    #Move Parceiro
    if keys[pygame.K_w] and keys[pygame.K_a]:
        p2CharAnim = p2Mon["walk"]
        p2_start_frame = 5
        p2_pos_y = p2_pos_y - (vel2 * dt)
        p2_pos_x = p2_pos_x - (vel2 * dt)
    elif keys[pygame.K_s] and keys[pygame.K_a]:
        p2CharAnim = p2Mon["walk"]
        p2_start_frame = 7
        p2_pos_y = p2_pos_y + (vel2 * dt)
        p2_pos_x = p2_pos_x - (vel2 * dt)
    elif keys[pygame.K_w] and keys[pygame.K_d]:
        p2CharAnim = p2Mon["walk"]
        p2_start_frame = 3
        p2_pos_y = p2_pos_y - (vel2 * dt)
        p2_pos_x = p2_pos_x + (vel2 * dt)
    elif keys[pygame.K_s] and keys[pygame.K_d]:
        p2CharAnim = p2Mon["walk"]
        p2_start_frame = 1
        p2_pos_y = p2_pos_y + (vel2 * dt)
        p2_pos_x = p2_pos_x + (vel2 * dt)
    elif keys[pygame.K_d]:
        p2CharAnim = p2Mon["walk"]
        p2_start_frame = 2
        p2_pos_x = p2_pos_x + (vel2 * dt)
    elif keys[pygame.K_a]:
        p2CharAnim = p2Mon["walk"]
        p2_start_frame = 6
        p2_pos_x = p2_pos_x - (vel2 * dt)
    elif keys[pygame.K_w]:
        p2CharAnim = p2Mon["walk"]
        p2_start_frame = 4
        p2_pos_y = p2_pos_y - (vel2 * dt)
    elif keys[pygame.K_s]:
        p2CharAnim = p2Mon["walk"]
        p2_start_frame = 0
        p2_pos_y = p2_pos_y + (vel2 * dt)
    elif keys[pygame.K_z]:
        p2CharAnim = p2Mon["strike"]
    elif p2_animation_frame == 0:
        p2CharAnim = p2Mon["idle"]
         

    #Animação
    p1_anim_time = p1_anim_time + dt 
    if p1_anim_time > p1CharAnim["animTime"]: 
        p1_animation_frame = p1_animation_frame + 1 
        if p1_animation_frame > p1CharAnim["frameReset"]: 
            p1_animation_frame = 0
        p1_anim_time = 0 

    p2_anim_time = p2_anim_time + dt 
    if p2_anim_time > p2CharAnim["animTime"]: 
        p2_animation_frame = p2_animation_frame + 1 
        if p2_animation_frame > p2CharAnim["frameReset"]: 
            p2_animation_frame = 0
        p2_anim_time = 0

    # Altura e Largura das Sprites
    p1_wdt = p1CharAnim["spriteSheet"].get_width()/(p1CharAnim["largura"])
    p1_hgt = p1CharAnim["spriteSheet"].get_height()/(p1CharAnim["altura"])
    p2_wdt = p2CharAnim["spriteSheet"].get_width()/(p2CharAnim["largura"])
    p2_hgt = p2CharAnim["spriteSheet"].get_height()/(p2CharAnim["altura"])

    #Timer
    if minutos < 10 and segundos < 10:
        cronometro = font.render("0%d:0%d"%(minutos,segundos), "False", "white")
    elif segundos < 10:
        cronometro = font.render("%d:0%d"%(minutos,segundos), "False", "white")
    elif minutos < 10:
        cronometro = font.render("0%d:%d"%(minutos,segundos), "False", "white")
    
    #Pontuações
    pontosP1 = font.render("%d"%pontP1, "False", "blue")
    pontosP2 = font.render("%d"%pontP2, "False", "orange")

    #Criando maçãs
    timerItem += dt
    if timerItem > 2000:
        item = pygame.Rect(random.randint(72,1342), random.randint(72,858), item_wdt, item_hgt)
        lMacaCol.append(item)
        timerItem = 0


    # Colisão
    collider_p1 = pygame.Rect(p1_pos_x-(p1_wdt//4), p1_pos_y-(p1_hgt//4), p1_wdt*0.5, p1_hgt*0.4)
    collider_p2 = pygame.Rect(p2_pos_x-(p2_wdt//4), p2_pos_y-(p2_hgt//4), p2_wdt*0.5, p2_hgt*0.4)
    
    if collider_p1.collidelist(lColliders) >= 0:
        p1_pos_x = old_p1_x
        p1_pos_y = old_p1_y
    elif collider_p1.collidelist(lMacaCol) >= 0:
        pontP1 += 1
        lMacaCol.remove(lMacaCol[collider_p1.collidelist(lMacaCol)])
        collect_sound.play()
        
    if collider_p2.collidelist(lColliders) >= 0:
        p2_pos_x = old_p2_x
        p2_pos_y = old_p2_y
    elif collider_p2.collidelist(lAguaCol) >= 0:
        p2_pos_x = old_p2_x
        p2_pos_y = old_p2_y
    elif collider_p2.collidelist(lMacaCol) >= 0:
        pontP2 += 1
        lMacaCol.remove(lMacaCol[collider_p2.collidelist(lMacaCol)])
        collect_sound.play()



    

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
            elif char == "9":
                screen.blit(tileset, (j*tile_wdt, i*tile_wdt), (tile_wdt*8, tile_wdt*5, tile_wdt, tile_wdt))
            elif char == "V":
                screen.blit(tileset, (j*tile_wdt, i*tile_wdt), (tile_wdt*0, tile_wdt*0, tile_wdt, tile_wdt))


    #Desenha personagens      
    screen.blit(p1CharAnim["spriteSheet"],(p1_pos_x-(p1_wdt//2), p1_pos_y-(p1_hgt//2)),(p1_animation_frame*p1_wdt, p1_start_frame*p1_hgt, p1_wdt,p1_hgt))
    screen.blit(p2CharAnim["spriteSheet"],(p2_pos_x-(p2_wdt//2), p2_pos_y-(p2_hgt//2)),(p2_animation_frame*p2_wdt, p2_start_frame*p2_hgt, p2_wdt,p2_hgt))

    # Hitbux Debug
    pygame.draw.rect(screen, "red", collider_p1)
    pygame.draw.rect(screen, "red", collider_p2)



    #Desenha objetos
    for i in lMacaCol:
        screen.blit(maca,(i.left, i.top),(0, 0, item_wdt, item_hgt))
    

    #Desenha contadores
    screen.blit(cronometro, cronometro.get_rect(top=0, left=640))

    #Barrinha
    pygame.draw.rect(screen, ("black"), (650,50,100,24))
    if tempoPercent >= 30:
        pygame.draw.rect(screen, ("pink"), (650,50,tempoPercent,24))
    else:
        pygame.draw.rect(screen, ("red"), (650,50,tempoPercent,24))

    #Desenha pontuação
    screen.blit(p1Mon["portrait"]["spriteSheet"],(1300,7),(p1PortraitFrame*port1_wdt, p1PortraitFrame*port1_hgt, port1_wdt,port1_hgt))
    screen.blit(pontosP1, pontosP1.get_rect(top=0, left=1350))
    screen.blit(p2Mon["portrait"]["spriteSheet"],(48,7),(p2PortraitFrame*port2_wdt, p2PortraitFrame*port2_hgt, port2_wdt,port2_hgt))
    screen.blit(pontosP2, pontosP2.get_rect(top=0, left=98))




  

# Pygame
def main_loop(screen):  
    global clock
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # fecha o jogo
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    punch_sound.play()

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
pygame.mixer.init()
collect_sound = pygame.mixer.Sound("collect_apples.mp3")
punch_sound = pygame.mixer.Sound('punch.mp3')
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()

## Debug