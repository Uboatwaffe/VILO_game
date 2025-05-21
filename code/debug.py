import pygame

pygame.init()
font = pygame.font.Font(None, 30)


def debug(info, y=10, x=10):
    """
    A simple debug function that prints text on the screen at the specified coordinates.

    Args:
        info (str): The text to be displayed.
        y (int, optional): The y-coordinate of the text. Defaults to 10.
        x (int, optional): The x-coordinate of the text. Defaults to 10.

    """
    ''' Disabled by Uboatwaffe
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)
    '''
