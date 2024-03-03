import pygame
from pygame.locals import *


class pyButton:
    def __init__(self, display, pos = (0, 0), size = (20, 20), color = (255, 255, 255), text = "", command = lambda: None, hover_color = (255, 255, 255), hover_text_color = (0, 0, 0), corner_radius = 0, border = 0, border_color = (0, 0, 0), text_size = 10):

        pygame.init()

        self.display = display
        self.pos = pos
        self.size = size
        self.color = color
        self.text = text
        self.text_size = text_size
        self.display = display
        self.command = command
        self.hover_color = hover_color
        self.hover_text_color = hover_text_color
        self.corner_radius = corner_radius
        self.border = border
        self.border_color = border_color

        self.rect_color = self.color

        self.font = pygame.font.SysFont("Arial", text_size)
        self.show_text = self.font.render(self.text, False, (0, 0, 0)).convert()
        self.show_text_rect = self.show_text.get_rect()

        self.rect = pygame.Rect((0, 0), self.size)
        self.rect.center = self.pos

        self.show_text_rect.center = self.rect.center

    def detect_hover(self):

        if self.rect.colliderect(pygame.Rect((pygame.mouse.get_pos()[0] / 4, pygame.mouse.get_pos()[1] / 4),(1, 1))):
            self.rect_color = self.hover_color
        else: self.rect_color = self.color

    def check_for_click(self, event):

        if event.type == MOUSEBUTTONDOWN:
            self.command()

    def render(self):

        self.detect_hover()
        pygame.draw.rect(self.display, self.rect_color, self.rect, 0, self.corner_radius)
        if self.border >= 1:
            pygame.draw.rect(self.display, self.border_color, self.rect, self.border, self.corner_radius)
        self.display.blit(self.show_text, self.show_text_rect)
