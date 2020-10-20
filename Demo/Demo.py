import random
import time
import json
import pygame
import sys


class Pygame:
    def __init__(self):
        self.screen = None
        self.press_text = "- Press any button -"
        self.clock = None

    def start_game(self):
        pygame.init()
        bg_start = pygame.image.load("image/BG/DragondemoDemo.png")
        self.screen = pygame.display.set_mode((800, 500))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("The revenge of Gandara")
        running = True
        while running:
            self.screen.blit(bg_start, (0, 0))
            self.press_tx()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_RETURN:
                        game = Game()
                        mode = "start game"
                        if mode == "start game":
                            char = game.select_char()
                            if not char:
                                continue
                            player = Player(char)

                        game.stage(player)
                        while True:
                            process = game.process_chapter(player)
                            item = game.process_battle(process, player)
                            if item == 1 or item == 2:
                                re = game.item(item, player)
                                if not re:
                                    continue
                            elif item == 3:
                                continue

                            if game.enemy.hp <= 0:
                                break

                            game.process_enemy(player)
                            if player.hp <= 0:
                                break

                        game.end(player)
            pygame.display.flip()

    def press_tx(self):
        pygame.font.init()
        font = pygame.font.Font("alagard.ttf", 30)
        text_surface = font.render(self.press_text, False, (0, 0, 0))
        self.screen.blit(text_surface, (270, 400))


