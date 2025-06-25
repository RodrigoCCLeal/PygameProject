import pygame
import random

p1_animation_frame = 0
p1_directionFrame = 0
p1_pos_x = 1000
p1_pos_y = 475
p1_anim_time = 0
p2_animation_frame = 0
p2_directionFrame = 0
p2_pos_x = 400
p2_pos_y = 475
p2_anim_time = 0
enemy_animation_frame = 0
enemy_directionFrame = 0
enemy_pos_x = 720
enemy_pos_y = 480
enemy_anim_time = 0
width = 24 * 60
height = 24 * 40
tempoRestante = 180000
cont = 0
minutos = tempoRestante//60000
segundos = 0
mapa = []
lColliders = []
lAguaCol = []
timerItem = 0
lMacaCol = []
pontP1 = 0
pontP2 = 0
pontEnemy = 0
target = "coiso"
hitstun = 500
MAP_FILES = {1: r"mapas/mapa1.txt", 2: r"mapas/mapa2.txt", 3: r"mapas/mapa3.txt"}
pygame.display.set_caption("APPLE WOODS")#muda o nome da janela
icone = pygame.image.load('objects/GoldenApple.png')
pygame.display.set_icon(icone)
#telas final e inicial
clock = pygame.time.Clock() 
tela_inicio_mudkip_frames = []
tela_inicio_chimchar_frames = []
wiggly_final_resized_frames = [] 
tela_inicio_mudkip_animation_frame = 0
tela_inicio_mudkip_anim_time = 0
tela_inicio_chimchar_animation_frame = 0
tela_inicio_chimchar_anim_time = 0
wiggy_final_animation_frame = 0
wiggy_final_anim_time = 0
wiggly_final = None
mudkip_inicio = None 
chimchar_inicio = None

def load_inicio_final():
    global mudkip_inicio, chimchar_inicio, wiggly_final
    global tela_inicio_mudkip_frames, tela_inicio_mudkip_anim_time, mudkip_inicio
    global tela_inicio_chimchar_animation_frame, tela_inicio_chimchar_anim_time, tela_inicio_chimchar_frames, chimchar_inicio
    global wiggly_final_animation_frame, wiggly_final_anim_time, wiggly_final_resized_frames
    global font, font_menor, font_maior 

    wiggly_final={"final_anim": {"spriteSheet": pygame.image.load("spritesMons/wigglytuff/wigglytuff_final.png"),"frame_pixel_width": 275 ,"frame_pixel_height": 245,"num_frames_x": 5,"num_frames_y": 12,"frameReset": 59,"animTime": 20}}
    mudkip_inicio = {"intro_anim": {"spriteSheet": pygame.image.load("spritesMons/mudkip/mudkip_inicio.png"),"frame_pixel_width": 340,"frame_pixel_height": 490,"num_frames_x": 5,"num_frames_y": 11,"frameReset": 50, "animTime": 25}}
    chimchar_inicio = {"intro_anim": {"spriteSheet": pygame.image.load("spritesMons/chimchar/chimchar_inicio.png"), "frame_pixel_width": 400,"frame_pixel_height": 510,"num_frames_x": 5,"num_frames_y": 6,"frameReset": 27, "animTime": 32}}
    
    #mudkip
    for y_frame in range(mudkip_inicio["intro_anim"]["num_frames_y"]):
        for x_frame in range(mudkip_inicio["intro_anim"]["num_frames_x"]):
            rect = pygame.Rect(
                x_frame * mudkip_inicio["intro_anim"]["frame_pixel_width"],
                y_frame * mudkip_inicio["intro_anim"]["frame_pixel_height"],
                mudkip_inicio["intro_anim"]["frame_pixel_width"],
                mudkip_inicio["intro_anim"]["frame_pixel_height"]
            )
            frame_original = mudkip_inicio["intro_anim"]["spriteSheet"].subsurface(rect)
            tela_inicio_mudkip_frames.append(frame_original)

    #chimchar
    for y_frame in range(chimchar_inicio["intro_anim"]["num_frames_y"]):
        for x_frame in range(chimchar_inicio["intro_anim"]["num_frames_x"]):
            rect = pygame.Rect(
                x_frame * chimchar_inicio["intro_anim"]["frame_pixel_width"],
                y_frame * chimchar_inicio["intro_anim"]["frame_pixel_height"],
                chimchar_inicio["intro_anim"]["frame_pixel_width"],
                chimchar_inicio["intro_anim"]["frame_pixel_height"]
            )
            frame_original = chimchar_inicio["intro_anim"]["spriteSheet"].subsurface(rect)
            tela_inicio_chimchar_frames.append(frame_original)

    #wigglytuff
    frame_width_original = wiggly_final["final_anim"]["frame_pixel_width"]
    frame_height_original = wiggly_final["final_anim"]["frame_pixel_height"] 
    for y_frame in range(wiggly_final["final_anim"]["num_frames_y"]):
        for x_frame in range(wiggly_final["final_anim"]["num_frames_x"]):
            rect = pygame.Rect(x_frame * frame_width_original, y_frame * frame_height_original, frame_width_original, frame_height_original)
            frame_original = wiggly_final["final_anim"]["spriteSheet"].subsurface(rect)
            wiggly_final_resized_frames.append(frame_original)    

