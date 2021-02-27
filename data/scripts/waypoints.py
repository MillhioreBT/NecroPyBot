from todo import *

#oo____oo____oo____________________________________oo___________oo___________
#oo____oo____oo__ooooo___o___oo____ooooo___ooooo_______oo_ooo___oo_____oooo__
#oo____oo____oo_oo___oo__o___oo____o___oo_oo___oo__oo__ooo___o_oooo___oo___o_
#_oo__oooo__oo__oo___oo__o___oo___oo___oo_oo___oo__oo__oo____o__oo______oo___
#__oooo__oooo___oo___oo___ooooo___oo___oo_oo___oo__oo__oo____o__oo__o_o___oo_
#___oo____oo_____oooo_o_o____oo_o_ooooo____ooooo__oooo_oo____o___ooo___oooo__
#________________________ooooo__oooo_________________________________________

def WaypointScriptRunning(player, interval):
    button_cave_bot_colour = Menus.Main.cave_bot.GetForegroundColour()
    if player and g_game.getCheckWaypoints():
        if not g_game.stop_walking and not g_game.buy_pots:
            if not g_game.attacking and not g_game.looting:
                g_waypoints.run(player)
                if button_cave_bot_colour != wx.BLACK:
                    Menus.Main.cave_bot.SetForegroundColour(wx.BLACK)
                return
    if button_cave_bot_colour == wx.BLACK:
        Menus.Main.cave_bot.SetForegroundColour(Menus.ScriptLockedColour)

def scriptRecWaypoints(player, interval):
    if player and g_waypoints.record:
        player_pos = player.getPosition()
        if not g_waypoints.lastRecord and g_waypoints.count() > 0:
            g_waypoints.lastRecord = g_waypoints.get(-1)
        if not g_waypoints.lastRecord or g_waypoints.lastRecord.getPosition().getDistance(player_pos) >= 10:
            g_waypoints.lastRecord = Waypoint(player_pos)
            wx.CallAfter(Menus.CaveBot.AddWaypointOrder, g_waypoints.lastRecord)

script = Script("Waypoints", 100, locked=True)
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
    if player:
        defaultMsg = player.getDefaultMessage()
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
                    count = int(lstring.match(defaultMsg, "(%d+) cargas")) or 0
                    if count != Player.Potions[p]:
                        if player.getStorageValue('verify_buy_pots'):
                            if Player.lastPotions[p] < count:
                                g_dispatcher.addTask(0, Client.speak, "Recarga exitosa.")
                            else:
                                g_dispatcher.addTask(0, Client.speak, "Intentare recargar nuevamente.")
                                g_game.buy_pots = True
                            player.setStorageValue('verify_buy_pots', False)
                        Player.lastPotions[p] = Player.Potions[p]
                        Player.Potions[p] = count
                    break

script = Script("PotionUpdate", 100, locked=True)
script.onThink = scriptPotionUpdate
script.register()

def scriptBuyPotions(player, interval):
    if player:
        if g_game.buy_pots:
            success = True
            for pot in ('hp','mp','shp','smp','ghp','gmp'):
                charges = Player.Potions[pot]
                if charges != 0 and charges < 3000:
                    success = False
                    if not player.isInFight():
                        player.say("!cargar %s, 3000" % pot)
                        time.sleep(0.2)
                        defaultMsg = player.getDefaultMessage()
                        if "Has comprado" in defaultMsg:
                            new_charges = int(lstring.match(defaultMsg, "Ahora tienes (%d+)")) or 0
                            buy_charges = new_charges - charges
                            print("You have bought %d charges, now you have %d potions." % (buy_charges, new_charges))
                            g_dispatcher.addTask(0, Client.speak, "Has comprado %d cargas, ahora tienes %d potas." % (buy_charges, new_charges))
                            Player.Potions[pot] = new_charges
                            success = True
                            break
                        elif "No tienes" in defaultMsg:
                            print("You don't have enough money.")
                            g_dispatcher.addTask(0, Client.speak, "No tienes suficiente dinero.")
                            break
                        else:
                            print("The command to buy potions was executed, but the purchase could not be verified.")
                            g_dispatcher.addTask(0, Client.speak, "No se pudo verificar la recarga de las potas, intentare verificar una ves mas.")
                            player.setStorageValue('verify_buy_pots', True)
                            success = True
            if success:
                g_game.buy_pots = False
        elif not player.getStorageValue('verify_buy_pots'):
            for pot in ('hp','mp','shp','smp','ghp','gmp'):
                charges = Player.Potions[pot]
                if charges != 0 and charges < 500:
                    g_game.buy_pots = True
                    print("You have %d %s charges left. Waiting to buy." % (charges, pot))
                    g_dispatcher.addTask(0, Client.speak, "Te quedan %d potas. Esperando para comprar." % charges)
                    break

script = Script("BuyPotions", 1000, locked=True)
script.onThink = scriptBuyPotions
script.register()
