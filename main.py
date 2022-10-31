import pygame
pygame.init()

# Окно
pygame.display.set_mode((800, 600))
pygame.display.set_caption('Major League')
pygame.display.set_icon(pygame.image.load("img/logo/logoTest.ico"))

# ФПС
clock = pygame.time.Clock()
FPS = 60  # Число итераций цикла за секунду. Frames Per Second (17 млс)

# Основной цикл обработки. Закрытие проги
GmRun = True
while GmRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            GmRun = False

clock.tick(FPS)