def tela_inicio():
    global mapa_arquivo
    global mudkip_inicio, chimchar_inicio 
    global tela_inicio_mudkip_animation_frame, tela_inicio_mudkip_anim_time
    global tela_inicio_chimchar_animation_frame, tela_inicio_chimchar_anim_time
    global clock, width, height, screen

    tela_inicio = pygame.image.load("telas/tela_inicio.png")
    tela_inicio = pygame.transform.scale(tela_inicio, (width, height))

    tela_inicio_mudkip_animation_frame = 0
    tela_inicio_mudkip_anim_time = 0
    tela_inicio_chimchar_animation_frame = 0
    tela_inicio_chimchar_anim_time = 0
    
    esperando = True
    while esperando:
        dt = clock.get_time()
        
        tela_inicio_mudkip_anim_time += dt
        if tela_inicio_mudkip_anim_time > mudkip_inicio["intro_anim"]["animTime"]:
            tela_inicio_mudkip_animation_frame += 1
            if tela_inicio_mudkip_animation_frame > mudkip_inicio["intro_anim"]["frameReset"]:
                tela_inicio_mudkip_animation_frame = 0
            tela_inicio_mudkip_anim_time = 0

    
        tela_inicio_chimchar_anim_time += dt
        if tela_inicio_chimchar_anim_time > chimchar_inicio["intro_anim"]["animTime"]:
            tela_inicio_chimchar_animation_frame += 1
            if tela_inicio_chimchar_animation_frame > chimchar_inicio["intro_anim"]["frameReset"]:
                tela_inicio_chimchar_animation_frame = 0
            tela_inicio_chimchar_anim_time = 0

        screen.blit(tela_inicio, (0, 0)) 

        if tela_inicio_mudkip_frames: 
            current_mudkip_frame = tela_inicio_mudkip_frames[tela_inicio_mudkip_animation_frame]
            pos_x_mudkip = width // 2 - current_mudkip_frame.get_width() + 180  
            pos_y_mudkip = height // 2 - current_mudkip_frame.get_height() // 2 + 150
            screen.blit(current_mudkip_frame, (pos_x_mudkip, pos_y_mudkip))

        if tela_inicio_chimchar_frames:
            current_chimchar_frame= tela_inicio_chimchar_frames[tela_inicio_chimchar_animation_frame]
            pos_x_chimchar = pos_x_mudkip + 400
            pos_y_chimchar = height // 2 - current_chimchar_frame.get_height() // 2 + 150
            screen.blit(current_chimchar_frame, (pos_x_chimchar, pos_y_chimchar))

        pygame.display.update()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #sys.exit()
            elif event.type == pygame.KEYDOWN:
                esperando = False

    # Tela de seleção de Mapas
    opcao = escolher_mapa(screen)
    mapa_arquivo = MAP_FILES[opcao]

