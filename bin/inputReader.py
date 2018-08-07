import menu
import os
import dat
import msvcrt
import battle
import eventHandler
import equipment
import music
import MenuScreen

def ReadInput():

    while msvcrt.kbhit():
        msvcrt.getwch()

    dat.PlayerInput = raw_input()

    if dat.characterMenuFlag == 1:
        characterProcessing()
    elif dat.characterMenuFlag == 2:
        inventoryProcessing()
    else:
        processInput()

def processInput():
    if dat.Location == 'town':
        townProcessing()
    elif dat.Location == 'field':
        fieldProcessing()
    elif dat.Location == 'shop':
        shopProcessing()
    else:
        os.system('cls')
        print ("Cant find location")

def characterProcessing():

    while 0 == 0:
        if dat.characterMenuFlag == 1:
            statsProcessing()
        if dat.characterMenuFlag == 2:
            inventoryProcessing()
        if dat.characterMenuFlag == 0:
            break

def statsProcessing():
    while 0 == 0:
        os.system('cls')

        menu.Refresh(0)

        while msvcrt.kbhit():
            msvcrt.getwch()

        dat.PlayerInput = raw_input()

        if dat.PlayerInput.upper() == 'Q':
            os.system('cls')
            print('No description established...')
            os.system('pause')
        elif dat.PlayerInput.upper() == 'A':
            dat.characterMenuFlag = 0
            break
        elif dat.PlayerInput.upper() == 'I':
            dat.characterMenuFlag = 2
            break
        else:
            os.system('cls')
            menu.Refresh(0)

def inventoryProcessing():
    while 0 == 0:
        os.system('cls')

        menu.Refresh(4)

        while msvcrt.kbhit():
            msvcrt.getwch()

        dat.PlayerInput = raw_input()

        if dat.PlayerInput.upper() == 'A':
            dat.characterMenuFlag = 0
            break
        elif dat.PlayerInput.upper() == 'C':
            dat.characterMenuFlag = 1
            break
        else:
            os.system('cls')
            menu.Refresh(4)

def shopProcessing():
    while msvcrt.kbhit():
        msvcrt.getwch()

    dat.PlayerInput = raw_input()

    if dat.PlayerInput.upper() == '1':
        if dat.Gold > 39:
            dat.Gold -= 40
            equipment.changeWep('dagger')
        menu.Refresh(2)
    elif dat.PlayerInput.upper() == '7':
        if dat.Gold > 9 and dat.equipmentPotionCount < 10:
            music.playSE('Sounds/Equip.wav')
            dat.Gold -= 10
            dat.equipmentPotionCount += 1
    elif dat.PlayerInput.upper() == '8':
        if dat.Gold > 19 and dat.equipmentManaPotionCount < 3:
            music.playSE('Sounds/Equip.wav')
            dat.Gold -= 20
            dat.equipmentManaPotionCount += 1
    elif dat.PlayerInput.upper() == 'GOLD':
        os.system('cls')
        dat.Gold += 100
        menu.Refresh(2)
    elif dat.PlayerInput.upper() == '2':
        if dat.Gold > 99:
            dat.Gold -= 100
            equipment.changeWep('shortsword')
        menu.Refresh(2)
    elif dat.PlayerInput.upper() == '3':
        if dat.Gold > 299:
            dat.Gold -= 300
            equipment.changeWep('longsword')
        menu.Refresh(2)
    elif dat.PlayerInput.upper() == '4':
        if dat.Gold > 99:
            dat.Gold -= 100
            equipment.changeArmor('leatherarmor')
        menu.Refresh(2)
    elif dat.PlayerInput.upper() == '5':
        if dat.Gold > 399:
            dat.Gold -= 400
            equipment.changeArmor('platearmor')
        menu.Refresh(2)
    elif dat.PlayerInput.upper() == '6':
        if dat.Gold > 49:
            dat.Gold -= 50
            equipment.changeShield('shield')
        menu.Refresh(2)
    elif dat.PlayerInput.upper() == 'A':
        dat.sceneTransition = 1
        menu.Refresh(1)
    elif dat.PlayerInput.upper() == 'I':
        menu.Refresh(4)
        dat.characterMenuFlag = 2
        characterProcessing()
        menu.Refresh(2)
    else:
        menu.Refresh(2)

def townProcessing():
    while msvcrt.kbhit():
        msvcrt.getwch()

    dat.PlayerInput = raw_input()

    if dat.PlayerInput.upper() == 'C':
        menu.Refresh(0)
        dat.characterMenuFlag = 1
        characterProcessing()
        menu.Refresh(1)
    elif dat.PlayerInput.upper() == 'R':
        MenuScreen.restScreen()
        dat.characterCurrentHP = dat.characterHP
        dat.characterCurrentMP = dat.characterMP
        os.system('pause')
        menu.Refresh(1)
    elif dat.PlayerInput.upper() == 'EXIT':
        dat.gameOverFlag = 1
    elif dat.PlayerInput.upper() == 'B':
        battle.initialize('Slime', 'Goblin', 'DeathKnight', '2 Slimes emerge!!!', 0, 'regular')
        #dat.sceneTransition = 1
        menu.Refresh(1)
    elif dat.PlayerInput.upper() == 'S':
        dat.sceneTransition = 1
        menu.Refresh(2)
    elif dat.PlayerInput.upper() == 'F':
        dat.sceneTransition = 1
        menu.Refresh(3)
    else:
        menu.Refresh(1)

def fieldProcessing():
    while msvcrt.kbhit():
        msvcrt.getwch()

    dat.PlayerInput = raw_input()

    if dat.PlayerInput.upper() == '1':
        os.system('cls')
        eventHandler.zone1Events()
        menu.Refresh(3)
    elif dat.PlayerInput.upper() == '2':
        os.system('cls')
        eventHandler.zone2Events()
        menu.Refresh(3)
    elif dat.PlayerInput.upper() == '3':
        os.system('cls')
        eventHandler.zone3Events()
        menu.Refresh(3)
    elif dat.PlayerInput.upper() == '4':
        os.system('cls')
        eventHandler.zone4Events()
        menu.Refresh(3)
    elif dat.PlayerInput.upper() == '5':
        os.system('cls')
        eventHandler.zone5Events()
        menu.Refresh(3)
    elif dat.PlayerInput.upper() == 'A':
        dat.sceneTransition = 1
        menu.Refresh(1)
    elif dat.PlayerInput.upper() == 'C':
        menu.Refresh(0)
        dat.characterMenuFlag = 1
        characterProcessing()
        menu.Refresh(3)
    elif dat.PlayerInput.upper() == 'I':
        menu.Refresh(4)
        dat.characterMenuFlag = 2
        characterProcessing()
        menu.Refresh(3)
    else:menu.Refresh(3)

def getMenuCode():
    if dat.Location == 'town':
        return 1
    if dat.Location == 'shop':
        return 2
    if dat.Location == 'field':
        return 3

