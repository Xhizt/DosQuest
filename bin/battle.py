import time
import os
import dat
import music
import msvcrt
import math
import experience
import skill
import random

#   Christian Tavares | DosQuest | 7/12/2018
#
#   This file is specifically designed for handling the battle sequence, and will terminate once the player runs, the
#   enemies have all reached zero HP, or the player reaches zero HP. The program resumes where battle.py was called.

class variables():  #Temporary variables used only in this class

    battleMessage = 'nothing'
    PlayerTurn = 1
    playerDefending = 0
    playerBlock = .5
    run = 0

    target = 1
    target1 = '>>>'
    target2 = '   '
    target3 = '   '

    enemy1Type = 'null'
    enemy2Type = 'null'
    enemy3Type = 'null'

    player = [0]*6 #LV,HP,MP,ATT,DEF,Block
    enemy1arr = [0]*6#LV,HP,MP,ATT,DEF
    enemy2arr = [0]*6#LV,HP,MP,ATT,DEF
    enemy3arr = [0,0,0,0,0]#LV,HP,MP,ATT,DEF

def initialize(enemy1,enemy2,enemy3,Message,preEmptive,battleType):  #initialize variables
    variables.target = 1
    variables.target1 = '>>>'
    variables.target2 = '   '
    variables.target3 = '   '
    variables.run = 0
    variables.PlayerTurn = 1
    variables.playerBlock = 0
    variables.enemy1arr = [0] * 6
    variables.enemy2arr = [0] * 6
    variables.enemy3arr = [0] * 6

    #The lines below were used to play music during the battles. Regular battles had 2 themes that could play.

    #if battleType == 'regular':
        #randomnum = random.randint(1,100)
        #if randomnum < 51:
            #music.playTrackLooping('Sounds/Battle.wav')
        #else:
            #music.playTrackLooping('Sounds/ChaozFantasy.wav')
    #if battleType == 'boss':
        #music.playTrackLooping('Sounds/Boss.wav')

    variables.battleMessage = Message

    if preEmptive == 1:  #Pre-emptive catch, makes it so that enemies attack first
        variables.PlayerTurn = 0

    variables.playerBlock = .5  #50% damage reduction

    variables.player[0] = dat.characterLV
    variables.player[1] = dat.characterCurrentHP
    variables.player[2] = dat.characterCurrentMP
    variables.player[3] = (dat.characterSTR + dat.equipmentWeaponATT)
    variables.player[4] = (dat.characterDEF + dat.equipmentArmorDEF + dat.equipmentShieldDEF)
    variables.player[5] = dat.equipmentArmorBlock

    variables.playerBlock -= dat.equipmentArmorBlock

    variables.enemy1Type = enemy1
    getVariables(enemy1,1)
    variables.enemy2Type = enemy2
    getVariables(enemy2,2)
    variables.enemy3Type = enemy3
    getVariables(enemy3,3)

    os.system('cls')
    battleWindowRefresh(Message)
    idle()

def idle():  #The equivalent of inputReader's ReadInput function. Waits for user input and responds accordingly
    while 0 == 0:

        if variables.enemy1arr[1] <= 0:
            if variables.enemy2arr[1] <= 0:
                if variables.enemy3arr[1] <= 0:
                    break  #A loop break that checks if all enemies have zero hp or less. Victory

        if variables.run == 1:
            break  #Run from fight, end battle

        if variables.PlayerTurn == 0:  # Enemy's turn
            enemyTurn()

        if variables.player[1] < 1:
            break  #A loop break checking if player hp is less than 1. Lose Battle

        targetCheck()  #Sets the player's target. Draws a '>>>" on screen. Decides which foe is hit with single target attacks

        while msvcrt.kbhit():
            msvcrt.getwch()  # Stops console from accepting input until everything is displayed

        UserInput = raw_input("Choose your action!('run' to run away!): ")
        battleProcessing(UserInput)

    if variables.player[1] <= 0:
        loseBattle()  #Lose
    elif variables.run == 1:
        dat.characterCurrentHP = variables.player[1]
        runAway()  #Run
    else:
        dat.characterCurrentHP = variables.player[1]
        dat.characterCurrentMP = variables.player[2]
        goldDropped = experience.addGold(variables.enemy1Type, variables.enemy2Type, variables.enemy3Type)
        exp = experience.showExpGain(variables.enemy1Type, variables.enemy2Type, variables.enemy3Type)
        winBattle(goldDropped, exp)
        experience.addExperience(variables.enemy1Type, variables.enemy2Type, variables.enemy3Type)
    return  #Victory!

