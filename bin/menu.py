import os
import pygame
import inputReader
import MenuScreen
import dat
import music

#   Christian Tavares | DosQuest | 7/12/2018
#
#   This file is called to refresh the terminal menus during gameplay. The Refresh function has functionality for
#   playing music files you choose in .wav format only.

def initialize():  #Called when the program is first initialized.
    pygame.init()
    dat.sceneTransition = 1 #Var used to indicate if there is an actual location change
    Refresh(1)              #Refresh menu screen with text
    while 0 == 0:
        if dat.gameOverFlag == 1: #Gameover catch in an infinite loop to read terminal input.
                                  #If gameOverFlag = 1, the program will terminate
            break
        inputReader.processInput()
    return

def Refresh(menuCode):
    if menuCode == 0:
        MenuScreen.characterMenu()
    if menuCode == 1:
        if dat.sceneTransition == 1:
            music.killMusic()
            #music.playTrackLooping("Sounds/FILENAME.wav")
            dat.sceneTransition = 0
        dat.Location = 'town'
        MenuScreen.townMenu()
    if menuCode == 2:
        if dat.sceneTransition == 1:
            music.killMusic()
            #music.playTrackLooping("Sounds/FILENAME.wav")
            dat.sceneTransition = 0
        dat.Location = 'shop'
        MenuScreen.shopMenu()
    if menuCode == 3:
        if dat.sceneTransition == 1:
            music.killMusic()
            #music.playTrackLooping("Sounds/FILENAME.wav")
            dat.sceneTransition = 0
        dat.Location = 'field'
        MenuScreen.fieldMenu()
    if menuCode == 4:
        MenuScreen.inventoryMenu()