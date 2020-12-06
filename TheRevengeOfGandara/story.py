from RevengeGandara import *
import pygame
import json
import sys


def story(main):
    pygame.init()
    if main.chapter == 1:
        file = "text/prologue_text.json"
    elif main.chapter == 2:
        file = "text/chapter2.json"
    elif main.chapter == 3:
        file = "text/chapter3.json"
    elif main.chapter == 4:
        file = "text/chapter4.json"
    else:
        file = "text/ending.json"

    with open(file, "r") as f:
        r = json.load(f)
        i = 0
        if main.chapter == 1:
            bg_story = pygame.image.load("image/BG/prologue_1.png")
        elif main.chapter == 2:
            bg_story = pygame.image.load("image/BG/chap2.png")
        elif main.chapter == 3:
            bg_story = pygame.image.load("image/BG/chap3.png")
        elif main.chapter == 4:
            bg_story = pygame.image.load("image/BG/black_bg.png")
        else:
            with open("save_game.json", "r") as f:
                read = json.load(f)
                player = read[0]
            if player == "DollyFish":
                bg_story = pygame.image.load("image/BG/ending_dol.png")
            elif player == "LittleMint":
                bg_story = pygame.image.load("image/BG/ending_mint.png")
            elif player == "Madmook":
                bg_story = pygame.image.load("image/BG/ending_mook.png")

        running = True
        while running:
            main.screen.blit(bg_story, (0, 0))
            text = r[i]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        i += 1
                        if i == len(r):
                            return

            if main.chapter == 1:
                if i == 2:
                    bg_story = pygame.image.load("image/BG/prologue_2.png")
                elif i == 7:
                    bg_story = pygame.image.load("image/BG/prologue_3.png")
                elif i == 11:
                    bg_story = pygame.image.load("image/BG/prologue_4.png")

            elif main.chapter == 3:
                if i == 2:
                    bg_story = pygame.image.load("image/BG/white_bg.png")

            elif main.chapter == 4:
                if i == 3:
                    bg_story = pygame.image.load("image/BG/ch4_dragon.png")

            else:
                if i == 5:
                    bg_story = pygame.image.load("image/BG/ending.png")

            if 1 <= len(r[i]) <= 5:
                position = (365, 410)
            elif 6 <= len(r[i]) <= 8:
                position = (360, 410)
            elif 9 <= len(r[i]) <= 10:
                position = (350, 410)
            elif 11 <= len(r[i]) <= 14:
                position = (345, 410)
            elif 15 <= len(r[i]) == 17:
                position = (270, 410)
            elif 18 <= len(r[i]) == 22:
                position = (240, 410)
            elif 23 <= len(r[i]) <= 25:
                position = (230, 410)
            elif 26 <= len(r[i]) <= 28:
                position = (210, 410)
            elif 29 <= len(r[i]) <= 31:
                position = (200, 410)
            elif 32 <= len(r[i]) <= 35:
                position = (160, 410)
            elif 36 <= len(r[i]) <= 37:
                position = (150, 410)
            elif 38 <= len(r[i]) <= 40:
                position = (125, 410)
            elif 41 <= len(r[i]) <= 42:
                position = (115, 410)
            elif 43 == len(r[i]) :
                position = (105, 410)
            elif 44 == len(r[i]) :
                position = (75, 410)
            elif 45 <= len(r[i]) <= 50:
                position = (65, 410)
            elif len(r[i]) >= 51:
                position = (35, 410)

            main.press_tx(text, position)
            pygame.display.flip()


if __name__ == '__main__':
    main = StartGame()
    i = 1
    while i != 6:
        main.chapter = i
        story(main)
        i += 1

