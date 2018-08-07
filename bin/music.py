import pygame
import winsound

def playTrackLooping(path):
    winsound.PlaySound(path, winsound.SND_ASYNC | winsound.SND_LOOP)

def playSE(path):
    pygame.mixer.Sound(path).play()

def killMusic():
    winsound.PlaySound(None, winsound.SND_PURGE)