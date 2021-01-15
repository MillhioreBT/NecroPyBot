from todo import *

#oo______________________________ooo___oo______oo___________ooo____oo__________oo_____oo____oooo_________
#oo_______ooooo__oo____o__ooooo___oo___oo______oo____ooooo__oooo___oo__ooooo___oo__________oo_____o___oo_
#oo______oo____o_oo____o_oo____o__oo___oo______oo____o___oo_oo_oo__oo_oo___oo_oooo____oo__ooooo___o___oo_
#oo______ooooooo_oo___o__ooooooo__oo___oo______oo___oo___oo_oo__oo_oo_oo___oo__oo_____oo__oo______o___oo_
#oo______oo_______oo_o___oo_______oo____oo____oo____oo___oo_oo___oooo_oo___oo__oo__o__oo__oo_______ooooo_
#ooooooo__ooooo____oo_____ooooo__ooooo____oooo____o_ooooo___oo____ooo__ooooo____ooo__oooo_oo_____o____oo_
#_________________________________________________oooo____________________________________________ooooo__

def scriptLevelUpNotification(player, interval):
    if player and Game.isShowNotifications():
        currentlevel = player.getLevel()
        afterLevel = player.getStorageValue("afterLevel")
        if afterLevel and afterLevel < currentlevel:
            toaster.show_toast("Level Up!",
                   "You advanced from Level %s to Level %s." % (afterLevel, currentlevel),
                   icon_path="necroxia.ico",
                   duration=4)
        player.setStorageValue("afterLevel", currentlevel)

#oo____oo____oo__________________________oo__________________ooooooo__ooo___________________________________
#oo____oo____oo__ooooo__oo_ooo__oo_ooo_______oo_ooo___oooo___oo____oo__oo____ooooo___o___oo__ooooo__oo_ooo__
#oo____oo____oo_oo___oo_ooo___o_ooo___o__oo__ooo___o_oo__oo__oo____oo__oo___oo___oo__o___oo_oo____o_ooo___o_
#_oo__oooo__oo__oo___oo_oo______oo____o__oo__oo____o_oo___o__oooooo____oo___oo___oo__o___oo_ooooooo_oo______
#__oooo__oooo___oo___oo_oo______oo____o__oo__oo____o__oooooo_oo________oo___oo___oo___ooooo_oo______oo______
#___oo____oo_____oooo_o_oo______oo____o_oooo_oo____o_o____oo_oo_______ooooo__oooo_o_o____oo__ooooo__oo______
#_____________________________________________________ooooo__________________________ooooo__________________

def scriptWarningPlayerOnScreen(player, interval):
    if player and Game.isWarningPlayerOnScreen() and not player.isInPz():
        players = Game.getPlayers(True)
        if len(players) >= 2:
            found_no_friends = []
            for p in players:
                if p != player and not p.isFriend():
                    found_no_friends.append(p.getName())
            if found_no_friends:
                warning_message = "Advertencia: hay %d jugador%s a la vista: %s%s"
                player_names = ""
                for index, name in enumerate(found_no_friends):
                    player_names += name
                    if index >= 2:
                        break
                    else:
                        player_names += ', '
                players_in_sight = len(found_no_friends)
                Client.speak(warning_message % (players_in_sight, (players_in_sight > 1 and 'es' or ''), player_names, (players_in_sight > 3 and ' y otros.' or '.')))

def scriptCancelCaveBotAndTeleportTemple(player, interval):
    if player and Game.isTeleportToTemple() and not player.isInPz():
        if not player.isInFight():
            if player.getStorageValue("teleporToTemple"):
                player.say("!tp temple")
                defaultMsg = Player.getDefaultMessage()
                foundCancel = [x for x in ('Tu', 'puedes') if x in defaultMsg]
                if foundCancel:
                    player.setStorageValue("teleporToTemple", None)
                    player.setStorageValue("logout", True)
                    Client.speak("Tu no puedes usar el hechizo de teleportacion!")
                    return
            elif player.getStorageValue("logout"):
                player.setStorageValue("logout", None)
                # logout
                return
        enemies = Game.getEnemies()
        watching_me = player.getStorageValue("watchingme") or 0
        if enemies:
            for enemy in enemies:
                enemyKey = "foundenemy[%s]" % enemy.getName()
                lastFound = player.getStorageValue(enemyKey)
                if not lastFound:
                    lastFound = time.time()
                    player.setStorageValue(enemyKey, lastFound)
                else:
                    seconds = time.time() - lastFound
                    if seconds >= 10:
                        player.setStorageValue(enemyKey, time.time())
                        watching_me += 1
                        player.setStorageValue("watchingme", watching_me)
        watching_me_last = player.getStorageValue("watchingmelast") or 0
        if (watching_me - watching_me_last) > 10:
            player.setStorageValue("watchingmelast", watching_me)
            Client.speak("Advertencia: creo que te estan observando.")
            player.setStorageValue("teleporToTemple", True)

