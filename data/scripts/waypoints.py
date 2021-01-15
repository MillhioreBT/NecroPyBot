from todo import *

#oo____oo____oo____________________________________oo___________oo___________
#oo____oo____oo__ooooo___o___oo____ooooo___ooooo_______oo_ooo___oo_____oooo__
#oo____oo____oo_oo___oo__o___oo____o___oo_oo___oo__oo__ooo___o_oooo___oo___o_
#_oo__oooo__oo__oo___oo__o___oo___oo___oo_oo___oo__oo__oo____o__oo______oo___
#__oooo__oooo___oo___oo___ooooo___oo___oo_oo___oo__oo__oo____o__oo__o_o___oo_
#___oo____oo_____oooo_o_o____oo_o_ooooo____ooooo__oooo_oo____o___ooo___oooo__
#________________________ooooo__oooo_________________________________________

def WaypointScriptRunning(player, interval):
    if player and Game.getCheckWaypoints() and not Game.IsAttacking and not Game.IsLooting:
        Waypoints.running(player)

def scriptRecWaypoints(player, interval):
    if player and Game.RecWaypoints:
        playerPos = player.getPosition()
        if not Waypoints.lastPositionRec and len(Waypoints.waypoints) > 0:
            Waypoints.lastPositionRec = Waypoints.waypoints[-1]
        if not Waypoints.lastPositionRec or Waypoints.lastPositionRec.getPosition().getDistance(playerPos) >= 10:
            Waypoints.lastPositionRec = Waypoint(playerPos)
            wx.CallAfter(MenuProperties.CaveBotMenu.AddWaypointOrder, Waypoints.lastPositionRec)

script = Script("Waypoints", 100, locked=True, hide=True)
script.onThink = WaypointScriptRunning
script.onThink = scriptRecWaypoints
script.register()

#ooooooo___________oo_____oo__________________oo______oo________________oo__________oo____________
#oo____oo__ooooo___oo__________ooooo__oo_ooo__oo______oo____ooooo___oooooo__ooooo___oo_____ooooo__
#oo____oo_oo___oo_oooo____oo__oo___oo_ooo___o_oo______oo____o___oo_oo___oo_oo___oo_oooo___oo____o_
#oooooo___oo___oo__oo_____oo__oo___oo_oo____o_oo______oo___oo___oo_oo___oo_oo___oo__oo____ooooooo_
#oo_______oo___oo__oo__o__oo__oo___oo_oo____o__oo____oo____oo___oo_oo___oo_oo___oo__oo__o_oo______
#oo________ooooo____ooo__oooo__ooooo__oo____o____oooo____o_ooooo____oooooo__oooo_o___ooo___ooooo__
#________________________________________________________oooo_____________________________________

def scriptPotionUpdate(player, interval):
    defaultMsg = Player.getDefaultMessage()
    if defaultMsg:
        pots = {
            'hp': "cargas de Health",
            'mp': "cargas de Mana",
            'shp': "cargas de Strong Health",
            'smp': "cargas de Strong Mana",
            'ghp': "cargas de Great Health",
            'gmp': "cargas de Great Mana"
        }
        for p in pots:
            if pots[p] in defaultMsg:
                count = int(luaString_match(defaultMsg, "(%d+) cargas")) or 0
                if count != Player.Potions[p]:
                    Player.Potions[p] = count
                break

script = Script("PotionUpdate", 100, locked=True)
script.onThink = scriptPotionUpdate
script.register()

def scriptBuyPotions(player, interval):
    if player:
        if Game.IsBuyPots:
            success = True
            for pot in ('hp','mp','shp','smp','ghp','gmp'):
                if Player.Potions[pot] != 0 and Player.Potions[pot] < 3000:
                    print(pot)
                    success = False
                    if not player.isInFight():
                        player.say("!cargar %s, 3000" % pot)
                        time.sleep(0.01)
                        defaultMsg = Player.getDefaultMessage()
                        if "Has comprado" in defaultMsg:
                            newCharges = int(luaString_match(defaultMsg, "Ahora tienes (%d+)")) or 0
                            Client.speak("Has comprado %d cargas, ahora tienes %d potas." % (newCharges - Player.Potions[pot], newCharges))
                            Player.Potions[pot] = newCharges
                            success = True
                            break
                        elif "No tienes" in defaultMsg:
                            Client.speak("No tienes suficiente dinero.")
                            break
            if success:
                Game.IsBuyPots = False
        else:
            for pot in ('hp','mp','shp','smp','ghp','gmp'):
                if Player.Potions[pot] != 0 and Player.Potions[pot] < 500:
                    Game.IsBuyPots = True
                    Client.speak("Advertencia: te quedan %d cargas. Iniciando procedimiento de recarga..." % Player.Potions[pot])
                    break

script = Script("BuyPotions", 1000, locked=True)
script.onThink = scriptBuyPotions
script.register()
