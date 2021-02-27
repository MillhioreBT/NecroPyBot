from todo import *

#___oooo____________________________________________
#_oo____oo__ooooo__oo_ooo_____ooooo___oooo___ooooo__
#oo________oo___oo_ooo___o____o___oo_oo___o_oo____o_
#oo________oo___oo_oo________oo___oo___oo___ooooooo_
#_oo____oo_oo___oo_oo________oo___oo_o___oo_oo______
#___oooo____ooooo__oo______o_ooooo____oooo___ooooo__
#__________________________oooo_____________________

def wait_for_open_corpse(position):
    tries = 3
    while not g_game.isExistContainerOpened():
        Send_RightClick(position.x, position.y)
        time.sleep(1)
        tries -= 1
        if not tries:
            return False
    return True

def wait_for_looted(player):
    start = time.time_ns()
    while g_game.isExistContainerOpened() and player.lootItems():
        if (time.time_ns() - start) > GAME_AUTOLOOT_WAITING:
            return False
    return True

def wait_for_close_containers():
    start = time.time_ns()
    while g_game.isExistContainerOpened():
        g_game.closeContainer()
        time.sleep(0.001)
        if (time.time_ns() - start) > GAME_AUTOLOOT_WAITING:
            return False
    return True

def scriptCacheLastCreatures(player, interval):
    if g_game.getAutoLootStatus():
        remove_targets = []
        for index, target in enumerate(g_game.cache_targets):
            if target.getHppc() <= 0:
                remove_targets.append(index)
                can_add_corpse = True
                for corpse in g_game.cache_corpses:
                    if corpse.getPosition() == target.getPosition():
                        can_add_corpse = False
                        break
                if can_add_corpse:
                    g_game.cache_corpses.append(Corpse(target))
        for index in sorted(remove_targets, key=lambda n: -n):
            del g_game.cache_targets[index]

def scriptCacheCorpses(player, interval):
    if g_game.getAutoLootStatus():
        current_corpse = None
        remove_corpses = []
        for index, corpse in enumerate(g_game.cache_corpses):
            if not corpse.isValid():
                remove_corpses.append(index)
            elif not corpse.isWait():
                current_corpse = corpse
                g_game.looting = True
                break
        if remove_corpses:
            for index in sorted(remove_corpses, key=lambda n: -n):
                del g_game.cache_corpses[index]
        free_capacity = player.getCapacity()
        if current_corpse and free_capacity > 50000:
            corpse_pos = current_corpse.getPosition()
            corpse_dist = Player.Position().getDistance(corpse_pos)
            if corpse_dist <= 5:
                if wait_for_close_containers():
                    if wait_for_open_corpse(corpse_pos.getPositionOnWindow()):
                        wait_for_looted(player)
                    wait_for_close_containers()
                    current_corpse.setLooted()
            else:
                current_corpse.wait()
        elif not current_corpse:
            g_game.looting = False
            if free_capacity <= 50000:
                Menus.CaveBot.autolootStatus.SetValue(False)

script = Script("AutoLoot", 200, locked=True)
script.onThink = scriptCacheCorpses
script.onThink = scriptCacheLastCreatures
script.register(__name__)
