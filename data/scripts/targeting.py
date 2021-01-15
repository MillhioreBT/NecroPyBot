from todo import *

#oooooooo__________________________________oo_____oo__________________
#___oo_____ooooo__oo_ooo___oooo____ooooo___oo_________oo_ooo___oooo___
#___oo____oo___oo_ooo___o_oo__oo__oo____o_oooo____oo__ooo___o_oo__oo__
#___oo____oo___oo_oo______oo___o__ooooooo__oo_____oo__oo____o_oo___o__
#___oo____oo___oo_oo_______oooooo_oo_______oo__o__oo__oo____o__oooooo_
#___oo_____oooo_o_oo______o____oo__ooooo____ooo__oooo_oo____o_o____oo_
#__________________________ooooo_______________________________ooooo__

def getMonsterOnGroups():
    """Obtener un diccionario con listas de cada tipo de monstruo"""
    monsters = Game.getMonsters(True)
    groups = {}
    for monster in monsters:
        targetMonsters = Targeting.getMonsters()
        for mType in targetMonsters:
            targetName = mType.getName()
            sorteable = False
            if monster.getName() == targetName:
                if not targetName in groups:
                    groups[targetName] = []
                groups[targetName].append(monster)
                sorteable = True
            if sorteable:
                groups[targetName].sort(key=lambda m: (m.getPosition().getDistance(Player.Position()), abs(m.getHppc()-100)))
    return groups

def scriptModTargeting(player, interval):
    if not MenuProperties.TargetingFrame.CheckBoxRunTarget.IsChecked():
        return
    """La variable global de la clase Game, "Game.IsAttacking" solamente puede ser modificada en este script para mantener la coherencia"""
    if not player or player.isInPz():
        Game.IsAttacking = False
        return False
    target = player.getTargetSquare()
    if target and target.isPlayer():
        Game.IsAttacking = False
        return False
    groups = getMonsterOnGroups()
    if groups:
        for targetName in groups:
            monsters = groups[targetName]
            monster = monsters[0]
            targetMonster = Targeting.getMonsterByName(targetName)
            if targetMonster.getAction() != "Attack":
                continue
            checkCount = TargetMonster.transformCount[targetMonster.getCount()]
            if checkCount(len(monsters)):
                player.setTarget(monster)
                Game.IsAttacking = True
                return True
            if monster.getDistance(player) == 1:
                player.setTarget(monster)
    Game.IsAttacking = False
    return False

script = Script("Mod Targeting", 250, locked=True)
script.onThink = scriptModTargeting
script.register()

#_ooooo____________________ooo___ooo__________
#oo___oo____ooooo___ooooo___oo____oo____oooo__
#_oo________o___oo_oo____o__oo____oo___oo___o_
#___oo_____oo___oo_ooooooo__oo____oo_____oo___
#oo___oo___oo___oo_oo_______oo____oo___o___oo_
#_ooooo__o_ooooo____ooooo__ooooo_ooooo__oooo__
#________oooo_________________________________

def isTarget(monster):
    """Esta funcion devuelve el TargetMonster si encuentra uno para el monster dado"""
    targetMonsters = Targeting.getMonsters()
    targetMonsters.sort(key=lambda mType: mType.getPriority())
    for mType in targetMonsters:
        if mType.getName() == monster.getName():
            return mType
    return False

def scriptUseSpells(player, interval):
    if not player or player.isInPz():
        return
    monsters = Game.getMonsters(True, [1, 1])
    for monster in monsters:
        mType = isTarget(monster)
        if mType:
            pluralSpellKey = mType.getPluralSpell()
            if len(pluralSpellKey) > 2:
                return Client.sendKeys(pluralSpellKey)
    target = player.getTargetSquare()
    if target:
        mType = isTarget(target)
        if mType:
            singleSpellKey = mType.getSingleSpell()
            if len(singleSpellKey) > 2:
                return Client.sendKeys(singleSpellKey)

script = Script("TargetingSpells", 100, running=True)
script.onThink = scriptUseSpells
script.register()
