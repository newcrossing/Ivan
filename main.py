import math

import pygame
import random
from constants import *
from text import Text
from weapon import *
from text import *

# Создаем игру и окно
pygame.init()

pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Бой")
clock = pygame.time.Clock()

text = Text()
text.setAmmoAll(Weapon.ammoAll)
text.setAmmo(Weapon.ammo)

class Gun(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image = pygame.image.load('src/wepon.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.bottom = 100



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


            all_sprites.add(bullet)
            bullets_spites.add(bullet)


# Создаю спрайты 2 штуки
all_sprites = pygame.sprite.Group()
bullets_spites = pygame.sprite.Group()
gun_spites = pygame.sprite.Group()
player_spites = pygame.sprite.Group()

# Создаю игрока
player = Player()
gun = Gun()

# Добавляю игрока в спрайт
all_sprites.add(player)
player_spites.add(player)

all_sprites.add(gun)
gun_spites.add(gun)


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
            if event.key == pygame.K_r:
                Weapon.reloadWeapon()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # ищу угол между точками
                dy = player.rect.centerx - mouse_x
                dx = player.rect.centery - mouse_y
                rads = math.atan2(-dy, dx)
                degs = math.degrees(rads)
                player.shoot(degs)

    # Обновление
    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, gun_spites, False)
    if hits:
        print(hits)

    # Рендеринг
    screen.fill(WHITE)
    all_sprites.draw(screen)

    text.setAmmo(Weapon.ammo)
    text.setAmmoAll(Weapon.ammoAll)
    text.blit(screen)

    # После отрисовки всего
    pygame.display.flip()

pygame.quit()
