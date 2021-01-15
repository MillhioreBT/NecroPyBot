from todo import *

#ooooooo__________________ooooooo__________________oo____oo_________________________
#oo______o____o____ooooo__oo____oo__ooooo__oo_ooo__oo____oo__ooooo__oo____o_oo_ooo__
#oooo_____oo_o_____o___oo_oo____oo_oo____o_ooo___o_oo____oo_oo___oo_oo____o_ooo___o_
#oo________oo_____oo___oo_oooooo___ooooooo_oo______oooooooo_oo___oo_oo____o_oo______
#oo_______o_oo____oo___oo_oo_______oo______oo______oo____oo_oo___oo_ooo___o_oo______
#ooooooo_o___oo_o_ooooo___oo________ooooo__oo______oo____oo__ooooo__oo_ooo__oo______
#_______________oooo________________________________________________________________

def scriptExpPerHour(player, interval):
    if not player:
        return
    currentExp = player.getExperience()
    Events.Player_onChangeExperience(currentExp, Player.lastExp)
    Player.lastExp = currentExp
    checkExpSpeed(player)
    wx.CallAfter(MenuProperties.MainMenu.UpdatePlayerStatus)

script = Script("Exp/Hour", 1000, hide=True, locked=True)
script.onThink = scriptExpPerHour
script.register()
