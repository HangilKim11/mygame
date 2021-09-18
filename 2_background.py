import pygame

#初期化
pygame.init()

#画面の大きさ
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#タイトル
pygame.display.set_caption("My game")

#背景
background = pygame.image.load("C:/Python workspace/Project-mygame/background.jpg")

#イベントループ
#ゲーム進行中
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #ウィンドウ閉じたらループ終了
            running = False
    
    #screen.fill((0, 0, 255)) #RGBで背景描く
    screen.blit(background, (0, 0)) #イメージで背景描く
    pygame.display.update() #背景アップデート

#ゲーム終了
pygame.quit()

