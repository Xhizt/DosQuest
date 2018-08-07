import os
import dat
import battle
import MenuScreen

def battle1a():
    MenuScreen.battlePrompt()
    battle.initialize('Slime', 'null', 'null', 'A Slime emerges!!!', 0, 'regular')

def battle1b():
    MenuScreen.battlePrompt()
    battle.initialize('Slime', 'Slime', 'null', '2 Slimes emerge!!!', 0, 'regular')

def battle1c():
    MenuScreen.battlePrompt()
    battle.initialize('Goblin', 'null', 'null', 'A Goblin emerges!!!', 0, 'regular')

def loot1():
    print '\n\n\n\n\n\n\n          You have obtained a potion!\n\n\n\n\n\n'
    if dat.equipmentPotionCount < 10:
        dat.equipmentPotionCount += 1
    os.system('pause')

def loot2():
    print '\n\n\n\n\n\n\n          You have obtained a couple potions!\n\n\n\n\n\n'
    if dat.equipmentPotionCount < 10:
        dat.equipmentPotionCount += 1
    if dat.equipmentManaPotionCount < 4:
        dat.equipmentManaPotionCount += 1
    os.system('pause')

def battle2a():
    MenuScreen.battlePrompt()
    battle.initialize('Slime', 'Slime', 'null', '2 Slimes emerge!!!', 0, 'regular')

def battle2b():
    MenuScreen.battlePrompt()
    battle.initialize('Insect', 'Slime', 'null', 'An Insect and Slime emerge!!!', 0, 'regular')

def battle2c():
    MenuScreen.battlePrompt()
    battle.initialize('Slime', 'Slime', 'Slime', '3 Slimes emerge!!!', 0, 'regular')

def battle2d():
    MenuScreen.battlePrompt()
    battle.initialize('Insect', 'Insect', 'null', '2 Insects emerge!!!', 0, 'regular')

def loot3():
    print '\n\n\n\n\n\n\n          You have obtained 1 man potion and some gold!!!\n\n\n\n\n\n'
    if dat.equipmentPotionCount < 10:
        dat.equipmentManaPotionCount += 1
    dat.Gold += 25
    os.system('pause')

def battle3a():
    MenuScreen.battlePrompt()
    battle.initialize('Goblin', 'Slime', 'Slime', '2 Slimes and a Slime emerge!!!', 0, 'regular')

def battle3b():
    MenuScreen.battlePrompt()
    battle.initialize('Goblin', 'Goblin', 'null', '2 Slimes and a Slime emerge!!!', 0, 'regular')

def battle3c():
    MenuScreen.battlePrompt()
    battle.initialize('Goblin', 'Slime', 'Insect', 'Enemy party emerges!!!', 0, 'regular')

def battle3d():
    MenuScreen.battlePrompt()
    battle.initialize('Goblin', 'Goblin', 'Insect', 'Enemy party emerges!!!', 0, 'regular')

def loot4():
    print '\n\n\n\n\n\n\n          You have found a Goblin stash!!!\n\n\n\n\n\n'
    dat.Gold += 50
    os.system('pause')

def battle4a():
    MenuScreen.battlePrompt()
    battle.initialize('DeathKnight', 'null', 'null', 'A Death Knight emerges!!!', 0, 'regular')

def battle4b():
    MenuScreen.battlePrompt()
    battle.initialize('DeathKnight', 'Goblin', 'null', 'A Death Knight and Goblin emerge!!!', 0, 'regular')

def battle4c():
    MenuScreen.battlePrompt()
    battle.initialize('DeathKnight', 'DeathKnight', 'null', '2 Death Knights emerge!!!', 0, 'regular')

def loot5():
    print '\n\n\n\n\n\n\n          You have found a Treasure Coffer!!!\n\n\n\n\n\n'
    dat.Gold += 100
    os.system('pause')

def zuuBattle():
    MenuScreen.battlePrompt()
    battle.initialize('Zuu', 'null', 'null', 'A Zuu emerges. It is HUGE!!!', 0, 'boss')