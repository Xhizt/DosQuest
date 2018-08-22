import pygame
import winsound

#   Christian Tavares | DosQuest | 7/12/2018
#
#   This file handles all sounds and music.

def playTrackLooping(path):  #Play tracks in the background
    winsound.PlaySound(path, winsound.SND_ASYNC | winsound.SND_LOOP)

def playSE(path):  #Play sound effects
    pygame.mixer.Sound(path).play()

def killMusic():  #Stop background tracks
    winsound.PlaySound(None, winsound.SND_PURGE)