import dat
import os
import music
import random

def getNext():
    next = dat.characterLV * 100
    return next

def showExpGain(enemy1,enemy2,enemy3):
    music.killMusic()
    expGain = checkXP(enemy1)
    expGain += checkXP(enemy2)
    expGain += checkXP(enemy3)
    return expGain

def addExperience(enemy1,enemy2,enemy3):
    music.killMusic()
    expGain = checkXP(enemy1)
    expGain += checkXP(enemy2)
    expGain += checkXP(enemy3)
    dat.characterXP += int(expGain)
    checkPlayerLV()

def addGold(enemy1,enemy2,enemy3):
    goldGain = checkGold(enemy1)
    goldGain += checkGold(enemy2)
    goldGain += checkGold(enemy3)
    dat.Gold += int(goldGain)
    return goldGain

def checkPlayerLV():
    while dat.characterXP >= getNext():
        dat.characterXP -= getNext()
        dat.characterLV += 1
        if dat.characterLV == 2:
            dat.characterHP += 5
            dat.characterMP += 10
            dat.characterSTR += 1
            dat.characterDEX += 1
            dat.characterMAG += 5
        if dat.characterLV == 3:
            dat.characterHP += 7
            dat.characterMP += 10
            dat.characterDEX += 1
            dat.characterMAG += 5
        if dat.characterLV == 4:
            dat.characterHP += 9
            dat.characterMP += 10
            dat.characterSTR += 1
            dat.characterDEX += 1
            dat.characterMAG += 5
        if dat.characterLV == 5:
            dat.characterHP += 11
            dat.characterMP += 10
            dat.characterDEX += 1
            dat.characterMAG += 5
        if dat.characterLV == 6:
            dat.characterHP += 13
            dat.characterSTR += 1
            dat.characterDEX += 1
            dat.characterMAG += 5
        levelUp()

def checkXP(enemy):
    if enemy == 'null':
        return 0
    if enemy == 'Slime':
        return 30
    if enemy == 'Insect':
        return 55
    if enemy == 'Goblin':
        return 90
    if enemy == 'DeathKnight':
        return 150
    if enemy == 'Zuu':
        return 400

def checkGold(enemy):
    if enemy == 'null':
        return 0
    if enemy == 'Slime':
        value = random.randint(4, 8)
        return value
    if enemy == 'Insect':
        value = random.randint(8, 15)
        return value
    if enemy == 'Goblin':
        value = random.randint(22, 33)
        return value
    if enemy == 'DeathKnight':
        value = random.randint(31, 46)
        return value
    if enemy == 'Zuu':
        return 300

def levelUp():
    os.system('cls')
    music.playSE('Sounds/Levelup.wav')
    dat.characterCurrentHP = dat.characterHP
    dat.characterCurrentMP = dat.characterMP
    print ('\n\n\n\n\n\n      You are now Level {}').format(dat.characterLV)
    os.system('pause')
