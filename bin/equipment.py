import dat
import music

def getArmor(armorID):
    if armorID == 0:
        dat.equipmentArmorDEF = 0
    if armorID == 1:
        dat.equipmentArmorDEF = 3
    if armorID == 2:
        dat.equipmentArmorDEF = 8

def changeWep(weapon):
    music.playSE('Sounds/Equip.wav')
    if weapon == 'dagger':
        dat.equipmentWeapon = 'Dagger'
        dat.equipmentWeaponATT = 3
    if weapon == 'shortsword':
        dat.equipmentWeapon = 'Shortsword'
        dat.equipmentWeaponATT = 11
    if weapon == 'longsword':
        dat.equipmentWeapon = 'Longsword'
        dat.equipmentWeaponATT = 21

def changeArmor(armor):
    music.playSE('Sounds/Equip.wav')
    if armor == 'leatherarmor':
        dat.equipmentArmor = 'Leather Armor'
        dat.equipmentArmorDEF = 4
    if armor == 'platearmor':
        dat.equipmentArmor = 'Plate Armor'
        dat.equipmentArmorDEF = 9

def changeShield(shield):
    music.playSE('Sounds/Equip.wav')
    if shield == 'shield':
        dat.equipmentShield = 'Shield'
        dat.equipmentArmorBlock = 0.25
        dat.equipmentShieldDEF = 2