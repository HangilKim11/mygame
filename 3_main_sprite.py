import pygame

#初期化
pygame.init()

#画面の大きさ
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#タイトル
pygame.display.set_caption("My game")

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

#イベントループ
#ゲーム進行中
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #ウィンドウ閉じたらループ終了
            running = False
    
    #screen.fill((0, 0, 255)) #RGBで背景描く
    screen.blit(background, (0, 0)) #イメージで背景描く
    screen.blit(character, (character_xpos, character_ypos)) #イメージでスプライト(キャラクタ)描く
    pygame.display.update() #背景アップデート

#ゲーム終了
pygame.quit()

