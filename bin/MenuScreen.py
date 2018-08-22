import os
import dat
import inputReader
import experience
import os
import time

#   Christian Tavares | DosQuest | 7/12/2018
#
#   This file holds all of the game's menu screens. Some of the above libraries are unused

def restScreen():
    os.system('cls')  #Clean up terminal
    print('\n\n\n\n\n\n\n')
    print '\n\n'
    print '    You are fully Rested!'
    print '    Your HP and MP have been replenished!!!'
    print '\n\n\n\n\n'
    print '\n\n'

def inventoryMenu():
    os.system('cls')
    print('\n\n'
          '    These are your current items...\n'
          '\n\n\n\n\n')
    print '    Weapon:  ', dat.equipmentWeapon, '\n'
    print '    Armor:   ', dat.equipmentArmor, '\n'
    print '    Shield:  ', dat.equipmentShield, '\n'
    print '\n'
    print '    Health Potion(s): ', dat.equipmentPotionCount, '          Mana Potion(s): ', dat.equipmentManaPotionCount
    print '\n'
    print '    A: Exit, C: Return to Character Information'
    print '\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'

def townMenu():
    os.system('cls')
    print('\n\n'
          '    Welcome to RPGTown!\n'
          '\n\n\n\n\n\n\n\n'
          '        F: Enter the Field\n'
          '        S: Go to Shop\n'
          '        C: Character Info\n'
          '        R: Rest\n'
          '\n\n\n\n\n\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

def characterMenu():
    os.system('cls')

    attack = dat.characterSTR + dat.equipmentWeaponATT  #Fetch character stats
    armor = dat.characterDEF + dat.equipmentArmorDEF + dat.equipmentShieldDEF
    nextLV = experience.getNext()

    print '\n\n  Name: ', dat.characterName, '\n'
    print('\n\n\n')
    print '  HP: ', dat.characterCurrentHP, '/', dat.characterHP, '                           MP: ', dat.characterCurrentMP, '/', dat.characterMP
    print('\n')
    print '  Strength: ', dat.characterSTR, '                            Attack: ', attack
    print
    print '  Defense: ', dat.characterDEF, '                              Armor: ', armor
    print
    print '  Dexterity: ', dat.characterDEX, '                           Magic: ', dat.characterMAG
    print
    print '  Experience: ', dat.characterXP, '                           Next Level: ', nextLV
    print('\n')
    print '  A: Exit this screen, Q: View stat descriptions, I: Inventory\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'

def shopMenu():
    os.system('cls')
    print('\n'
          '    Welcome to my Shop!\n'
          '\n\n'
          '    1.) Dagger       3  ATT,    40G\n'
          '    2.) Shortsword   11 ATT,    100G\n'
          '    3.) Longsword    21 ATT,    300G\n'
          '    4.) L.Armor      4  DEF,    100G\n'
          '    5.) Plate Armor  9  DEF,    400G\n'
          '    6.) Shield       2  DEF,    75% Block,   50G\n'
          '\n'
          '    7.) Buy Health Potion  10G    8.) Buy Mana Potion  20G\n\n\n'
          '    Type: "x" to buy an item. (1 would buy a Dagger)\n\n'
          '    I: Inventory\n'
          '    A: Leave\n')
    print '    Gold: ', dat.Gold, '\n\n'
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

def fieldMenu():
    os.system('cls')
    next = experience.getNext()  #Fetch required XP to level up
    print('\n  You arrive at the open fields!')
    print '\n\n  Lv: ', dat.characterLV, '        Gold: ', dat.Gold, '        Exp: ', dat.characterXP, '/', next, '\n\n'
    print('\n')
    print('  1.) East Fields    (Low Threat)')
    print('  2.) West Fields    (Moderate Threat)')
    print('  3.) Goblin Camp    (Moderate/High Threat)')
    print('  4.) Old Ruins      (High Threat!)')
    print('  5.) Challenge the Area Boss (LV: 10)')
    print('\n')
    print('  C.) Character Information            I:) Inventory')
    print('\n')
    print('  A: Return to town, Press "x" to explore an area (x = number 1-4)\n\n')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

def battlePrompt():  #Pre-battle screen
    os.system('cls')
    print '\n\n\n\n\n\n\n\n'
    print '    Monsters have appeared!\n\n\n\n\n\n\n'
    os.system('pause')

def gameOver():  #Utility game over screen just in case it is needed
    os.system('cls')
    print '\n\n\n\n\n\n          The game has been ended!\n\n\n\n\n\n'
    os.system('pause')