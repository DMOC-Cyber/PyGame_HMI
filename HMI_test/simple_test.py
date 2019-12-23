import os
from pathlib import Path, PurePath
import sys

import pygame
from pygame.locals import *

main_dir = Path(".")
main_dir = main_dir.resolve()  # Convert to absolute path
data_dir = Path(PurePath(main_dir).joinpath("data"))
data_dir = data_dir.resolve()  # Convert to absolute path


def load_image(name, color_key=None):
    """Load named image. Assumes image is in 'data' directory."""
    full_name = Path(PurePath(data_dir).joinpath(name))
    try:
        image = pygame.image.load(full_name.resolve())
    except pygame.error:
        print(f"Cannot load image {image}")
        raise SystemExit(str(pygame.get_error()))
    image = image.convert()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_color_key(color_key, RLEACCEL)
    return image, image.get_rect()


class Valve(pygame.sprite.Sprite):
    """Generate valve symbol"""
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(str(data_dir) + "/Valve.png")
        self.rect = self.image.get_rect()
        self.area = screen.get_rect()
        self.position = False

    def change_position(self):
        """Fully open or close a valve"""
        if self.position:
            self.image = pygame.image.load(str(data_dir) + "/open_valve.png")
        else:
            self.image = pygame.image.load(str(data_dir) + "/close_valve.png")
        # else:
        #     raise ValueError("Invalid position provided")


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    screen.blit(background, (0, 0))
    pygame.display.flip()

    clock = pygame.time.Clock()
    valve = Valve()
    all_sprites = pygame.sprite.RenderPlain(valve)

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                run = False
            elif event.type == MOUSEBUTTONDOWN:
                if valve.position is False:
                    valve.position = True
                elif valve.position is True:
                    valve.position = False
                valve.change_position()

        all_sprites.update()

        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
