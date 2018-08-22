import math
import random
import battle
import fieldScreens

#   Christian Tavares | DosQuest | 7/12/2018
#
#   This file is exactly what it sounds like. Using a random number gen, it will make a specified event from fieldScreens
#   occur. Each function is for each area in the field, and eventually every zone in the game. Not all above libraries are used.

def zone1Events():
    roll = random.randint(1, 100)
    if roll > 0 and roll < 31:
        fieldScreens.battle1a()
    elif roll > 30 and roll < 56:
        fieldScreens.battle1b()
    elif roll > 55 and roll < 71:
        fieldScreens.battle1c()
    elif roll > 70 and roll < 91:
        fieldScreens.loot1()
    elif roll > 90 and roll < 101:
        fieldScreens.loot2()
    else:
        raw_input(roll)

def zone2Events():
    roll = random.randint(1, 100)
    if roll > 0 and roll < 31:
        fieldScreens.battle2a()
    elif roll > 30 and roll < 51:
        fieldScreens.battle2b()
    elif roll > 50 and roll < 71:
        fieldScreens.battle2c()
    elif roll > 70 and roll < 91:
        fieldScreens.battle2d()
    elif roll > 90 and roll < 101:
        fieldScreens.loot3()
    else:
        raw_input(roll)

def zone3Events():
    roll = random.randint(1, 100)
    if roll > 0 and roll < 21:
        fieldScreens.battle3a()
    elif roll > 20 and roll < 56:
        fieldScreens.battle3b()
    elif roll > 55 and roll < 71:
        fieldScreens.battle3c()
    elif roll > 70 and roll < 91:
        fieldScreens.battle2d()
    elif roll > 90 and roll < 101:
        fieldScreens.loot4()
    else:
        raw_input(roll)

def zone4Events():
    roll = random.randint(1, 100)
    if roll > 0 and roll < 41:
        fieldScreens.battle4a()
    elif roll > 40 and roll < 61:
        fieldScreens.battle4b()
    elif roll > 60 and roll < 91:
        fieldScreens.battle4c()
    elif roll > 90 and roll < 101:
        fieldScreens.loot5()
    else:
        raw_input(roll)

def zone5Events():
    fieldScreens.zuuBattle()