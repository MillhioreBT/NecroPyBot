from todo import *

def scriptMessageUpdate(player, interval):
    if player:
        for message in TextMessage.getMessages():
            sender = message.getSender()
            content = message.getText()
            thing = Game.getThingLook()
            if thing.getId() > 99 and content[:7] == 'You see':
                #message.content.append("ItemId: %d" % thing.getId())
                #TextMessage.setMessageByIndex(message)
                Player.setDefaultMessage("ItemId: %d" % thing.getId(), 100)
                message.remove()
            elif sender and sender != player.getName():
                txt = "%s: %s" % (sender, content)
                error(txt)
                #Client.speak(txt)
                message.remove()
            else:
                creature = Game.getCreatureById(thing.getCount())
                if creature and content[:7] == 'You see':
                    message.content.append(str(creature.getPosition()))
                    TextMessage.setMessageByIndex(message)
                    Player.setDefaultMessage("Cid: %d" % creature.getId(), 100)
                    message.remove()

script = Script("TextMessageUpdate", 100, locked=True)
script.onThink = TextMessage.updateCache
script.onThink = scriptMessageUpdate
script.register()
