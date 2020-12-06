from object import *
from all_text import *
import sys
import RevengeGandara
import pygame
import time
import random
import json


class Game:
    def __init__(self):
        self.atk = None
        self.enemy_atk = None
        self.enemy = None
        self.text = None
        self.text2 = None
        self.pos_tx = None
        self.pos_tx2 = None
        self.arrow = None
        self.pos_arrow = None
        self.super_text = None
        self.weapon = None
        self.healing = None
        self.enemy_weapon = None
        self.enemy_healing = None
        self.effect = Effect()
        self.enemy_effect = None

    def stage(self, player, main):
        pygame.init()
        if main.chapter == 1:
            self.enemy = Enemy("Poppy Army", 10)
        elif main.chapter == 2:
            self.enemy = Enemy("Lord Chavis", 15)
        elif main.chapter == 3:
            self.enemy = Enemy("Chavis&Poppy", 20)
            player.x = 120
        else:
            self.enemy = Enemy("Gandragon", 25)
            player.x = 550

        self.enemy_effect = EnemyEffect(self.enemy)
        bg_stage2 = self.enemy.bg

        running = True
        self.text = self.enemy.text
        self.pos_tx = (250, 410)

        while running:
            self.super_text = Text(player, self.enemy)
            self.atk = player.atk
            self.enemy_atk = self.enemy.atk
            main.screen.blit(bg_stage2, (0, 0))
            main.screen.blit(player.sprite, (player.x, player.y))
            main.screen.blit(self.enemy.sprite, (self.enemy.x, self.enemy.y))
            if self.text:
                main.press_tx(self.text, self.pos_tx)

            if self.text2:
                main.press_tx(self.text2, self.pos_tx2)

            if self.weapon:
                if self.effect.position1 < 480:
                    self.effect.position1 += 4
                    self.effect.position2 -= 4
                main.screen.blit(self.weapon, (self.effect.position1, self.effect.position2))

            if self.healing:
                if self.effect.position2 > 180:
                    self.effect.position2 -= 2
                main.screen.blit(self.healing, (self.effect.position1, self.effect.position2))

            if self.enemy_weapon:
                if self.enemy_effect.position1 > 320:
                    self.enemy_effect.position1 -= 4
                    self.enemy_effect.position2 += 4
                main.screen.blit(self.enemy_weapon, (self.enemy_effect.position1, self.enemy_effect.position2))

            if self.enemy_healing:
                if self.enemy_effect.y_heal > 10:
                    self.enemy_effect.y_heal -= 2
                main.screen.blit(self.enemy_healing, (self.enemy_effect.x_heal, self.enemy_effect.y_heal))

            self.hp_bar(player, main)
            if self.text2 == self.super_text.player_defeat:
                if player.x >= -200:
                    player.x -= 20
                else:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                RevengeGandara.main_game()

            elif self.text2 == self.super_text.enemy_defeat:
                if self.enemy.x <= 900:
                    self.enemy.x += 20
                else:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                main.chapter += 1
                                with open("save_game.json", "w") as f:
                                    data = [player.name, main.chapter, player.hp, player.mp, player.potion,
                                            player.mana_potion]
                                    json.dump(data, f)
                                    self.text2 = None
                                    return

            else:
                if player.x >= 120:
                    player.x -= 10

                if self.enemy.x <= self.enemy.x_true:
                    self.enemy.x += 10
                else:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                        if event.type == pygame.KEYDOWN:
                            if self.arrow:
                                if event.key == pygame.K_RIGHT:
                                    if self.pos_arrow == self.arrow.pos1:
                                        self.pos_arrow = self.arrow.pos2

                                    elif self.pos_arrow == self.arrow.pos2:
                                        self.pos_arrow = self.arrow.pos3

                                elif event.key == pygame.K_LEFT:
                                    if self.pos_arrow == self.arrow.pos2:
                                        self.pos_arrow = self.arrow.pos1

                                    elif self.pos_arrow == self.arrow.pos3:
                                        self.pos_arrow = self.arrow.pos2

                                elif event.key == pygame.K_RETURN:
                                    if self.text2 == self.super_text.battle_command:
                                        if self.pos_arrow == self.arrow.pos1:
                                            cmd = self.process_battle(player, 1)
                                        elif self.pos_arrow == self.arrow.pos2:
                                            cmd = self.process_battle(player, 2)
                                        elif self.pos_arrow == self.arrow.pos3:
                                            self.item()

                                    elif self.text2 == self.super_text.chs_item:
                                        if self.pos_arrow == self.arrow.pos1:
                                            check = self.process_item(player, 1)
                                        elif self.pos_arrow == self.arrow.pos2:
                                            check = self.process_item(player, 2)
                                        elif self.pos_arrow == self.arrow.pos3:
                                            self.process_chapter(player)

                            else:
                                if player.hp <= 0:
                                    self.text2 = f"{player.name} have been defeated"
                                    self.pos_tx2 = (200, 410)

                                elif self.enemy.hp <= 0:
                                    self.text2 = f"{self.enemy.name} have been defeated"
                                    self.pos_tx2 = (180, 410)

                                elif self.text2 in self.super_text.battle_box:
                                    if cmd:
                                        if cmd == "atk":
                                            self.enemy.hp -= self.atk
                                            self.weapon = None
                                            self.effect.position1 = 320
                                            self.effect.position2 = 250
                                            self.text2 = f"{self.enemy.name} lost {self.atk} HP!"
                                            self.pos_tx2 = (250, 410)

                                        elif cmd == "magic":
                                            self.enemy.hp -= self.atk * 2
                                            player.mp -= 1
                                            self.weapon = None
                                            self.effect.position1 = 320
                                            self.effect.position2 = 250
                                            self.text2 = f"{self.enemy.name} lost {self.atk * 2} HP!"
                                            self.pos_tx2 = (250, 410)
                                    else:
                                        self.process_chapter(player)

                                elif self.text2 in self.super_text.atk_box:
                                    enemy_cmd = self.process_enemy()

                                elif self.text2 in self.super_text.item_box:
                                    if check:
                                        self.healing = None
                                        self.effect.position2 = 250
                                        enemy_cmd = self.process_enemy()
                                    else:
                                        self.process_chapter(player)

                                elif self.text2 in self.super_text.chavis_atk:
                                    if enemy_cmd == "atk":
                                        self.text2 = f"{player.name} lost {self.enemy_atk} hp!"
                                        self.enemy_weapon = None
                                        self.enemy_effect.position1 = 480
                                        self.enemy_effect.position2 = 40
                                        self.pos_tx2 = (260, 410)
                                        player.hp -= self.enemy_atk
                                    elif enemy_cmd == "magic":
                                        self.text2 = f"{player.name} lost {self.enemy_atk * 2} hp!"
                                        self.enemy_weapon = None
                                        self.enemy_effect.position1 = 480
                                        self.enemy_effect.position2 = 40
                                        self.pos_tx2 = (260, 410)
                                        player.hp -= self.enemy_atk * 2
                                        self.enemy.mp -= 1
                                else:
                                    self.enemy_healing = None
                                    self.enemy_effect.y_heal = 80
                                    self.process_chapter(player)

            if self.arrow:
                if time.time() % 1 < 0.4:
                    main.screen.blit(self.arrow.arrow, self.pos_arrow)


            pygame.display.flip()

    def process_chapter(self, player):
        self.text = f"What {player.name} do?"

        self.pos_tx = (80, 375)
        self.text2 = self.super_text.battle_command
        self.pos_tx2 = (100, 430)
        self.arrow = Arrow((55, 427), (290, 427), (520, 427))
        self.pos_arrow = self.arrow.pos1

    def item(self):
        self.text = "Choose your items"
        self.pos_tx = (60, 375)
        self.text2 = self.super_text.chs_item
        self.pos_tx2 = (70, 430)
        self.arrow = Arrow((35, 427), (300, 427), (580, 427))
        self.pos_arrow = self.arrow.pos1

    def process_item(self, player, item):
        check = False
        if item == 1:
            if player.potion == 0:
                self.text2 = "You don't have item...."
                self.pos_tx2 = (250, 410)
                self.text, self.pos_tx, self.arrow = None, None, None

            elif player.hp == player.max_hp:
                self.text2 = "You have full HP!!"
                self.pos_tx2 = (250, 410)
                self.text, self.pos_tx, self.arrow = None, None, None

            else:
                self.text2 = f"{player.name} restored HP!"
                self.healing = self.effect.heal
                self.pos_tx2 = (250, 410)
                restore = 0
                while player.hp < player.max_hp:
                    player.hp += 1
                    restore += 1
                    if restore == 3:
                        break
                player.potion -= 1
                self.text, self.pos_tx, self.arrow = None, None, None
                check = True

        elif item == 2:
            if player.mana_potion == 0:
                self.text2 = "You don't have item...."
                self.pos_tx2 = (250, 410)
                self.text, self.pos_tx, self.arrow = None, None, None

            elif player.mp == player.max_mp:
                self.text2 = "You have full MP!!"
                self.pos_tx2 = (250, 410)
                self.text, self.pos_tx, self.arrow = None, None, None

            else:
                self.text2 = f"{player.name} restored MP!"
                self.healing = self.effect.mp
                self.pos_tx2 = (250, 410)
                restore = 0
                while player.mp < player.max_mp:
                    player.mp += 1
                    restore += 1
                    if restore == 3:
                        break
                player.mana_potion -= 1
                self.text, self.pos_tx, self.arrow = None, None, None
                check = True
        return check

    def process_battle(self, player, command):
        if command == 1:
            self.text2 = f"{player.name} use slash !!!"
            self.weapon = self.effect.sword
            self.pos_tx2 = (250, 410)
            self.text, self.pos_tx, self.arrow = None, None, None
            return "atk"

        elif command == 2:
            if player.mp == 0:
                self.text2 = "You don't have mana...."
                self.pos_tx2 = (250, 410)
                self.text, self.pos_tx, self.arrow = None, None, None
                return
            self.text2 = f"{player.name} use magic !!!"
            self.weapon = self.effect.magic
            self.pos_tx2 = (250, 410)
            self.text, self.pos_tx, self.arrow = None, None, None
            return "magic"

    def process_enemy(self):
        ran_list = [1, 2]
        ran_list2 = [1, 2, 3]
        ran = random.choice(ran_list)
        ran2 = random.choice(ran_list2)
        if self.enemy.mp == 0:
            ran = 1

        if ran == 2 and ran2 == 3:
            if self.enemy.hp == self.enemy.max_hp:
                self.text2 = f"{self.enemy.name} use healing but full HP..."
                x = self.set_x_po(len(self.text2))
                self.pos_tx2 = (x, 410)

            else:
                self.text2 = f"{self.enemy.name} use healing!!!"
                self.enemy_healing = self.enemy_effect.heal
                self.pos_tx2 = (230, 410)
                restore = 0
                while self.enemy.hp < self.enemy.max_hp:
                    self.enemy.hp += 1
                    restore += 1
                    if restore == 2:
                        break
                self.enemy.mp -= 1

            self.text, self.pos_tx, self.arrow = None, None, None
        elif ran == 1:
            self.text2 = f"{self.enemy.name} use {self.enemy.enemy_atk_name}!!!"
            self.enemy_weapon = self.enemy_effect.enemy_atk
            x = self.set_x_po(len(self.text2))
            self.pos_tx2 = (x, 410)
            return "atk"

        elif ran == 2:
            self.text2 = f"{self.enemy.name} use {self.enemy.enemy_magic_name}!!!"
            self.enemy_weapon = self.enemy_effect.enemy_magic
            x = self.set_x_po(len(self.text2))
            self.pos_tx2 = (x, 410)
            return "magic"

    def hp_bar(self, player, main):
        if player.hp < 0:
            player.hp = 0

        if self.enemy.hp < 0:
            self.enemy.hp = 0

        main.press_tx(f"{player.name}", (490, 230))
        main.press_tx(f"HP: {player.hp}   MP : {player.mp}", (520, 280))
        main.press_tx(f"{self.enemy.name}", (80, 65))
        main.press_tx(f"HP: {self.enemy.hp}", (130, 110))

    @staticmethod
    def set_x_po(text):
        if 20 <= text <= 25:
            x = 220
        elif 26 <= text <= 30:
            x = 200
        elif 31 <= text <= 33:
            x = 170
        else:
            x = 140
        return x
