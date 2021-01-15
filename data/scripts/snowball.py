from todo import *

#_ooooo_____________________________oo______________ooo___ooo___
#oo___oo_oo_ooo___ooooo__oo_______o_oooooo___ooooo___oo____oo___
#_oo_____ooo___o_oo___oo_oo__oo___o_oo___oo_oo___oo__oo____oo___
#___oo___oo____o_oo___oo_oo__oo___o_oo___oo_oo___oo__oo____oo___
#oo___oo_oo____o_oo___oo__oo_oo__o__oo___oo_oo___oo__oo____oo___
#_ooooo__oo____o__ooooo____oo__oo___oooooo___oooo_o_ooooo_ooooo_
#_______________________________________________________________

snowball_players = None

def isPlayerInList(p):
	for sp in snowball_players:
		if sp.getId() == p.getId():
			return True
	return False

cacheScript = Script("Snowball Cache", 200, running=False)
def scriptSnowballCache(player, interval):
	players = Game.getPlayers(True, Filter=lambda p: p.getId() != Player.CachePlayerID)
	if players:
		global snowball_players
		if not snowball_players:
			snowball_players = players
			print("Se ha actualizado la lista de snowball_players con %d players." % len(snowball_players))
			return
		for p in players:
			if not isPlayerInList(p):
				snowball_players.append(p)
				print("Player %s añadido a la lista de snowball_players" % p.getName())
cacheScript.onThink = scriptSnowballCache
cacheScript.register()

def scriptSnowball(player, interval):
    if not player or not snowball_players:
        return
    playerDir = player.getDirection()
    playerPos = Player.Position()
    local_players = list(snowball_players)
    local_players.sort(key=lambda p: p.getPosition().getDistance(Player.Position()) == 4, reverse=True)
    for p in local_players:
        p_pos = p.getPosition()
        if playerPos.getDistance(p_pos) != 4:
            break
        if not player.isVisible():
            continue
        if p_pos.x == playerPos.x and p_pos.y < playerPos.y: # Shoot ^^
            if playerDir != DIRECTION_NORTH:
                keyboard.press_and_release("Control + Up")
                time.sleep(0.050)
            keyboard.press_and_release("F1")
        elif p_pos.y == playerPos.y and p_pos.x > playerPos.x: # Shoot >>
            if playerDir != DIRECTION_EAST:
                keyboard.press_and_release("Control + Right")
                time.sleep(0.050)
            keyboard.press_and_release("F1")
        elif p_pos.x == playerPos.x and p_pos.y > playerPos.y: # Shoot vv
            if playerDir != DIRECTION_SOUTH:
                keyboard.press_and_release("Control + Down")
                time.sleep(0.050)
            keyboard.press_and_release("F1")
        elif p_pos.y == playerPos.y and p_pos.x < playerPos.x: # Shoot <<
            if playerDir != DIRECTION_WEST:
                keyboard.press_and_release("Control + Left")
                time.sleep(0.050)
            keyboard.press_and_release("F1")

script = Script("Snowball", 100, running=False)
script.onThink = scriptSnowball
script.register()
