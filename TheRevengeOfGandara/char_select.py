from object import Arrow
import pygame
import time
import sys
import json


def select_char(main):
    pygame.init()
    running = True
    arrow = Arrow((40, 405), (280, 405), (530, 405))
    position = arrow.pos1
    bg_char = pygame.image.load("image/BG/select_bg.png")
    while running:
        main.screen.blit(bg_char, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if position == arrow.pos1:
                        position = arrow.pos2

                    elif position == arrow.pos2:
                        position = arrow.pos3

                elif event.key == pygame.K_LEFT:
                    if position == arrow.pos2:
                        position = arrow.pos1

                    elif position == arrow.pos3:
                        position = arrow.pos2

                elif event.key == pygame.K_RETURN:
                    if position == arrow.pos1:
                        save(main, "DollyFish")
                        return "DollyFish"
                    elif position == arrow.pos2:
                        save(main, "Madmook")
                        return "Madmook"
                    elif position == arrow.pos3:
                        save(main, "LittleMint")
                        return "LittleMint"

        if time.time() % 1 < 0.4:
            main.screen.blit(arrow.arrow, position)
        pygame.display.flip()


def save(main, char):
    with open("save_game.json", "w") as f:
        data = [char, main.chapter, 20, 5, 7, 7]
        json.dump(data, f)
