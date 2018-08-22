import dat
import music

#   Christian Tavares | DosQuest | 7/12/2018
#
#   This file is filled with functions specifically for changing your equipment

def changeWep(weapon):  #Change player's Weapon
    music.playSE('Sounds/Equip.wav')
    if weapon == 'dagger':
        dat.equipmentWeapon = 'Dagger'
        dat.equipmentWeaponATT = 3  #Alters weapon attack stat based off of the sent 'weapon' string
    if weapon == 'shortsword':
        dat.equipmentWeapon = 'Shortsword'
        dat.equipmentWeaponATT = 11
    if weapon == 'longsword':
        dat.equipmentWeapon = 'Longsword'
        dat.equipmentWeaponATT = 21

def changeArmor(armor):  #Change player's Armor
    music.playSE('Sounds/Equip.wav')
    if armor == 'leatherarmor':
        dat.equipmentArmor = 'Leather Armor'
        dat.equipmentArmorDEF = 4  #Alters armor defense stat based off of the sent 'armor' string
    if armor == 'platearmor':
        dat.equipmentArmor = 'Plate Armor'
        dat.equipmentArmorDEF = 9

def changeShield(shield):  #Change player's Shield
    music.playSE('Sounds/Equip.wav')
    if shield == 'shield':
        dat.equipmentShield = 'Shield'
        dat.equipmentArmorBlock = 0.25  #.25 means 25%. This gives the player an additional 25% damage reduction while blocking
        dat.equipmentShieldDEF = 2      #The shield's defense stat