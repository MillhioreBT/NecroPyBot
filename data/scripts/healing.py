from todo import *

#oo____oo_________________ooo____oo__________________
#oo____oo__ooooo___ooooo___oo________oo_ooo___oooo___
#oo____oo_oo____o_oo___oo__oo____oo__ooo___o_oo__oo__
#oooooooo_ooooooo_oo___oo__oo____oo__oo____o_oo___o__
#oo____oo_oo______oo___oo__oo____oo__oo____o__oooooo_
#oo____oo__ooooo___oooo_o_ooooo_oooo_oo____o_o____oo_
#_____________________________________________ooooo__

def scriptHealing(player, interval):
    if not player:
        return

    Player.lastHppc = player.getHppc()
    Player.lastMppc = player.getMppc()

    healSpell = SpellHotkey.getByName("HealSpell")
    if Player.lastHppc != 0 and Player.lastHppc <= healSpell.getHppc():
        Send_Keystrokes(healSpell.getButton())

    Player.lastHppc = player.getHppc()
    ghp_hotkey = SpellHotkey.getByName("GreatHealthPotion")
    if Player.lastHppc != 0 and Player.lastHppc <= ghp_hotkey.getHppc():
        Send_Keystrokes(ghp_hotkey.getButton())

    gmp_hotkey = SpellHotkey.getByName("GreatManaPotion")
    if Player.lastMppc != 0 and Player.lastMppc <= gmp_hotkey.getMppc():
        Send_Keystrokes(gmp_hotkey.getButton())

    playerName = player.getName()
    if player.isMage():
        manashield_spell = SpellHotkey.getByName("Manashield")
        if player.getMppc() >= manashield_spell.getHppc() and not player.isManashield():
            Send_Keystrokes(manashield_spell.getButton())
    else:
        manashield_spell = SpellHotkey.getByName("Manashield")
        if player.getHppc() <= manashield_spell.getHppc() and not player.isManashield():
            Send_Keystrokes(manashield_spell.getButton())
        elif player.getHppc() > manashield_spell.getHppc() and player.isManashield():
            Send_Keystrokes(manashield_spell.getButton())

    haste_spell = SpellHotkey.getByName("Haste")
    if not player.isInPz() and player.getMppc() >= haste_spell.getMppc() and player.isInFight():
        nextUse = haste_spell.getNextUse()
        if (not player.isHasted() or player.isParalized() or (nextUse != 0 and nextUse <= sec_to_ns(1))):
            haste_spell.use()

    buff_spell = SpellHotkey.getByName("BuffSpell")
    if not player.isInPz() and player.getMppc() >= buff_spell.getMppc() and player.isInFight():
        nextUse = buff_spell.getNextUse()
        if (not player.isPartyBuff() or (nextUse != 0 and nextUse <= sec_to_ns(1))):
            buff_spell.use()

script = Script("Healing", 200, running=True)
script.setDescription("Script que se encarga de las curaciones, buff y damages.")
script.onThink = scriptHealing
script.register(__name__)
