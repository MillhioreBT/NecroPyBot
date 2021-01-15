from todo import *

#___oooo____________________________________________
#_oo____oo__ooooo__oo_ooo_____ooooo___oooo___ooooo__
#oo________oo___oo_ooo___o____o___oo_oo___o_oo____o_
#oo________oo___oo_oo________oo___oo___oo___ooooooo_
#_oo____oo_oo___oo_oo________oo___oo_o___oo_oo______
#___oooo____ooooo__oo______o_ooooo____oooo___ooooo__
#__________________________oooo_____________________

def scriptCacheLastCreatures(player, interval):
    cacheLastCreatures = Game.getCacheLastCreatures()
    if cacheLastCreatures:
        for monster in cacheLastCreatures:
            if monster.getHppc() <= 0:
                Game.addCacheCorpses(Corpse(monster))

def scriptCacheCorpses(player, interval):
    if not MenuProperties.CaveBotMenu.autolootStatus.IsChecked():
        return
    if Game.LastCorpse:
        if Game.LastCorpse.isExpire():
            Game.LastCorpse = None
        elif not Game.IsAttacking:
            if player.getCapacity() <= 50000:
                if Game.LastCorpse:
                    Game.LastCorpse.setLooted()
                Game.LastCorpse = None
                Game.IsLooting = False
                MenuProperties.CaveBotMenu.autolootStatus.SetValue(False)
                Client.speak("Tienes muy poca capacidad, el sistema de auto saqueo se ha desabilitado.")
                return
            playerPos = Player.Position()
            corpsePos = Game.LastCorpse.getPosition()
            corpseDistance = playerPos.getDistance(corpsePos)
            if corpseDistance <= 6:
                start = time.time_ns()
                while Game.isExistContainerOpened():
                    Game.closeContainer()
                    if (time.time_ns() - start) > GAME_AUTOLOOT_WAITING:
                        break
                toPos = corpsePos.getPositionOnWindow()
                Client.rightClick(toPos.x, toPos.y)
                time.sleep(1)
                start = time.time_ns()
                while Player.lootItems():
                    if (time.time_ns() - start) > GAME_AUTOLOOT_WAITING:
                        break
                start = time.time_ns()
                while Game.isExistContainerOpened():
                    Game.closeContainer()
                    if (time.time_ns() - start) > GAME_AUTOLOOT_WAITING:
                        break
                if Game.LastCorpse:
                    Game.LastCorpse.setLooted()
            Game.LastCorpse = None
            return
    cacheCorpses = Game.getCacheCorpses()
    if cacheCorpses:
        for corpse in cacheCorpses:
            if corpse.isValid():
                Game.LastCorpse = corpse
                Game.IsLooting = True
                return
    Game.IsLooting = False

script = Script("AutoLoot", 200, locked=True)
script.onThink = scriptCacheCorpses
script.onThink = scriptCacheLastCreatures
script.register()