def mostrar_tela_final(tela, score1, score2, largura, altura):
    global wiggly_final, wiggly_final_animation_frame, wiggly_final_anim_time, wiggly_final_resized_frames
    global width, height, clock, font_maior, font_menor
    
    wiggly_final_animation_frame = 0
    wiggly_final_anim_time = 0

    tela_final_fundo = pygame.transform.scale(pygame.image.load("telas/tela_fundo_final.png"), (width, height))

    if pontEnemy >= pontP1+pontP2:
        texto = font_maior.render("Derrota!", True, (0, 0, 0))
    else:
        texto = font_maior.render("Vitória!", True, (0, 0, 0))
    
    score1Texto = font.render(f"%s: {score1} pontos" %p1Mon["nome"], True, (255, 255, 255))
    score2Texto = font.render(f"%s: {score2} pontos" %p2Mon["nome"], True, (255, 255, 255))
    score3Texto = font.render(f"%s: {pontEnemy} pontos" %enemyMon["nome"], True, (255, 255, 255))
    #textoSair = font_menor.render("Aperte SPACE para sair do Jogo.", True, (255, 208, 0))
    #textoReiniciar = font_menor.render("Aperte R para voltar ao menu do Jogo.", True, (255, 208, 0))
    #textoSair_tracado = font_menor.render("Aperte SPACE para sair do Jogo.", True, (0, 0, 0))
    #textoReiniciar_tracado = font_menor.render("Aperte R para voltar ao menu do Jogo.", True, (0, 0, 0))
    #------------------fiz esses textos direto na imagem ----------------------

    #não fechar a janela direto
    esperando = True
    while esperando:
        dt = clock.get_time()

        wiggly_final_anim_time = wiggly_final_anim_time + dt
        if wiggly_final_anim_time > wiggly_final["final_anim"]["animTime"]:
            wiggly_final_animation_frame = wiggly_final_animation_frame + 1
            if wiggly_final_animation_frame > wiggly_final["final_anim"]["frameReset"]:
                wiggly_final_animation_frame = 0
            wiggly_final_anim_time = 0
        
        tela.blit(tela_final_fundo, (0, 0))
        tela.blit(texto, (largura//2 - texto.get_width()//2, altura//5))
        tela.blit(score1Texto, (largura//2 - score1Texto.get_width()//2, altura//3))
        tela.blit(score2Texto, (largura//2 - score2Texto.get_width()//2, altura//3 + 50))
        tela.blit(score3Texto, (largura//2 - score3Texto.get_width()//2, altura//3 + 100))
        #tela.blit(textoSair_tracado, (largura//4 - textoSair.get_width()//2 - 77, altura//1.1 ))
        #tela.blit(textoReiniciar_tracado, (largura//4 - textoSair.get_width()//2 - 77, altura//1.2 - 20))
        #tela.blit(textoSair, (largura//4 - textoSair.get_width()//2 - 80, altura//1.1))
        #tela.blit(textoReiniciar, (largura//4 - textoSair.get_width()//2 - 80, altura//1.2 - 20))
        #------------------fiz esses textos direto na imagem ----------------------
        
        current_wiggy_frame = wiggly_final_resized_frames[wiggly_final_animation_frame]
        pos_x_wiggy = (largura / 2) - (current_wiggy_frame.get_width() / 2) #pra ficar centralizado no x
        pos_y_wiggy = (altura / 2) + 100
        tela.blit(current_wiggy_frame, (pos_x_wiggy, pos_y_wiggy))
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN: 
                if evento.key == pygame.K_SPACE: #finaliza jogo
                    esperando = False
                elif evento.key == pygame.K_r: #reinicia jogo
                    esperando = False #fecha tela final
                    return True

def distancia(a,b,x,y):
    return ((a-x)**2 + (b-y)**2)**(1/2)

def load_mapa(filename):    #Lê o conteúdo do arquivo para a matriz
    global mapa
    mapa.clear() # para evitar anexação duplicada
    file = open(filename,"r")
    for line in file.readlines():
        mapa.append(line)
    file.close()

def escolher_mapa(screen) -> int:
    global inimigo
    ## Mostra tela de escolha e devolve 1, 2 ou 3.
    selecao_img = pygame.image.load("telas/tela_mapas.png").convert_alpha()
    selecao_img = pygame.transform.scale(selecao_img, (width, height))
    screen.blit(selecao_img, (0, 0))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() #; sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    inimigo = 0
                    return 1
                if event.key == pygame.K_2:
                    inimigo = 1
                    return 2
                if event.key == pygame.K_3:
                    inimigo = 2
                    return 3

def load():
    global clock, p1CharAnim, tileset, tile_wdt,tile_hgt, clock, p1_hgt,p1_wdt,p2_wdt,p2_hgt, p1CharAnim, p1Mon, p2CharAnim, p2Mon, font, font_menor, font_maior
    global collider_p1, collider_p2, maca, item_wdt, item_hgt, tempoRestante, port1_wdt, port1_hgt, port2_wdt, port2_hgt, enemyMon, enemyCharAnim, enemyVida, enemyPort_wdt, enemyPort_hgt
    global mapa_arquivo
    global collect_sound, punch_sound 

    clock = pygame.time.Clock() 
    load_mapa(mapa_arquivo)
    tileset = pygame.image.load("mapas/meadowTileset.png")
    musicas = ["Sons/038 - Monster House!.mp3","Sons/068 - Dialga's Fight to the Finish!.mp3","Sons/029 - Apple Woods.mp3"]
    pygame.mixer.music.load("%s" %musicas[inimigo])
    pygame.mixer.music.play(-1)

    mudkip = {"nome": "Mudkip", "color": "blue", "speed": 0.1, "water":False, "damage": 3,
              "idle":{"spriteSheet": pygame.image.load("spritesMons/mudkip/Mudkip-Idle-Anim.png"), "largura": 7, "altura": 8, "frameReset": 6, "animTime": 100 },
              "sleep":{"spriteSheet": pygame.image.load("spritesMons/mudkip/Mudkip-Sleep-Anim.png"), "largura": 2, "altura": 1, "frameReset": 1, "animTime": 500 },
              "walk":{ "spriteSheet": pygame.image.load("spritesMons/mudkip/Mudkip-Walk-Anim.png"), "largura": 6, "altura": 8, "frameReset": 5, "animTime": 100 },
              "attack":{"spriteSheet": pygame.image.load("spritesMons/mudkip/Mudkip-Attack-Anim.png"), "largura": 10, "altura": 8, "frameReset": 9, "animTime": 75 },
              "hurt":{"spriteSheet": pygame.image.load("spritesMons/mudkip/Mudkip-Hurt-Anim.png"), "largura": 2, "altura": 8, "frameReset": 1, "animTime": 250 },
              "portrait": {"spriteSheet": pygame.image.load("spritesMons/mudkip/mudkip_portrait.png"), "largura": 5, "altura": 8}}
    chimchar = {"nome": "Chimchar", "color": "orange", "speed":0.12, "water":True, "damage": 5,
                "idle":{"spriteSheet": pygame.image.load("spritesMons/chimchar/Chimchar-Idle-Anim.png"), "largura": 5, "altura": 8, "frameReset": 4, "animTime": 100 },
                "sleep":{"spriteSheet": pygame.image.load("spritesMons/chimchar/Chimchar-Sleep-Anim.png"), "largura": 2, "altura": 1, "frameReset": 1, "animTime": 500 },
                "walk":{ "spriteSheet": pygame.image.load("spritesMons/chimchar/Chimchar-Walk-Anim.png"), "largura": 7, "altura": 8, "frameReset": 6, "animTime": 100 },
                "attack":{"spriteSheet": pygame.image.load("spritesMons/chimchar/Chimchar-Strike-Anim.png"), "largura": 10, "altura": 8, "frameReset": 9, "animTime": 75 },
                "hurt":{"spriteSheet": pygame.image.load("spritesMons/chimchar/Chimchar-Hurt-Anim.png"), "largura": 2, "altura": 8, "frameReset": 1, "animTime": 250 },
                "portrait": {"spriteSheet": pygame.image.load("spritesMons/chimchar/chimchar_portrait.png"), "largura": 5, "altura": 8}}
    bulbasaur = {"nome": "Bulbasaur","color": "dark green", "speed": 0.1, "water":True, "damage": 4,
              "idle":{"spriteSheet": pygame.image.load("spritesMons/bulbasaur/Bulbasaur-Idle-Anim.png"), "largura": 3, "altura": 8, "frameReset": 2, "animTime": 200 },
              "sleep":{"spriteSheet": pygame.image.load("spritesMons/bulbasaur/Bulbasaur-Sleep-Anim.png"), "largura": 2, "altura": 1, "frameReset": 1, "animTime": 500 },
              "walk":{ "spriteSheet": pygame.image.load("spritesMons/bulbasaur/Bulbasaur-Walk-Anim.png"), "largura": 6, "altura": 8, "frameReset": 5, "animTime": 150 },
              "attack":{"spriteSheet": pygame.image.load("spritesMons/bulbasaur/Bulbasaur-Attack-Anim.png"), "largura": 11, "altura": 8, "frameReset": 10, "animTime": 50 },
              "hurt":{"spriteSheet": pygame.image.load("spritesMons/bulbasaur/Bulbasaur-Hurt-Anim.png"), "largura": 2, "altura": 8, "frameReset": 1, "animTime": 250 },
              "portrait": {"spriteSheet": pygame.image.load("spritesMons/bulbasaur/Bulbasaur_portrait.png"), "largura": 5, "altura": 8}}
    wiggly = {"nome": "Wigglytuff","color": "pink", "speed": 0.07, "water":True, "damage": 10,
              "idle":{"spriteSheet": pygame.image.load("spritesMons/wigglytuff/Wiggly-Idle-Anim.png"), "largura": 4, "altura": 8, "frameReset": 3, "animTime": 150 },
              "sleep":{"spriteSheet": pygame.image.load("spritesMons/wigglytuff/Wiggly-Sleep-Anim.png"), "largura": 2, "altura": 1, "frameReset": 1, "animTime": 500 },
              "walk":{ "spriteSheet": pygame.image.load("spritesMons\wigglytuff\Wiggly-Walk-Anim.png"), "largura": 4, "altura": 8, "frameReset": 3, "animTime": 150 },
              "attack":{"spriteSheet": pygame.image.load("spritesMons/wigglytuff/Wiggly-Attack-Anim.png"), "largura": 10, "altura": 8, "frameReset": 9, "animTime": 75 },
              "hurt":{"spriteSheet": pygame.image.load("spritesMons/wigglytuff/Wiggly-Hurt-Anim.png"), "largura": 2, "altura": 8, "frameReset": 1, "animTime": 250 },
              "portrait": {"spriteSheet": pygame.image.load("spritesMons/wigglytuff/wigglytuff_portrait.png"), "largura": 5, "altura": 8}}
    chatot = {"nome": "Chatot","color": "white", "speed": 0.15, "water":False, "damage": 1,
              "idle":{"spriteSheet": pygame.image.load("spritesMons/chatot/Chatot-Idle-Anim.png"), "largura": 8, "altura": 8, "frameReset": 7, "animTime": 150 },
              "sleep":{"spriteSheet": pygame.image.load("spritesMons/chatot/Chatot-Sleep-Anim.png"), "largura": 2, "altura": 1, "frameReset": 1, "animTime": 500 },
              "walk":{ "spriteSheet": pygame.image.load("spritesMons/chatot/Chatot-Walk-Anim.png"), "largura": 6, "altura": 8, "frameReset": 5, "animTime": 150 },
              "attack":{"spriteSheet": pygame.image.load("spritesMons/chatot/Chatot-Attack-Anim.png"), "largura": 14, "altura": 8, "frameReset": 13, "animTime": 50 },
              "hurt":{"spriteSheet": pygame.image.load("spritesMons/chatot/Chatot-Hurt-Anim.png"), "largura": 2, "altura": 8, "frameReset": 1, "animTime": 250 },
              "portrait": {"spriteSheet": pygame.image.load("spritesMons/chatot/chatot_portrait.png"), "largura": 5, "altura": 8}}
    inimigos = [chatot, bulbasaur, wiggly]
    p1Mon = mudkip
    p2Mon = chimchar
    p1CharAnim = p1Mon["idle"]
    p2CharAnim = p2Mon["idle"]

    enemyMon = inimigos[inimigo]
    enemyCharAnim = enemyMon["sleep"]
    enemyVida = 50

    tile_wdt = tileset.get_width()/16
    tile_hgt = tileset.get_height()/25

    port1_wdt = p1Mon["portrait"]["spriteSheet"].get_width()/p1Mon["portrait"]["largura"]
    port1_hgt = p1Mon["portrait"]["spriteSheet"].get_height()/p1Mon["portrait"]["altura"]

    port2_wdt = p2Mon["portrait"]["spriteSheet"].get_width()/p2Mon["portrait"]["largura"]
    port2_hgt = p2Mon["portrait"]["spriteSheet"].get_height()/p2Mon["portrait"]["altura"]

    enemyPort_wdt = enemyMon["portrait"]["spriteSheet"].get_width()/enemyMon["portrait"]["largura"]
    enemyPort_hgt = enemyMon["portrait"]["spriteSheet"].get_height()/enemyMon["portrait"]["altura"]

    font = pygame.font.Font("PKMN-Mystery-Dungeon.ttf", 75)
    font_menor = pygame.font.Font("PKMN-Mystery-Dungeon.ttf", 55)
    font_maior = pygame.font.Font("PKMN-Mystery-Dungeon.ttf", 95)

    maca = pygame.image.load("objects/Apple.png")
    item_wdt = maca.get_width()
    item_hgt = maca.get_height()

    for (y,l) in enumerate(mapa):
        for (x,c) in enumerate(l):
            parede = pygame.Rect(x*tile_wdt, y*tile_hgt, tile_wdt, tile_hgt)            
            if c == "W":
                lColliders.append(parede)
            elif c == "9":
                lAguaCol.append(parede)
    
    collect_sound = pygame.mixer.Sound("Sons\collect_apples.mp3")
    punch_sound = pygame.mixer.Sound('Sons\punch.mp3')

def update(dt):
    global p1_animation_frame, p1_directionFrame, p1_pos_x, p1_pos_y, p1_anim_time, collider_p1, p1CharAnim, p1Mon, p1_wdt, p1_hgt, p1PortraitFrame
    global p2_animation_frame, p2_directionFrame, p2_pos_y, p2_pos_x, p2_anim_time, collider_p2, p2CharAnim, p2Mon, p2_wdt, p2_hgt, p2PortraitFrame
    global enemy_animation_frame, enemy_directionFrame, enemy_pos_y, enemy_pos_x, enemy_anim_time, collider_enemy, enemyCharAnim, enemyMon, enemy_wdt, enemy_hgt, hitstun
    global minutos, segundos, cont, timerItem, pontP1, pontP2, pontEnemy, cronometro, pontosP1, pontosP2, pontosEnemy, tempoRestante, tempoPercent, running, fim, enemyVida, target, enemyPortraitFrame
    
    if tempoRestante <= 0:
        running = False #para o jogo
        fim = mostrar_tela_final(screen, pontP1, pontP2, width, height) 
        if fim:
            resetar_jogo()
            tela_inicio()
            load()
            main_loop(screen)

    keys = pygame.key.get_pressed()

    tempoRestante -= dt
    tempoPercent = tempoRestante/2250
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
    enemyPortraitFrame = 0

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

    enemy_anim_time = enemy_anim_time + dt 
    if enemy_anim_time > enemyCharAnim["animTime"]: 
        enemy_animation_frame = enemy_animation_frame + 1 
        if enemy_animation_frame > enemyCharAnim["frameReset"]: 
            enemy_animation_frame = 0
        enemy_anim_time = 0

    #Move P1
    if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        p1CharAnim = p1Mon["walk"]
        p1_directionFrame = 5
        p1_pos_y = p1_pos_y - (p1Mon["speed"] * dt)
        p1_pos_x = p1_pos_x - (p1Mon["speed"] * dt)
    elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        p1CharAnim = p1Mon["walk"]
        p1_directionFrame = 7
        p1_pos_y = p1_pos_y + (p1Mon["speed"] * dt)
        p1_pos_x = p1_pos_x - (p1Mon["speed"] * dt)
    elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        p1CharAnim = p1Mon["walk"]
        p1_directionFrame = 3
        p1_pos_y = p1_pos_y - (p1Mon["speed"] * dt)
        p1_pos_x = p1_pos_x + (p1Mon["speed"] * dt)
    elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
        p1CharAnim = p1Mon["walk"]
        p1_directionFrame = 1
        p1_pos_y = p1_pos_y + (p1Mon["speed"] * dt)
        p1_pos_x = p1_pos_x + (p1Mon["speed"] * dt)
    elif keys[pygame.K_RIGHT]:
        p1CharAnim = p1Mon["walk"]
        p1_directionFrame = 2
        p1_pos_x = p1_pos_x + (p1Mon["speed"] * dt)
    elif keys[pygame.K_LEFT]:
        p1CharAnim = p1Mon["walk"]
        p1_directionFrame = 6
        p1_pos_x = p1_pos_x - (p1Mon["speed"] * dt) 
    elif keys[pygame.K_UP]:
        p1CharAnim = p1Mon["walk"]
        p1_directionFrame = 4
        p1_pos_y = p1_pos_y - (p1Mon["speed"] * dt)
    elif keys[pygame.K_DOWN]:
        p1CharAnim = p1Mon["walk"]
        p1_directionFrame = 0
        p1_pos_y = p1_pos_y + (p1Mon["speed"] * dt)
    elif keys[pygame.K_KP_0]:
        p1CharAnim = p1Mon["attack"]
    elif p1_animation_frame == 0:
        p1CharAnim = p1Mon["idle"]


    #Move P2
    if keys[pygame.K_w] and keys[pygame.K_a]:
        p2CharAnim = p2Mon["walk"]
        p2_directionFrame = 5
        p2_pos_y = p2_pos_y - (p2Mon["speed"] * dt)
        p2_pos_x = p2_pos_x - (p2Mon["speed"] * dt)
    elif keys[pygame.K_s] and keys[pygame.K_a]:
        p2CharAnim = p2Mon["walk"]
        p2_directionFrame = 7
        p2_pos_y = p2_pos_y + (p2Mon["speed"] * dt)
        p2_pos_x = p2_pos_x - (p2Mon["speed"] * dt)
    elif keys[pygame.K_w] and keys[pygame.K_d]:
        p2CharAnim = p2Mon["walk"]
        p2_directionFrame = 3
        p2_pos_y = p2_pos_y - (p2Mon["speed"] * dt)
        p2_pos_x = p2_pos_x + (p2Mon["speed"] * dt)
    elif keys[pygame.K_s] and keys[pygame.K_d]:
        p2CharAnim = p2Mon["walk"]
        p2_directionFrame = 1
        p2_pos_y = p2_pos_y + (p2Mon["speed"] * dt)
        p2_pos_x = p2_pos_x + (p2Mon["speed"] * dt)
    elif keys[pygame.K_d]:
        p2CharAnim = p2Mon["walk"]
        p2_directionFrame = 2
        p2_pos_x = p2_pos_x + (p2Mon["speed"] * dt)
    elif keys[pygame.K_a]:
        p2CharAnim = p2Mon["walk"]
        p2_directionFrame = 6
        p2_pos_x = p2_pos_x - (p2Mon["speed"] * dt)
    elif keys[pygame.K_w]:
        p2CharAnim = p2Mon["walk"]
        p2_directionFrame = 4
        p2_pos_y = p2_pos_y - (p2Mon["speed"] * dt)
    elif keys[pygame.K_s]:
        p2CharAnim = p2Mon["walk"]
        p2_directionFrame = 0
        p2_pos_y = p2_pos_y + (p2Mon["speed"] * dt)
    elif keys[pygame.K_e]:
        p2CharAnim = p2Mon["attack"]
    elif p2_animation_frame == 0:
        p2CharAnim = p2Mon["idle"]
        

    # Altura e Largura das Sprites
    p1_wdt = p1CharAnim["spriteSheet"].get_width()/(p1CharAnim["largura"])
    p1_hgt = p1CharAnim["spriteSheet"].get_height()/(p1CharAnim["altura"])
    p2_wdt = p2CharAnim["spriteSheet"].get_width()/(p2CharAnim["largura"])
    p2_hgt = p2CharAnim["spriteSheet"].get_height()/(p2CharAnim["altura"])
    enemy_wdt = enemyCharAnim["spriteSheet"].get_width()/(enemyCharAnim["largura"])
    enemy_hgt = enemyCharAnim["spriteSheet"].get_height()/(enemyCharAnim["altura"])


    #Timer
    if minutos < 10 and segundos < 10:
        cronometro = font.render("0%d:0%d"%(minutos,segundos), False, "white")
    elif segundos < 10:
        cronometro = font.render("%d:0%d"%(minutos,segundos), False, "white")
    elif minutos < 10:
        cronometro = font.render("0%d:%d"%(minutos,segundos), False, "white")

    #Pontuações
    pontosP1 = font.render("%d"%pontP1, "False", p1Mon["color"])
    pontosP2 = font.render("%d"%pontP2, "False", p2Mon["color"])
    pontosEnemy = font.render("%d"%pontEnemy, "False", enemyMon["color"])

    #Criando maçãs
    timerItem += dt
    if timerItem > 2000:
        item = pygame.Rect(random.randint(72,1342), random.randint(72,858), item_wdt, item_hgt)
        lMacaCol.append(item)
        timerItem = 0

    if lMacaCol != [] and target not in lMacaCol:
        target = random.choice(lMacaCol)

    # Inimigo
    enemy_center_x = enemy_pos_x-enemy_wdt//2
    enemy_center_y = enemy_pos_y-enemy_hgt//2
    if enemyCharAnim == enemyMon["sleep"]:
        enemyVida += dt*0.01
        if enemyVida >= 80:
            enemyCharAnim = enemyMon["walk"]
        elif enemyVida < 0:
            enemyVida = 0
    elif enemyCharAnim == enemyMon["walk"]:
        if abs(enemy_center_x - target.left)<=1 and (enemy_center_y - target.top)<0:
            enemy_directionFrame = 0
            enemy_pos_y = enemy_pos_y + dt*enemyMon["speed"]
        elif abs(enemy_center_x - target.left)<=1 and (enemy_center_y - target.top)>0:
            enemy_directionFrame = 4
            enemy_pos_y = enemy_pos_y - dt*enemyMon["speed"]
        elif (enemy_center_x - target.left)<0 and abs(enemy_center_y - target.top)<=1:
            enemy_directionFrame = 2
            enemy_pos_x = enemy_pos_x + dt*enemyMon["speed"]
        elif (enemy_center_x - target.left)>0 and abs(enemy_center_y - target.top)<=1:
            enemy_directionFrame = 6
            enemy_pos_x = enemy_pos_x - dt*enemyMon["speed"]
        elif (enemy_center_x - target.left)<0 and (enemy_center_y - target.top)<0:
            enemy_directionFrame = 1
            enemy_pos_y = enemy_pos_y + dt*enemyMon["speed"]
            enemy_pos_x = enemy_pos_x + dt*enemyMon["speed"]
        elif (enemy_center_x - target.left)<0 and (enemy_center_y - target.top)>0:
            enemy_directionFrame = 3
            enemy_pos_y = enemy_pos_y - dt*enemyMon["speed"]
            enemy_pos_x = enemy_pos_x + dt*enemyMon["speed"]
        elif (enemy_center_x - target.left)>0 and (enemy_center_y - target.top)<0:
            enemy_directionFrame = 7
            enemy_pos_y = enemy_pos_y + dt*enemyMon["speed"]
            enemy_pos_x = enemy_pos_x - dt*enemyMon["speed"]
        elif (enemy_center_x - target.left)>0 and (enemy_center_y - target.top)>0:
            enemy_directionFrame = 5
            enemy_pos_y = enemy_pos_y - dt*enemyMon["speed"]
            enemy_pos_x = enemy_pos_x - dt*enemyMon["speed"]
        elif enemy_animation_frame == 0 and lMacaCol == []:
            enemyCharAnim = enemyMon["idle"]
    elif enemyCharAnim == enemyMon["hurt"]:
        hitstun -= dt
        if hitstun <= 0:
            hitstun = 500
            enemyCharAnim = enemyMon["walk"]
        

    # Colisão
    collider_p1 = pygame.Rect(p1_pos_x-(p1_wdt//4), p1_pos_y-(p1_hgt//4), p1_wdt*0.5, p1_hgt*0.4)
    collider_p2 = pygame.Rect(p2_pos_x-(p2_wdt//4), p2_pos_y-(p2_hgt//4), p2_wdt*0.5, p2_hgt*0.4)
    collider_enemy = pygame.Rect(enemy_pos_x-(enemy_wdt//4), enemy_pos_y-(enemy_hgt//4), enemy_wdt*0.8, enemy_hgt*0.8)

    if collider_p1.collidelist(lColliders) >= 0:
        p1_pos_x = old_p1_x
        p1_pos_y = old_p1_y
    if collider_p1.collidelist(lMacaCol) >= 0:
        pontP1 += 1
        lMacaCol.remove(lMacaCol[collider_p1.collidelist(lMacaCol)])
        pygame.mixer.Sound.play(collect_sound)
    if collider_p1.collidelist(lAguaCol) >= 0 and p1Mon["water"]:
        p1_pos_x = old_p1_x
        p1_pos_y = old_p1_y
    if collider_p1.scale_by(2).colliderect(collider_enemy) and p1CharAnim == p1Mon["attack"] and p1_animation_frame == 4:
        enemyVida -= p1Mon["damage"]
        if lMacaCol != []:
            target = random.choice(lMacaCol)
        pygame.mixer.Sound.play(punch_sound)
        enemyCharAnim = enemyMon["hurt"]
        enemy_animation_frame = 0
        if pontEnemy > 0 and enemyCharAnim == enemyMon["hurt"]:
            pontEnemy -= 1
            item = pygame.Rect(random.randint(int(enemy_pos_x-24),int(enemy_pos_x+24)), random.randint(int(enemy_pos_y-24),int(enemy_pos_y+24)), item_wdt, item_hgt)
            lMacaCol.append(item)
        
    if collider_p2.collidelist(lColliders) >= 0:
        p2_pos_x = old_p2_x
        p2_pos_y = old_p2_y
    if collider_p2.collidelist(lMacaCol) >= 0:
        pontP2 += 1
        lMacaCol.remove(lMacaCol[collider_p2.collidelist(lMacaCol)])
        pygame.mixer.Sound.play(collect_sound)
    if collider_p2.collidelist(lAguaCol) >= 0 and p2Mon["water"]:
        p2_pos_x = old_p2_x
        p2_pos_y = old_p2_y
    if collider_p2.scale_by(2).colliderect(collider_enemy) and p2CharAnim == p2Mon["attack"] and p2_animation_frame == 4:
        enemyVida -= p2Mon["damage"]
        if lMacaCol != []:
            target = random.choice(lMacaCol)
        pygame.mixer.Sound.play(punch_sound)
        enemyCharAnim = enemyMon["hurt"]
        enemy_animation_frame = 0
        if pontEnemy > 0 and enemyCharAnim == enemyMon["hurt"]:
            pontEnemy -= 1
            item = pygame.Rect(random.randint(int(enemy_pos_x-24),int(enemy_pos_x+24)), random.randint(int(enemy_pos_y-24),int(enemy_pos_y+24)), item_wdt, item_hgt)
            lMacaCol.append(item)
    
    if collider_enemy.collidelist(lMacaCol) >= 0:
        if enemyCharAnim == enemyMon["hurt"]:
            pass
        else:
            lMacaCol.remove(lMacaCol[collider_enemy.collidelist(lMacaCol)])
            pygame.mixer.Sound.play(collect_sound)
            pontEnemy += 1
            enemyVida += 10
            if enemyVida >= 80:
                enemyVida = 80

    if enemyVida <= 10:
        enemy_directionFrame = 0
        enemyCharAnim = enemyMon["sleep"]
        hitstun = 500
    
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

    #Barrinha
    pygame.draw.rect(screen, ("black"), (enemy_pos_x-40,enemy_pos_y+10,80,14))
    if enemyVida >= 30:
        pygame.draw.rect(screen, (enemyMon["color"]), (enemy_pos_x-40,enemy_pos_y+10,enemyVida,14))
    else:
        pygame.draw.rect(screen, ("red"), (enemy_pos_x-40,enemy_pos_y+10,enemyVida,14))

    #Desenha personagens      
    screen.blit(p1CharAnim["spriteSheet"],(p1_pos_x-(p1_wdt//2), p1_pos_y-(p1_hgt//2)),(p1_animation_frame*p1_wdt, p1_directionFrame*p1_hgt, p1_wdt,p1_hgt))
    screen.blit(p2CharAnim["spriteSheet"],(p2_pos_x-(p2_wdt//2), p2_pos_y-(p2_hgt//2)),(p2_animation_frame*p2_wdt, p2_directionFrame*p2_hgt, p2_wdt,p2_hgt))
    screen.blit(enemyCharAnim["spriteSheet"],(enemy_pos_x-(enemy_wdt//2), enemy_pos_y-(enemy_hgt//2)),(enemy_animation_frame*enemy_wdt, enemy_directionFrame*enemy_hgt, enemy_wdt,enemy_hgt))

    #Desenha objetos
    for i in lMacaCol:
        screen.blit(maca,(i.left, i.top),(0, 0, item_wdt, item_hgt))


    #Desenha contadores
    screen.blit(cronometro, cronometro.get_rect(top=0, left=640))

    #Desenha pontuação
    screen.blit(p1Mon["portrait"]["spriteSheet"],(148,7),(p1PortraitFrame*port1_wdt, p1PortraitFrame*port1_hgt, port1_wdt,port1_hgt))
    screen.blit(pontosP1, pontosP1.get_rect(top=0, left=198))
    screen.blit(p2Mon["portrait"]["spriteSheet"],(48,7),(p2PortraitFrame*port2_wdt, p2PortraitFrame*port2_hgt, port2_wdt,port2_hgt))
    screen.blit(pontosP2, pontosP2.get_rect(top=0, left=98))
    screen.blit(enemyMon["portrait"]["spriteSheet"],(248,7),(enemyPortraitFrame*enemyPort_wdt, enemyPortraitFrame*enemyPort_hgt, enemyPort_wdt,enemyPort_hgt))
    screen.blit(pontosEnemy, pontosEnemy.get_rect(top=0, left=298))

def resetar_jogo():
    global p1_pos_x, p1_pos_y, p2_pos_x, p2_pos_y
    global p1_animation_frame, p2_animation_frame, p1_anim_time, p2_anim_time, p1_directionFrame, p2_directionFrame
    global pontP1, pontP2
    global tempoRestante, minutos, segundos, cont, timerItem, tempoPercent
    global lMacaCol

    # reiniciar variáveis
    p1_pos_x, p1_pos_y = 1000, 475 
    p2_pos_x, p2_pos_y = 400, 475

    p1_animation_frame, p1_directionFrame, p1_anim_time = 0, 0, 0
    p2_animation_frame, p2_directionFrame, p2_anim_time = 0, 0, 0

    pontP1 = 0
    pontP2 = 0

    tempoRestante = 180000
    minutos = 3
    segundos = 0
    cont = 0
    timerItem = 0

    lMacaCol.clear()   

def main_loop(screen):
    global clock, running
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # fecha o jogo
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


#Programa principal
pygame.init()
screen = pygame.display.set_mode((width, height))
load_inicio_final()
tela_inicio()
load()
main_loop(screen)
pygame.quit()

#Debug