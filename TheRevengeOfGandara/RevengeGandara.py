import story
import time
import pygame
import sys
import json
import char_select
import object
import game


class StartGame:
    def __init__(self):
        self.screen = None
        self.press_text = "- Press any button -"
        self.chapter = 1
        self.clock = None
        self.char = None
        self.start_game()

    def start_game(self):
        pygame.init()
        bg_start = pygame.image.load("image/BG/Gandara.png")
        arrow = object.Arrow((80, 425), (300, 425), (530, 425))
        self.screen = pygame.display.set_mode((800, 500))
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        pygame.display.set_caption("The revenge of Gandara")
        text = self.press_text
        pos_tx = (270, 420)
        pos_arrow = arrow.pos1
        running = True
        while running:
            self.screen.blit(bg_start, (0, 0))
            if text == self.press_text:
                if time.time() % 1 < 0.4:
                    self.press_tx(text, pos_tx)
            else:
                self.press_tx(text, pos_tx)
                if time.time() % 1 < 0.4:
                    self.screen.blit(arrow.arrow, pos_arrow)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if text != self.press_text:
                        if event.key == pygame.K_RIGHT:
                            if pos_arrow == arrow.pos1:
                                pos_arrow = arrow.pos2

                            elif pos_arrow == arrow.pos2:
                                pos_arrow = arrow.pos3

                        elif event.key == pygame.K_LEFT:
                            if pos_arrow == arrow.pos2:
                                pos_arrow = arrow.pos1

                            elif pos_arrow == arrow.pos3:
                                pos_arrow = arrow.pos2

                        elif event.key == pygame.K_RETURN:
                            if pos_arrow == arrow.pos1:
                                self.chapter = 1
                                return
                            elif pos_arrow == arrow.pos2:
                                try:
                                    with open("save_game.json", "r") as f:
                                        r = json.load(f)
                                        self.chapter = r[1]
                                except FileNotFoundError:
                                    pass
                                return
                            elif pos_arrow == arrow.pos3:
                                pygame.quit()
                                sys.exit()

                    text = "New Game         Load Game          Exit"
                    pos_tx = (120, 430)
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            pygame.display.flip()

    def press_tx(self, text, position):
        pygame.font.init()
        font = pygame.font.Font("alagard.ttf", 30)
        text_surface = font.render(text, False, (0, 0, 0))
        self.screen.blit(text_surface, position)


def main_game():
    main = StartGame()
    while main.chapter <= 5:
        story.story(main)
        if main.chapter == 1:
            main.char = char_select.select_char(main)
        elif main.chapter == 5:
            main_game()
        with open("save_game.json", "r") as f:
            r = json.load(f)
            main.chapter = r[1]
            main.char = r[0]
            player = object.Player(main.char, r[2], r[3], r[4], r[5])
        games = game.Game()
        games.stage(player, main)


if __name__ == '__main__':
    main_game()
