import pygame


class Box(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image = pygame.image.load('src/box.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.bottom = 100