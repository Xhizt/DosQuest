import time
import os
import dat
import battle
import music
import msvcrt
import math
import experience

#   Christian Tavares | DosQuest | 7/12/2018
#
#   This file handles all skills to add into the game. It makes things more universal, and even monsters should
#   Be able to use the same skills in the future. Some of the above libraries are unused.

def spinSlash():                                      #Only one skill is in the game currently
    #switches.hitAllEnemies = 1
    music.playSE('Sounds/Skill1.wav')
    os.system('cls' if os.name == 'nt' else 'clear')
    battle.variables.battleMessage = 'Player uses Spinslash!'
    battle.battleWindowRefresh(battle.variables.battleMessage)
    time.sleep(1)

    if battle.variables.enemy1arr[1] > 0:  #First enemy
        result = math.ceil((battle.variables.player[3] - battle.variables.enemy1arr[4]) * 0.9)
        battle.variables.enemy1arr[1] -= int(result)
        os.system('cls' if os.name == 'nt' else 'clear')
        battle.variables.battleMessage = '{} took {} damage!'.format(battle.variables.enemy1Type, int(result))
        battle.battleWindowRefresh(battle.variables.battleMessage)
        music.playSE('Sounds/Damage2.wav')
        time.sleep(0.5)

    if battle.variables.enemy2arr[1] > 0:  #Second enemy
        result = math.ceil((battle.variables.player[3] - battle.variables.enemy2arr[4]) * 0.9)
        battle.variables.enemy2arr[1] -= int(result)
        os.system('cls' if os.name == 'nt' else 'clear')
        battle.variables.battleMessage = '{} took {} damage!'.format(battle.variables.enemy2Type, int(result))
        battle.battleWindowRefresh(battle.variables.battleMessage)
        music.playSE('Sounds/Damage2.wav')
        time.sleep(0.5)

    if battle.variables.enemy3arr[1] > 0:  #Third enemy
        result = math.ceil((battle.variables.player[3] - battle.variables.enemy3arr[4]) * 0.9)
        battle.variables.enemy3arr[1] -= int(result)
        os.system('cls' if os.name == 'nt' else 'clear')
        battle.variables.battleMessage = '{} took {} damage!'.format(battle.variables.enemy3Type, int(result))
        battle.battleWindowRefresh(battle.variables.battleMessage)
        music.playSE('Sounds/Damage2.wav')
        time.sleep(0.5)