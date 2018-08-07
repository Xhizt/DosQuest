import os
import pygame
import inputReader
import MenuScreen
import dat
import music

def initialize():
    pygame.init()
    dat.sceneTransition = 1
    Refresh(1)
    while 0 == 0:
        if dat.gameOverFlag == 1:
            break
        inputReader.processInput()
    return

def Refresh(menuCode):
    if menuCode == 0:
        MenuScreen.characterMenu()
    if menuCode == 1:
        if dat.sceneTransition == 1:
            music.killMusic()
            music.playTrackLooping("Sounds/Chrono-Cross-The-Girl-who-.wav")
            dat.sceneTransition = 0
        dat.Location = 'town'
        MenuScreen.townMenu()
    if menuCode == 2:
        if dat.sceneTransition == 1:
            music.killMusic()
            music.playTrackLooping("Sounds/Final-Fantasy-IV-Within-th.wav")
            dat.sceneTransition = 0
        dat.Location = 'shop'
        MenuScreen.shopMenu()
    if menuCode == 3:
        if dat.sceneTransition == 1:
            music.killMusic()
            music.playTrackLooping("Sounds/DKC2-Mining-Melancholy.wav")
            dat.sceneTransition = 0
        dat.Location = 'field'
        MenuScreen.fieldMenu()
    if menuCode == 4:
        MenuScreen.inventoryMenu()