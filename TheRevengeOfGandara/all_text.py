class Text:
    def __init__(self, player, enemy):
        self.battle_command = " 1 ATTACK             2 SPELL             3 ITEM"

        self.chs_item = f" 1 HP Potion x{player.potion}        2 MP Potion x{player.mana_potion}        3 Back"

        self.item_box = ["You don't have item....", "You have full HP!!", f"{player.name} restored HP!",
                         "You have full MP!!", f"{player.name} restored MP!"]

        self.battle_box = [f"{player.name} use slash !!!", f"{player.name} use magic !!!", "You don't have mana...."]

        self.atk_box = [f"{enemy.name} lost {player.atk} HP!", f"{enemy.name} lost {player.atk * 2} HP!"]

        self.chavis_atk = [f"{enemy.name} use {enemy.enemy_atk_name}!!!", f"{enemy.name} use {enemy.enemy_magic_name}!!!"]

        self.player_defeat = f"{player.name} have been defeated"

        self.enemy_defeat = f"{enemy.name} have been defeated"
