import pygame

#初期化
pygame.init()

#画面の大きさ
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#タイトル
pygame.display.set_caption("My game")

#イベントループ
#ゲーム進行中
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #ウィンドウ閉じたらループ終了
            running = False

#ゲーム終了
pygame.quit()