def scriptShowFps(player, interval):
    if MenuProperties.ExtrasFrame.showFps.IsChecked():
        if not Client.getShowFps():
            Client.setShowFps(True)
    elif Client.getShowFps():
        Client.setShowFps(False)

def scriptOneshootWarning(player, interval):
    if player:
        if player.isMage():
            dmgs = player.getDmgs(True)
            if dmgs >= 30:
                Client.speak("Peligro: te estan bajando de %d%% la mana!" % dmgs)
        else:
            dmgs = player.getDmgs(False)
            if dmgs >= 40:
                Client.speak("Peligro: te estan bajando de %d%% la salud!" % dmgs)


script = Script("Miscellaneous", 1000, locked=True)
script.onThink = scriptWarningPlayerOnScreen
script.onThink = scriptLevelUpNotification
script.onThink = scriptCancelCaveBotAndTeleportTemple
script.onThink = scriptShowFps
script.onThink = scriptOneshootWarning
script.register()

#oo_______oo__________oo_______oo____oo____oo_________________oo_____
#oo____________oooo___oo_ooo___oo____oo____oo__ooooo___ooooo__oo___o_
#oo_______oo__oo__oo__ooo___o_oooo___oo____oo_oo___oo_oo___oo_oo__o__
#oo_______oo__oo___o__oo____o__oo____oooooooo_oo___oo_oo______oooo___
#oo_______oo___oooooo_oo____o__oo__o_oo____oo_oo___oo_oo______oo__o__
#ooooooo_oooo_o____oo_oo____o___ooo__oo____oo__oooo_o__ooooo__oo___o_
#______________ooooo_________________________________________________

def scriptLightHack():
    player = Game.getPlayerClient()
    if not player:
        return
    lightHackState = player.getStorageValue("lightHack")
    if not lightHackState:
        player.setStorageValue("lightHack", True)
        player.setStorageValue("lightHackInfo", player.getLight())
        player.setLight(100, 20)
        return
    player.setStorageValue("lightHack", False)
    lightInfo = player.getStorageValue("lightHackInfo")
    player.setLight(lightInfo['colour'], lightInfo['amount'])

keyboard.add_hotkey('ctrl+f11', scriptLightHack)

#_ooooo__oo_________________________ooooooo__________________
#oo___oo_oo_ooo___ooooo__oo_______o_oo_________ooooo___oooo__
#_oo_____ooo___o_oo___oo_oo__oo___o_oooo_______o___oo_oo___o_
#___oo___oo____o_oo___oo_oo__oo___o_oo________oo___oo___oo___
#oo___oo_oo____o_oo___oo__oo_oo__o__oo________oo___oo_o___oo_
#_ooooo__oo____o__ooooo____oo__oo___oo______o_ooooo____oooo__
#___________________________________________oooo_____________

keyboard.add_hotkey('alt+f8', lambda: wx.CallAfter(MenuProperties.ExtrasFrame.showFps.SetValue, not MenuProperties.ExtrasFrame.showFps.IsChecked()))

#_ooooo__oo_________________________ooo_____ooo_________________________
#oo___oo_oo_ooo___ooooo__oo_______o_oooo___oooo__ooooo__oo_ooo__oo____o_
#_oo_____ooo___o_oo___oo_oo__oo___o_oo_oo_oo_oo_oo____o_ooo___o_oo____o_
#___oo___oo____o_oo___oo_oo__oo___o_oo__ooo__oo_ooooooo_oo____o_oo____o_
#oo___oo_oo____o_oo___oo__oo_oo__o__oo_______oo_oo______oo____o_ooo___o_
#_ooooo__oo____o__ooooo____oo__oo___oo_______oo__ooooo__oo____o_oo_ooo__
#_______________________________________________________________________

keyboard.add_hotkey('ctrl+f12', lambda: wx.CallAfter(MenuProperties.MainMenu.OnToggle))
