from todo import *

#oooooooo__________________________________oo_____oo__________________
#___oo_____ooooo__oo_ooo___oooo____ooooo___oo_________oo_ooo___oooo___
#___oo____oo___oo_ooo___o_oo__oo__oo____o_oooo____oo__ooo___o_oo__oo__
#___oo____oo___oo_oo______oo___o__ooooooo__oo_____oo__oo____o_oo___o__
#___oo____oo___oo_oo_______oooooo_oo_______oo__o__oo__oo____o__oooooo_
#___oo_____oooo_o_oo______o____oo__ooooo____ooo__oooo_oo____o_o____oo_
#__________________________ooooo_______________________________ooooo__

def get_valid_targets(around=[7, 5]):
    targets, counts = [], defaultdict(int)
    monsters = None
    for m_type in g_targeting.get():
        if m_type.action != 'Attack':
            continue
        if monsters is None:
            monsters = g_game.getMonsters(True, around)
            if not monsters:
                return targets, counts
        m_type_name = m_type.name
        for monster in monsters:
            monster_name = monster.getName()
            if monster_name == m_type_name:
                counts[monster_name] += 1
                targets.append(monster.setType(m_type))
    return targets, counts

def scriptModTargeting(player, interval):
    if player and not player.isInPz():
        if Menus.Targeting.CheckBoxRunTarget.IsChecked():
            target = player.getTargetSquare()
            if not target or not target.isPlayer() and target.getId():
                range_distance = int(Menus.Targeting.range_distance.GetValue())
                targets, counts = get_valid_targets([range_distance, range_distance])
                if targets:
                    targets.sort(key=lambda m: (m.getType().priority, m.getDistanceToPlayer(), -m.getHppc()))
                    target = targets[0]
                    m_type = target.getType()
                    if TargetMonster.check_count[m_type.count](counts[m_type.name]):
                        if player.isWalking():
                            Send_Keystrokes("{ESC}")
                        player.setTarget(target)
                        g_game.attacking = True
                        return True
                    elif target.getDistance(player) == 1:
                        player.setTarget(target)
                    #Send_LeftClick(1345, 190)
    g_game.attacking = False
    return False

#_ooooo____________________ooo___ooo__________
#oo___oo____ooooo___ooooo___oo____oo____oooo__
#_oo________o___oo_oo____o__oo____oo___oo___o_
#___oo_____oo___oo_ooooooo__oo____oo_____oo___
#oo___oo___oo___oo_oo_______oo____oo___o___oo_
#_ooooo__o_ooooo____ooooo__ooooo_ooooo__oooo__
#________oooo_________________________________

def scriptUseSpells(player, interval):
    if player and not player.isInPz():
        range_distance = int(Menus.Targeting.range_distance.GetValue())
        monsters, counts = get_valid_targets([range_distance, range_distance])
        if monsters:
            monsters.sort(key=lambda m: counts[m.getType().name], reverse=True)
            m_type = monsters[0].getType()
            if counts[m_type.name] > 1:
                return Send_Keystrokes(m_type.pluralSpell)
            target = player.getTargetSquare()
            if target:
                target_name = target.getName()
                for monster in monsters:
                    if target_name == m_type.name:
                        return Send_Keystrokes(m_type.singleSpell)

script = Script("Targeting", 100, running=True)
script.onThink = scriptUseSpells
script.onThink = scriptModTargeting
script.register(__name__)