def battleProcessing(input):

    if input.upper() == 'K':  #Use the only skill you have! Spinslash
        os.system('cls' if os.name == 'nt' else 'clear')
        battleWindowRefresh(variables.battleMessage)
        variables.PlayerTurn = 0  #Expends the player's turn here
        if variables.player[2] > 4:
            variables.player[2] -= 5
            skill.spinSlash()
        else:  #Catch for if player doesn't have 5 mp
            os.system('cls' if os.name == 'nt' else 'clear')
            variables.battleMessage = 'Not enough MP!'
            battleWindowRefresh(variables.battleMessage)
    elif input.upper() == 'G':  #Mana recovery potion
        os.system('cls' if os.name == 'nt' else 'clear')
        battleWindowRefresh(variables.battleMessage)
        if dat.equipmentManaPotionCount > 0:  #Check for potions
            if variables.player[2] < dat.characterMP:
                variables.player[2] = dat.characterMP
                dat.equipmentManaPotionCount -= 1  #Remove 1 potion
                music.playSE("Sounds/Recovery.wav")
                time.sleep(0.5)  #Adds delay to text display, allowing the player to read the battle messages
                os.system('cls' if os.name == 'nt' else 'clear')
                variables.PlayerTurn = 0
                variables.battleMessage = 'Player uses a Mana Potion!! MP Recovered!!!'
                battleWindowRefresh(variables.battleMessage)
            else:  #Catch if MP is full
                os.system('cls' if os.name == 'nt' else 'clear')
                variables.battleMessage = 'You are at maximum MP!'
                battleWindowRefresh(variables.battleMessage)
    elif input.upper() == 'H':  #Health potion
        os.system('cls' if os.name == 'nt' else 'clear')
        battleWindowRefresh(variables.battleMessage)
        if dat.equipmentPotionCount > 0:  #Check for potions
            recoveredHP = int(dat.characterHP * .40)
            if recoveredHP + variables.player[1] > dat.characterHP:  #If restored hp makes current HP higher than max, reduces current amount.
                recoveredHP = (recoveredHP + variables.player[1]) - dat.characterHP
                variables.player[1] = dat.characterHP
                dat.equipmentPotionCount -= 1
                music.playSE("Sounds/Recovery.wav")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                variables.PlayerTurn = 0
                variables.battleMessage = 'Player uses a Potion! Restored {} HP!!'.format(recoveredHP)
                battleWindowRefresh(variables.battleMessage)
            elif variables.player[1] == dat.characterHP:  #Catch if HP is full
                os.system('cls' if os.name == 'nt' else 'clear')
                variables.battleMessage = 'You are at maximum HP!'
                battleWindowRefresh(variables.battleMessage)
            else:  #Normal usage of HP potion, adds recovered amount
                variables.player[1] += recoveredHP
                dat.equipmentPotionCount -= 1
                music.playSE("Sounds/Recovery.wav")
                time.sleep(0.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                variables.PlayerTurn = 0
                variables.battleMessage = 'Player uses a Potion! Restored {} HP!!'.format(recoveredHP)
                battleWindowRefresh(variables.battleMessage)
        else:  #No potions
            os.system('cls' if os.name == 'nt' else 'clear')
            variables.battleMessage = 'No Potions!'
            battleWindowRefresh(variables.battleMessage)
    elif input.upper() == 'R':  #Run Away!!!
        os.system('cls' if os.name == 'nt' else 'clear')
        runRoll = random.randint(1, 100)
        if runRoll > 60:  #40% chance to run away
            variables.run = 1
            dat.sceneTransition = 1
        else:  #Fail
            os.system('cls' if os.name == 'nt' else 'clear')
            variables.PlayerTurn = 0
            variables.battleMessage = 'Unable to run!'
            battleWindowRefresh(variables.battleMessage)
    elif input.upper() == 'D':  #Defend for 1 turn, reducing incoming damage
        os.system('cls' if os.name == 'nt' else 'clear')
        battleWindowRefresh(variables.battleMessage)
        variables.playerDefending = 1  #Set defending flag to 'yes'
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        variables.PlayerTurn = 0
        variables.battleMessage = 'Player defends!'
        battleWindowRefresh(variables.battleMessage)
    elif input.upper() == 'A':  #Attack selected target
        os.system('cls' if os.name == 'nt' else 'clear')
        battleWindowRefresh(variables.battleMessage)
        music.playSE("Sounds/Damage.wav")
        time.sleep(0.5)

        if variables.target == 1:  #Enemy 1
            result = variables.player[3] - variables.enemy1arr[4]
            variables.enemy1arr[1] -= result  #Damage
            if variables.enemy1arr[1] < 0:  #Catch to make enemy hp = 0 if they are negative
                variables.enemy1arr[1] = 0
        if variables.target == 2:  #Enemy 2
            result = variables.player[3] - variables.enemy2arr[4]
            variables.enemy2arr[1] -= result
            if variables.enemy2arr[1] < 0:
                variables.enemy2arr[1] = 0
        if variables.target == 3:  #Enemy 3
            result = variables.player[3] - variables.enemy3arr[4]
            variables.enemy3arr[1] -= result
            if variables.enemy3arr[1] < 0:
                variables.enemy3arr[1] = 0

        os.system('cls' if os.name == 'nt' else 'clear')
        variables.PlayerTurn = 0
        variables.battleMessage = 'Player attacks!! Enemy took {} damage!'.format(result)
        battleWindowRefresh(variables.battleMessage)
    elif input.upper() == 'S':  #Switch targets
        os.system('cls' if os.name == 'nt' else 'clear')
        battleWindowRefresh(variables.battleMessage)
        variables.target += 1
        if variables.target == 4:  #Reset to 1 if the integer is impossible
            variables.target = 1

        if variables.target == 1 and variables.enemy1arr[1] < 1:  #Check if enemy is alive before drawing an arrow
            variables.target = variables.target + 1
        if variables.target == 2 and variables.enemy2arr[1] < 1:
            variables.target += 1
        if variables.target == 3 and variables.enemy3arr[1] < 1:
            variables.target = 1

        if variables.target == 1:  #Draw which variable has the target arrow
            variables.target1 = '>>>'
            variables.target2 = '   '
            variables.target3 = '   '
        if variables.target == 2:
            variables.target1 = '   '
            variables.target2 = '>>>'
            variables.target3 = '   '
        if variables.target == 3:
            variables.target1 = '   '
            variables.target2 = '   '
            variables.target3 = '>>>'

        os.system('cls' if os.name == 'nt' else 'clear')
        variables.battleMessage = "Switched!!!"
        battleWindowRefresh(variables.battleMessage)
    elif input.upper() == "M":  # Magic
        os.system('cls' if os.name == 'nt' else 'clear')
        battleWindowRefresh(variables.battleMessage)
        if variables.player[2] > 24:  # Test Player's MP. If not 25+, cancels action
            music.playSE("Sounds\Spell.wav")
            time.sleep(0.5)

            if variables.target == 1:
                result = (dat.characterMAG - variables.enemy1arr[4]) * 2
                variables.enemy1arr[1] -= int(result)
            if variables.target == 2:
                result = (dat.characterMAG - variables.enemy2arr[4]) * 2
                variables.enemy2arr[1] -= int(result)
            if variables.target == 3:
                result = (dat.characterMAG - variables.enemy3arr[4]) * 2
                variables.enemy3arr[1] -= int(result)

            variables.player[2] = variables.player[2] - 25  # MP cost
            os.system('cls' if os.name == 'nt' else 'clear')
            variables.PlayerTurn = 0
            variables.battleMessage = 'PLAYER casts a spell! ENEMY took {} damage!'.format(result)
            battleWindowRefresh(variables.battleMessage)
        else:  # Not enough MP catch
            os.system('cls' if os.name == 'nt' else 'clear')
            variables.battleMessage = 'Not enough MP!'
            battleWindowRefresh(variables.battleMessage)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        battleWindowRefresh(variables.battleMessage)

def enemyTurn():  #enemy
    if variables.enemy1arr[1] > 0:  #enemy 1
        if variables.playerDefending == 0:
            time.sleep(1)
            music.playSE("Sounds\Damage.wav")
            damage = variables.enemy1arr[3] - variables.player[4]
            if damage < 0:  #Catch so enemy cannot heal player for having negative rolls
                damage = 0
            else:
                variables.player[1] -= damage
            os.system('cls' if os.name == 'nt' else 'clear')
            variables.battleMessage = '{} attacks! Player takes {} damage!!'.format(variables.enemy1Type,damage)
            battleWindowRefresh(variables.battleMessage)
        else:  #Catch if player is defending
            time.sleep(1)
            music.playSE("Sounds\Defense.wav")
            damage = math.ceil((variables.enemy1arr[3] - variables.player[4]) * variables.playerBlock)
            if damage < 0:
                damage = 0
            else:
                variables.player[1] -= int(damage)
            os.system('cls' if os.name == 'nt' else 'clear')
            variables.battleMessage = '{} attacks! Player takes {} damage!!'.format(variables.enemy1Type, int(damage))
            battleWindowRefresh(variables.battleMessage)
        if variables.player[1] < 1:
            return
    if variables.enemy2arr[1] > 0:  #enemy 2
        if variables.playerDefending == 0:
            time.sleep(1)
            music.playSE("Sounds\Damage.wav")
            damage = variables.enemy2arr[3] - variables.player[4]
            if damage < 0:  #Catch so enemy cannot heal player for having negative rolls
                damage = 0
            else:
                variables.player[1] -= damage
            os.system('cls' if os.name == 'nt' else 'clear')
            variables.battleMessage = '{} attacks! Player takes {} damage!!'.format(variables.enemy2Type,damage)
            battleWindowRefresh(variables.battleMessage)
        else:  #Catch if player is defending
            time.sleep(1)
            music.playSE("Sounds\Defense.wav")
            damage = math.ceil((variables.enemy2arr[3] - variables.player[4]) * variables.playerBlock)
            if damage < 0:
                damage = 0
            else:
                variables.player[1] -= int(damage)
            os.system('cls' if os.name == 'nt' else 'clear')
            variables.battleMessage = '{} attacks! Player takes {} damage!!'.format(variables.enemy2Type, int(damage))
            battleWindowRefresh(variables.battleMessage)
    if variables.enemy3arr[1] > 0:  #enemy 3
        if variables.playerDefending == 0:
            time.sleep(1)
            music.playSE("Sounds\Damage.wav")
            damage = variables.enemy3arr[3] - variables.player[4]
            if damage < 0:  #Catch so enemy cannot heal player for having negative rolls
                damage = 0
            else:
                variables.player[1] -= damage
            os.system('cls' if os.name == 'nt' else 'clear')
            variables.battleMessage = '{} attacks! Player takes {} damage!!'.format(variables.enemy3Type, int(damage))
            battleWindowRefresh(variables.battleMessage)
        else:  #Catch if player is defending
            time.sleep(1)
            music.playSE("Sounds\Defense.wav")
            damage = math.ceil((variables.enemy3arr[3] - variables.player[4]) * variables.playerBlock)
            if damage < 0:
                damage = 0
            else:
                variables.player[1] -= int(damage)
            os.system('cls' if os.name == 'nt' else 'clear')
            variables.battleMessage = '{} attacks! Player takes {} damage!!'.format(variables.enemy3Type, damage)
            battleWindowRefresh(variables.battleMessage)

    time.sleep(1)
    variables.playerDefending = 0  #Remove player defending flag
    variables.PlayerTurn = 1  #Flag up for player turn

def targetCheck():  #Check player targets in case they are targeting a now dead enemy
    if eval('variables.enemy{}arr[{}]'.format(variables.target, 1)) <= 0:
        variables.target += 1

        if variables.target == 2:
            if variables.enemy2arr[0] == 'No Enemy' or variables.enemy2arr[1] < 1:
                variables.target += 1
        if variables.target == 3:
            if variables.enemy3arr[0] == 'No Enemy' or variables.enemy3arr[1] < 1:
                variables.target += 1
        if variables.target == 4:
            variables.target = 1
        if variables.target == 1:
            if variables.enemy1arr[0] == 'No Enemy' or variables.enemy1arr[1] < 1:
                variables.target += 1

        if variables.target == 1:
            variables.target1 = '>>>'
            variables.target2 = '   '
            variables.target3 = '   '
        if variables.target == 2:
            variables.target1 = '   '
            variables.target2 = '>>>'
            variables.target3 = '   '
        if variables.target == 3:
            variables.target1 = '   '
            variables.target2 = '   '
            variables.target3 = '>>>'

        os.system('cls' if os.name == 'nt' else 'clear')
        battleWindowRefresh(variables.battleMessage)

def getVariables(enemy,enemyNumber):  #One function that encapsulates all of your variable loading from dat.py
    if enemyNumber == 1:
        if enemy != 'null':
            variables.enemy1arr[0] = eval('dat.' + variables.enemy1Type + 'LV')
            variables.enemy1arr[1] = eval('dat.' + variables.enemy1Type + 'HP')
            variables.enemy1arr[2] = eval('dat.' + variables.enemy1Type + 'MP')
            variables.enemy1arr[3] = eval('dat.' + variables.enemy1Type + 'ATT')
            variables.enemy1arr[4] = eval('dat.' + variables.enemy1Type + 'DEF')
        else:
            variables.enemy1arr[0] = 'No Enemy'
            variables.enemy1Type == 'empty'
    if enemyNumber == 2:
        if enemy != 'null':
            variables.enemy2arr[0] = eval('dat.' + variables.enemy2Type + 'LV')
            variables.enemy2arr[1] = eval('dat.' + variables.enemy2Type + 'HP')
            variables.enemy2arr[2] = eval('dat.' + variables.enemy2Type + 'MP')
            variables.enemy2arr[3] = eval('dat.' + variables.enemy2Type + 'ATT')
            variables.enemy2arr[4] = eval('dat.' + variables.enemy2Type + 'DEF')
        else:
            variables.enemy2arr[0] = 'No Enemy'
            variables.enemy2Type == 'empty'
    if enemyNumber == 3:
        if enemy != 'null':
            variables.enemy3arr[0] = eval('dat.' + variables.enemy3Type + 'LV')
            variables.enemy3arr[1] = eval('dat.' + variables.enemy3Type + 'HP')
            variables.enemy3arr[2] = eval('dat.' + variables.enemy3Type + 'MP')
            variables.enemy3arr[3] = eval('dat.' + variables.enemy3Type + 'ATT')
            variables.enemy3arr[4] = eval('dat.' + variables.enemy3Type + 'DEF')
        else:
            variables.enemy3arr[0] = 'No Enemy'
            variables.enemy3Type == 'empty'

def battleWindowRefresh(ExtraMessage):    #Used for loading variables
    if variables.enemy1arr[1] < 0:
        variables.enemy1arr[1] = 0
    if variables.enemy2arr[1] < 0:
        variables.enemy2arr[1] = 0
    if variables.enemy3arr[1] < 0:
        variables.enemy3arr[1] = 0

    if variables.enemy1arr[0] != 'No Enemy':
        enemy1String = " {}Enemy1: LV {} {}HP      ATT: {}     DEF: {}".format(variables.target1, variables.enemy1arr[0], variables.enemy1arr[1], variables.enemy1arr[3], variables.enemy1arr[4])
    else:
        enemy1String = "    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    if variables.enemy2arr[0] != 'No Enemy':
        enemy2String = " {}Enemy2: LV {} {}HP      ATT: {}     DEF: {}".format(variables.target2, variables.enemy2arr[0], variables.enemy2arr[1], variables.enemy2arr[3], variables.enemy2arr[4])
    else:
        enemy2String = "    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    if variables.enemy3arr[0] != 'No Enemy':
        enemy3String = " {}Enemy3: LV {} {}HP      ATT: {}     DEF: {}".format(variables.target3, variables.enemy3arr[0], variables.enemy3arr[1], variables.enemy3arr[3], variables.enemy3arr[4])
    else:
        enemy3String = "    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    print
    print
    print
    print
    print enemy1String
    print enemy2String
    print enemy3String
    print
    print
    print
    print
    print "    You: ", variables.player[1], "HP    ", variables.player[2], "MP    ATT: ", variables.player[3], "   MAG: ", dat.characterMAG, "   DEF: ", variables.player[4]
    print
    print "\n    ", ExtraMessage
    print
    print "\n    A: Attack, S: Switch target, M: Cast Magic, D: Defend, K: Skills(5mp)"
    print "    R: Run Away!"
    print "    H: Healing Potion ({}/10)      G: Mana Potion({}/3)\n\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>".format(dat.equipmentPotionCount,dat.equipmentManaPotionCount)
    return

def winBattle(gold, exp):
    music.killMusic()
    dat.sceneTransition = 1
    os.system('cls')
    print ('\n\n\n\n\n\n You Win!\n\n You have obtained {} gold and {} exp!!!\n\n\n\n\n\n\n\n').format(gold,exp)
    os.system('pause')
    return

def loseBattle():
    music.killMusic()
    dat.sceneTransition = 1
    music.playTrackLooping('Sounds/Game-Over-Theme.wav')
    os.system('cls')
    print '\n\n\n\n\n\n You Lose!!!'
    os.system('pause')
    return

def runAway():
    music.killMusic()
    dat.sceneTransition = 1
    os.system('cls')
    print '\n\n\n\n\n\n You Successfully ran away!!!'
    os.system('pause')
    return