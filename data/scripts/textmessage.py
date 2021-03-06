from todo import *

def scriptMessageUpdate(player, interval):
    if player:
        for message in TextMessage.getMessages():
            sender = message.getSender()
            content = message.getText()
            thing = g_game.getThingLook()
            if thing.getId() > 99 and content[:7] == 'You see':
                #message.content.append("ItemId: %d" % thing.getId())
                #TextMessage.setMessageByIndex(message)
                player.setDefaultMessage("ItemId: %d" % thing.getId(), 100)
                message.remove()
            elif sender and g_game.isSpeakMessages() and g_game.getPlayerByName(sender) and sender != player.getName():
                g_dispatcher.addTask(0, Client.speak, content)
                message.remove()
            else:
                creature = g_game.getCreatureById(thing.getCount())
                if creature and content[:7] == 'You see':
                    message.content.append(str(creature.getPosition()))
                    TextMessage.setMessageByIndex(message)
                    player.setDefaultMessage("Cid: %d" % creature.getId(), 100)
                    message.remove()

script = Script("TextMessageUpdate", 100, locked=True)
script.onThink = TextMessage.updateCache
script.onThink = scriptMessageUpdate
script.register(__name__)