class Game:
    def __init__(self, chapter=1):
        self.atk = None
        self.chapter = chapter
        self.enemy = None

    @staticmethod
    def select_char():
        running = True
        arrow = Arrow((30, 405), (270, 405), (520, 405))
        position = arrow.pos1
        bg_char = pygame.image.load("image/BG/plain bg.png")
        while running:
            main.screen.blit(bg_char, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if position == arrow.pos1:
                            position = arrow.pos2

                        elif position == arrow.pos2:
                            position = arrow.pos3

                    if event.key == pygame.K_LEFT:
                        if position == arrow.pos2:
                            position = arrow.pos1

                        elif position == arrow.pos3:
                            position = arrow.pos2

                    if event.key == pygame.K_BACKSPACE:
                        return False

                    if event.key == pygame.K_RETURN:
                        if position == arrow.pos1:
                            return "DollyFish"
                        elif position == arrow.pos2:
                            return "Madmook"
                        elif position == arrow.pos3:
                            return "LittleMint"

            main.screen.blit(arrow.arrow, position)
            pygame.display.flip()

    def stage(self, player):
        if self.chapter == 1:
            self.enemy = Enemy("Lord Chavis", 15)

        bg_stage2 = pygame.image.load("image/BG/battle bg.png")
        running = True
        while running:
            main.screen.blit(bg_stage2, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    return

            main.screen.blit(player.sprite, (player.x, player.y))
            main.screen.blit(self.enemy.sprite, (self.enemy.x, self.enemy.y))
            self.display_text(self.enemy.text, (250, 410))
            self.hp_bar(player)
            if player.x >= 120:
                player.x -= 10

            if self.enemy.x <= 480:
                self.enemy.x += 10

            pygame.display.flip()

    def hp_bar(self, player):
        if player.hp < 0:
            player.hp = 0

        if self.enemy.hp < 0:
            self.enemy.hp = 0

        self.display_text(f"{player.name}", (490, 230))
        self.display_text(f"HP: {player.hp}   MP : {player.mp}", (520, 280))
        self.display_text(f"{self.enemy.name}", (80, 65))
        self.display_text(f"HP: {self.enemy.hp}", (130, 110))

    @staticmethod
    def display_text(text, position):
        dis_font = pygame.font.Font("alagard.ttf", 30)
        text_surface = dis_font.render(text, False, (0, 0, 0))
        main.screen.blit(text_surface, position)

    def process_chapter(self, player):
        bg_stage = pygame.image.load("image/BG/battle bg.png")
        running = True
        arrow = Arrow((55, 427), (290, 427), (520, 427))
        position = arrow.pos1
        while running:
            main.screen.blit(bg_stage, (0, 0))
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

                    if event.key == pygame.K_LEFT:
                        if position == arrow.pos2:
                            position = arrow.pos1

                        elif position == arrow.pos3:
                            position = arrow.pos2

                    if event.key == pygame.K_RETURN:
                        if position == arrow.pos1:
                            return 1
                        elif position == arrow.pos2:
                            return 2
                        elif position == arrow.pos3:
                            return 3

            main.screen.blit(player.sprite, (player.x, player.y))
            main.screen.blit(self.enemy.sprite, (self.enemy.x, self.enemy.y))
            self.hp_bar(player)
            self.battle_command(player)
            main.screen.blit(arrow.arrow, position)
            pygame.display.flip()

    def battle_command(self, player):
        self.display_text(f"What {player.name} do?", (80, 375))
        self.display_text(" 1 ATTACK             2 SPELL             3 ITEM", (100, 430))

    def item(self, item, player):
        bg_stage = pygame.image.load("image/BG/battle bg.png")
        running = True
        check = False
        while running:
            main.screen.blit(bg_stage, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if check:
                            if item == 1:
                                restore = 0
                                while player.hp < player.max_hp:
                                    player.hp += 1
                                    restore += 1
                                    if restore == 3:
                                        break
                                player.potion -= 1
                                return True
                            elif item == 2:
                                restore = 0
                                while player.mp < player.max_mp:
                                    player.mp += 1
                                    restore += 1
                                    if restore == 3:
                                        break
                                player.mana_potion -= 1
                                return True
                        else:
                            return False
            if item == 1:
                if player.potion == 0:
                    self.display_text("You don't have item....", (250, 410))

                elif player.hp == player.max_hp:
                    self.display_text("You have full HP!!", (250, 410))

                else:
                    self.display_text(f"{player.name} restored HP!", (250, 410))
                    check = True

            elif item == 2:
                if player.mana_potion == 0:
                    self.display_text("You don't have item....", (250, 410))

                elif player.mp == player.max_mp:
                    self.display_text("You have full MP!!", (250, 410))

                else:
                    self.display_text(f"{player.name} restored MP!", (250, 410))
                    check = True

            main.screen.blit(player.sprite, (player.x, player.y))
            main.screen.blit(self.enemy.sprite, (self.enemy.x, self.enemy.y))
            self.hp_bar(player)
            pygame.display.flip()

    def process_battle(self, command, player):
        self.atk = player.atk
        bg_stage = pygame.image.load("image/BG/battle bg.png")
        running = True
        arrow = Arrow((35, 427), (300, 427), (580, 427))
        position = arrow.pos1
        check = True
        while running:
            main.screen.blit(bg_stage, (0, 0))
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

                    if event.key == pygame.K_LEFT:
                        if position == arrow.pos2:
                            position = arrow.pos1

                        elif position == arrow.pos3:
                            position = arrow.pos2

                    if event.key == pygame.K_RETURN:
                        if check:
                            if command == 1:
                                self.enemy.hp -= self.atk
                                return
                            elif command == 2:
                                self.enemy.hp -= self.atk * 2
                                player.mp -= 1
                                return
                            elif command == 3:
                                if position == arrow.pos1:
                                    return 1

                                elif position == arrow.pos2:
                                    return 2

                                elif position == arrow.pos3:
                                    return 3
                        else:
                            return

            main.screen.blit(player.sprite, (player.x, player.y))
            main.screen.blit(self.enemy.sprite, (self.enemy.x, self.enemy.y))
            self.hp_bar(player)

            if command == 1:
                self.display_text(f"{player.name} use slash !!!", (250, 395))
                # self.critical()
                self.display_text(f"{self.enemy.name} lost {self.atk} HP!", (250, 425))

            elif command == 2:
                if player.mp != 0:
                    self.display_text(f"{player.name} use magic !!!", (250, 395))
                    # self.critical()
                    self.display_text(f"{self.enemy.name} lost {self.atk * 2} HP!", (250, 425))
                else:
                    self.display_text("You don't have MP!", (250, 410))
                    check = False

            elif command == 3:
                self.display_text(f"Choose your items", (60, 375))
                self.display_text(
                    f" 1 HP Potion x{player.potion}        2 MP Potion x{player.mana_potion}        3 Back", (70, 430))
                main.screen.blit(arrow.arrow, position)
            pygame.display.flip()

    def process_enemy(self, player):
        self.atk = self.enemy.atk
        ran_list = [1, 2]
        ran_list2 = [1, 2, 3]
        ran = random.choice(ran_list)
        ran2 = random.choice(ran_list2)
        if self.enemy.mp == 0:
            ran = 1

        bg_stage = pygame.image.load("image/BG/battle bg.png")
        running = True
        while running:
            main.screen.blit(bg_stage, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if ran == 2 and ran2 == 3:
                            restore = 0
                            while self.enemy.hp < self.enemy.max_hp:
                                self.enemy.hp += 1
                                restore += 1
                                if restore == 2:
                                    break
                        if ran == 1:
                            player.hp -= self.atk
                        elif ran == 2:
                            player.hp -= self.atk * 2

                        return

            if ran == 2 and ran2 == 3:
                if self.enemy.hp == self.enemy.max_hp:
                    self.display_text(f"{self.enemy.name} use healing but full HP...", (220, 410))
                else:
                    self.display_text(f"{self.enemy.name} use healing!!!", (230, 410))

            elif ran == 1:
                self.display_text(f"{self.enemy.name} use Hamon punch!!!", (180, 395))
                self.display_text(f"{player.name} lost {self.atk} hp!", (260, 425))

            elif ran == 2:
                self.display_text(f"{self.enemy.name} use GLUT!!!", (230, 395))
                self.display_text(f"{player.name} lost {self.atk * 2} hp!", (260, 425))

            main.screen.blit(player.sprite, (player.x, player.y))
            main.screen.blit(self.enemy.sprite, (self.enemy.x, self.enemy.y))
            self.hp_bar(player)
            pygame.display.flip()

    def critical(self):
        cri = random.randint(1, 10)
        if cri == 5:
            self.atk *= 2
            print("Critical damage!!!")

    def end(self, player):
        bg_stage = pygame.image.load("image/BG/battle bg.png")
        running = True
        while running:
            main.screen.blit(bg_stage, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return

            main.screen.blit(player.sprite, (player.x, player.y))
            if player.hp <= 0:
                self.display_text(f"{player.name} have been defeated", (200, 410))
                if player.x >= -200:
                    player.x -= 20

            main.screen.blit(self.enemy.sprite, (self.enemy.x, self.enemy.y))
            if self.enemy.hp <= 0:
                self.display_text(f"{self.enemy.name} have been defeated", (200, 410))
                if self.enemy.x <= 900:
                    self.enemy.x += 20

            self.hp_bar(player)
            pygame.display.flip()


class Object:
    def __init__(self, name, hp, mp, atk):
        self.name = name
        self.max_hp = hp
        self.hp = self.max_hp
        self.atk = atk
        self.max_mp = mp
        self.mp = self.max_mp


class Player(Object):
    def __init__(self, name, hp=10, mp=5, atk=2):
        if name == "DollyFish":
            self.sprite = pygame.image.load("image/sprite/dolly fish_half.png")
            self.sprite = pygame.transform.scale(self.sprite, (200, 173))
        elif name == "Madmook":
            self.sprite = pygame.image.load("image/sprite/madmook.png")
            self.sprite = pygame.transform.scale(self.sprite, (200, 173))
        elif name == "LittleMint":
            self.sprite = pygame.image.load("image/sprite/lil mint.png")
            self.sprite = pygame.transform.scale(self.sprite, (210, 173))

        self.x = 550
        self.y = 170
        self.potion = 3
        self.mana_potion = 3
        super().__init__(name, hp, mp, atk)


class Enemy(Object):
    def __init__(self, name, hp=10, mp=5, atk=1):
        if name == "Lord Chavis":
            self.sprite = pygame.image.load("image/sprite/lord cv.png")
            self.sprite = pygame.transform.scale(self.sprite, (195, 257))
        self.text = f"{name} appeared"
        self.x = -30
        self.y = -30

        super().__init__(name, hp, mp, atk)


class Arrow:
    def __init__(self, pos1, pos2, pos3):
        self.arrow = pygame.image.load("image/sprite/right-arrow.png")
        self.pos1 = pos1
        self.pos2 = pos2
        self.pos3 = pos3


if __name__ == '__main__':
    main = Pygame()
    main.start_game()
