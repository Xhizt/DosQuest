import menu
import os
import dat
import msvcrt
import battle
import eventHandler
import equipment
import music
import MenuScreen

#   Christian Tavares | DosQuest | 7/12/2018
#
#   This file is used to read the input of the player, then process that input depending on which menu they are on.
#   There are a series of 'if' trees for each menu, as well as a function to pull a numerical value depending on a string.
#   Not all above libraries are used.

def ReadInput():

    while msvcrt.kbhit():  #Prevents the terminal from receiving and processing data before the screen fully paints.
        msvcrt.getwch()    #This is very important for the 'sleep' function to time windows.

    dat.PlayerInput = raw_input()  #player's text input
    processInput()

def processInput():  #Sends you to a processing function depending on player's location
    if dat.Location == 'town':
        townProcessing()
    elif dat.Location == 'field':
        fieldProcessing()
    elif dat.Location == 'shop':
        shopProcessing()
    else:
        os.system('cls')
        print ("Cant find location")  #in the unlikely event that the 'location' variable isn't written properly

def characterProcessing():  #This handles both inventory and stats processing with the use of the characterMenuFlag var

    while 0 == 0:
        if dat.characterMenuFlag == 1:
            statsProcessing()
        if dat.characterMenuFlag == 2:
            inventoryProcessing()
        if dat.characterMenuFlag == 0:  #end
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
            print('No description established...')  #No menu yet, shows descriptions for statistics
            os.system('pause')
        elif dat.PlayerInput.upper() == 'A':  #Exit
            dat.characterMenuFlag = 0
            break
        elif dat.PlayerInput.upper() == 'I':  #Inventory
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

        if dat.PlayerInput.upper() == 'A':  #Exit
            dat.characterMenuFlag = 0
            break
        elif dat.PlayerInput.upper() == 'C':  #Character
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
            equipment.changeWep('dagger')  #This string depicts what gets equipped on purchase. See 'equipment.py'
        menu.Refresh(2)
    elif dat.PlayerInput.upper() == '7':
        if dat.Gold > 9 and dat.equipmentPotionCount < 10:  #Max HP potions = 10
            music.playSE('Sounds/Equip.wav')
            dat.Gold -= 10
            dat.equipmentPotionCount += 1
    elif dat.PlayerInput.upper() == '8':
        if dat.Gold > 19 and dat.equipmentManaPotionCount < 3:  #Max MP potions = 3
            music.playSE('Sounds/Equip.wav')
            dat.Gold -= 20
            dat.equipmentManaPotionCount += 1
    elif dat.PlayerInput.upper() == 'GOLD':  #hidden command to get gold
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
    elif dat.PlayerInput.upper() == 'A':  #Exit
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
    elif dat.PlayerInput.upper() == 'R':  #rest
        MenuScreen.restScreen()
        dat.characterCurrentHP = dat.characterHP
        dat.characterCurrentMP = dat.characterMP
        os.system('pause')
        menu.Refresh(1)
    elif dat.PlayerInput.upper() == 'EXIT':  #Close game
        dat.gameOverFlag = 1

    #The below commented out lines of code were used to test the battle system from town

    #elif dat.PlayerInput.upper() == 'B':
        #battle.initialize('Slime', 'Goblin', 'DeathKnight', '2 Slimes emerge!!!', 0, 'regular')
        #dat.sceneTransition = 1
        #menu.Refresh(1)

    elif dat.PlayerInput.upper() == 'S':  #Shop
        dat.sceneTransition = 1
        menu.Refresh(2)
    elif dat.PlayerInput.upper() == 'F':  #Field
        dat.sceneTransition = 1
        menu.Refresh(3)
    else:
        menu.Refresh(1)

def fieldProcessing():
    while msvcrt.kbhit():
        msvcrt.getwch()

    dat.PlayerInput = raw_input()

    if dat.PlayerInput.upper() == '1':  #Zone 1: East Fields
        os.system('cls')
        eventHandler.zone1Events()
        menu.Refresh(3)
    elif dat.PlayerInput.upper() == '2':  #Zone 2: West Fields
        os.system('cls')
        eventHandler.zone2Events()
        menu.Refresh(3)
    elif dat.PlayerInput.upper() == '3':  #Zone 3: Goblin Camp
        os.system('cls')
        eventHandler.zone3Events()
        menu.Refresh(3)
    elif dat.PlayerInput.upper() == '4':  #Zone 4: Old Ruins
        os.system('cls')
        eventHandler.zone4Events()
        menu.Refresh(3)
    elif dat.PlayerInput.upper() == '5':  #Zone 5: Area Boss
        os.system('cls')
        eventHandler.zone5Events()
        menu.Refresh(3)
    elif dat.PlayerInput.upper() == 'A':  #Exit
        dat.sceneTransition = 1
        menu.Refresh(1)
    elif dat.PlayerInput.upper() == 'C':  #Character
        menu.Refresh(0)
        dat.characterMenuFlag = 1
        characterProcessing()
        menu.Refresh(3)
    elif dat.PlayerInput.upper() == 'I':  #Inventory
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

