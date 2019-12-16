import os
from pathlib import Path, PurePath
import sys

import pygame
from pygame.locals import *

main_dir = Path(".")
main_dir = main_dir.resolve()  # Convert to absolute path
data_dir = Path(PurePath(main_dir).joinpath("data"))
data_dir = data_dir.resolve()


def load_image(name, color_key=None):
    """Load named image"""
    full_name = Path(PurePath(data_dir).joinpath(name))
    try:
        # image = pygame.image.load(full_name.resolve())
        image = pygame.image.load("HMI_test/data/Valve.svg")
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
        # self.image = load_image("Valve.svg")
        self.image = pygame.image.load("/home/codyjackson/PycharmProjects/PyGame-HMI/HMI_test/data/Valve.png")
        self.rect = self.image.get_rect()
        self.area = screen.get_rect()
        # self.rect.topleft = 300, 200

    def change_position(self):
        pass


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    screen.blit(background, (0, 0))
    pygame.display.flip()

    valve = Valve()
    all_sprites = pygame.sprite.RenderPlain(valve)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                run = False

        all_sprites.update()

        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()