import pygame


class Object:
    def __init__(self, name, hp, mp, atk):
        self.name = name
        self.max_hp = 20
        self.hp = hp
        self.atk = atk
        self.max_mp = 5
        self.mp = mp


class Player(Object):
    def __init__(self, name, hp=20, mp=5, potion=7, mana=7, atk=2):
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
        self.potion = potion
        self.mana_potion = mana
        super().__init__(name, hp, mp, atk)


class Enemy(Object):
    def __init__(self, name, hp=10, mp=5, atk=1):
        self.x_true = 480
        self.x = -30
        self.y = -30

        if name == "Poppy Army":
            self.sprite = pygame.image.load("image/sprite/poppy.png")
            self.sprite = pygame.transform.scale(self.sprite, (195, 207))
            self.enemy_atk_name = "Poppy Heart"
            self.enemy_magic_name = "Chavis Coffee"
            self.bg = pygame.image.load("image/BG/poppy_bg.png")
        elif name == "Lord Chavis":
            self.sprite = pygame.image.load("image/sprite/lord cv.png")
            self.sprite = pygame.transform.scale(self.sprite, (195, 257))
            self.enemy_atk_name = "Harmon Punch"
            self.enemy_magic_name = "Glut Leaves"
            self.bg = pygame.image.load("image/BG/chavis_bg.png")
        elif name == "Chavis&Poppy":
            self.sprite = pygame.image.load("image/sprite/poppyandcv.png")
            self.sprite = pygame.transform.scale(self.sprite, (505, 257))
            self.enemy_atk_name = "Bubble Explode"
            self.enemy_magic_name = "Poppy Headbutt"
            self.bg = pygame.image.load("image/BG/cvpp_bg.png")
            self.x = 340
            self.x_true = 340
        else:
            self.sprite = pygame.image.load("image/sprite/real_gandragon.png")
            self.sprite = pygame.transform.scale(self.sprite, (195, 207))
            self.enemy_atk_name = "Bipolar Roar"
            self.enemy_magic_name = "F Flare"
            self.bg = pygame.image.load("image/BG/dragon_bg.png")
            self.x_true = 500

        self.text = f"{name} appeared"
        super().__init__(name, hp, mp, atk)


class Arrow:
    def __init__(self, pos1, pos2, pos3):
        self.arrow = pygame.image.load("image/sprite/right-arrow.png")
        self.pos1 = pos1
        self.pos2 = pos2
        self.pos3 = pos3


class Effect:
    def __init__(self, pos_x=320, pos_y=250):
        self.sword = pygame.image.load("image/sprite/sword.png")
        self.magic = pygame.image.load("image/sprite/fireball.png")
        self.heal = pygame.image.load("image/sprite/potion_greenheal.png")
        self.mp = pygame.image.load("image/sprite/potion_blueheal.png")
        self.position1 = pos_x
        self.position2 = pos_y


class EnemyEffect:
    def __init__(self, enemy, pos_x=480, pos_y=40):
        self.x_heal = 480
        self.y_heal = 80
        self.heal = pygame.image.load("image/sprite/potion_greenheal.png")
        if enemy.name == "Poppy Army":
            self.enemy_atk = pygame.image.load("image/sprite/poppy_heart.png")
            self.enemy_magic = pygame.image.load("image/sprite/poppy_cgcoffee.png")
        elif enemy.name == "Lord Chavis":
            self.enemy_atk = pygame.image.load("image/sprite/harmon.png")
            self.enemy_magic = pygame.image.load("image/sprite/glut_leaves.png")
        elif enemy.name == "Chavis&Poppy":
            self.enemy_atk = pygame.image.load("image/sprite/charpop_normal_attack.png")
            self.enemy_magic = pygame.image.load("image/sprite/poppy_rotate.png")
            self.x_heal = 490
        else:
            self.enemy_atk = pygame.image.load("image/sprite/gd_normal_attack.png")
            self.enemy_magic = pygame.image.load("image/sprite/fireball_gandragon.png")

        self.heal = pygame.image.load("image/sprite/greenheal.png")
        self.position1 = pos_x
        self.position2 = pos_y
