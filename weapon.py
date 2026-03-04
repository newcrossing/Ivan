import math

import pygame
import random

from constants import HEIGHT, WIDTH


class Weapon(pygame.sprite.Sprite):
    img = pygame.image.load('src/ball.png')
    sizeBullet = (9, 9)
    ammo = 5  # боезапас
    ammoAll = 50  # Всего патронов
    AMMO_E = 5  # емкость магазина

    # Передаем для инициализации координаты места старта x и y
    def __init__(self, x, y, deg=0):
        """
        Инициализирует полет снаряда.

        :param x: координаты старта x
        :param y: координаты старта y
        :param deg: угол полета санряда в градусах, 0 - вверх, далее по часовой стрелке
        """
        sound_shot = pygame.mixer.Sound('src/music/shot.wav')
        sound_shot.play()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(self.sizeBullet)
        self.image = pygame.transform.scale(self.img, self.sizeBullet)

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.deg = deg

        self.floatX = x  # реальные координаты в float x
        self.floatY = y  # реальные координаты в float y

        self.speed = 5  # скорость полета санаряда

        Weapon.ammo -= 1

    def update(self):
        self.floatY -= math.cos(math.radians(self.deg)) * self.speed
        self.floatX += math.sin(math.radians(self.deg)) * self.speed

        self.rect.y = self.floatY
        self.rect.x = self.floatX

        # убить, если он заходит за верхнюю часть экрана
        if (self.rect.bottom < 0 or self.rect.top > HEIGHT or
                self.rect.left > WIDTH or self.rect.right < 0):
            # Weapon.ammo += 1
            self.kill()

    @staticmethod
    def reloadWeapon():
        """
        Перезарядка оружия

        """
        diff = Weapon.AMMO_E - Weapon.ammo  # сколько патронов не хватает в магине сейчас
        # TODO: Сделать ограничение, сейчас патроны могут уйти  в минус при перезарядке
        Weapon.ammoAll -= 5
        Weapon.ammo = 5
        sound_shot = pygame.mixer.Sound('src/music/reload.wav')
        sound_shot.play()

    @staticmethod
    def shot_fail():
        sound_shot = pygame.mixer.Sound('src/music/shot_fail.wav')
        sound_shot.play()


