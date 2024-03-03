class Level_2:
    def __init__(self, display, screen):

        import pygame
        from pygame.locals import KEYDOWN, QUIT, K_ESCAPE

        from levels.scripts.camera import Camera_for_small_spaces, Camera_for_big_spaces
        from levels.scripts.levels_map import level_2

        from levels.scripts.player import Player
        from levels.scripts.map import Map
        

        pygame.init()

        player = Player(pos=display.get_rect().center)
        map = Map(level=level_2)

        clock = pygame.time.Clock()
        running = True
        while running:
            screen.fill((20, 24, 30))
            screen.blit(pygame.transform.scale(display, screen.get_size()), Camera_for_big_spaces(display, (0, 0), player.rect.center))
            display.fill((14, 200, 210))



            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    running = False

                player.check_for_movement(event=event)


            player.walk()
            player.check_for_collisions(map.tiles)
            player.render(display)
            map.map_render(display)

            pygame.display.flip()
            clock.tick(60)