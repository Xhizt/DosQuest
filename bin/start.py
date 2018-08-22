import menu
import MenuScreen
import pygame

#   Christian Tavares | DosQuest | 7/12/2018
#
#   This file is where everything initializes. It is launched from a .bat file, however.

pygame.mixer.init()       #Launch Pygame
menu.initialize()         #Open a menu screen
MenuScreen.gameOver()     #Will run when the gameOverFlag var == 1