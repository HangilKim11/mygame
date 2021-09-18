import pygame

#初期化
pygame.init()

#画面の大きさ
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#タイトル
pygame.display.set_caption("My game")

#FPS
clock = pygame.time.Clock()


#背景呼び出し
background = pygame.image.load("C:/Python workspace/Project-mygame/background.jpg")

#スプライト(キャラクタ)呼び出し
character = pygame.image.load("C:/Python workspace/Project-mygame/character2.png")

#スプライト(キャラクタ)大きさ
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xpos = (screen_width - character_width) / 2 #画面中央に位置
character_ypos = screen_height-character_height - 50 #画面の一番下に位置

#移動距離
to_x = 0
to_y = 0

#移動スピード
character_speed = 0.5

#イベントループ
#ゲーム進行中
running = True
while running:
    dt = clock.tick(60) #1秒間のフレーム数
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #ウィンドウ閉じたら
            running = False #ループ終了

        if event.type == pygame.KEYDOWN: #キー押したら
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: #キー放したら
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    #速度にdtかけることでフレーム関係なく速度維持
    character_xpos += to_x * dt
    character_ypos += to_y * dt

    #画面から出られなくする
    if character_xpos < 0:
        character_xpos = 0
    elif character_xpos > screen_width - character_width:
        character_xpos = screen_width - character_width

    if character_ypos < 0:
        character_ypos = 0
    elif character_ypos > screen_height - character_height:
        character_ypos = screen_height - character_height


    #screen.fill((0, 0, 255)) #RGBで背景描く
    screen.blit(background, (0, 0)) #イメージで背景描く
    screen.blit(character, (character_xpos, character_ypos)) #イメージでスプライト(キャラクタ)描く
    pygame.display.update() #背景アップデート

#ゲーム終了
pygame.quit()

