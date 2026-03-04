import math

import pygame
import random
from constants import *
from text import Text
from weapon import *
from text import *
from box import *

# Создаем игру и окно
pygame.init()

pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Бой")
clock = pygame.time.Clock()

text = Text()
text.setAmmoAll(Weapon.ammoAll)
text.setAmmo(Weapon.ammo)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((90, 90))
        self.image = pygame.image.load('src/hero.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = int(WIDTH / 2)
        self.rect.bottom = int(HEIGHT - 10)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -8
        if keystate[pygame.K_d]:
            self.speedx = 8
        if keystate[pygame.K_w]:
            self.speedy = -8
        if keystate[pygame.K_s]:
            self.speedy = 8
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed():
                Weapon.reloadWeapon()

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self, deg):
        if Weapon.ammo > 0:
            bullet = Weapon(self.rect.centerx, self.rect.centery, deg)

            sprites_all.add(bullet)
            sprites_weapon.add(bullet)

    def get_deg(self, x2, y2):
        """
        Получает унол между двумя точками в градусах

        """
        dy = self.rect.centerx - x2
        dx = self.rect.centery - y2
        rads = math.atan2(-dy, dx)
        return math.degrees(rads)


# Создаю спрайты группы
sprites_all = pygame.sprite.Group()
sprites_weapon = pygame.sprite.Group()
sprites_box = pygame.sprite.Group()
sprites_player = pygame.sprite.Group()

# Создаю игрока
player = Player()
box = Box()

# Добавляю игрока в спрайт
sprites_all.add(player)
sprites_player.add(player)

sprites_all.add(box)
sprites_box.add(box)

running = True

while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
            if event.key == pygame.K_r:
                Weapon.reloadWeapon()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                player.shoot(player.get_deg(mouse_x, mouse_y))

    # Обновление
    sprites_all.update()

    hits = pygame.sprite.spritecollide(player, sprites_box, False)
    # if hits:
    #     print(hits)

    # Рендеринг
    screen.fill(WHITE)
    sprites_all.draw(screen)

    text.setAmmo(Weapon.ammo)
    text.setAmmoAll(Weapon.ammoAll)
    text.blit(screen)

    # После отрисовки всего
    pygame.display.flip()

pygame.quit()
