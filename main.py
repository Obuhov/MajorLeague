import pygame
pygame.init()

# Окно. HWSURFACE- (HardwareAcRen) аппаратное ускорение отрисовки(Fullscr)
sc = pygame.display.set_mode((800, 600), pygame.HWSURFACE | pygame.FULLSCREEN)
pygame.display.set_caption('Major League')
pygame.display.set_icon(pygame.image.load("img/logo/logoTest.ico"))

white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

#(R, G, B) 0 - отсутствие цв. 255 - полная насыщенность цв.
# Буферизация. Перерисовка опр. Объекта (При указании)
pygame.display.update()

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
