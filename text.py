import math

import pygame
import random
from constants import *
from weapon import *


class Text():
    ammo = 0
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font(None, 30)

    def blit(self, screen):
        screen.blit(self.renderAmmoAll, (WIDTH - 200, 10))
        screen.blit(self.renderAmmo, (WIDTH - 200, 30))

    def setAmmoAll(self, text):
        self.ammoAll = text
        self.renderAmmoAll = self.font.render(f"Патроны: {str(self.ammoAll)}", True, (0, 0, 0))


    def setAmmo(self, text):
        self.ammo = text
        self.renderAmmo = self.font.render(f"В магазине: {str(self.ammo)}", True, (0, 0, 0))
