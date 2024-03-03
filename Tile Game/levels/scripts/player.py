import pygame
from pygame.locals import *

class Player:
    def __init__(self, pos):

        self.velocity = {
            "right":False,
            "left":False,
            "up":False,
            "down":False
            }
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((50, 25, 25))
        self.rect = self.surf.get_rect()
        self.rect.center = pos

    def check_for_movement(self, event):

        if event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == K_d:
                self.velocity["right"] = True
            if event.key == K_LEFT or event.key == K_a:
                self.velocity["left"] = True
            if event.key == K_UP or event.key == K_w:
                self.velocity["up"] = True
            if event.key == K_DOWN or event.key == K_s:
                self.velocity["down"] = True
        if event.type == KEYUP:
            if event.key == K_RIGHT or event.key == K_d:
                self.velocity["right"] = False
            if event.key == K_LEFT or event.key == K_a:
                self.velocity["left"] = False
            if event.key == K_UP or event.key == K_w:
                self.velocity["up"] = False
            if event.key == K_DOWN or event.key == K_s:
                self.velocity["down"] = False

    def walk(self):

        self.rect.x += (self.velocity["right"] * 1)
        self.rect.x -= (self.velocity["left"] * 1)
        self.rect.y -= (self.velocity["up"] * 1)
        self.rect.y += (self.velocity["down"] * 1)


    def check_for_collisions(self, tiles_of_map):

        for tile in tiles_of_map:
            if self.rect.colliderect(tile):
                if self.velocity["right"] == True:
                    self.rect.x -= 1
                if self.velocity["left"] == True:
                    self.rect.x += 1
                if self.velocity["up"] == True:
                    self.rect.y += 1
                if self.velocity["down"] == True:
                    self.rect.y -= 1


    def render(self, display):

        display.blit(self.surf, self.rect)