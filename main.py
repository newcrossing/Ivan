import math

import pygame
import random

from pygame.examples.midi import NullKey

WIDTH = 480
HEIGHT = 600
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Бой")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((90, 90))
        self.image = pygame.image.load('src/hero.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_UP]:
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.speedy = 8


        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.centery)
        all_sprites.add(bullet)
        bullets_spites.add(bullet)


class Bullet(pygame.sprite.Sprite):
    img = pygame.image.load('src/ball.png')
    speedy = -5
    sizeBullet = (9, 9)

    # Передаем для инициализации координаты места старта x и y

    def __init__(self, x, y, deg=20):
        """
        Инициализирует полет снаряда.

        :param x: координаты старта x
        :param y: координаты старта y
        :param deg: угол полета санряда в градусах, 0 - вверх, далее по часовой стрелке
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.sizeBullet))
        self.image = pygame.transform.scale(self.img, (self.sizeBullet))

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.deg = deg

        self.floatX = x  # реальные координаты в float x
        self.floatY = y  # реальные координаты в float y

        self.speed = random.randrange(1, 1000) / 100


        print(f"cos= {math.cos(math.radians(self.deg))}, sin= {math.sin(math.radians(self.deg))}")

    def update(self):
        self.floatY -= math.cos(math.radians(self.deg)) * self.speed
        self.floatX += math.sin(math.radians(self.deg)) * self.speed

        self.rect.y = self.floatY
        self.rect.x = self.floatX

        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()


# Создаю спрайты 2 штуки
all_sprites = pygame.sprite.Group()
bullets_spites = pygame.sprite.Group()

# Создаю игрока
player = Player()

# Добавляю игрока в спрайт
all_sprites.add(player)
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)

    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
        elif event.type == pygame.MOUSEBUTTONUP:
            player.shoot()
    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(WHITE)
    all_sprites.draw(screen)
    # После отрисовки всего
    pygame.display.flip()

pygame.quit()
