import pygame

def Camera_for_small_spaces(display, display_pos, player_center_pos):

    offset = pygame.math.Vector2()
    offset.x = display.get_width() / 2 - player_center_pos[0]
    offset.y = display.get_height() / 2 - player_center_pos[1]

    new_pos = pygame.math.Vector2()
    new_pos.x = (display_pos[0] + offset.x) * 2.5
    new_pos.y = (display_pos[1] + offset.y) * 2.5

    return new_pos

def Camera_for_big_spaces(display, display_pos, player_pos):

    offset = pygame.math.Vector2()
    offset.x = display.get_width() / 2 - player_pos[0]
    offset.y = display.get_height() / 2 - player_pos[1]

    new_pos = pygame.math.Vector2()
    new_pos.x = (display_pos[0] + offset.x) * 4
    new_pos.y = (display_pos[1] + offset.y) * 4

    return new_pos