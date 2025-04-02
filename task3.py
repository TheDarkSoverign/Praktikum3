import pygame
import time

pygame.init()

# Глобальные переменные (настройки)
window_width = 800
window_height = 600
fon = 'back.png'  # изображение должно быть в том же каталоге, что и код на питоне

# Запуск
window = pygame.display.set_mode((window_width, window_height))  # создание окна указанных размеров
pygame.display.set_caption("Игра v1.0")  # установка надписи окна программы

speed = 0  # текущая скорость перемещения
sdvig_fona = 0  # сдвиг фона

img1 = pygame.image.load(fon)  # загрузка фона игры из файла
back_fon = pygame.transform.scale(img1, (window_width, window_height))  # размеры картинки back - те же, что и у окна

class Player(pygame.sprite.Sprite):
    def __init__(self, filename, hero_x=100, hero_y=250, x_speed=0, y_speed=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)  # загрузка героя из файла
        self.rect = self.image.get_rect()
        self.rect.x = hero_x
        self.rect.y = hero_y
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        ''' перемещает персонажа, применяя текущую горизонтальную и вертикальную скорость '''
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # Ограничение границ экрана
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > window_width:
            self.rect.right = window_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > window_height:
            self.rect.bottom = window_height

        # Сдвиг фона при достижении границ
        global sdvig_fona
        if self.rect.right >= window_width:
            sdvig_fona = (sdvig_fona - 5) % window_width
        elif self.rect.left <= 0:
            sdvig_fona = (sdvig_fona + 5) % window_width

filename = 'player.png'
hero = Player(filename)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # пришло ли событие нажатия на крестик
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero.x_speed = -5
            if event.key == pygame.K_RIGHT:
                hero.x_speed = 5
            if event.key == pygame.K_UP:
                hero.y_speed = -5
            if event.key == pygame.K_DOWN:
                hero.y_speed = 5
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                hero.x_speed = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                hero.y_speed = 0

    hero.update()
    window.blit(back_fon, (sdvig_fona, 0))
    if sdvig_fona != 0:
        window.blit(back_fon, (sdvig_fona - window_width, 0))
    window.blit(hero.image, hero.rect)

    pygame.display.update()
    time.sleep(0.02)

pygame.quit()
