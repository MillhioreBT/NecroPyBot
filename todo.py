import win32con
import win32com
import json
import win32gui
import win32api
import sys
import time
import traceback
import wx
import threading
import os
import pythoncom
import keyboard
import re
import math
import datetime
import pyscreenshot as ImageGrab
import importlib
import emoji
import signal

OS_WINDOWS = sys.platform == 'win32'
OS_LINUX = not OS_WINDOWS

from queue import Queue
from timeit import default_timer as timer
from random import *
from win32com.client import Dispatch
from ctypes import *
from ctypes.wintypes import *
from ReadWriteMemory import ReadWriteMemory
from pywinauto.application import Application
from win10toast import ToastNotifier
toaster = ToastNotifier()

from py_cron_schedule import CronSchedule, CronFormatError
from sympy import oo as OO
user32 = windll.user32

#ooooo                             ooooo             o8                           o888o                                 
# 888       oooo  oooo   ooooooo    888  oo oooooo o888oo ooooooooo8 oo oooooo  o888oo ooooooo    ooooooo    ooooooooo8 
# 888        888   888   ooooo888   888   888   888 888  888oooooo8   888    888 888   ooooo888 888     888 888oooooo8  
# 888      o 888   888 888    888   888   888   888 888  888          888        888 888    888 888         888         
#o888ooooo88  888o88 8o 88ooo88 8o o888o o888o o888o 888o  88oooo888 o888o      o888o 88ooo88 8o  88ooo888    88oooo888 

import lupa
from lupa import LuaRuntime
lua = LuaRuntime(unpack_returned_tuples=True)
luaString_match = lua.eval("string.match")
luaString_gmatch = lua.eval("string.gmatch")

#ooooooooooo                                                 
# 888    88  oo oooooo oooo  oooo  oo ooo oooo    oooooooo8  
# 888ooo8     888   888 888   888   888 888 888  888ooooooo  
# 888    oo   888   888 888   888   888 888 888          888 
#o888ooo8888 o888o o888o 888o88 8o o888o888o888o 88oooooo88  

ADDRESS_GAMECLIENT_SHOWFPS = 0x6DDFD4
ADDRESS_GAMECLIENT_XOR = 0x53A760
ADDRESS_PLAYERHEALTH = 0x6D8000
ADDRESS_PLAYERMAXHEALTH = 0x6D8048
ADDRESS_PLAYERMANA = 0x53A794
ADDRESS_PLAYERMAXMANA = 0x53A764
ADDRESS_PLAYERLEVEL = 0x53A778
ADDRESS_PLAYERID = 0x6D8050
ADDRESS_PLAYEREXPERINECE = 0x53A768
ADDRESS_PLAYERTARGETID = 0x6D45A8
ADDRESS_PLAYERINPZTILE = 0x733E90
ADDRESS_CLIENTICONS = 0x53A710
ADDRESS_PLAYERPOSX = 0x6D8054
ADDRESS_PLAYERPOSY = 0x6D8058
ADDRESS_PLAYERPOSZ = 0x6D805C
ADDRESS_PLAYERISTARGED = 0x53A790
ADDRESS_PLAYERLASTPING = 0x6D4688
ADDRESS_PLAYERLASTPONG = 0x6D8044
ADDRESS_PLAYERUPDATE_POSZ = 0x6D8008
ADDRESS_PLAYERVOCATION = 0x54B6A4 # Aparentemente no es la direccion correcta (Need fix)
ADDRESS_PLAYERGOTOPOSX = 0x6D804C
ADDRESS_PLAYERGOTOPOSY = 0x6D8044
ADDRESS_PLAYERGOTOPOSZ = 0x6D805C
ADDRESS_BUTTONS_MOVING = 0x53A6C8
ADDRESS_PLAYER_SOUL = 0x53a77c
ADDRESS_PLAYER_MAGICLEVEL = 0x53a780
ADDRESS_PLAYER_DELTASPEED = 0x53a788
ADDRESS_PLAYER_BASESPEED = 0x53a720
ADDRESS_PLAYER_OFFLINETRAINING = 0x53a750
ADDRESS_PLAYER_STAMINA = 0x53a7e0
ADDRESS_PLAYER_FOODTIME = 0x53a75c
ADDRESS_PLAYER_FIST = 0x53a6dc
ADDRESS_PLAYER_CLUB = 0x53a6e0
ADDRESS_PLAYER_SWORD = 0x53a6e4
ADDRESS_PLAYER_AXE = 0x53a6e8
ADDRESS_PLAYER_DISTANCE = 0x53a6ec
ADDRESS_PLAYER_SHIELDING = 0x53a6f0
ADDRESS_PLAYER_FISH = 0x53a6f4
ADDRESS_PLAYER_CAPACITY = 0x6D8040
ADDRESS_PLAYER_MAGICLEVELPERCENT = 0x53a78c
ADDRESS_PLAYER_FISTPERCENT = 0x53a79c
ADDRESS_PLAYER_CLUBPERCENT = 0x53a7a0
ADDRESS_PLAYER_SWORDPERCENT = 0x53a7a4
ADDRESS_PLAYER_AXEPERCENT = 0x53a7a8
ADDRESS_PLAYER_DISTANCEPERCENT = 0x53a7ac
ADDRESS_PLAYER_SHIELDINGPERCENT = 0x53a7b0
ADDRESS_PLAYER_FISHPERCENT = 0x53a7b4
ADDRESS_PLAYER_CRITICALCHANCE = 0x53a6f8
ADDRESS_PLAYER_CRITICALAMOUNT = 0x53a6fc
ADDRESS_PLAYER_LIFELEECHCHANCE = 0x53a700
ADDRESS_PLAYER_LIFELEECHAMOUNT = 0x53a704
ADDRESS_PLAYER_MANALEECHCHANCE = 0x53a708
ADDRESS_PLAYER_MANALEECHAMOUNT = 0x53a70c
ADDRESS_PLAYER_STEPSTOPOINT = 0x53a798
#ADDRESS_PLAYER_TAKETOINVENTORY = 0x53a75c
ADDRESS_PLAYER_CONNECTIONSTATUS = 0x53a7e8
ADDRESS_CLIENT_CURSOR2STATE = 0x54C294
ADDRESS_CLIENT_CURSORSTATE = 0x54C23C
ADDRESS_CLIENT_CURSORLASTPOSX = 0x54C288
ADDRESS_CLIENT_CURSORLASTPOSY = 0x54C2A4
ADDRESS_NEWANYMESSAGE = 0x00531B8C
OFFSET_NEWANYMESSAGE = (0x00)
ADDRESS_INVENTORY_TOGGLE = 0x00778884
ADDRESS_SPACE_CONTAINER = 0x00778884
ADDRESS_SPACE_CONTAINER_OFFSETS = (0x4, 0x30, 0x24, 0xC, 0xC, 0x38, 0x44)
ADDRESS_INVENTORY_OFFSETS = (0x4, 0x24, 0x10, 0xC, 0x38, 0x18)
ADDRESS_CONTAINER_START = 0x0077EB3C
ADDRESS_CONTAINER_POINTER_COUNT = (0x4, 0x0, 0x18, 0xC, 0x4C, 0x4)
ADDRESS_CONTAINER_POINTER_ID = (0x4, 0x0, 0x18, 0xC, 0x4C, 0x8)
ADDRESS_CONTAINER_SLOT_SEPARATOR = 32 # 32 is 0x20
ADDRESS_ID_ONLOOKCLICK = 0x6D4604 # ItemId/CreatureType
ADDRESS_COUNT_ONLOOKCLICK = 0x6D4600 # Count/CreatureId
ADDRESS_NUMBEROFATTACKCLICKS = 0x6D8DC0
ADDRESS_DEFAULT_MESSAGE_INTERVAL = 0x58DE98
ADDRESS_DEFAULT_MESSAGE = 0x58DEA0
ADDRESS_SLOT_START = 0x778A28
ADDRESS_SLOT_COUNT = 0x04
ADDRESS_SLOT_SEPARATOR = 0x20
ADDRESS_MOUSE_CLICKACTION = 0x54C23C
ADDRESS_MOUSE_CLICKACTION_THING = 0x54C24C
ADDRESS_MOUSE_CLICKACTION_COMPLEMENT = 0x54C294
ADDRESS_MOUSE_LASTCLICK_POSX = 0x54C2A4 #0x54C2A4
ADDRESS_MOUSE_LASTCLICK_POSY = 0x54C288 #0x54C288
ADDRESS_MOUSE_THINGFOCUS_POSX = 0x54C250 # TilePosX or isContainer65535
ADDRESS_MOUSE_THINGFOCUS_POSY = 0x54C2A8 # TilePosY or ContainerIndex or SlotInventory
ADDRESS_MOUSE_THINGFOCUS_POSZ = 0x54C280 # TilePosZ or ContainerSlot
ADDRESS_BATTLELIST_MAXINDEX = 1300
ADDRESS_BATTLELIST_CID = 0x732880
ADDRESS_BATTLELIST_NAME = 0x732884
ADDRESS_BATTLELIST_TYPE = 0x732888
ADDRESS_BATTLELIST_POSZ = 0x7328A4
ADDRESS_BATTLELIST_POSY = 0x7328A8
ADDRESS_BATTLELIST_POSX = 0x7328AC
ADDRESS_BATTLELIST_MOVEMENTY = 0x7328B0 # 4294967264 4294967295
ADDRESS_BATTLELIST_MOVEMENTX = 0x7328B4
ADDRESS_BATTLELIST_LIGHTAMOUNT = 0x7328FC
ADDRESS_BATTLELIST_LIGHTCOLOR = 0x732900
ADDRESS_BATTLELIST_HPPC = 0x73290C
ADDRESS_BATTLELIST_ISVI = 0x732924
ADDRESS_BATTLELIST_ISWA = 0x7328D0
ADDRESS_BATTLELIST_SQUARECOLOR = 0x732930
ADDRESS_BATTLELIST_SQUARETOGGLE = 0x732934
ADDRESS_BATTLELIST_PARTY = 0x73291c
ADDRESS_BATTLELIST_SKULL = 0x732918
ADDRESS_BATTLELIST_LOOKTYPE = 0x7328E0
ADDRESS_BATTLELIST_LOOKHEAD = 0x7328E4
ADDRESS_BATTLELIST_LOOKPRIMARY = 0x7328E8
ADDRESS_BATTLELIST_LOOKSECONDARY = 0x7328EC
ADDRESS_BATTLELIST_LOOKDETAIL = 0x7328F0
ADDRESS_BATTLELIST_LOOKADDON = 0x7328F4
ADDRESS_BATTLELIST_LOOKMOUNT = 0x7328F8
ADDRESS_BATTLELIST_DIRECTION = 0x7328B8
ADDRESS_BATTLELIST_LASTDIR = 0x7328D4
ADDRESS_BATTLELIST_GUILDEMBLEM = 0x732920
ADDRESS_BATTLELIST_SUMMONERTYPE = 0x73293C
ADDRESS_BATTLELIST_ICONRAY = 0x732938
ADDRESS_BATTLELIST_SPEED = 0x732910
ADDRESS_BATTLELIST_EXPRESSIONBUBBLE = 0x732940
ADDRESS_BATTLELIST_NEXT = 0xDC
ADDRESS_MESSAGE_LINES = 0x58E0BC
ADDRESS_MESSAGE_SPEAKER = 0x58E0C0
ADDRESS_MESSAGE_SEPLINE = 0x28
ADDRESS_MESSAGE_INDEX = 0x58E0A4
ADDRESS_MESSAGE_INTERVAL = 0x58E0A8
ADDRESS_MESSAGE_TYPE = 0x58E0AC
ADDRESS_MESSAGE_POSX = 0x58E0B0
ADDRESS_MESSAGE_POSY = 0x58E0B4
ADDRESS_MESSAGE_POSZ = 0x58E0B8
ADDRESS_MESSAGE_ACTIVE = 0x58E0A0
ADDRESS_MESSAGE_SEPARATOR = 0x288
ADDRESS_WINDOW_HEIGHT = 0x723E34
ADDRESS_WINDOW_WIDTH = 0x723E44
ADDRESS_CHAT_CONTENT = 0x00778884
ADDRESS_CHAT_CONTENT_OFFSETS = (0x34, 0x10, 0xC, 0x40, 0x40, 0x2C, 0x0)
AUTOID_PLAYERS = 0x10000000
AUTOID_MONSTERS = 0x40000000
AUTOID_NPCS = 0x80000000
CREATURETYPE_PLAYER = 0
CREATURETYPE_MONSTER = 1
CREATURETYPE_NPC = 2
CREATURETYPE_SUMMON_OWN = 3
CREATURETYPE_SUMMON_OTHERS = 4
ACCOUNTADDRESS_IS_CONNECTED = 0x71A8E8
ACCOUNT_STATUS_DISCONNECTED = -1
ACCOUNT_STATUS_CONNECTED = 0
M_PI = 3.14159265358979323846

"""
    1/100 consume alrededor de 20% en un procesador de 3.60GHz
    1/10 consume alrededor de 5% en un procesador de 3.60GHz
"""
THREAD_MIN_TICKS = 1/10

ICON_POISON = 1 << 0
ICON_BURN = 1 << 1
ICON_ENERGY =  1 << 2
ICON_DRUNK = 1 << 3
ICON_MANASHIELD = 1 << 4
ICON_PARALYZE = 1 << 5
ICON_HASTE = 1 << 6
ICON_SWORDS = 1 << 7
ICON_DROWNING = 1 << 8
ICON_FREEZING = 1 << 9
ICON_DAZZLED = 1 << 10
ICON_CURSED = 1 << 11
ICON_PARTY_BUFF = 1 << 12
ICON_REDSWORDS = 1 << 13
ICON_PIGEON = 1 << 14
ICON_BLEEDING = 1 << 15

SHIELD_NONE = 0
SHIELD_WHITEYELLOW = 1
SHIELD_WHITEBLUE = 2
SHIELD_BLUE = 3
SHIELD_YELLOW = 4
SHIELD_BLUE_SHAREDEXP = 5
SHIELD_YELLOW_SHAREDEXP = 6
SHIELD_BLUE_NOSHAREDEXP_BLINK = 7
SHIELD_YELLOW_NOSHAREDEXP_BLINK = 8
SHIELD_BLUE_NOSHAREDEXP = 9
SHIELD_YELLOW_NOSHAREDEXP = 10
SHIELD_GRAY = 11

SKULL_NONE = 0
SKULL_YELLOW = 1
SKULL_GREEN = 2
SKULL_WHITE = 3
SKULL_RED = 4
SKULL_BLACK = 5
SKULL_ORANGE = 6

GUILDEMBLEM_NONE = 0
GUILDEMBLEM_ALLY = 1
GUILDEMBLEM_ENEMY = 2
GUILDEMBLEM_NEUTRAL = 3
GUILDEMBLEM_MEMBER = 4
GUILDEMBLEM_OTHER = 5

SQ_COLOR_BLACK = 0
SQ_COLOR_BLUE = 5
SQ_COLOR_LIGHTGREEN = 30
SQ_COLOR_LIGHTBLUE = 35
SQ_COLOR_MAYABLUE = 95
SQ_COLOR_DARKRED = 108
SQ_COLOR_LIGHTGREY = 129
SQ_COLOR_SKYBLUE = 143
SQ_COLOR_PURPLE = 155
SQ_COLOR_RED = 180
SQ_COLOR_ORANGE = 198
SQ_COLOR_YELLOW = 210
SQ_COLOR_WHITE_EXP = 215
SQ_COLOR_NONE = 255

TEXTCOLOR_BLUE = 5
TEXTCOLOR_LIGHTGREEN = 30
TEXTCOLOR_LIGHTBLUE = 35
TEXTCOLOR_MAYABLUE = 95
TEXTCOLOR_DARKRED = 108
TEXTCOLOR_LIGHTGREY = 129
TEXTCOLOR_SKYBLUE = 143
TEXTCOLOR_PURPLE = 154
TEXTCOLOR_ELECTRICPURPLE = 155
TEXTCOLOR_RED = 180
TEXTCOLOR_PASTELRED = 194
TEXTCOLOR_ORANGE = 198
TEXTCOLOR_YELLOW = 210
TEXTCOLOR_WHITE_EXP = 215
TEXTCOLOR_NONE = 255

COLOR_NONE = 0x0
COLOR_BLACK = 0x000000
COLOR_SILVER = 0xC0C0C0
COLOR_GRAY = 0x808080
COLOR_WHITE = 0xFFFFFF
COLOR_MAROON = 0x800000
COLOR_RED = 0xFF0000
COLOR_PURPLE = 0x800080
COLOR_FUCHSIA = 0xFF00FF
COLOR_GREEN = 0x008000
COLOR_LIME = 0x00FF00
COLOR_OLIVE = 0x808000
COLOR_YELLOW = 0xFFFF00
COLOR_NAVY = 0x000080
COLOR_BLUE = 0x0000FF
COLOR_TEAL = 0x008080
COLOR_AQUA = 0x00FFFF

WINDOWSCREENKEY = '%sx%s' % (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
WINDOW_CENTER_POSITION = {
    '1440x900': (627, 350, 63, 63/32), # Precision completa!
    '1366x768': (590, 285, 50, 50/32), # Precision completa!
    '1280x1024': (557, 398, 56, 56/32) # Le falta precision!
}

# Actualmente no se esta utulizando este dict
WINDOW_CENTER_BATTLELIST = {
    '1440x900': (1276, 290),
    '1366x768': (1276, 290),
    '1280x1024': (1276, 290)
}

WINDOW_SCREEN_OPTIONS = {
    '1440x900': { # Configuracion completa!
        'lootPos': (1300, 170),
        'closeContainer': (1427, 265),
        'toogleInventory': (1275, 162),
        'Offensive': (1330, 190),
        'Balanced': (1350, 190),
        'Defensive': (1470, 190),
        'isOpenInventory': 360,
        'isExistContainerOpened': 579
    },
    '1366x768': { # Configuracion completa!
        'lootPos': (1225, 170),
        'closeContainer': (1353, 265),
        'toogleInventory': (1202, 162),
        'Offensive': (1255, 170),
        'Balanced': (1275, 170),
        'Defensive': (1295, 170),
        'isOpenInventory': 360,
        'isExistContainerOpened': 454
    },
    '1280x1024': { # Le falta configuracion!
        'lootPos': (1300, 170),
        'closeContainer': (1427, 265),
        'toogleInventory': (1275, 162),
        'Offensive': (1330, 190),
        'Balanced': (1350, 190),
        'Defensive': (1470, 190),
        'isOpenInventory': 360,
        'isExistContainerOpened': 579
    }
}

if not (WINDOWSCREENKEY in WINDOW_CENTER_POSITION):
    print("Tu tamaño de pantalla no existe en la base de datos.")
    exit()

SCREENSIZE = WINDOW_CENTER_POSITION[WINDOWSCREENKEY]
BATTLESIZE = WINDOW_CENTER_BATTLELIST[WINDOWSCREENKEY]
SCREEN_OPTIONS = WINDOW_SCREEN_OPTIONS[WINDOWSCREENKEY]

DIRECTION_NORTH = 0
DIRECTION_EAST = 1
DIRECTION_SOUTH = 2
DIRECTION_WEST = 3
DIRECTION_SOUTHWEST = 4
DIRECTION_SOUTHEAST = 5
DIRECTION_NORTHWEST = 6
DIRECTION_NORTHEAST = 7

ACTION_TYPE_ONUSE = 0
ACTION_TYPE_ONWAIT = 1

WM_MOUSEFIRST = 0x200
WM_MOUSEMOVE = 0x200
WM_LBUTTONDOWN = 0x201
WM_LBUTTONUP = 0x202
WM_LBUTTONDBLCLK = 0x203
WM_RBUTTONDOWN = 0x204
WM_RBUTTONUP = 0x205
WM_RBUTTONDBLCLK = 0x206
WM_MBUTTONDOWN = 0x207
WM_MBUTTONUP = 0x208
WM_MBUTTONDBLCLK = 0x209
WM_MOUSEWHEEL = 0x20A
WM_MOUSEHWHEEL = 0x20E
WM_XBUTTONDOWN = 0x020B
WM_XBUTTONUP = 0x020C
MK_LBUTTON = 0x0001
MK_RBUTTON = 0x0002
MK_SHIFT = 0x0004
MK_CONTROL = 0x0008
MK_MBUTTON = 0x0010
MK_XBUTTON1 = 0x0020
MK_XBUTTON2 = 0x0040

MESSAGE_INFO_DESCR = 20
MESSAGE_MONSTER_SAY = 14
MESSAGE_MAXINDEX = 10

VOCATION_SORCERER = 1
VOCATION_DRUID = 2
VOCATION_PALADIN = 3
VOCATION_KNIGHT = 4
VOCATION_SLASHER = 5

VK_ENTER = "{Enter}"
VK_F1 = "{F1}"
VK_F2 = "{F2}"
VK_F3 = "{F3}"
VK_F4 = "{F4}"
VK_F5 = "{F5}"
VK_F6 = "{F6}"
VK_F7 = "{F7}"
VK_F8 = "{F8}"
VK_F9 = "{F9}"
VK_F10 = "{F10}"
VK_F11 = "{F11}"
VK_F12 = "{F12}"
VK_UP = "{Up}"
VK_DOWN = "{Down}"
VK_LEFT = "{Left}"
VK_RIGHT = "{Right}"

CONTAINER_POSITION = 65535

MESSAGE_UNSPECIFIED = 0
MESSAGE_SAY = 1
MESSAGE_WHISPER = 2
MESSAGE_YELL = 3
MESSAGE_PRIVATEMESSAGE = 7
MESSAGE_WHITEMESSAGE = 6
MESSAGE_REDMESSAGESTATIC = 9
MESSAGE_REDMESSAGE = 10
MESSAGE_DARKYELLOWMESSAGE = 12
MESSAGE_ORANGEMESSAGE = 16
MESSAGE_WHITEMESSAGESTATIC = 19
MESSAGE_GREENMESSAGE = 22
MESSAGE_BLUEMESSAGE = 24
MESSAGE_TYPENAMES = {
    MESSAGE_SAY: ' says',
    MESSAGE_WHISPER: ' whispers',
    MESSAGE_YELL: ' yells',
    MESSAGE_PRIVATEMESSAGE: ''
}

GAME_TITLE = "Origin Server"
PROCESS_NAME = "Necroxia Origin.exe"
PROCESS = None
PROCESS_BASEADDRESS = None
CLIENT_HANDLE = None
BOT_PID = 0

# Propiedades para crear un "campo gravitacional" y controlar personajes de un cliente a otro
GAME_ASSIST_TITLE = "Tibia - "
PROCESS_ASSIST_NAME = "Origin.exe"
PROCESS_ASSIST = None
CLIENT_ASSIST_HANDLE = None

__DEBUG__ = False

#oooo     oooo            o88               
# 8888o   888   ooooooo   oooo  oo oooooo   
# 88 888o8 88   ooooo888   888   888   888  
# 88  888  88 888    888   888   888   888  
#o88o  8  o88o 88ooo88 8o o888o o888o o888o 

class Main:
    
    def run():
        Client.updateApp()
        #Client.updateAssistApp()
        DataBot.LoadHotkeyPresets()
        if DataBot.updateAutoloadSettings():
            player = Game.getPlayerClient()
            if player:
                DataBot.LoadHealingMiscellaneousToFile(player.getName())
                wx.CallAfter(MenuProperties.ExtrasFrame.autoloadSettings.SetValue, True)
        wx.CallAfter(MenuProperties.MainMenu.UpdateTimeLeft, (0, 0, 0))
        wx.CallAfter(MenuProperties.MainMenu.UpdateExpPerHour, 0)
        Script.loadscripts()
        # Welcomen message XD
        message = TextMessage(1)
        message.setIndex(1)
        message.setVisible(True)
        message.setTime(5000)
        message.setType(MESSAGE_INFO_DESCR)
        message.setLines(2)
        message.content = ['NecroPyBOT:','Welcomen to the version: 3.1','Create by: Alx']
        TextMessage.setMessageByIndex(message)

#  oooooooo8 o888  o88                          o8   
#o888     88  888  oooo  ooooooooo8 oo oooooo o888oo 
#888          888   888 888oooooo8   888   888 888   
#888o     oo  888   888 888          888   888 888   
# 888oooo88  o888o o888o  88oooo888 o888o o888o 888o 

class Client:
    
    App = 0
    Window = 0
    AssistApp = 0
    AssistWindow = 0
    screenshot_delay = 0

    def updateApp():
        if (Client.App == 0):
            Client.App = Application().connect(process=PROCESS.pid)
            Client.Window = Client.App.window(title=GAME_TITLE)
            if Client.Window:
                global CLIENT_HANDLE
                CLIENT_HANDLE = Client.Window.handle

    def updateAssistApp():
        if (Client.AssistApp == 0):
            Client.AssistApp = Application().connect(process=PROCESS_ASSIST.pid)
            Client.AssistWindow = Client.AssistApp.window(title=GAME_ASSIST_TITLE)
            if Client.AssistWindow:
                global CLIENT_ASSIST_HANDLE
                CLIENT_ASSIST_HANDLE = Client.AssistWindow.handle
                if __DEBUG__:
                    print("[Client]: se ha actualizado el cliente de asistencia.")

    def sendChars(chars):
        return Client.Window.send_chars(chars)

    def sendKeys(keys, assist: bool = False):
        try:
            if not assist:
                return Client.Window.send_keystrokes(keys)
            return Client.AssistWindow.send_keystrokes(keys)
        except:
            print("Unexpected error:", sys.exc_info()[0])

    def sendHotkey(player, value):
        hotkey = None
        vtype = type(value)
        foundId = 0
        if vtype is str:
            if value in Game.Items:
                foundId = Game.Items[value]
            else:
                hotkey = Hotkey.getByWords(player, value)
                if hotkey:
                    return Client.sendKeys(hotkey.getButton())
        if foundId or vtype is int:
            hotkey = Hotkey.getByItemId(player, (not foundId and value or foundId))
            if hotkey:
                Client.sendKeys(hotkey.getButton())

    def leftClick(x, y):
        try:
            lParam = ((y << 16) | x)
            user32.PostMessageW(CLIENT_HANDLE, 0x0201, 0x0, lParam)
            user32.PostMessageW(CLIENT_HANDLE, 0x0202, 0x0, lParam)
        except:
            print("Unexpected error:", sys.exc_info()[0])

    def rightClick(x, y):
        try:
            lParam = ((y << 16) | x)
            user32.PostMessageW(CLIENT_HANDLE, 0x0204, 0x0, lParam)
            user32.PostMessageW(CLIENT_HANDLE, 0x0205, 0x0, lParam)
        except:
            print("Unexpected error:", sys.exc_info()[0])

    def pressEnter():
        user32.PostMessageW(CLIENT_HANDLE, 0x0100, 0x0D, 0x0)
        user32.PostMessageW(CLIENT_HANDLE, 0x0101, 0x0D, 0x0)

    def speak(text=""):
        if text:
            Windows_Speak = Dispatch('SAPI.Spvoice')
            return Windows_Speak.Speak(text)

    def screenshot(filename):
        if len(filename) == 0:
            return print("[Screenshot/Error]: es necesario proporcionar un nombre valido al archivo.")
        # grab fullscreen
        #win32gui.SetForegroundWindow(CLIENT_HANDLE)
        print("Wait 0.5 seconds for the screenshot...")
        time.sleep(0.5)
        im = ImageGrab.grab()
        # save image file
        im.save('screenshots/%s.png' % filename)
        print("[Screenshot/Success]: %s.png se ha guardado correctamente.")

    def fastClickLoot(x, y):
        try:
            lParam = (y << 16) | x
            user32.PostMessageW(CLIENT_HANDLE, 0x0100, 0x11, 0x0)
            user32.PostMessageW(CLIENT_HANDLE, 0x0201, 0x0, lParam)
            user32.PostMessageW(CLIENT_HANDLE, 0x0202, 0x0, lParam)
            user32.PostMessageW(CLIENT_HANDLE, 0x0101, 0x11, 0x0)
        except:
            print("Unexpected error:", sys.exc_info()[0])

    def fastClickLoot_Assist(x, y):
        try:
            lParam = (y << 16) | x
            user32.PostMessageW(CLIENT_ASSIST_HANDLE, 0x0201, 0x0, lParam)
            user32.PostMessageW(CLIENT_ASSIST_HANDLE, 0x0202, 0x0, lParam)
        except:
            print("Unexpected error:", sys.exc_info()[0])

    def setShowFps(mode: bool = True):
        Memory.setNumber(ADDRESS_GAMECLIENT_SHOWFPS, mode and 65536 or 0)

    def getShowFps():
        return Memory.getNumber(ADDRESS_GAMECLIENT_SHOWFPS) == 65536

# oooooooo8   o8                                                         
#888        o888oo ooooooo  oo oooooo   ooooooo     oooooooo8 ooooooooo8 
# 888oooooo  888 888     888 888    888 ooooo888  888    88o 888oooooo8  
#        888 888 888     888 888      888    888   888oo888o 888         
#o88oooo888   888o 88ooo88  o888o      88ooo88 8o 888     888  88oooo888 
#                                                  888ooo888             

class Storage:
    data = {}

    def clear():
        Storage.data.clear()

#  oooooooo8                                    o8                                       
#o888     88 oo oooooo    ooooooooo8  ooooooo o888oo oooo  oooo  oo oooooo    ooooooooo8 
#888          888    888 888oooooo8   ooooo888 888    888   888   888    888 888oooooo8  
#888o     oo  888        888        888    888 888    888   888   888        888         
# 888oooo88  o888o         88oooo888 88ooo88 8o 888o   888o88 8o o888o         88oooo888 

class Creature:

    def __init__(self, index=0):
        self.index = index
        self.offset = int(ADDRESS_BATTLELIST_NEXT) * index
        self.cacheId = -1
        self.cacheName = ""

    def __eq__(self, other):
        if isinstance(self, (Creature, Player)) and isinstance(other, (Creature, Player)):
            return self.getId() == other.getId()
        return False

    def getId(self):
        if self.cacheId != -1:
            return self.cacheId
        self.cacheId = Memory.getNumber(self.offset + ADDRESS_BATTLELIST_CID)
        return self.cacheId

    def getPosition(self):
        return Position(Memory.getNumber(self.offset + ADDRESS_BATTLELIST_POSX), Memory.getNumber(self.offset + ADDRESS_BATTLELIST_POSY), Memory.getNumber(self.offset + ADDRESS_BATTLELIST_POSZ))

    def getPositionOnWindow(self, assist: bool = False):
        return self.getPosition().getPositionOnWindow(assist)

    def getPositionOnBattle(self):
        pass

    def getDistance(self, other):
        return self.getPosition().getDistance(other.getPosition())

    def getDistanceToPlayer(self):
        return self.getPosition().getDistance(Player.Position())

    def getType(self):
        return Memory.getNumber(self.offset + ADDRESS_BATTLELIST_TYPE)

    def getName(self):
        return Memory.getString(self.offset + ADDRESS_BATTLELIST_NAME)

    """TEST"""
    def setName(self, name: str):
        return Memory.setString(self.offset + ADDRESS_BATTLELIST_NAME, name)

    def getHppc(self):
        return Memory.getNumber(self.offset + ADDRESS_BATTLELIST_HPPC)

    def getOutfit(self):
        return {
            'lookType': Memory.getNumber(self.offset + ADDRESS_BATTLELIST_LOOKTYPE),
		    'lookHead': Memory.getNumber(self.offset + ADDRESS_BATTLELIST_LOOKHEAD),
		    'lookBody': Memory.getNumber(self.offset + ADDRESS_BATTLELIST_LOOKPRIMARY),
		    'lookLegs': Memory.getNumber(self.offset + ADDRESS_BATTLELIST_LOOKSECONDARY),
		    'lookFeet': Memory.getNumber(self.offset + ADDRESS_BATTLELIST_LOOKDETAIL),
		    'lookAddon': Memory.getNumber(self.offset + ADDRESS_BATTLELIST_LOOKADDON),
		    'lookMount': Memory.getNumber(self.offset + ADDRESS_BATTLELIST_LOOKMOUNT) }

    def getDirection(self):
        return Memory.getNumber(self.offset + ADDRESS_BATTLELIST_DIRECTION)

    def getParty(self):
        return Memory.getNumber(self.offset + ADDRESS_BATTLELIST_PARTY)

    def setParty(self, party=SHIELD_NONE):
        return Memory.setNumber(self.offset + ADDRESS_BATTLELIST_PARTY, party)
    
    def getSquare(self):
        return [Memory.getNumber(self.offset + ADDRESS_BATTLELIST_SQUARECOLOR), Memory.getNumber(self.offset + ADDRESS_BATTLELIST_SQUARETOGGLE) == 1]
    
    def setSquare(self, color=SQ_COLOR_BLACK, enable=False):
        return Memory.setNumber(self.offset + ADDRESS_BATTLELIST_SQUARECOLOR, color) and Memory.setNumber(self.offset + ADDRESS_BATTLELIST_SQUARETOGGLE, enable and 1 or 0)

    def getLight(self):
        return {
            'amount': Memory.getNumber(self.offset + ADDRESS_BATTLELIST_LIGHTAMOUNT),
            'colour': Memory.getNumber(self.offset + ADDRESS_BATTLELIST_LIGHTCOLOR)
        }

    def setLight(self, colour, amount):
        Memory.setNumber(self.offset + ADDRESS_BATTLELIST_LIGHTAMOUNT, amount)
        Memory.setNumber(self.offset + ADDRESS_BATTLELIST_LIGHTCOLOR, colour)

    def getSkull(self):
        return Memory.getNumber(self.offset + ADDRESS_BATTLELIST_SKULL)

    def setSkull(self, skullType=SKULL_NONE):
        return Memory.setNumber(self.offset + ADDRESS_BATTLELIST_SKULL, skullType)

    def getGuildEmblem(self):
        return Memory.getNumber(self.offset + ADDRESS_BATTLELIST_GUILDEMBLEM)

    def setSummonerType(self):
        return Memory.getNumber(self.offset + ADDRESS_BATTLELIST_SUMMONERTYPE)

    def getIconRay(self):
        return Memory.getNumber(self.offset + ADDRESS_BATTLELIST_ICONRAY)

    def getSpeed(self):
        return Memory.getNumber(self.offset + ADDRESS_BATTLELIST_SPEED)

    def getExpressionBubble(self):
        return Memory.getNumber(self.offset + ADDRESS_BATTLELIST_EXPRESSIONBUBBLE)

    def isVisible(self):
        return Memory.getNumber(self.offset + ADDRESS_BATTLELIST_ISVI) == 1

    def isWalking(self):
        return Memory.getNumber(self.offset + ADDRESS_BATTLELIST_ISWA) == 1

    def isCreature(self):
        return self.getId() >= AUTOID_PLAYERS

    def isPlayer(self):
        return self.isCreature() and self.getId() < AUTOID_MONSTERS

    def isMonster(self):
        cid = self.getId()
        return cid >= AUTOID_MONSTERS and cid < AUTOID_NPCS

    def isNpc(self):
        return self.getId() >= AUTOID_NPCS

    def isFriend(self):
        if self.getName() in Player.Friends:
            return True
        return False

    def isSubFriend(self):
        if self.getName() in Player.SubFriends:
            return True
        return False

    def isEnemy(self):
        if self.getName() in Player.Enemys:
            return True
        return False

    def isSubEnemy(self):
        if self.getName() in Player.SubEnemys:
            return True
        return False

    def isPartyMember(self):
        return self.getParty() >= SHIELD_BLUE

    def setWalking(self, walking):
        return Memory.setNumber(self.offset + ADDRESS_BATTLELIST_ISWA, walking and 1 or 0)

    def getMovementDir(self, reverse=[False,False]):
        movementx = Memory.getNumber(self.offset + ADDRESS_BATTLELIST_MOVEMENTX)
        movementy = Memory.getNumber(self.offset + ADDRESS_BATTLELIST_MOVEMENTY)
        if movementx == 0 and movementy == 0:
            return Position(), None
        multipliers = [1,-1]
        if reverse[0]:
            multipliers = multipliers[::-1]
        step = 32
        direction = None
        if movementx > 0 and movementx <= step:
            movementx = movementx * multipliers[0] # Left Movement
            direction = DIRECTION_WEST
        elif movementx > step:
            movementx = (4294967296 - movementx) * multipliers[1] # Right Movement
            direction = DIRECTION_EAST
        if movementy > 0 and movementy <= step:
            movementy = movementy * multipliers[0] # Up Movement
            if not direction:
                direction = DIRECTION_NORTH
            elif direction == DIRECTION_WEST:
                direction = DIRECTION_NORTHWEST
            else:
                direction = DIRECTION_NORTHEAST
        elif movementy > step:
            movementy = (4294967296 - movementy) * multipliers[1] # Down Movement
            if not direction:
                direction = DIRECTION_SOUTH
            elif direction == DIRECTION_WEST:
                direction = DIRECTION_SOUTHWEST
            else:
                direction = DIRECTION_SOUTHEAST
        """Invertir el sentido del contador, normalmente es de 32 hasta 0, pero cuando esta invertido entonces es desde 0 hasta 32"""
        if reverse[1]:
            if movementx > 0:
                movementx = step - movementx
            elif movementx < 0:
                movementx = (movementx+step) * -1
            if movementy > 0:
                movementy = step - movementy
            elif movementy < 0:
                movementy = (movementy+step) * -1
        return Position(math.ceil(movementx * SCREENSIZE[3]), math.ceil(movementy * SCREENSIZE[3])), direction

    def getStorageValue(self, key):
        playerName = self.getName()
        if playerName in Storage.data:
            if key in Storage.data[playerName]:
                return Storage.data[playerName][key]
        return None

    def setStorageValue(self, key, value):
        playerName = self.getName()
        if not playerName in Storage.data:
            Storage.data[playerName] = {}
        Storage.data[playerName][key] = value
        return True

    def setOutfit(self, outfit):
        Memory.setNumber(self.offset + ADDRESS_BATTLELIST_LOOKTYPE, outfit['lookType'])
        Memory.setNumber(self.offset + ADDRESS_BATTLELIST_LOOKHEAD, outfit['lookHead'])
        Memory.setNumber(self.offset + ADDRESS_BATTLELIST_LOOKPRIMARY, outfit['lookBody'])
        Memory.setNumber(self.offset + ADDRESS_BATTLELIST_LOOKSECONDARY, outfit['lookLegs'])
        Memory.setNumber(self.offset + ADDRESS_BATTLELIST_LOOKDETAIL, outfit['lookFeet'])
        Memory.setNumber(self.offset + ADDRESS_BATTLELIST_LOOKADDON, outfit['lookAddon'])
        Memory.setNumber(self.offset + ADDRESS_BATTLELIST_LOOKMOUNT, outfit['lookMount'])
        return True

#ooooo ooooo             o8   oooo                               
# 888   888   ooooooo  o888oo  888  ooooo ooooooooo8 oooo   oooo 
# 888ooo888 888     888 888    888o888   888oooooo8   888   888  
# 888   888 888     888 888    8888 88o  888           888 888   
#o888o o888o  88ooo88    888o o888o o888o  88oooo888     8888    
#                                                     o8o888     

class Hotkey:
    def __init__(self, button=None, words="", itemId=0):
        self.button = None
        if isinstance(button, (str, int)):
            self.button = "{F%s}" % button
        self.words = words
        self.itemId = itemId

    def __str__(self):
        return "[Button: %s | Words: %s | ItemId: %s]" % (self.button, self.words, self.itemId)

    def getButton(self):
        return self.button

    def getWords(self):
        return self.words

    def getItemId(self):
        return self.itemId

    @staticmethod
    def getByItemId(player, itemId: int):
        playerName = player.getName()
        if playerName in DataBot.HotkeyPresets:
            for hk in DataBot.HotkeyPresets[playerName]:
                if hk.getItemId() == itemId:
                    return hk
        else:
            if DataBot.HotkeyActivePreset in DataBot.HotkeyPresets:
                for hk in DataBot.HotkeyPresets[DataBot.HotkeyActivePreset]:
                    if hk.getItemId() == itemId:
                        return hk
    
    @staticmethod
    def getByWords(player, words: str):
        playerName = player.getName()
        if playerName in DataBot.HotkeyPresets:
            for hk in DataBot.HotkeyPresets[playerName]:
                if words in hk.getWords():
                    return hk
        else:
            if DataBot.HotkeyActivePreset in DataBot.HotkeyPresets:
                for hk in DataBot.HotkeyPresets[DataBot.HotkeyActivePreset]:
                    if words in hk.getWords():
                        return hk

# oooooooo8                         o888  o888  ooooo ooooo             o8   oooo        
#888        ooooooooo    ooooooooo8  888   888   888   888   ooooooo  o888oo  888  ooooo 
# 888oooooo  888    888 888oooooo8   888   888   888ooo888 888     888 888    888o888    
#        888 888    888 888          888   888   888   888 888     888 888    8888 88o   
#o88oooo888  888ooo88     88oooo888 o888o o888o o888o o888o  88ooo88    888o o888o o888o 
#           o888                                                                         

class SpellHotkey:

    spellList = {}

    def __init__(self, name='Unknow', button='{F5}', health=[0, 0], mana=[0, 0], cooldown=0):
        self.name = name
        self.button = button
        self.health = health
        self.mana = mana
        self.lastUsed = 0
        self.cooldown = cooldown
        SpellHotkey.spellList[self.name] = self

    """ GET """

    def getName(self):
        return self.name

    def getButton(self):
        return self.button

    def getHp(self):
        return self.health[0]

    def getHppc(self):
        return self.health[1]

    def getMp(self):
        return self.mana[0]

    def getMppc(self):
        return self.mana[1]

    def getLastUsed(self):
        return self.lastUsed

    def getCooldown(self):
        return self.cooldown

    def getNextUse(self):
        if self.lastUsed <= time.time_ns():
            return 0
        return (self.lastUsed - time.time_ns())

    """ SET """

    def setName(self, name):
        self.name = name

    def setButton(self, button):
        self.button = button

    def setHp(self, hp):
        self.health[0] = hp

    def setHppc(self, hppc):
        self.health[1] = hppc

    def setMp(self, mp):
        self.mana[0] = mp

    def setMppc(self, mppc):
        self.mana[1] = mppc

    def setLastUsed(self, ns):
        self.lastUsed = ns

    def setCooldown(self, cooldown):
        self.cooldown = cooldown

    """ OTHERS """

    def use(self):
        Client.sendKeys(self.getButton())
        self.setLastUsed(time.time_ns() + sec_to_ns(self.getCooldown()))

    """ STATIC """

    @staticmethod
    def getByName(name):
        if name in SpellHotkey.spellList:
            return SpellHotkey.spellList[name]

# Create Spell Default
if __DEBUG__:
    print("Create default spells...")

SpellHotkey("HealSpell", '{F5}', [0, 90], [0, 0], 0)
SpellHotkey("GreatHealthPotion", '{F6}', [0, 70], [0, 0], 0)
SpellHotkey("GreatManaPotion", '{F13}', [0, 0], [0, 0], 0)
SpellHotkey("VocationID", '{F14}', [0, 0], [0, 0], 0)
SpellHotkey("Haste", '{F7}', [0, 0], [0, 5], 6)
SpellHotkey("Manashield", '{F10}', [0, 20], [0, 5], 0)
SpellHotkey("BuffSpell", '{F2}', [0, 0], [0, 5], 60)

if __DEBUG__:
    print("%d spell create correctly!" % len(SpellHotkey.spellList))

#ooooooooo               o8              oooooooooo               o8   
# 888    88o   ooooooo o888oo  ooooooo    888    888   ooooooo  o888oo 
# 888    888   ooooo888 888    ooooo888   888oooo88  888     888 888   
# 888    888 888    888 888  888    888   888    888 888     888 888   
#o888ooo88    88ooo88 8o 888o 88ooo88 8o o888ooo888    88ooo88    888o 

class DataBot:

    AutoloadSettings = False
    
    @staticmethod
    def updateAutoloadSettings():
        if os.path.isfile('data/databot.txt'):
            with open('data/databot.txt') as json_file:
                data = json.load(json_file)
                if 'AutoloadSettings' in data:
                    DataBot.AutoloadSettings = data['AutoloadSettings']
                    MenuProperties.ExtrasFrame.autoloadSettings.SetValue(DataBot.AutoloadSettings)
                    return DataBot.AutoloadSettings

    @staticmethod
    def setAutoloadSettings(mode):
        DataBot.AutoloadSettings = mode
        with open('data/databot.txt', 'w') as outfile:
            datacode = {'AutoloadSettings': mode}
            json.dump(datacode, outfile)

    """Healing/Miscellaneous Save And Load"""
    @staticmethod
    def SaveHealingMiscellaneousToFile(file="default"):
        """Este metodo guardara la configuracion del healing"""
        # Healing/Miscellaneous to datacode
        heal_spell = SpellHotkey.getByName("HealSpell")
        if heal_spell:
            heal_spell.setButton('{%s}' % MenuProperties.HealingFrame.healSpellHotkey.GetValue())
            heal_spell.setHppc(int(MenuProperties.HealingFrame.healSpellValue.GetValue()))
        ghp_hotkey = SpellHotkey.getByName("GreatHealthPotion")
        if ghp_hotkey:
            ghp_hotkey.setButton('{%s}' % MenuProperties.HealingFrame.GH_PotionHotkey.GetValue())
            ghp_hotkey.setHppc(int(MenuProperties.HealingFrame.GH_PotionValue.GetValue()))
        gmp_hotkey = SpellHotkey.getByName("GreatManaPotion")
        if gmp_hotkey:
            gmp_hotkey.setButton('{%s}' % MenuProperties.HealingFrame.GM_PotionHotkey.GetValue())
            gmp_hotkey.setMppc(int(MenuProperties.HealingFrame.GM_PotionValue.GetValue()))
        vocation_id = SpellHotkey.getByName("VocationID")
        if vocation_id:
            vocation_id.setButton(MenuProperties.HealingFrame.VocationHotkey.GetValue())
            vocation_id.setHppc(int(MenuProperties.HealingFrame.VocationID.GetValue()))
        haste_spell = SpellHotkey.getByName("Haste")
        if haste_spell:
            haste_spell.setButton('{%s}' % MenuProperties.HealingFrame.hasteSpellHotkey.GetValue())
            haste_spell.setHppc(int(MenuProperties.HealingFrame.hasteSpellValue.GetValue()))
        manashield_spell = SpellHotkey.getByName("Manashield")
        if manashield_spell:
            manashield_spell.setButton('{%s}' % MenuProperties.HealingFrame.manashieldHotkey.GetValue())
            manashield_spell.setHppc(int(MenuProperties.HealingFrame.manashieldValue.GetValue()))
        buff_spell = SpellHotkey.getByName("BuffSpell")
        if buff_spell:
            buff_spell.setButton('{%s}' % MenuProperties.HealingFrame.buffSpellHotkey.GetValue())
            buff_spell.setHppc(int(MenuProperties.HealingFrame.buffSpellValue.GetValue()))
        datacode = []
        for spellName in SpellHotkey.spellList:
            spellHotkey = SpellHotkey.spellList[spellName]
            match = re.compile(r'(\w\d+)').search(spellHotkey.getButton())
            datacode.append({
                'name': spellName,
                'button': match and match.group() or '',
                'health': spellHotkey.health,
                'mana': spellHotkey.mana
            })
        with open('data/%s.txt' % file, 'w') as outfile:
            json.dump(datacode, outfile)
            print("[DataBot]: se ha guardado el archivo data/%s.txt correctamente." % file)

    @staticmethod
    def LoadHealingMiscellaneousToFile(file="default"):
        """Este metodo cargara la configuracion del healing"""
        if not os.path.isfile('data/%s.txt' % file):
            return print("[DataBot]: No se pudo cargar la configuracion para %s." % file)
        with open('data/%s.txt' % file) as json_file:
            data = json.load(json_file)
            for s in data:
                button = '{%s}' % s['button']
                SpellHotkey(s['name'], button, s['health'], s['mana'])
                #print("load spellHotkey %s | Keys: %s" % (s['name'], button))
            print("[DataBot]: se ha cargado el archivo data/%s.txt" % file)
            wx.CallAfter(MenuProperties.HealingFrame.UpdateHotkeys)

    """ Waypoints Save And Load """
    @staticmethod
    def LoadCaveBotFromFile(file="default"):
        """Este metodo cargara la configuracion del cavebot, waypoints, looting"""
        with open('data/cavebot/%s.txt' % file) as json_file:
            data = json.load(json_file)
            # Waypoints
            Waypoints.waypoints.clear()
            if 'waypoints' in data:
                posStrList = []
                for p in data['waypoints']:
                    w = Waypoint(Position(p['x'], p['y'], p['z']), ('t' in p and p['t'] or WAYPOINT_TYPE_STAND))
                    if 'nx' in p:
                        w.setNodePos(Position(p['nx'], p['ny'], p['nz']))
                    if 'a' in p:
                        w.setAction(WaypointAction(p['a']['t'], Position(p['a']['x'], p['a']['y'], p['a']['z']), p['a']['r']))
                    Waypoints.waypoints.append(w)
                MenuProperties.CaveBotMenu.OrderWaypoints()
            # Looting
            if not MenuProperties.CaveBotMenu.autolootLocked.IsChecked():
                Looting.itemList.clear()
            if 'looting' in data:
                looStrList = []
                for itemId in data['looting']:
                    Looting.addItem(itemId)
                MenuProperties.CaveBotMenu.OrderLooting()
            print("[CaveBot]: se ha cargado el archivo data/cavebot/%s.txt correctamente." % file)

    @staticmethod
    def SaveCaveBotToFile(file="default"):
        """Este metodo guardara la configuracion del cavebot, waypoints, looting"""
        datacode = {}
        datacode['waypoints'] = []
        datacode['looting'] = []
        # Waypoints to datacode
        for w in Waypoints.getWaypoints():
            pos = w.getPosition()
            npos = w.getNodePos()
            wdata = {'t': w.getType(), 'x': pos.x,'y': pos.y,'z': pos.z}
            if npos:
                wdata['nx'] = npos.x
                wdata['ny'] = npos.y
                wdata['nz'] = npos.z
            waction = w.getAction()
            if waction:
                apos = waction.getPosition()
                wdata['a'] = {
                    't': waction.getType(),
                    'r': waction.getRepeat(),
                    'x': apos.x,
                    'y': apos.y,
                    'z': apos.z
                }
            datacode['waypoints'].append(wdata)
        # Looting to datacode
        for i in Looting.getItems():
            datacode['looting'].append(i)
        with open('data/cavebot/%s.txt' % file, 'w') as outfile:
            json.dump(datacode, outfile)
            print("[CaveBot]: se ha guardado el archivo data/cavebot/%s.txt correctamente." % file)
            MenuProperties.CaveBotFrame.fileSelected.Set(MenuProperties.CaveBotFrame.GetFiles())

    """ Targeting Save And Load """
    @staticmethod
    def LoadTargetingFromFile(file="default"):
        """Este metodo cargas en la clase Targeting todos los monstruos que estan guardados en el archivo"""
        with open('data/targeting/%s.txt' % file) as json_file:
            data = json.load(json_file)
            tmStrList = []
            for m in data['monsterList']:
                targetMonster = TargetMonster(m['name'])
                targetMonster.setDistance(m['distance'])
                targetMonster.setSingleSpell(m['singleSpell'])
                targetMonster.setPluralSpell(m['pluralSpell'])
                targetMonster.setIgnoreCount(m['ignoreCount'])
                targetMonster.setPriority(m['priority'])
                targetMonster.setCount(m['count'])
                targetMonster.setAction(m['action'])
                Targeting.monsterList.append(targetMonster)
                tmStrList.append(str(targetMonster))
            MenuProperties.TargetingFrame.monsterList.Set(tmStrList)
            print("[Targeting]: se ha cargado el archivo data/targeting/%s.txt correctamente." % file)

    @staticmethod
    def SaveTargetingToFile(file="default"):
        """Este metodo guardas en un archivo personalizado todas los monstruos que estan en la clase Targeting"""
        datacode = {}
        datacode['monsterList'] = []
        for tm in Targeting.getMonsters():
            datacode['monsterList'].append({
                'name': tm.getName(),
                'distance': tm.getDistance(),
                'singleSpell': tm.getSingleSpell(),
                'pluralSpell': tm.getPluralSpell(),
                'ignoreCount': tm.getIgnoreCount(),
                'priority': tm.getPriority(),
                'count': tm.getCount(),
                'action': tm.getAction()
                })
        with open('data/targeting/%s.txt' % file, 'w') as outfile:
            json.dump(datacode, outfile)
            print("[Targeting]: se ha guardado el archivo data/targeting/%s.txt correctamente." % file)
            MenuProperties.TargetingFrame.fileSelected.Set(MenuProperties.TargetingFrame.GetFiles())

    HotkeyActivePreset = ""
    HotkeyPresets = {}
    """Load Hotkeys Presets"""
    @staticmethod
    def LoadHotkeyPresets():
        with open('%s\Origin\Origin.cfg' % os.getenv('APPDATA')) as cfg_file:
            for line in cfg_file:
                if "HotkeyPreset" in line:
                    playerName = luaString_match(line, '%("(.-)"')
                    button = luaString_match(line, ',(%d-),')
                    command = luaString_match(line, ',"(.-)\n?"')
                    itemId = luaString_match(line, '"",(%d-),')
                    #if __DEBUG__:
                        #print("Hotkey (PlayerName: %s Button: %s Command: %s ItemId: %s) loaded!" % (playerName, button, command, itemId))
                    if not (playerName in DataBot.HotkeyPresets):
                        DataBot.HotkeyPresets[playerName] = []
                    DataBot.HotkeyPresets[playerName].append(Hotkey(button, command, itemId))
                elif "HotkeyActivePreset" in line:
                    DataBot.HotkeyActivePreset = luaString_match(line, '"(.-)"')
                    print("Default hotkey list: %s" % DataBot.HotkeyActivePreset)

#ooooooooooo                          o8   oooo     oooo                        
#88  888  88 ooooooooo8 oooo   oooo o888oo  8888o   888   oooooooo8   oooooooo8 
#    888    888oooooo8    888o888    888    88 888o8 88  888ooooooo 888    88o  
#    888    888           o88 88o    888    88  888  88          888 888oo888o  
#   o888o     88oooo888 o88o   o88o   888o o88o  8  o88o 88oooooo88 888     888 
#                                                                    888ooo888  

class TextMessage:

    cache = []
    lastReadIndex = 0

    def __init__(self, offset):
        self.index = 0
        self.visible = False
        self.time = 0
        self.type = 0
        self.lines = 0
        self.text = ""
        self.content = []
        self.removed = False
        self.sender = ""
        self.position = Position()
        self.offset = offset

    def __str__(self):
        return str(self.__dict__)

    def isRemoved(self):
        return self.removed

    def setRemoved(self, removed=True):
        self.removed = removed

    def getIndex(self):
        return self.index

    def setIndex(self, index=0):
        self.index = index

    def isVisible(self):
        return self.visible

    def setVisible(self, visible=False):
        self.visible = visible

    def getTime(self):
        return self.time

    def setTime(self, time=0):
        self.time = time

    def getType(self):
        return self.type
    
    def setType(self, type=MESSAGE_UNSPECIFIED):
        self.type = type

    def setLines(self, lines):
        self.lines = lines

    def getLines(self):
        return self.lines

    def getText(self):
        return self.text

    def setText(self, text=""):
        self.text = text

    def getSender(self):
        return self.sender

    def setSender(self, sender=""):
        self.sender = sender
    
    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def getOffset(self):
        return self.offset

    def isPrivate(self):
        return self.type == MESSAGE_PRIVATEMESSAGE

    def isYell(self):
        return self.type == MESSAGE_YELL

    def isWhisper(self):
        return self.type == MESSAGE_WHISPER

    def isDefault(self):
        return self.type == MESSAGE_SAY

    @staticmethod
    def updateTime():
        for k, m in enumerate(TextMessage.cache):
            if m.isVisible():
                AOM = ADDRESS_MESSAGE_SEPARATOR * m.getOffset()
                m.setVisible(Memory.getNumber(ADDRESS_MESSAGE_ACTIVE +AOM) == 1)
                m.setTime(m.isVisible() and Memory.getNumber(ADDRESS_MESSAGE_INTERVAL +AOM) or 0)
            if not m.isVisible() or m.getTime() <= 0:
                TextMessage.cache.pop(k)
                break

    def remove(self):
        for k, m in enumerate(TextMessage.cache):
            if m.getIndex() == self.getIndex():
                m.setRemoved()
                TextMessage.cache.pop(k)
                return True
        return False

    @staticmethod
    def concat(table: list, separator=" "):
        Str = ""
        for s in table:
            if type(s) is str:
                Str += s+separator
        return Str[:-1]

    @staticmethod
    def getMessageByIndex(index):
        message = TextMessage(index)
        AOM = ADDRESS_MESSAGE_SEPARATOR * index
        message.setIndex(Memory.getNumber(ADDRESS_MESSAGE_INDEX +AOM))
        message.setVisible(Memory.getNumber(ADDRESS_MESSAGE_ACTIVE +AOM) == 1)
        message.setTime(message.isVisible() and Memory.getNumber(ADDRESS_MESSAGE_INTERVAL +AOM) or 0)
        message.setType(MESSAGE_UNSPECIFIED)
        if message.getTime() <= 0:
            return False
        message.setPosition(Position(Memory.getNumber(ADDRESS_MESSAGE_POSX +AOM), Memory.getNumber(ADDRESS_MESSAGE_POSY +AOM), Memory.getNumber(ADDRESS_MESSAGE_POSZ +AOM)))
        message.setType(Memory.getNumber(ADDRESS_MESSAGE_TYPE +AOM))
        lines = Memory.getNumber(ADDRESS_MESSAGE_LINES +AOM)
        for i in range(0, lines):
            message.content.append(Memory.getString(ADDRESS_MESSAGE_SPEAKER + (ADDRESS_MESSAGE_SEPLINE * i) +AOM, 40))
        if message.content:
            Str = message.content[0]
            if message.getType() == MESSAGE_SAY:
                result = Str.find(" says:")
                if result != -1:
                    message.setSender(Str[:result])
                if len(message.content) > 1:
                    message.content.pop(0)
                message.setText(TextMessage.concat(message.content))
            elif message.getType() == MESSAGE_WHISPER:
                result = Str.find(" whispers:")
                if result != -1:
                    message.setSender(Str[:result])
                if len(message.content) > 1:
                    message.content.pop(0)
                message.setText(TextMessage.concat(message.content))
            elif message.getType() == MESSAGE_YELL:
                result = Str.find(" yells:")
                if result != -1:
                    message.setSender(Str[:result])
                if len(message.content) > 1:
                    message.content.pop(0)
                message.setText(TextMessage.concat(message.content))
            elif message.getType() == MESSAGE_PRIVATEMESSAGE:
                result = Str.find(":")
                if result != -1:
                    message.setSender(Str[:result])
                if len(message.content) > 1:
                    message.content.pop(0)
                message.setText(TextMessage.concat(message.content))
            else:
                message.setSender("")
                message.setText(TextMessage.concat(message.content))
        return message

    @staticmethod
    def setMessageByIndex(message):
        AOM = ADDRESS_MESSAGE_SEPARATOR * message.getOffset()
        Memory.setNumber(ADDRESS_MESSAGE_INDEX +AOM, message.getIndex())
        Memory.setNumber(ADDRESS_MESSAGE_ACTIVE +AOM, message.isVisible())
        Memory.setNumber(ADDRESS_MESSAGE_INTERVAL +AOM, message.getTime())
        position = message.getPosition()
        Memory.setNumber(ADDRESS_MESSAGE_POSX +AOM, position.x)
        Memory.setNumber(ADDRESS_MESSAGE_POSY +AOM, position.y)
        Memory.setNumber(ADDRESS_MESSAGE_POSZ +AOM, position.z)
        Memory.setNumber(ADDRESS_MESSAGE_TYPE +AOM, message.getType())
        Memory.setNumber(ADDRESS_MESSAGE_LINES +AOM, len(message.content))
        for i, content in enumerate(message.content):
            Memory.setString(ADDRESS_MESSAGE_SPEAKER + (ADDRESS_MESSAGE_SEPLINE * i) +AOM, content)
        return message

    @staticmethod
    def getCountMessages(count=0):
	    messages = []
	    for index in range(count):
		    txtmsg = TextMessage.getMessageByIndex(index)
		    if txtmsg:
			    messages.append(txtmsg)
	    return messages

    @staticmethod
    def updateCache(player, interval):
        messages = TextMessage.getCountMessages(10)
        TextMessage.updateTime()
        for k, m in enumerate(messages):
            if m.getIndex() > TextMessage.lastReadIndex:
                TextMessage.cache.append(m)
                TextMessage.lastReadIndex = m.getIndex()

    @staticmethod
    def getMessages():
	    return TextMessage.cache

#ooooooooooo oooo        o88                           
#88  888  88  888ooooo   oooo  oo oooooo     oooooooo8 
#    888      888   888   888   888   888  888    88o  
#    888      888   888   888   888   888   888oo888o  
#   o888o    o888o o888o o888o o888o o888o 888     888 
#                                           888ooo888  

class Thing:
    def __init__(self, itemId=-1, count=-1, position=None, index=-1):
        self.itemId = itemId
        self.count = count
        self.position = position
        self.index = index

    def getId(self):
        return self.itemId

    def getCount(self):
        return self.count

    def getPosition(self):
        if not self.position:
            self.position = Position()
        return self.position

    def getPositionOnWindow(self, assist: bool = False):
        return self.getPosition().getPositionOnWindow(assist)

    def getIndex(self):
        return self.index

    def setId(self, id):
        self.itemId = id

    def setCount(self, count):
        self.count = count

    def setPosition(self, position=None):
        if not position:
            self.position = Position(CONTAINER_POSITION, 64, self.index)
            return False
        self.position = position
        return True

    def setIndex(self, index):
        self.index = index

#  oooooooo8                                                           
#o888     88   ooooooo  oo oooooo  ooooooooo    oooooooo8   ooooooooo8 
#888         888     888 888    888 888    888 888ooooooo  888oooooo8  
#888o     oo 888     888 888        888    888         888 888         
# 888oooo88    88ooo88  o888o       888ooo88   88oooooo88    88oooo888 
#                                  o888                                

class Corpse(Thing):
    def __init__(self, creature: Creature):
        Thing.__init__(self, creature.getId(), 99)
        self.setPosition(creature.getPosition())
        self.looted = False
        self.expire = 0
        self.create_time = time.time()

    def isLooted(self):
        return self.looted

    def getExpire(self):
        return self.expire

    def getCreateTime(self):
        return self.create_time

    def setLooted(self, looted=True):
        self.looted = looted

    def setExpire(self, expire=0):
        self.expire = expire

    def setCreateTime(self, create_time=None):
        if not create_time:
            self.create_time = time.time()
            return False
        self.create_time = create_time
        return True

    def isExpire(self):
        expire = (time.time() - self.getCreateTime()) >= (60 * 5)
        if expire:
            """No se debe eliminar el cuerpo, por que si se elimina de la lista, entonces volvera a entrar en el ciclo de muerte y recrear un nuevo cuerpo como resultado, por lo tanto el BOT debe reiniciarse cada cierto tiempo para que no sufra de colapso, este limite es super ridiculo, un caso que probablemente nunca suceda."""
            # Game.popCacheCorpses(self)
        return expire

    def canSee(self):
        playerPos = Player.Position()
        pos = self.getPosition()
        return pos.getDistanceX(playerPos) <= 7 and pos.getDistanceY(playerPos) <= 5

    def isValid(self):
        return not self.isExpire() and not self.isLooted() and self.canSee()

#  oooooooo8                        o8              o88                                      
#o888     88   ooooooo  oo oooooo o888oo  ooooooo   oooo  oo oooooo   ooooooooo8 oo oooooo   
#888         888     888 888   888 888    ooooo888   888   888   888 888oooooo8   888    888 
#888o     oo 888     888 888   888 888  888    888   888   888   888 888          888        
# 888oooo88    88ooo88  o888o o888o 888o 88ooo88 8o o888o o888o o888o  88oooo888 o888o       

class Container:

    def getItem(index=0) -> Thing:
        return Thing(Memory.getNumber(ADDRESS_CONTAINER_START, ADDRESS_CONTAINER_POINTER_ID, ADDRESS_CONTAINER_SLOT_SEPARATOR * index), Memory.getNumber(ADDRESS_CONTAINER_START, ADDRESS_CONTAINER_POINTER_COUNT, ADDRESS_CONTAINER_SLOT_SEPARATOR * index), index=index)

    def getItems() -> list:
        """Devuelve una lista de cosas encontradas en el primer contenedor"""
        index = 0
        items = []
        item = Container.getItem(index)
        while item.getId() > 99:
            if index > 30: # Esto es solo es caso de emergencia, no deberia llegar a este limite nunca!
                break
            item.setPosition(Position(CONTAINER_POSITION, 64, index))
            items.append(item)
            index = index +1
            item = Container.getItem(index)
        return items

    def getItemById(itemId: int) -> Thing:
        """Devuelve un Thing si lo encuentramos en el contenedor"""
        items = Container.getItems()
        if items:
            for item in items:
                if item.getId() == itemId:
                    return item

#oooo     oooo                                                           
# 8888o   888  ooooooooo8 oo ooo oooo    ooooooo  oo oooooo  oooo   oooo 
# 88 888o8 88 888oooooo8   888 888 888 888     888 888    888 888   888  
# 88  888  88 888          888 888 888 888     888 888         888 888   
#o88o  8  o88o  88oooo888 o888o888o888o  88ooo88  o888o          8888    
#                                                             o8o888     

# const variable
# Establish rights and basic options needed for all process declartion / iteration
TH32CS_SNAPPROCESS = 2
STANDARD_RIGHTS_REQUIRED = 0x000F0000
SYNCHRONIZE = 0x00100000
PROCESS_ALL_ACCESS = (STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 0xFFF)
TH32CS_SNAPMODULE = 0x00000008
TH32CS_SNAPTHREAD = 0x00000004

class MODULEENTRY32(Structure):
    _fields_ = [ ( 'dwSize' , c_long ) , 
                ( 'th32ModuleID' , c_long ),
                ( 'th32ProcessID' , c_long ),
                ( 'GlblcntUsage' , c_long ),
                ( 'ProccntUsage' , c_long ) ,
                ( 'modBaseAddr' , c_long ) ,
                ( 'modBaseSize' , c_long ) , 
                ( 'hModule' , c_void_p ) ,
                ( 'szModule' , c_char * 256 ),
                ( 'szExePath' , c_char * 260 ) ]


CreateToolhelp32Snapshot = windll.kernel32.CreateToolhelp32Snapshot
Process32First = windll.kernel32.Process32First
Process32Next = windll.kernel32.Process32Next
Module32First = windll.kernel32.Module32First
Module32Next = windll.kernel32.Module32Next
GetLastError = windll.kernel32.GetLastError
OpenProcess = windll.kernel32.OpenProcess
GetPriorityClass = windll.kernel32.GetPriorityClass
CloseHandle = windll.kernel32.CloseHandle

def loadProcess():
    try:
        hModuleSnap = DWORD
        me32 = MODULEENTRY32()
        me32.dwSize = sizeof(MODULEENTRY32)
        hModuleSnap = CreateToolhelp32Snapshot(TH32CS_SNAPMODULE, PROCESS.pid)
        ret = Module32First(hModuleSnap, pointer(me32))
        if ret == 0:
            print('ListProcessModules() Error on Module32First[%d]' % GetLastError())
            CloseHandle(hModuleSnap)
        while ret:
            found = str(me32.szModule).find(PROCESS_NAME)
            if found != -1:
                global PROCESS_BASEADDRESS
                PROCESS_BASEADDRESS = me32.modBaseAddr
            ret = Module32Next(hModuleSnap , pointer(me32))
        CloseHandle(hModuleSnap)
        return PROCESS_BASEADDRESS
    except:
        print("Error in ListProcessModules")

class Memory:

    def loadGameClient():
        global PROCESS
        global PROCESS_ASSIST
        PROCESS = ReadWriteMemory.get_process_by_name_list(PROCESS_NAME)
        if not PROCESS:
            exit()
        elif len(PROCESS) == 1:
            PROCESS = PROCESS[0]
            PROCESS.get_all_access_handle()
            PROCESS.set_keep_process(True)
            loadProcess()
            PROCESS_ASSIST = ReadWriteMemory.get_process_by_name_list(PROCESS_ASSIST_NAME)
            if PROCESS_ASSIST:
                PROCESS_ASSIST = PROCESS_ASSIST[0]
                PROCESS_ASSIST.get_all_access_handle()
                PROCESS_ASSIST.set_keep_process(True)
                if __DEBUG__:
                    print("[Memory]: se ha actualizado el proceso de asistencia correctamente.")
            return True
        else:
            MenuProperties.ChooseFrame = GuiChooseMenu(MenuProperties.MainMenu)
            copyList = PROCESS
            pStr = []
            for index, p in enumerate(copyList):
                PROCESS = p
                p.get_all_access_handle()
                loadProcess()
                player_name = ""
                player = Game.getPlayerClient()
                if player:
                    player_name = player.getName()
                pStr.append('%d) [Origin]: %s' % (index, player_name))
            PROCESS = copyList
            MenuProperties.ChooseFrame.clientList.Set(pStr)
            return False

    def getNumber(address, offsets=(), sepOffset=0) -> int:
        return PROCESS.read(PROCESS_BASEADDRESS + int(address), None, offsets, sepOffset)

    def getNumberLong(address, offsets=(), sepOffset=0) -> int:
        return PROCESS.read_long(PROCESS_BASEADDRESS + int(address), None, offsets, sepOffset)

    def getString(address, sizeBytes=255, offsets=(), sepOffset=0) -> str:
        return PROCESS.read(PROCESS_BASEADDRESS + int(address), sizeBytes, offsets, sepOffset)

    def setNumber(address, value: int, offsets=(), sepOffset=0) -> bool:
        return PROCESS.write(PROCESS_BASEADDRESS + int(address), value, offsets, sepOffset)

    def setString(address, value: str, offsets=(), sepOffset=0) -> bool:
        return PROCESS.write(PROCESS_BASEADDRESS + int(address), value, offsets, sepOffset)

#oooooooooo o888                                              
# 888    888 888   ooooooo oooo   oooo ooooooooo8 oo oooooo   
# 888oooo88  888   ooooo888 888   888 888oooooo8   888    888 
# 888        888 888    888  888 888  888          888        
#o888o      o888o 88ooo88 8o   8888     88oooo888 o888o       
#                           o8o888                            

class Player(Creature):

    # Cache para el ultimo ClientPlayer encontrado
    CachePlayer = None
    CachePlayerID = 0

    """ Estas dos variables son esteticas, esto significa que solo las uso para darle detalles extras y posiblemente innesesarios"""
    LastPosition = 0
    HowLongStand = time.time()

    LastClickCount = 0
    lastExp = 0

    lastExps = None
    expSpeed = None
    levelPercent = 0

    """Extras"""
    lastLowHp = None
    lastHppc = 0
    lastMppc = 0

    """Control de pociones, esto es exclusivo de necroxia origin"""
    Potions = {
    'hp': 0,
    'mp': 0,
    'shp': 0,
    'smp': 0,
    'ghp': 0,
    'gmp': 0
    }

    """Modulo de Aimbot"""
    Friends = {}
    SubFriends = {}
    Enemys = {}
    SubEnemys = {}

    def __init__(self, index=0):
        Creature.__init__(self, index)

    def getLevel(self):
        return Memory.getNumber(ADDRESS_PLAYERLEVEL)

    def getExperience(self):
        return Memory.getNumberLong(ADDRESS_PLAYEREXPERINECE)

    def getLevelPercent(self):
        return Player.levelPercent

    @staticmethod
    def getExpForLevel(level):
        level = level - 1
        return ((50 * level * level * level) - (150 * level * level) + (400 * level)) / 3

    @staticmethod
    def getPercentLevel(count, nextLevelCount):
        if nextLevelCount == 0:
            return 0
        result = (count * 100) / nextLevelCount
        if result > 100:
            return 0
        return result

    def getClientXor(self):
        return Memory.getNumber(ADDRESS_GAMECLIENT_XOR)

    def getIcons(self):
        return Memory.getNumber(ADDRESS_CLIENTICONS)

    def hasIcon(self, icons):
        return (self.getIcons() & icons) != 0

    def isParalized(self):
        return self.hasIcon(ICON_PARALYZE)

    def isHasted(self):
        return self.hasIcon(ICON_HASTE)

    def isInFight(self):
        return self.hasIcon(ICON_SWORDS)

    def isPzLocked(self):
        return self.hasIcon(ICON_REDSWORDS)

    def isDazzled(self):
        return self.hasIcon(ICON_DAZZLED)

    def isPoisoned(self):
        return self.hasIcon(ICON_POISON)

    def isBurned(self):
        return self.hasIcon(ICON_BURN)

    def isEnergized(self):
        return self.hasIcon(ICON_ENERGY)

    def isDrunk(self):
        return self.hasIcon(ICON_DRUNK)

    def isManashield(self):
        return self.hasIcon(ICON_MANASHIELD)

    def isDrowning(self):
        return self.hasIcon(ICON_DROWNING)

    def isFreezing(self):
        return self.hasIcon(ICON_FREEZING)

    def isCursed(self):
        return self.hasIcon(ICON_CURSED)

    def isPartyBuff(self):
        return self.hasIcon(ICON_PARTY_BUFF)

    def isPigeon(self):
        return self.hasIcon(ICON_PIGEON)

    def isInPz(self):
        return self.isPigeon()

    def isBleeding(self):
        return self.hasIcon(ICON_BLEEDING)

    def getHealth(self):
        return Memory.getNumber(ADDRESS_PLAYERHEALTH) ^ self.getClientXor()

    def getMaxHealth(self):
        return Memory.getNumber(ADDRESS_PLAYERMAXHEALTH) ^ self.getClientXor()

    def getCapacity(self):
        return Memory.getNumber(ADDRESS_PLAYER_CAPACITY) ^ self.getClientXor()

    def getHealthPercent(self):
        return ((self.getHealth() / self.getMaxHealth()) * 100)

    def getDmgs(self, mana):
        if not mana:
            dmgs = self.getHppc() - Player.lastHppc
            if dmgs >= 0:
                return 0
            return abs(min(dmgs, 0))
        else:
            dmgs = self.getMppc() - Player.lastMppc
            if dmgs >= 0:
                return 0
            return abs(min(dmgs, 0))

    def getMana(self):
        return Memory.getNumber(ADDRESS_PLAYERMANA) ^ self.getClientXor()

    def getMaxMana(self):
        return Memory.getNumber(ADDRESS_PLAYERMAXMANA) ^ self.getClientXor()

    def getManaPercent(self):
        return ((self.getMana() / self.getMaxMana()) * 100)

    getHppc = getHealthPercent
    getMppc = getManaPercent

    def getTargetId(self):
        return Memory.getNumber(ADDRESS_PLAYERTARGETID)

    def getTarget(self):
        return Game.getCreatureById(self.getTargetId())

    def getPosX(self):
        return Memory.getNumber(ADDRESS_PLAYERPOSX)

    def getPosY(self):
        return Memory.getNumber(ADDRESS_PLAYERPOSY)

    def getPosZ(self):
        return Memory.getNumber(ADDRESS_PLAYERPOSZ)

    def getPosition(self):
        return Position(self.getPosX(), self.getPosY(), self.getPosZ())

    def getTargetSquareId(self):
        return Memory.getNumber(ADDRESS_PLAYERISTARGED)
    
    def getTargetSquare(self):
        return Game.getCreatureById(self.getTargetSquareId())

    def isAttacking(self):
        return self.getTargetSquareId() != 0

    @staticmethod
    def Position():
        """Este metodo es utilizado solamente para calcular distancias en las funciones de spectators
        para calcular la posicion del jugador use getPosition por defecto."""
        return Position(Memory.getNumber(ADDRESS_PLAYERPOSX), Memory.getNumber(ADDRESS_PLAYERPOSY), Memory.getNumber(ADDRESS_PLAYERPOSZ))

    def getVocationId(self):
        #return Memory.getNumber(ADDRESS_PLAYERVOCATION)
        vocation_id = SpellHotkey.getByName("VocationID")
        return vocation_id.getHppc()

    def isMage(self):
        return self.getVocationId() in (VOCATION_SORCERER, VOCATION_DRUID)

    def getSoul(self):
        return Memory.getNumber(ADDRESS_PLAYER_SOUL)

    def getMagicLevel(self):
        return Memory.getNumber(ADDRESS_PLAYER_MAGICLEVEL)

    def getSpeedDelta(self):
        return Memory.getNumber(ADDRESS_PLAYER_DELTASPEED)

    def getSpeedBase(self):
        return Memory.getNumber(ADDRESS_PLAYER_BASESPEED)

    def getOfflineTraining(self):
        return Memory.getNumber(ADDRESS_PLAYER_OFFLINETRAINING)

    def getStamina(self):
        return Memory.getNumber(ADDRESS_PLAYER_STAMINA)

    def getFoodTime(self):
        return Memory.getNumber(ADDRESS_PLAYER_FOODTIME)

    def getFistSkill(self):
        return {
            'level': Memory.getNumber(ADDRESS_PLAYER_FIST),
            'percent': Memory.getNumber(ADDRESS_PLAYER_FISTPERCENT)
        }

    def getClubSkill(self):
        return {
            'level': Memory.getNumber(ADDRESS_PLAYER_CLUB),
            'percent': Memory.getNumber(ADDRESS_PLAYER_CLUBPERCENT)
        }

    def getSwordSkill(self):
        return {
            'level': Memory.getNumber(ADDRESS_PLAYER_SWORD),
            'percent': Memory.getNumber(ADDRESS_PLAYER_SWORDPERCENT)
        }

    def getAxeSkill(self):
        return {
            'level': Memory.getNumber(ADDRESS_PLAYER_AXE),
            'percent': Memory.getNumber(ADDRESS_PLAYER_AXEPERCENT)
        }

    def getDistanceSkill(self):
        return {
            'level': Memory.getNumber(ADDRESS_PLAYER_DISTANCE),
            'percent': Memory.getNumber(ADDRESS_PLAYER_DISTANCEPERCENT)
        }

    def getShieldingSkill(self):
        return {
            'level': Memory.getNumber(ADDRESS_PLAYER_SHIELDING),
            'percent': Memory.getNumber(ADDRESS_PLAYER_SHIELDINGPERCENT)
        }

    def getFishSkill(self):
        return {
            'level': Memory.getNumber(ADDRESS_PLAYER_FISH),
            'percent': Memory.getNumber(ADDRESS_PLAYER_FISHPERCENT)
        }

    def getCriticalChance(self):
        return Memory.getNumber(ADDRESS_PLAYER_CRITICALCHANCE)

    def getCriticalAmount(self):
        return Memory.getNumber(ADDRESS_PLAYER_CRITICALAMOUNT)

    def getLifeLeechChance(self):
        return Memory.getNumber(ADDRESS_PLAYER_LIFELEECHCHANCE)

    def getLifeLeechAmount(self):
        return Memory.getNumber(ADDRESS_PLAYER_LIFELEECHAMOUNT)

    def getManaLeechChance(self):
        return Memory.getNumber(ADDRESS_PLAYER_MANALEECHCHANCE)

    def getManaLeechAmount(self):
        return Memory.getNumber(ADDRESS_PLAYER_MANALEECHAMOUNT)

    def getStepsToPoint(self):
        return Memory.getNumber(ADDRESS_PLAYER_STEPSTOPOINT)

    @staticmethod
    def isConnected():
        return Memory.getNumber(ADDRESS_PLAYER_CONNECTIONSTATUS) == 30

    @staticmethod
    def isDisconnected():
        return not Player.isConnected()

    @staticmethod
    def setGotoPosition(position):
        """Esta funciona establece la posicion a donde tiene que ir el personaje cuando se active su autowalking"""
        Memory.setNumber(ADDRESS_PLAYERGOTOPOSX, position.getX())
        Memory.setNumber(ADDRESS_PLAYERGOTOPOSY, position.getY())
        Memory.setNumber(ADDRESS_PLAYERGOTOPOSZ, position.getZ())

    @staticmethod
    def getTimeStand():
        return time.time() - Player.HowLongStand

    @staticmethod
    def getClickCounts():
        return Memory.getNumber(ADDRESS_NUMBEROFATTACKCLICKS)

    @staticmethod
    def hasClickCount():
        clickCount = Player.getClickCounts()
        if clickCount == Player.LastClickCount:
            return False
        Player.LastClickCount = clickCount
        return True

    @staticmethod
    def hasAttack():
        for i in range(5):
            if Player.hasClickCount():
                time.sleep(0.01)
                return True
        return False

    def setTarget(self, target):
        currentTarget = self.getTargetSquare()
        if currentTarget and currentTarget.getId() == target.getId():
            return False
        pMovePos, pMoveDir = self.getMovementDir(reverse=[False,True])
        tMovePos, tMoveDir = target.getMovementDir()
        cursorPos = target.getPositionOnWindow() + tMovePos + pMovePos
        #win32api.SetCursorPos((cursorPos.x,cursorPos.y))
        #MenuProperties.MainMenu.Move(wx.Point(cursorPos.x,cursorPos.y))
        Client.rightClick(cursorPos.x, cursorPos.y)
        if Player.hasAttack():
            Game.addCacheLastCreatures(target)
        return True

    @staticmethod
    def getDefaultMessage():
        return Memory.getString(ADDRESS_DEFAULT_MESSAGE)

    @staticmethod
    def setDefaultMessage(text: str, interval: int):
        return Memory.setString(ADDRESS_DEFAULT_MESSAGE, text) and Memory.setNumber(ADDRESS_DEFAULT_MESSAGE_INTERVAL, interval)

    @staticmethod
    def getChatContent():
        return Memory.getString(ADDRESS_CHAT_CONTENT, offsets=ADDRESS_CHAT_CONTENT_OFFSETS)

    @staticmethod
    def setChatContent(text: str):
        return Memory.setString(ADDRESS_CHAT_CONTENT, text, ADDRESS_CHAT_CONTENT_OFFSETS)

    def say(self, text: str):
        Player.setChatContent(text)
        Client.pressEnter()

    @staticmethod
    def lootItems():
        found = False
        items = Container.getItems()
        if items:
            for item in items[::-1]:
                if item.getId() in Looting.getItems():
                    found = True
                    item.setPosition()
                    lootPos = SCREEN_OPTIONS['lootPos']
                    Game.playerMoveThing(item, Position(lootPos[0], lootPos[1]))
                    time.sleep(GAME_AUTOLOOT_SPEED)
        return found

#oooooooooo                        o88    o8   o88                         
# 888    888  ooooooo    oooooooo8 oooo o888oo oooo   ooooooo  oo oooooo   
# 888oooo88 888     888 888ooooooo  888  888    888 888     888 888   888  
# 888       888     888         888 888  888    888 888     888 888   888  
#o888o        88ooo88   88oooooo88 o888o  888o o888o  88ooo88  o888o o888o 

class Position:
    """Para definir una Position debes pasarle cualquiera de los siguientes argumentos a esta clase:
        * __init__(x, y, z)
        * __init__((x, y, z)) or __init__([x, y, z])
        * __init__(Position(x, y, z))
    """
    def __init__(self, x=0, y=0, z=0):
        self.ups = []
        if isinstance(x, int): # X, Y, Z
            self.x = x
            self.y = y
            self.z = z
        elif isinstance(x, (tuple, list)): # (0, 0, 0) or [0, 0, 0]
            self.x = x[0]
            self.y = x[1]
            if len(x) == 3:
                self.z = x[2]
        elif isinstance(x, Position): # Position(0, 0, 0)
            self = x
        else:
            self.x = 0
            self.y = 0
            self.z = 0

    # Verificar si algun vector esta en cero y darle un valor dado, segun la lista self.ups
    def update(self):
        for n in self.ups:
            if self.x == 0:
                self.x = n
            elif self.y == 0:
                self.y = n
            elif self.z == 0:
                self.z = n

    # Sumar posiciones en matrix
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    # Restar posiciones en matrix
    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    # Multiplicar posiciones en matrix
    def __mul__(self, other):
        self.x *= other.x
        self.y *= other.y
        self.z *= other.z
        return self

    # Comparar dos posiciones
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.z == other.z)
        
    def __str__(self):
        return 'Pos x%s y%s z%s' % (self.x, self.y, self.z)

    def getString(self): pass

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def getOffsetX(self, other):
        return self.x - other.x

    def getOffsetY(self, other):
        return self.y - other.y

    def getOffsetZ(self, other):
        return self.z - other.z

    def getDistanceX(self, other):
        return abs(self.getOffsetX(other) - other.getOffsetX(other))

    def getDistanceY(self, other):
        return abs(self.getOffsetY(other) - other.getOffsetY(other))

    def getDistanceZ(self, other):
        return abs(self.getOffsetZ(other) - other.getOffsetZ(other))

    # Obtener distancia de una posicion a otra
    def getDistance(self, other) -> int:
        return max(max(abs(self.getDistanceX(other)), abs(self.getDistanceY(other))), abs(self.getDistanceZ(other)))

    # Obtener la posicion de pantalla segun la posicion dada
    def getPositionOnWindow(self, assist: bool = False):
        playerPos = Player.Position()
        diffx = self.getOffsetX(playerPos)
        diffy = self.getOffsetY(playerPos)
        return Position(SCREENSIZE[0]+(diffx*SCREENSIZE[2]), SCREENSIZE[1]+(diffy*SCREENSIZE[2]))

# oooooooo8                        o88               o8               
#888           ooooooo  oo oooooo  oooo ooooooooo  o888oo  oooooooo8  
# 888oooooo  888     888 888    888 888  888    888 888   888ooooooo  
#        888 888         888        888  888    888 888           888 
#o88oooo888    88ooo888 o888o      o888o 888ooo88    888o 88oooooo88  
#                                       o888                          

# clase que se encarga de guardar todos los scripts que se ejecutaran con el planificador
class Scripts:

    enclosure_queue = Queue()
    scriptsList = []
    modules = {}
    lastReload = False

    @staticmethod
    def getScriptList():
        return Scripts.scriptsList

    @staticmethod
    def getScriptByIndex(index):
        return Scripts.scriptsList[index]

    @staticmethod
    def getScriptByName(name):
        for script in Scripts.scriptsList:
            if script.getName() == name:
                return script

    @staticmethod
    def removeScriptByName(name):
        for index, script in enumerate(Scripts.scriptsList):
            if script.getName() == name:
                Scripts.scriptsList.pop(index)
                return True
        return False

    @staticmethod
    def addScript(script):
        Scripts.scriptsList.append(script)
        Scripts.scriptsList.sort(key=lambda s: (s.isLocked(), s.getInterval()))
        Scripts.enclosure_queue.put(script.getName())
        MenuProperties.ScriptsFrame.UpdateScriptList()
        return script.getIndex()

class Script:
    def __init__(self, name, interval=None, coinit=None, running=None, locked=False, hide=False):
        if Scripts.removeScriptByName(name):
            print("%s reload...")
        self.name = name
        self.tasks = []
        self.cinterval = 0
        self.interval = 1000000000
        self.running = (not running and locked or running)
        if interval:
            self.interval = interval * 1000 * 1000
        self.locked = locked
        self.hide = hide
        self.index = -1
        self.desc = "No description provided."
        self.module = ""

    def __setattr__(self, name, value):
        if name == "onThink" and callable(value):
            self.__dict__['tasks'].append(value)
        else:
            self.__dict__[name] = value

    def getName(self):
        return self.name

    def getRunning(self):
        return self.running

    def setRunning(self, status=True):
        self.running = status

    def getInterval(self):
        return self.interval

    def setInterval(self, interval):
        self.interval = interval

    def getIndex(self):
        return self.index

    def isLocked(self):
        return self.locked

    def isReloadable(self):
        return self.module

    def getThread(self):
        return self.thread

    def setDescription(self, description: str = 'No description provided.'):
        self.desc = description

    def getDescription(self):
        return self.desc
   
    def register(self, module_name = None):
        index = Scripts.addScript(self)
        self.module = module_name
        if module_name == Scripts.lastReload:
            Scripts.lastReload = self
            MenuProperties.ScriptsFrame.OnUpdateScript(self)
        return True

    def reload(self):
        if self.module:
            Scripts.lastReload = self.module
            importlib.reload(Scripts.modules[self.module])
            del self
            return Scripts.lastReload
        return False

    @staticmethod
    def update(script):
        if not script.tasks or not script.getRunning():
            return
        if script.cinterval <= time.time_ns():
            script.cinterval = time.time_ns() + script.interval
            for task in script.tasks:
                try:
                    task(Game.getPlayerClient(), script.interval)
                except:
                    print("Unexpected error:", sys.exc_info()[0])

    @staticmethod
    def loadscripts():
        for file in os.listdir("data/scripts"):
            if file.endswith(".py"):
                modir = 'data.scripts.%s' % file[:-3]
                Scripts.modules[modir] = importlib.import_module(modir)
        if __DEBUG__:
            print("Se han cargado %d scripts!" % len(Scripts.scriptsList))

#oooo     oooo                                           o88               o8               
# 88   88  88 ooooooo oooo   oooo ooooooooo     ooooooo  oooo  oo oooooo o888oo  oooooooo8  
#  88 888 88  ooooo888 888   888   888    888 888     888 888   888   888 888   888ooooooo  
#   888 888 888    888  888 888    888    888 888     888 888   888   888 888           888 
#    8   8   88ooo88 8o   8888     888ooo88     88ooo88  o888o o888o o888o 888o 88oooooo88  
#                      o8o888     o888                                                      

# Constants
WAYPOINT_MAX_DISTANCE = 30
WAYPOINT_TYPE_STAND = 0
WAYPOINT_TYPE_BUYPOT = 1
WAYPOINT_TYPE_ACTION = 2
WAYPOINT_TYPE_NODE = 3
WAYPOINT_TYPE_NEXT = 4

WAYPOINT_TYPENAMES = ["Stand", "Pots", "Action", "Node", "Next"]

class WaypointAction:

    TYPE_USEITEM = 1
    TYPE_USEITEMONXYZ = 2
    TYPE_LOOK = 3

    TYPE_NAMES = {
        'useitem': TYPE_USEITEM,
        'useitemonxyz': TYPE_USEITEM,
        'look': TYPE_LOOK
    }

    """Este objeto almacena una o mas acciones dadas a un Waypoint de tipo de Action"""
    def __init__(self, wtype: int, position: Position, repeat: int = 1):
        self.type = wtype
        self.position = position
        self.repeat = repeat

    def getType(self):
        return self.type

    def getPosition(self):
        return self.position

    def getRepeat(self):
        return self.repeat

    def isUseItem(self):
        return self.type == WaypointAction.TYPE_USEITEM

    def isUseItemOnXyz(self):
        return self.type == WaypointAction.TYPE_USEITEMONXYZ

    def isLook(self):
        return self.type == WaypointAction.TYPE_LOOK

class Waypoint:

    Colours = {
        #WAYPOINT_TYPE_STAND: wx.NullColour
        WAYPOINT_TYPE_ACTION: wx.Colour(240, 128, 128),
        WAYPOINT_TYPE_BUYPOT: wx.Colour(30, 219, 142),
        WAYPOINT_TYPE_NODE: wx.Colour(0, 150, 200),
        WAYPOINT_TYPE_NEXT: wx.Colour(100, 0, 200)
    }

    """Este objeto almacena un punto de referencia con propiedades especiales"""
    def __init__(self, position=Position(), type=WAYPOINT_TYPE_STAND):
        self.position = position
        self.node_position = None
        self.type = type
        self.action = None
        self.colour = None
        self.next_ways = ""
        self.updateColour()

    def updateColour(self):
        if self.type in Waypoint.Colours:
            self.colour = Waypoint.Colours[self.type]
            if self.getNodePos():
                nodeColour = Waypoint.Colours[WAYPOINT_TYPE_NODE]
                self.colour = wx.Colour(self.colour[0]+nodeColour[0], self.colour[1]+nodeColour[1], self.colour[2]+nodeColour[2])

    def __str__(self):
        return str(self.position)

    def getPosition(self) -> Position:
        return self.position

    def getType(self) -> int:
        return self.type

    def getAction(self):
        return self.action

    def setAction(self, action):
        self.action = action
        self.type = WAYPOINT_TYPE_ACTION
        self.updateColour()

    def setColour(self, colour):
        self.colour = colour

    def getColour(self):
        return self.colour

    def getDistance(self, position) -> int:
        return self.position.getDistance(position)

    def getInfo(self, beforeWaypoint, hereWaypoint) -> str:
        pos = self.getPosition()
        bpos = not beforeWaypoint and pos or beforeWaypoint.getPosition()
        return "%s [%s] x%s y%s z%s%s" % ((hereWaypoint and emoji.emojize(":fast_forward:", use_aliases=True, variant="emoji_type") or ''), WAYPOINT_TYPENAMES[self.getType()], pos.x, pos.y, pos.z, (pos.getDistance(bpos) > WAYPOINT_MAX_DISTANCE and emoji.emojize(" :x: ", use_aliases=True, variant="emoji_type") or ' '))

    def getNodePos(self):
        return self.node_position

    def setNodePos(self, pos):
        if isinstance(pos, Position):
            self.node_position = pos
            return
        raise ValueError("El parametro pasado no es un objeto de tipo 'Position'")

    def setType(self, wtype):
        self.type = wtype

    def isNode(self):
        return self.type == WAYPOINT_TYPE_NODE

    def isNext(self):
        return self.type == WAYPOINT_TYPE_NEXT

class Waypoints:
    """Este objeto se encargara de almacenar los puntos de referencia
    en el mapa"""

    waypoints = []
    currentWaypoint = 0
    lastPositionRec = False
    lastGotoPos = None
    reverseAdded = []

    @staticmethod
    def next():
        """Vamos al siguiente punto, y chequiamos"""
        Waypoints.currentWaypoint += 1
        Waypoints.check()
        return Waypoints.currentWaypoint
    
    @staticmethod
    def check():
        """Si esta fuera de rango, entonces comenzemos de nuevo"""
        if not index_in_list(Waypoints.waypoints, Waypoints.currentWaypoint):
            Waypoints.currentWaypoint = 0

    @staticmethod
    def getWaypoints() -> Waypoint:
        return Waypoints.waypoints

    @staticmethod
    def addWaypoint(waypoint):
        if isinstance(waypoint, list):
            for w in waypoint:
                Waypoints.waypoints.append(w)
        else:
            Waypoints.waypoints.append(waypoint)

    @staticmethod
    def removeWaypoint(index=-1):
        if isinstance(index, int):
            Waypoints.waypoints.pop(index)
        elif isinstance(index, Position):
            Waypoints.waypoints.remove(index)

    @staticmethod
    def getCurrentWaypoint() -> Waypoint:
        if index_in_list(Waypoints.waypoints, Waypoints.currentWaypoint):
            return Waypoints.waypoints[Waypoints.currentWaypoint]

    @staticmethod
    def getNextWaypoint() -> Waypoint:
        Waypoints.check()
        waypoint = Waypoints.getCurrentWaypoint()
        if not waypoint:
            if __DEBUG__:
                print("[CaveBot]: no existe ningun 'waypoint' en la lista.")
            return
        skipWaypoint = False
        playerPos = Player.Position()
        waypointPos = waypoint.getPosition()
        waypointNode = waypoint.getNodePos()
        if (playerPos == waypointPos or (waypointNode and playerPos == waypointNode)):
            Memory.setNumber(ADDRESS_PLAYERUPDATE_POSZ, playerPos.getZ())
            waypointType = waypoint.getType()
            if waypointType == WAYPOINT_TYPE_BUYPOT:
                Game.IsBuyPots = True
                if __DEBUG__:
                    print("[Waypoints]: buy potion start!")
            elif waypoint.isNext():
                DataBot.LoadCaveBotFromFile(waypoint.next_ways)
                currentWaypoint = 0
                lastPositionRec = False
                reverseAdded = []
                return
            skipWaypoint = True
        elif playerPos.z != waypointPos.z or waypointPos.getDistance(playerPos) > WAYPOINT_MAX_DISTANCE:
            skipWaypoint = True
            if __DEBUG__:
                print("[Waypoints]: invalid waypoints connection ( %s >> %s )" % (playerPos, waypointPos))
        if skipWaypoint:
            beforeIndex = Waypoints.currentWaypoint
            afterIndex = Waypoints.next()
            wx.CallAfter(MenuProperties.CaveBotFrame.UpdateWaypointTwo, waypoint, beforeIndex, Waypoints.getCurrentWaypoint(), afterIndex)
            return
        return waypoint

    @staticmethod
    def running(player):
        if len(Waypoints.waypoints) > 1:
            waypoint = Waypoints.getNextWaypoint()
            if waypoint:
                if not Game.StopWalking and not Game.IsBuyPots:
                    wPosition = waypoint.getPosition()
                    Player.setGotoPosition(wPosition)
                    player.setWalking(True)
                    if __DEBUG__:
                        if not Waypoints.lastGotoPos or Waypoints.lastGotoPos != wPosition:
                            Waypoints.lastGotoPos = wPosition
                            print("[CaveBot/Goto]: %s" % wPosition)
            elif __DEBUG__:
                print("[CaveBot/NoFound]: no found next waypoint!")

#ooooo                                o8   o88                           
# 888          ooooooo     ooooooo  o888oo oooo  oo oooooo     oooooooo8 
# 888        888     888 888     888 888    888   888   888  888    88o  
# 888      o 888     888 888     888 888    888   888   888   888oo888o  
#o888ooooo88   88ooo88     88ooo88    888o o888o o888o o888o 888     888 
#                                                             888ooo888  

class Looting:

    itemList = []

    def getItems() -> list:
        return Looting.itemList

    def addItem(itemId) -> bool:
        if not (itemId in Looting.itemList):
            Looting.itemList.append(itemId)
            return True

    def removeItem(itemId) -> bool:
        if itemId in Looting.itemList:
            Looting.itemList.remove(itemId)
            return True

#ooooooooooo                                                o8   o88                           
#88  888  88 ooooooo   oo oooooo     oooooooo8 ooooooooo8 o888oo oooo  oo oooooo     oooooooo8 
#    888     ooooo888   888    888 888    88o 888oooooo8   888    888   888   888  888    88o  
#    888   888    888   888         888oo888o 888          888    888   888   888   888oo888o  
#   o888o   88ooo88 8o o888o       888     888  88oooo888   888o o888o o888o o888o 888     888 
#                                   888ooo888                                       888ooo888  

class Targeting:

    monsterList = []

    @staticmethod
    def addMonster(targetMonster):
        if not Targeting.monsterList:
            Targeting.monsterList.append(targetMonster)
            return True
        for index, tm in enumerate(Targeting.monsterList):
            if tm.getName() == targetMonster.getName():
                Targeting.monsterList[index] = targetMonster
                return True
        Targeting.monsterList.append(targetMonster)
        return True

    @staticmethod
    def removeMonster(targetMonster):
        Targeting.monsterList.remove(targetMonster)

    @staticmethod
    def removeMonsterByIndex(index):
        Targeting.monsterList.pop(index)

    @staticmethod
    def getMonsters():
        return Targeting.monsterList

    @staticmethod
    def getMonsterByIndex(index):
        return Targeting.monsterList[index]

    @staticmethod
    def getMonsterByName(name):
        for tm in Targeting.monsterList:
            if tm.getName() == name:
                return tm

class TargetMonster:

    transformCount = {
        'Any': lambda l: True,
        '1': lambda l: l == 1,
        '1+': lambda l: l >= 1,
        '2': lambda l: l == 2,
        '2+': lambda l: l >= 2,
        '3': lambda l: l == 3,
        '3+': lambda l: l >= 3,
        '4': lambda l: l == 4,
        '4+': lambda l: l >= 4,
        '5': lambda l: l == 5,
        '5+': lambda l: l >= 5,
        '6': lambda l: l == 6,
        '6+': lambda l: l >= 6,
        '7': lambda l: l == 7,
        '7+': lambda l: l >= 7
    }
    
    def __init__(self, name):
        self.name = name
        self.distance = -1
        self.singleSpell = ""
        self.pluralSpell = ""
        self.ignoreCount = -1
        self.priority = 1
        self.count = "Any"
        self.action = "No Action"

    def __str__(self):
        if self.count != "Any":
            return '%s >> %s' % (self.name, self.count)
        return '%s' % self.name

    # >> SET <<
    def setName(self, name):
        self.name = name
    
    def setDistance(self, distance):
        self.distance = distance

    def setSingleSpell(self, spell):
        self.singleSpell = spell
    
    def setPluralSpell(self, spell):
        self.pluralSpell = spell
    
    def setIgnoreCount(self, ignoreCount):
        self.ignoreCount = ignoreCount
    
    def setPriority(self, priority):
        self.priority = priority
    
    def setCount(self, count):
        self.count = count
    
    def setAction(self, action):
        self.action = action
    
    # >> GET <<
    def getName(self):
        return self.name
    
    def getDistance(self):
        return self.distance

    def getSingleSpell(self):
        return self.singleSpell
    
    def getPluralSpell(self):
        return self.pluralSpell
    
    def getIgnoreCount(self):
        return self.ignoreCount
    
    def getPriority(self):
        return self.priority
    
    def getCount(self):
        return self.count
    
    def getAction(self):
        return self.action

#ooooooooooo            o888                                        o8                          
#88  888  88 ooooooooo8  888  ooooooooo8 oo ooo oooo   ooooooooo8 o888oo oo oooooo  oooo   oooo 
#    888    888oooooo8   888 888oooooo8   888 888 888 888oooooo8   888    888    888 888   888  
#    888    888          888 888          888 888 888 888          888    888         888 888   
#   o888o     88oooo888 o888o  88oooo888 o888o888o888o  88oooo888   888o o888o          8888    
#                                                                                    o8o888     

class TelemetryMessage:
    def __init__(self, message):
        self.message = message

    def getMessage(self):
        return self.message

#  ooooooo8                                      
#o888    88   ooooooo   oo ooo oooo   ooooooooo8 
#888    oooo  ooooo888   888 888 888 888oooooo8  
#888o    88 888    888   888 888 888 888         
# 888ooo888  88ooo88 8o o888o888o888o  88oooo888 
                                                

class Game:
    """Al comienzo de esta clase he definido variables estaticas de esta clase, con el proposito de
        tener una mejor comunicacion entre hilos y no tener problemas de entralazamiento
        No se si sea la mejor forma de tratar esto, pero es una opcion temporal, asi la llamare yo: GameTempConfig
    """

    # Player Status
    IsLooting = False
    IsAttacking = False
    IsBuyPots = False

    StopWalking = False
    StopAttacking = False

    # Bot Mods
    Waypoints_Enabled = True
    RecWaypoints = False

    #Cache
    CacheCreatures = []
    CacheLastCreatures = []
    CacheCorpses = []
    
    LastCorpse = []
    CheckLastCorpseOpened = 0
    CheckCorpseLooting = 0

    CacheBattleList = []

    Items = {
        'ghp': 239,
        'gmp': 238,
        'mw': 3180
    }

    #Messages
    LastChatIndex = 0
    LastChatContent = []

    #Area de telemetria
    TelemetryMessages = []

    """Aqui finaliza en apartado de variables estaticas de esta clase"""
    # Obtener el player del cliente
    @staticmethod
    def getPlayerClient() -> Player:
        playerId = Memory.getNumber(ADDRESS_PLAYERID)
        if playerId == Player.CachePlayerID:
            return Player.CachePlayer
        elif playerId == 0:
            Memory.loadGameClient()
            Client.updateApp()
            #Client.updateAssistApp()
            print("Re-estableciendo la conexion con el cliente...")
            return
        for index in range(ADDRESS_BATTLELIST_MAXINDEX):
            player = Player(index)
            if player.getId() == playerId:
                MenuProperties.MainMenu.SetTitle(u"%s BOT - %s" % (GAME_TITLE, player.getName()))
                MenuProperties.MainMenu.UpdatePlayerName(player)
                Player.CachePlayer = player
                Player.CachePlayerID = player.getId()
                Player.lastExp = player.getExperience()
                return player
        """En cualquier caso devolvamos el player guardado en la cache, para que algunos metodos del player globales aun puedan usarse"""
        return

    # Buscar un player con el nombre
    @staticmethod
    def getPlayerByName(playerName: str = "") -> Player:
        playerId = Memory.getNumber(ADDRESS_PLAYERID)
        for index in range(ADDRESS_BATTLELIST_MAXINDEX):
            offset = int(ADDRESS_BATTLELIST_NEXT) * index
            cid = Memory.getNumber(offset + ADDRESS_BATTLELIST_CID)
            if cid >= AUTOID_PLAYERS and cid < AUTOID_MONSTERS:
                name = Memory.getString(offset + ADDRESS_BATTLELIST_NAME)
                if playerName == name:
                    return playerId == cid and Player(index) or Creature(index)

    # Buscar un player con skull
    @staticmethod
    def getPlayerSkull(playerSkull: int = SKULL_WHITE) -> Player:
        playerId = Memory.getNumber(ADDRESS_PLAYERID)
        for index in range(ADDRESS_BATTLELIST_MAXINDEX):
            offset = int(ADDRESS_BATTLELIST_NEXT) * index
            cid = Memory.getNumber(offset + ADDRESS_BATTLELIST_CID)
            if cid >= AUTOID_PLAYERS and cid < AUTOID_MONSTERS:
                skullType = Memory.getNumber(offset + ADDRESS_BATTLELIST_SKULL)
                if (playerSkull == SKULL_NONE and skullType != SKULL_NONE) or (skullType == playerSkull):
                    return playerId == cid and Player(index) or Creature(index)

    # Buscar una creature con el nombre
    @staticmethod
    def getCreatureByName(creatureName) -> Creature:
        playerId = Memory.getNumber(ADDRESS_PLAYERID)
        for index in range(ADDRESS_BATTLELIST_MAXINDEX):
            offset = int(ADDRESS_BATTLELIST_NEXT) * index
            cid = Memory.getNumber(offset + ADDRESS_BATTLELIST_CID)
            if cid >= AUTOID_PLAYERS:
                name = Memory.getString(offset + ADDRESS_BATTLELIST_NAME)
                if creatureName == name:
                    return playerId == cid and Player(index) or Creature(index)

    # Buscar una creature con la ID
    @staticmethod
    def getCreatureById(creatureId) -> Creature:
        playerId = Memory.getNumber(ADDRESS_PLAYERID)
        for index in range(ADDRESS_BATTLELIST_MAXINDEX):
            offset = int(ADDRESS_BATTLELIST_NEXT) * index
            cid = Memory.getNumber(offset + ADDRESS_BATTLELIST_CID)
            if cid >= AUTOID_PLAYERS and cid == creatureId:
                return playerId == cid and Player(index) or Creature(index)

    # Obtener una lista con todas las creatures de la memoria
    @staticmethod
    def getCreatures(OnScreen=False, Around=[7, 5], Filter=None) -> Creature:
        creatures = []
        playerId = Memory.getNumber(ADDRESS_PLAYERID)
        playerPos = Player.Position()
        for index in range(ADDRESS_BATTLELIST_MAXINDEX):
            offset = int(ADDRESS_BATTLELIST_NEXT) * index
            cid = Memory.getNumber(offset + ADDRESS_BATTLELIST_CID)
            creature = cid == playerId and Player(index) or Creature(index)
            if creature.isCreature() and (not Filter or Filter(creature)):
                if OnScreen:
                    position = creature.getPosition()
                    if creature.isVisible() and position.z == playerPos.z:
                        if creature.getHppc() > 0:
                            if position.getDistanceX(playerPos) <= Around[0] and position.getDistanceY(playerPos) <= Around[1]:
                                creatures.append(creature)
                else:
                    creatures.append(creature)
        Game.CacheCreatures = creatures
        return creatures

    @staticmethod
    def getCreaturesCache(OnScreen=False, Around=[7, 5]):
        creatures = []
        playerPos = Player.Position()
        for creature in Game.CacheCreatures:
            if creature.isCreature():
                if OnScreen:
                    position = creature.getPosition()
                    if creature.isVisible() and position.z == playerPos.z:
                        if creature.getHppc() > 0:
                            if position.getDistanceX(playerPos) <= Around[0] and position.getDistanceY(playerPos) <= Around[1]:
                                creatures.append(creature)
                else:
                    creatures.append(creature)
        return creatures

    # Obtener una lista con todas las players de la memoria
    @staticmethod
    def getPlayers(OnScreen=False, Around=[7, 5], Filter=None) -> Player:
        players = []
        playerId = Memory.getNumber(ADDRESS_PLAYERID)
        playerPos = Player.Position()
        for index in range(ADDRESS_BATTLELIST_MAXINDEX):
            offset = int(ADDRESS_BATTLELIST_NEXT) * index
            cid = Memory.getNumber(offset + ADDRESS_BATTLELIST_CID)
            player = cid == playerId and Player(index) or Creature(index)
            if player.isPlayer() and (not Filter or Filter(player)):
                if OnScreen:
                    position = player.getPosition()
                    if player.isVisible() and position.z == playerPos.z:
                        if player.getHppc() > 0:
                            if position.getDistanceX(playerPos) <= Around[0] and position.getDistanceY(playerPos) <= Around[1]:
                                players.append(player)
                else:
                    players.append(player)
        return players

    # Obtener una lista con todas los monsters de la memoria
    @staticmethod
    def getMonsters(OnScreen=False, Around=[7, 5], Filter=None) -> Creature:
        monsters = []
        playerId = Memory.getNumber(ADDRESS_PLAYERID)
        playerPos = Player.Position()
        for index in range(ADDRESS_BATTLELIST_MAXINDEX):
            monster = Creature(index)
            if monster.isMonster() and (not Filter or Filter(monster)):
                if OnScreen:
                    position = monster.getPosition()
                    if monster.isVisible() and position.z == playerPos.z:
                        if monster.getHppc() > 0:
                            if position.getDistanceX(playerPos) <= Around[0] and position.getDistanceY(playerPos) <= Around[1]:
                                monsters.append(monster)
                else:
                    monsters.append(monster)
        return monsters

    # Obtener una lista con todas los npc's de la memoria
    @staticmethod
    def getNpcs(OnScreen=False, Around=[7, 5]) -> Creature:
        npcs = []
        playerId = Memory.getNumber(ADDRESS_PLAYERID)
        playerPos = Player.Position()
        for index in range(ADDRESS_BATTLELIST_MAXINDEX):
            npc = Creature(index)
            if npc.isNpc():
                if OnScreen:
                    position = npc.getPosition()
                    if npc.isVisible() and position.z == playerPos.z:
                        if npc.getHppc() > 0:
                            if position.getDistanceX(playerPos) <= Around[0] and position.getDistanceY(playerPos) <= Around[1]:
                                npcs.append(npc)
                else:
                    npcs.append(npc)
        return npcs

    @staticmethod
    def getEnemies():
        players = Game.getPlayers(True)
        found_enemies = []
        if len(players) >= 2:
            for player in players:
                if player != Player.CachePlayer and not player.isFriend():
                    found_enemies.append(player)
        return found_enemies

    @staticmethod
    def closeContainer():
        closeContainerPos = SCREEN_OPTIONS['closeContainer']
        return Client.leftClick(closeContainerPos[0], closeContainerPos[1])

    #@ Metodo special para mover cosas, probablemente no este muy optimizado, pero funciona rapido
    #@ Parametros requeridos: Thing(), Position()
    @staticmethod
    def playerMoveThing(thing, toPos):
        itemId = thing.getId()
        count = thing.getCount()
        fromPos = thing.getPosition()
        Memory.setNumber(0x6D4604, itemId) # ItemId/Type
        Memory.setNumber(0x6D4600, count) # ItemCount/CreatureId
        Memory.setNumber(0x54C250, fromPos.x) # PositionX/ContainerPos
        Memory.setNumber(0x54C2A8, fromPos.y) # PositionY/ContainerIndex
        Memory.setNumber(0x54C280, fromPos.z) # PositionZ/ContainerSlot
        Memory.setNumber(0x54C2B4, 2)
        Memory.setNumber(0x54C23C, 2)
        Memory.setNumber(0x54C23C, 6)
        Memory.setNumber(0x54C294, 6)
        Client.fastClickLoot(toPos.x, toPos.y)

    @staticmethod
    def getThingLook() -> Thing:
        return Thing(Memory.getNumber(ADDRESS_ID_ONLOOKCLICK), Memory.getNumber(ADDRESS_COUNT_ONLOOKCLICK))

    @staticmethod
    def getCacheLastCreatures():
        return Game.CacheLastCreatures

    @staticmethod
    def addCacheLastCreatures(creature: Creature):
        if Game.CacheLastCreatures:
            for other in Game.CacheLastCreatures:
                if other.getId() == creature.getId():
                    return False
        Game.CacheLastCreatures.append(creature)
        return True

    @staticmethod
    def popCacheLastCreatures(creature: Creature):
        if Game.CacheLastCreatures:
            for index, other in enumerate(Game.CacheLastCreatures):
                if other.getId() == creature.getId():
                    Game.CacheLastCreatures.pop(index)
                    return True
        return False

    @staticmethod
    def getCacheCorpses():
        return Game.CacheCorpses

    @staticmethod
    def addCacheCorpses(corpse):
        collision = []
        if Game.CacheCorpses:
            for other in Game.CacheCorpses:
                if other.getId() == corpse.getId():
                    return False
                elif not other.isExpire() and other.getPosition() == corpse.getPosition():
                    collision.append(other)
        if collision:
            for other in collision:
                other.setCreateTime(0)
                other.setLooted(True)
                if __DEBUG__:
                    print('The corpse %s has expire.' % other.getId())
        Game.CacheCorpses.append(corpse)
        return True

    @staticmethod
    def popCacheCorpses(corpse):
        if Game.CacheCorpses:
            for index, other in enumerate(Game.CacheCorpses):
                if other.getId() == corpse.getId():
                    Game.CacheCorpses.pop(index)
                    return True
        return False

    def shutdown():
        if OS_WINDOWS:
            #os.kill(BOT_PID, signal.CTRL_BREAK_EVENT)
            os.kill(BOT_PID, signal.CTRL_C_EVENT)
        else:
            #os.kill(BOT_PID, signal.SIGINT)
            os.kill(BOT_PID, signal.SIGBREAK)

    def updateLastChatContent(newMsg: str = ""):
        if newMsg:
            Game.LastChatContent.append(newMsg)
        if len(Game.LastChatContent) > 10:
            Game.LastChatContent.pop(0)

    def changeChatContentIndex(direction: bool = True):
        if Game.LastChatContent:
            if direction:
                MenuProperties.MainMenu.chatContent.ChangeValue(Game.LastChatContent[::-1][Game.LastChatIndex])
                Game.LastChatIndex = min(Game.LastChatIndex +1, len(Game.LastChatContent)-1)
            else:
                if Game.LastChatIndex == 0:
                    MenuProperties.MainMenu.chatContent.ChangeValue("")
                    return
                Game.LastChatIndex = max(0, Game.LastChatIndex -1)
                MenuProperties.MainMenu.chatContent.ChangeValue(Game.LastChatContent[::-1][Game.LastChatIndex])

    def getTelemetryMessages():
        return Game.TelemetryMessages

    def addTelemetryMessage(telemetryMessage):
        if not isinstance(telemetryMessage, TelemetryMessage):
            print("[GameBot]: estas intentando introducir a la lista de mensajes de telemetria un objeto que no es de mensaje de telemetria.")
            return
        return Game.TelemetryMessages.append(telemetryMessage)

    def readTelemetryMessages(index=None):
        if not Game.TelemetryMessages:
            return
        if index:
            if index in Game.TelemetryMessages:
                telemetryMessage = Game.TelemetryMessages[index]
                Client.speak(telemetryMessage.getMessage())
                Game.TelemetryMessages.pop(index)
                return
        telemetryMessage = Game.TelemetryMessages[0]
        Client.speak(telemetryMessage.getMessage())
        Game.TelemetryMessages.pop(0)

    def isOpenInventory():
        return Memory.getNumber(ADDRESS_INVENTORY_TOGGLE, ADDRESS_INVENTORY_OFFSETS) == SCREEN_OPTIONS['isOpenInventory']

    def isExistContainerOpened():
        if Game.isOpenInventory():
            Game.toogleInventory()
            time.sleep(0.1)
        return Memory.getNumber(ADDRESS_SPACE_CONTAINER, ADDRESS_SPACE_CONTAINER_OFFSETS) < SCREEN_OPTIONS['isExistContainerOpened']

    def toogleInventory():
        toogleInventory = SCREEN_OPTIONS['toogleInventory']
        Client.fastClickLoot(toogleInventory[0], toogleInventory[1])

    # EXTRAS
    def isWarningPlayerOnScreen():
        return MenuProperties.ExtrasFrame.warningPlayerScreen.IsChecked()

    def isShowNotifications():
        return MenuProperties.ExtrasFrame.showNotifications.IsChecked()

    def isTeleportToTemple():
        return MenuProperties.ExtrasFrame.teleportToTemple.IsChecked()

    # CAVEBOT
    def getAutoLootStatus():
        return MenuProperties.CaveBotFrame.autolootStatus.IsChecked()

    def getCheckWaypoints():
        return MenuProperties.CaveBotFrame.CheckBoxWaypoints.IsChecked()

# oooooooo8 o88                                      o888  
#888        oooo    oooooooo8 oo oooooo    ooooooo    888  
# 888oooooo  888  888    88o   888   888   ooooo888   888  
#        888 888   888oo888o   888   888 888    888   888  
#o88oooo888 o888o 888     888 o888o o888o 88ooo88 8o o888o 
#                  888ooo888                               

if OS_WINDOWS:
    # Function prototype for the handler function. Returns BOOL, takes a DWORD.
    HandlerRoutine = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.DWORD)
    def _ctrl_handler(sig):
        """Handle a sig event and return 0 to terminate the process"""
        if sig == signal.CTRL_C_EVENT:
            return Signal.dispatchSignalHandler(signal.SIGBREAK, None)
        elif sig == signal.CTRL_BREAK_EVENT:
            return Signal.dispatchSignalHandler(signal.SIGINT, None)
        else:
            print("UNKNOWN EVENT")
        return 0
    
    ctrl_handler = HandlerRoutine(_ctrl_handler)
    SetConsoleCtrlHandler = ctypes.windll.kernel32.SetConsoleCtrlHandler
    SetConsoleCtrlHandler.argtypes = (HandlerRoutine, wintypes.BOOL)
    SetConsoleCtrlHandler.restype = wintypes.BOOL

class Signal:

    def startHandler():
        for sig in (signal.SIGBREAK, signal.SIGTERM, signal.SIGINT):
            signal.signal(sig, Signal.dispatchSignalHandler)

    def dispatchSignalHandler(sig: int, frame):
        if sig == signal.SIGBREAK or sig == signal.CTRL_C_EVENT:
            Signal.sigbreakHandler()
            Signal.joinAndClose()
        elif sig == signal.SIGTERM:
            Signal.sigtermHandler()
        elif sig == signal.SIGINT or sig == signal.CTRL_BREAK_EVENT:
            Signal.sigintHandler()
            Signal.joinAndClose()
        return 0

    def sigbreakHandler():
        print("SIGBREAK received, shutting bot service down...")

    def sigtermHandler():
        print("SIGTERM received, shutting bot service down...")

    def sigintHandler():
        print("SIGINT received, shutting bot service down...")

    def joinAndClose():
        """Como no hay ningun proceso que quiera asegurarme que termine con exito antes de salir, entonces omito .join()"""
        g_zed.running = False
        g_yasuo.running = False
        g_k6.running = False
        g_sett.running = False
        PROCESS.close()
        App = wx.GetApp()
        App.ExitMainLoop()

#                               ooooooooooo                                 
#oooo  o  oooo oooo   oooo       888    88 ooooooo    ooooooo    ooooooooo8 
# 888 888 888    888o888         888ooo8   ooooo888 888     888 888oooooo8  
#  888888888     o88 88o         888     888    888 888         888         
#   88   88    o88o   o88o      o888o     88ooo88 8o  88ooo888    88oooo888 

def queueCheckEnclosures(self, q):
    while self.running:
        name = q.get()
        if isinstance(name, str):
            script = Scripts.getScriptByName(name)
            if script:
                Script.update(script)
                q.task_done()
                q.put(name)
        time.sleep(THREAD_MIN_TICKS)

class CreateThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, target=queueCheckEnclosures, args=(self, Scripts.enclosure_queue,))
        self.running = False

class MenuProperties:
    Font = "Operator Mono Light"
    FontSize = 8
    ChooseFrame = None
    AdminMode = False
    MainMenu = None
    ExtrasFrame = None
    HealingFrame = None
    CaveBotMenu = None
    TargetingFrame = None
    ScriptsFrame = None
    """Colours"""
    ScriptOffColour = wx.Colour(48, 55, 46)
    ScriptOnColour = wx.Colour(22, 160, 133)
    ScriptLockedColour = wx.Colour(220, 20, 60)
    """Strings"""
    ScriptRunningText = emoji.emojize(":white_check_mark:", use_aliases=True, variant="emoji_type")
    ScriptPauseText = emoji.emojize(":black_large_square:", use_aliases=True, variant="emoji_type")

#___oooo___oo________________________________________oooo___ooo____oo___________________oo____
#_oo____oo_oo_ooo___ooooo___ooooo___oooo___ooooo___oo____oo__oo_________ooooo__oo_ooo___oo____
#oo________ooo___o_oo___oo_oo___oo_oo___o_oo____o_oo_________oo____oo__oo____o_ooo___o_oooo___
#oo________oo____o_oo___oo_oo___oo___oo___ooooooo_oo_________oo____oo__ooooooo_oo____o__oo____
#_oo____oo_oo____o_oo___oo_oo___oo_o___oo_oo_______oo____oo__oo____oo__oo______oo____o__oo__o_
#___oooo___oo____o__ooooo___ooooo___oooo___ooooo_____oooo___ooooo_oooo__ooooo__oo____o___ooo__
#_____________________________________________________________________________________________

class GuiChooseMenu(wx.Frame):
    def __init__(self, parent):
        toolWindow = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.STAY_ON_TOP
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"%s BOT - Choose Client" % GAME_TITLE, pos=(800, 600), size=(250, 150), style=toolWindow)
        self.SetIcon(parent.icon)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        Panel = wx.Panel(self, wx.ID_ANY)
        Panel.SetFont(wx.Font(MenuProperties.FontSize, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, MenuProperties.Font))
        self.clientList = wx.ListBox(Panel, wx.ID_ANY, (5, 5), (220, 100), [], style=wx.LB_SINGLE|wx.LB_OWNERDRAW)
        self.clientList.Bind(wx.EVT_LISTBOX_DCLICK, self.OnSelectClient)
        self.Show()

    def OnClose(self, event):
        exit()

    def OnSelectClient(self, event):
        global PROCESS
        index = event.GetEventObject().GetSelection()
        for i, p in enumerate(PROCESS):
            if i != index:
                p.close()
        PROCESS = PROCESS[index]
        PROCESS.set_keep_process(True)
        loadProcess()
        Player.CachePlayerID = 0
        Player.CachePlayer = None
        Main.run()
        self.Hide()
        MenuProperties.MainMenu.Show()

#ooo_____ooo_________________________
#oooo___oooo__ooooo__oo_ooo__oo____o_
#oo_oo_oo_oo_oo____o_ooo___o_oo____o_
#oo__ooo__oo_ooooooo_oo____o_oo____o_
#oo_______oo_oo______oo____o_ooo___o_
#oo_______oo__ooooo__oo____o_oo_ooo__
#____________________________________

class GuiMainMenu(wx.Frame):
    def __init__(self):
        toolWindow = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.STAY_ON_TOP
        wx.Frame.__init__(self, None, id=wx.ID_ANY, title=u"%s BOT - Menu" % GAME_TITLE, pos=(800, 600), size=(370, 143), style=toolWindow)
        self.icon = wx.Icon()
        self.icon.CopyFromBitmap(wx.Bitmap("necroxia.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(self.icon)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        Panel = wx.Panel(self, wx.ID_ANY)
        Panel.SetFont(wx.Font(MenuProperties.FontSize, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, MenuProperties.Font))
        ButtonHealing = wx.Button(Panel, wx.ID_ANY, "Healing", (2, 0), (60, 20))
        ButtonHealing.Bind(wx.EVT_BUTTON, self.OnShowHideHealing)
        ButtonExtras = wx.Button(Panel, wx.ID_ANY, "Extras", (2, 20), (60, 20))
        ButtonExtras.Bind(wx.EVT_BUTTON, self.OnShowHideExtras)
        ButtonCaveBot = wx.Button(Panel, wx.ID_ANY, "CaveBot", (2, 40), (60, 20))
        ButtonCaveBot.Bind(wx.EVT_BUTTON, self.OnShowHideCaveBot)
        ButtonTargeting = wx.Button(Panel, wx.ID_ANY, "Targeting", (2, 60), (60, 20))
        ButtonTargeting.Bind(wx.EVT_BUTTON, self.OnShowHideTargeting)
        ButtonScripts = wx.Button(Panel, wx.ID_ANY, "Scripts", (62, 0), (60, 20))
        ButtonScripts.Bind(wx.EVT_BUTTON, self.OnShowHideScripts)
        ButtonCommands = wx.Button(Panel, wx.ID_ANY, "Cmd's", (62, 20), (60, 20))
        ButtonScreenshot = wx.Button(Panel, wx.ID_ANY, "Capture", (62, 40), (60, 20))
        ButtonScreenshot.Bind(wx.EVT_BUTTON, self.OnScreenshot)
        ButtonCreatures = wx.Button(Panel, wx.ID_ANY, "Creatures", (62, 60), (60, 20))
        ButtonAimbot = wx.Button(Panel, wx.ID_ANY, "Aimbot", (122, 0), (60, 20))
        ButtonLoad = wx.Button(Panel, wx.ID_ANY, "Load", (122, 20), (60, 20))
        ButtonLoad.Bind(wx.EVT_BUTTON, self.OnLoad)
        ButtonSave = wx.Button(Panel, wx.ID_ANY, "Save", (122, 40), (60, 20))
        ButtonSave.Bind(wx.EVT_BUTTON, self.OnSave)
        ButtonReload = wx.Button(Panel, wx.ID_ANY, "Hide", (122, 60), (60, 20))
        ButtonReload.Bind(wx.EVT_BUTTON, self.OnToggle)
        wx.StaticBox(Panel, wx.ID_ANY, "Small info of your player", (182, 0), (170, 80))
        self.playerName = wx.StaticText(Panel, wx.ID_ANY, "Name: Unknow", (192, 19), (60, 10))
        self.playerStatus = wx.StaticText(Panel, wx.ID_ANY, "Status:", (192, 34), (40, 10))

        self.timeLeft = wx.StaticText(Panel, wx.ID_ANY, "Time Left:", (192, 50), (70, 10))
        self.expPerHour = wx.StaticText(Panel, wx.ID_ANY, "Exp/Hour:", (192, 62), (50, 10))
        
        ButtonConsole = wx.Button(Panel, wx.ID_ANY, "[#]", (2, 82), (30, 20))
        ButtonConsole.Bind(wx.EVT_BUTTON, self.OnAdminToggle)
        self.chatContent = wx.TextCtrl(Panel, size=(290,18), pos=(32, 83), style=wx.TE_PROCESS_ENTER)
        self.chatContent.SetMaxLength(255)
        self.chatContent.HideNativeCaret()
        self.chatContent.Bind(wx.EVT_TEXT_ENTER, self.OnChatSend)
        self.chatContent.Bind(wx.EVT_CHAR, self.OnChatChar)
        ButtonConsole.Bind(wx.EVT_BUTTON, self.OnAdminToggle)
        ButtonSend = wx.Button(Panel, wx.ID_ANY, "[S]", (322, 82), (30, 20))
        ButtonSend.Bind(wx.EVT_BUTTON, self.OnChatSend)
        #ButtonSend.Bind(wx.TE_PROCESS_ENTER, self.OnChatSend)
        self.logConsole = wx.TextCtrl(Panel, size=(350,94), pos=(2, 104), style=wx.TE_READONLY|wx.TE_MULTILINE)
        #Button.Bind(wx.EVT_BUTTON, onButton)
        
        # Create Sub Frames
        MenuProperties.HealingFrame = GuiHealingMenu(self)
        MenuProperties.ExtrasFrame = GuiExtrasMenu(self)
        MenuProperties.CaveBotFrame = GuiCaveBotMenu(self)
        MenuProperties.TargetingFrame = GuiTargetingMenu(self)
        MenuProperties.ScriptsFrame = GuiScriptsMenu(self)
        # Mostrar el menu principal
        self.Show()
        MenuProperties.MainMenu = self

    def OnLoad(self, event):
        player = Game.getPlayerClient()
        if player:
            DataBot.LoadHealingMiscellaneousToFile(player.getName())

    def OnSave(self, event):
        player = Game.getPlayerClient()
        if player:
            DataBot.SaveHealingMiscellaneousToFile(player.getName())

    def OnToggle(self, event=None):
        if self.IsShown():
            self.Hide()
        else:
            self.Show()

    def OnClose(self, event):
        """Send SIGBREAK for kill process"""
        Game.shutdown()
    
    def OnScreenshot(self, event):
        player = Game.getPlayerClient()
        localtime = time.localtime(time.time())
        ltformated = "%d%d%s%d%d%d" % (localtime.tm_mday, localtime.tm_mon, localtime.tm_year, localtime.tm_hour, localtime.tm_min, localtime.tm_sec)
        Client.screenshot("%s-%s" % (player and player.getName() or "default", ltformated))
    
    def OnChatSend(self, event):
        content = self.chatContent.GetValue()
        if content:
            Player.setChatContent(content)
            Client.pressEnter()
            self.chatContent.SetValue("")
            Game.updateLastChatContent(content)

    def OnChatChar(self, event):
        keyCode = event.GetKeyCode()
        if keyCode == 315: # Button Up
            Game.changeChatContentIndex(True)
        elif keyCode == 317: # Button Down
            Game.changeChatContentIndex(False)
        event.Skip()

    def OnAdminToggle(self, event):
        MenuProperties.AdminMode = not MenuProperties.AdminMode
        if MenuProperties.AdminMode:
            self.SetSize(width=370, height=243)
        else:
            self.SetSize(width=370, height=143)

    def OnShowHideHealing(self, event):
        if MenuProperties.HealingFrame.IsShown():
            MenuProperties.HealingFrame.Hide()
        else:
            MenuProperties.HealingFrame.Show()

    def OnShowHideExtras(self, event):
        if MenuProperties.ExtrasFrame.IsShown():
            MenuProperties.ExtrasFrame.Hide()
        else:
            MenuProperties.ExtrasFrame.Show()

    def OnShowHideCaveBot(self, event):
        if MenuProperties.CaveBotFrame.IsShown():
            MenuProperties.CaveBotFrame.Hide()
        else:
            MenuProperties.CaveBotFrame.Show()

    def OnShowHideTargeting(self, event):
        if MenuProperties.TargetingFrame.IsShown():
            MenuProperties.TargetingFrame.Hide()
        else:
            MenuProperties.TargetingFrame.Show()

    def OnShowHideScripts(self, event):
        if MenuProperties.ScriptsFrame.IsShown():
            MenuProperties.ScriptsFrame.Hide()
        else:
            MenuProperties.ScriptsFrame.Show()

    def UpdatePlayerName(self, player):
        if player:
            self.playerName.SetLabel("Name: %s" % player.getName())

    def UpdatePlayerStatus(self):
        self.playerStatus.SetLabel("Status: %s" % (Player.isConnected() and "Connected." or "Disconnected"))

    def UpdateTimeLeft(self, timeList):
        self.timeLeft.SetLabel("Time Left: %dH:%dM:%dS" % timeList)

    def UpdateExpPerHour(self, expPerHour):
        self.expPerHour.SetLabel("Exp/Hour: %d" % expPerHour)

"""Tabla de posiciones relativas para el emplacement"""
EMPLACEMENT_OFFSETS = {
    "Center": Position(0, 0, 0),
    "North": Position(0, -1, 0),
    "East": Position(1, 0, 0),
    "South": Position(0, 1, 0),
    "West": Position(-1, 0, 0),
    "North-West": Position(-1, -1, 0),
    "North-East": Position(1, -1, 0),
    "South-East": Position(1, 1, 0),
    "Sout-West": Position(-1, 1, 0)
}

GAME_WAIT_ACTION = 1.5
GAME_AUTOLOOT_WAITING = 3000000000 # nanosegundos
GAME_AUTOLOOT_SPEED = 0.5 # seconds
GAME_AUTOLOOT_SPEED_LIST =  {
    "Fast": 0.5,
    "Normal": 0.7,
    "Slow": 1.0,
    "Very-Slow": 1.5
}

#___oooo___________________________ooooooo___________oo____
#_oo____oo__ooooo__oo____o__ooooo__oo____oo__ooooo___oo____
#oo________oo___oo_oo____o_oo____o_oooooooo_oo___oo_oooo___
#oo________oo___oo_oo___o__ooooooo_oo____oo_oo___oo__oo____
#_oo____oo_oo___oo__oo_o___oo______oo____oo_oo___oo__oo__o_
#___oooo____oooo_o___oo_____ooooo__ooooooo___ooooo____ooo__
#__________________________________________________________

class GuiCaveBotMenu(wx.Frame):
    def __init__(self, parent):
        toolWindow = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.STAY_ON_TOP | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"%s BOT - CaveBot" % GAME_TITLE, pos=(383, 159), size=(615, 445), style=toolWindow)
        self.SetIcon(parent.icon)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        Panel = wx.Panel(self, wx.ID_ANY)
        Panel.SetFont(wx.Font(MenuProperties.FontSize, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, MenuProperties.Font))
        wx.StaticBox(Panel, wx.ID_ANY, "Waypoints", (2, 0), (390, 270))
        wx.StaticBox(Panel, wx.ID_ANY, "CaveBot Hotkeys", (401, 0), (190, 50))
        # Looting
        wx.StaticBox(Panel, wx.ID_ANY, "Looting", (402, 49), (190, 220))
        self.LootingList = wx.ListBox(Panel, wx.ID_ANY, (410, 65), (173, 165), [], wx.LB_SINGLE)
        self.LootItemId =  wx.TextCtrl(Panel, wx.ID_ANY, "0", (410, 240), (75, 20))
        self.LootItemId.Bind(wx.EVT_CHAR, self.OnTextLootItemId)
        ButtonAddLoot = wx.Button(Panel, wx.ID_ANY, "Add", (485, 239), (50, 22))
        ButtonAddLoot.Bind(wx.EVT_BUTTON, self.OnAddItemId)
        ButtonRemLoot = wx.Button(Panel, wx.ID_ANY, "Remove", (535, 239), (50, 22))
        ButtonRemLoot.Bind(wx.EVT_BUTTON, self.OnRemItemId)
        wx.StaticBox(Panel, wx.ID_ANY, "Alerts", (212, 269), (180, 130))
        wx.StaticBox(Panel, wx.ID_ANY, "Options", (402, 269), (190, 80))
        self.autolootLocked = wx.CheckBox(Panel, wx.ID_ANY, "Maintain the list of items.", (407, 279), (180, 20))
        self.autolootStatus = wx.CheckBox(Panel, wx.ID_ANY, "Enable item looting.", (407, 299), (180, 20))
        wx.StaticText(Panel, wx.ID_ANY, "Lotting Speed:", (407, 319), (60, 25))
        self.autolootSpeed = wx.ComboBox(Panel, wx.ID_ANY, "Normal", (467, 319), (90, 20), choices=["Fast", "Normal", "Slow", "Very-Slow"], style=wx.CB_SIMPLE|wx.CB_READONLY&~wx.CB_DROPDOWN)
        self.autolootSpeed.Bind(wx.EVT_COMBOBOX, self.OnAutoLootSpeed)
        self.WaypointList = wx.ListBox(Panel, wx.ID_ANY, (12, 19), (180, 220), [], style=wx.LB_SINGLE|wx.LB_OWNERDRAW)
        self.WaypointList.Bind(wx.EVT_LISTBOX_DCLICK, self.OnWaypointCursor)
        #self.WaypointList.Bind(wx.EVT_MOTION, self.OnWaypointMotion)
        ButtonDelete = wx.Button(Panel, wx.ID_ANY, "Del", (142, 244), (50, 20))
        ButtonDelete.SetToolTip(wx.ToolTip("Eliminar el punto de referencia seleccionado."))
        ButtonDelete.Bind(wx.EVT_BUTTON, self.OnDelete)
        ButtonLabel = wx.Button(Panel, wx.ID_ANY, "Label", (72, 244), (60, 20))
        ButtonLabel.SetToolTip(wx.ToolTip("Agregar un comentario a lista."))
        ButtonClear = wx.Button(Panel, wx.ID_ANY, "Clear", (12, 244), (50, 20))
        ButtonClear.SetToolTip(wx.ToolTip("Limpiar la lista de puntos de referencias."))
        ButtonClear.Bind(wx.EVT_BUTTON, self.OnClear)
        wx.StaticText(Panel, wx.ID_ANY, "Emplacement", (202, 21), (70, 20))
        self.emplacement = wx.ComboBox(Panel, wx.ID_ANY, "Center", (275, 19), (90, 20), choices=["Center", "North", "East", "South", "West", "North-West", "North-East", "South-East", "South-West"], style=wx.CB_SIMPLE|wx.CB_READONLY&~wx.CB_DROPDOWN)
        self.emplacement.SetToolTip(wx.ToolTip("Movimiento relativo para los puntos de referencia."))
        ButtonStand = wx.Button(Panel, wx.ID_ANY, "Stand", (212, 49), (40, 20))
        ButtonStand.SetToolTip(wx.ToolTip("Punto de referencia standar."))
        ButtonStand.Bind(wx.EVT_BUTTON, self.OnStand)
        ButtonNode = wx.Button(Panel, wx.ID_ANY, "Node", (252, 49), (40, 20))
        ButtonNode.SetToolTip(wx.ToolTip("Punto de referencia para establecer un nodo."))
        ButtonNode.Bind(wx.EVT_BUTTON, self.OnNode)
        ButtonWalk = wx.Button(Panel, wx.ID_ANY, "Walk", (292, 49), (40, 20))
        ButtonWalk.SetToolTip(wx.ToolTip("Punto de referencia para caminar."))
        ButtonAction = wx.Button(Panel, wx.ID_ANY, "Action", (332, 49), (40, 20))
        ButtonAction.SetToolTip(wx.ToolTip("Punto de referencia para establecer una acción."))
        ButtonAction.Bind(wx.EVT_BUTTON, self.OnAction)
        ButtonRope = wx.Button(Panel, wx.ID_ANY, "Rope", (212, 69), (40, 20))
        ButtonRope.SetToolTip(wx.ToolTip("Punto de referencia para usar una cuerda."))
        ButtonLadder = wx.Button(Panel, wx.ID_ANY, "Ladder", (252, 69), (40, 20))
        ButtonLadder.SetToolTip(wx.ToolTip("Punto de referencia para subir una ladera."))
        ButtonShovel = wx.Button(Panel, wx.ID_ANY, "Shovel", (292, 69), (40, 20))
        ButtonShovel.SetToolTip(wx.ToolTip("Punto de referencia para usar una pala."))
        ButtonLure = wx.Button(Panel, wx.ID_ANY, "Lure", (332, 69), (40, 20))
        ButtonLure.SetToolTip(wx.ToolTip("Punto de referencia para lurear monstruos."))
        self.buttonRecPath = wx.Button(Panel, wx.ID_ANY, emoji.emojize(":movie_camera: Rec", use_aliases=True, variant="emoji_type"), (196, 99), (60, 20))
        self.buttonRecPath.SetToolTip(wx.ToolTip("Iniciar grabacion de camino."))
        self.buttonRecPath.Bind(wx.EVT_BUTTON, self.OnRec)
        ButtonBuyPots = wx.Button(Panel, wx.ID_ANY, emoji.emojize(":baby_bottle: Pot", use_aliases=True, variant="emoji_type"), (196, 120), (60, 20))
        ButtonBuyPots.SetToolTip(wx.ToolTip("Punto de referencia para cargar potions."))
        ButtonBuyPots.Bind(wx.EVT_BUTTON, self.OnBuyPots)
        self.buttonReversePath = wx.Button(Panel, wx.ID_ANY, emoji.emojize(":repeat_one: Rev", use_aliases=True, variant="emoji_type"), (196, 140), (60, 20))
        self.buttonReversePath.SetToolTip(wx.ToolTip("Agregar el camino en reversa."))
        self.buttonReversePath.Bind(wx.EVT_BUTTON, self.OnReversePath)
        self.extraScript = wx.TextCtrl(Panel, wx.ID_ANY, "", (260, 99), (125, 140), style=wx.TE_MULTILINE|wx.TE_NO_VSCROLL)
        self.buttonNextWays = wx.Button(Panel, wx.ID_ANY, emoji.emojize(":curly_loop: Next", use_aliases=True, variant="emoji_type"), (196, 161), (60, 20))
        self.buttonNextWays.SetToolTip(wx.ToolTip("Siguiente lista de waypoints."))
        self.buttonNextWays.Bind(wx.EVT_BUTTON, self.OnNext)
        CheckBoxLabel = wx.CheckBox(Panel, wx.ID_ANY, "labels", (202, 244), (80, 20))
        CheckBoxLabel.SetToolTip(wx.ToolTip("Seguir puntos de referencia que tengan comentarios."))
        self.CheckBoxWaypoints = wx.CheckBox(Panel, wx.ID_ANY, emoji.emojize(":running:waypoints", use_aliases=True, variant="emoji_type"), (282, 244), (100, 20))
        self.CheckBoxWaypoints.SetToolTip(wx.ToolTip("Seguir todos los puntos de referencia.\nLa distancia maxima de un punto a otro es de 30 SQM"))
        self.CheckBoxWaypoints.Bind(wx.EVT_CHECKBOX, self.OnFollowWaypoints)
        # Save And Load Settings
        wx.StaticBox(Panel, wx.ID_ANY, "Saving & Loading settings", (2, 269), (200, 130))
        self.fileSelected = wx.ListBox(Panel, wx.ID_ANY, (12, 289), (180, 60), self.GetFiles(), wx.LB_SINGLE)
        self.fileSelected.Bind(wx.EVT_LISTBOX, self.OnFileSelected)
        wx.StaticText(Panel, wx.ID_ANY, "Name:", (12, 355), (30, 20))
        self.fileName =  wx.TextCtrl(Panel, wx.ID_ANY, "default", (52, 352), (140, 20))
        self.fileName.SetToolTip(wx.ToolTip("Escribe el nombre del archivo para guardar."))
        ButtonEdit = wx.Button(Panel, wx.ID_ANY, "Edit", (12, 375), (60, 20))
        ButtonEdit.SetToolTip(wx.ToolTip("Sobrescribe el archivo seleccionado."))
        ButtonEdit.Bind(wx.EVT_BUTTON, self.OnEdit)
        ButtonSave = wx.Button(Panel, wx.ID_ANY, "Save", (72, 375), (60, 20))
        ButtonSave.SetToolTip(wx.ToolTip("Guardar un nuevo archivo."))
        ButtonSave.Bind(wx.EVT_BUTTON, self.OnSave)
        ButtonLoad = wx.Button(Panel, wx.ID_ANY, "Load", (132, 375), (60, 20))
        ButtonLoad.SetToolTip(wx.ToolTip("Cargar el archivo seleccionado."))
        ButtonLoad.Bind(wx.EVT_BUTTON, self.OnLoad)
        MenuProperties.CaveBotMenu = self

    def OnClose(self, event):
        return MenuProperties.MainMenu.OnShowHideCaveBot(event)

    def OnFileSelected(self, event):
        selection = self.fileSelected.GetSelection()
        if selection != wx.NOT_FOUND:
            fileName = self.fileSelected.GetString(selection)
            if fileName:
                self.fileName.ChangeValue(fileName)
    
    def OnEdit(self, event):
        selection = self.fileSelected.GetSelection()
        if selection != wx.NOT_FOUND:
            fileName = self.fileSelected.GetString(selection)
            if fileName:
                return DataBot.SaveCaveBotToFile(fileName)

    def OnSave(self, event):
        fileName = self.fileName.GetValue()
        if fileName:
            return DataBot.SaveCaveBotToFile(fileName)
        selection = self.fileSelected.GetSelection()
        if selection != wx.NOT_FOUND:
            fileName = self.fileSelected.GetString(selection)
            return DataBot.SaveCaveBotToFile(fileName)
    
    def OnLoad(self, event):
        selection = self.fileSelected.GetSelection()
        if selection != wx.NOT_FOUND:
            fileName = self.fileSelected.GetString(selection)
            return DataBot.LoadCaveBotFromFile(fileName)

    def OnAutoLootSpeed(self, event):
        GAME_AUTOLOOT_SPEED = GAME_AUTOLOOT_SPEED_LIST[event.GetEventObject().GetValue()]

    def GetEmplacementPos(self):
        return EMPLACEMENT_OFFSETS[self.emplacement.GetValue()]
            
    def OnStand(self, event):
        if not Game.RecWaypoints:
            player = Game.getPlayerClient()
            if player:
                Waypoints.waypoints.append(Waypoint(player.getPosition()+self.GetEmplacementPos()))
                self.OrderWaypoints()
                self.CleanReverseBack()
                self.WaypointList.EnsureVisible(len(Waypoints.waypoints) -1)
        elif __DEBUG__:
            print("[CaveBot/Waypoints]: no puedes establecer waypoint stand con la capturadora activada.")

    def OnBuyPots(self, event):
        if not Game.RecWaypoints:
            player = Game.getPlayerClient()
            if player:
                selection = self.WaypointList.GetSelection()
                if selection == wx.NOT_FOUND:
                    waypoint = Waypoint(player.getPosition()+self.GetEmplacementPos(), type=WAYPOINT_TYPE_BUYPOT)
                    Waypoints.waypoints.append(waypoint)
                else:
                    waypoint = Waypoints.waypoints[selection]
                    waypoint.type = WAYPOINT_TYPE_BUYPOT
                    waypoint.updateColour()
                self.OrderWaypoints()
                self.CleanReverseBack()
        elif __DEBUG__:
            print("[CaveBot/Waypoints]: no puedes establecer waypoint pots con la capturadora activada.")

    def OnNode(self, event):
        player = Game.getPlayerClient()
        if not player or not self.WaypointList:
            return
        selection = self.WaypointList.GetSelection()
        waypoint = selection == wx.NOT_FOUND and Waypoints.getCurrentWaypoint() or Waypoints.waypoints[selection]
        if waypoint.isStand():
            waypoint.setType(WAYPOINT_TYPE_NODE)
            waypoint.updateColour()
        waypoint.setNodePos(player.getPosition())
        self.UpdateWaypoint(waypoint, selection)
        self.CleanReverseBack()

    def OnAction(self, event):
        selection = self.WaypointList.GetSelection()
        if selection != wx.NOT_FOUND:
            waypoint = Waypoints.getWaypoints()[selection]
            strCode = self.extraScript.GetValue()
            # GET POSITION #
            it = luaString_gmatch(strCode, "%s?([xyzXYZ]?%d+)")
            position = Position()
            rit = it()
            while rit:
                if rit.isdigit():
                    position.ups.append(int(rit))
                elif rit[0].lower() == 'x':
                    position.x = int(rit[1:])
                elif rit[0].lower() == 'y':
                    position.y = int(rit[1:])
                elif rit[0].lower() == 'z':
                    position.z = int(rit[1:])
                rit = it()
            position.update()
            # END GET POSITION #
            # GET REPEAT ACTION #
            repeat = luaString_match(strCode, "repeat (%d+)") or 1
            # END REPEAT ACTION #
            waypoint.setAction(WaypointAction(WaypointAction.TYPE_USEITEMONXYZ, position, int(repeat)))
            self.UpdateWaypoint(waypoint, selection)

    def OnRec(self, event):
        if not Game.getCheckWaypoints():
            Game.RecWaypoints = not Game.RecWaypoints
            Waypoints.lastPositionRec = None
            event.GetEventObject().SetForegroundColour(Game.RecWaypoints and wx.RED or wx.NullColour)
        elif __DEBUG__:
            print("[CaveBot/Waypoints]: no puedes iniciar la captura con el check waypoints activado.")

    def OnFollowWaypoints(self, event):
        if Game.RecWaypoints:
            event.GetEventObject().SetValue(False)
            if __DEBUG__:
                print("[CaveBot/Waypoints]: no puedes iniciar el follow waypoints con la capturadora activada.")
            return

    def OrderWaypoints(self):
        posStrList = []
        wchecks = []
        for index, w in enumerate(Waypoints.getWaypoints()):
            beforeWaypoint = (index == 0 and Waypoints.waypoints[-1] or Waypoints.waypoints[index-1])
            posStrList.append(w.getInfo(beforeWaypoint, Waypoints.currentWaypoint == index))
            wchecks.append({'w': w, 's': index})
        self.WaypointList.Set(posStrList)
        for info in wchecks:
            color = info['w'].getColour()
            if color:
                self.WaypointList.SetItemBackgroundColour(info['s'], color)

    def AddWaypointOrder(self, waypoint):
        index = self.WaypointList.GetCount()
        wlen = len(Waypoints.waypoints)
        beforeWaypoint = (wlen > 0 and Waypoints.waypoints[-1] or None)
        posStrList = [waypoint.getInfo(beforeWaypoint, index == 0)]
        self.WaypointList.InsertItems(posStrList, index)
        Waypoints.waypoints.append(waypoint)
        if wlen+1 > 2:
            self.UpdateWaypoint(Waypoints.waypoints[0], 0)

    def UpdateWaypoint(self, waypoint, selection):
        beforeWaypoint = (selection == 0 and Waypoints.waypoints[-1] or Waypoints.waypoints[selection-1])
        self.WaypointList.SetString(selection, waypoint.getInfo(beforeWaypoint, Waypoints.currentWaypoint == selection))
        color = waypoint.getColour()
        if color:
            self.WaypointList.SetItemBackgroundColour(selection, color)

    def UpdateWaypointTwo(self, w1, s1, w2, s2):
        self.UpdateWaypoint(w1, s1)
        self.UpdateWaypoint(w2, s2)
        self.WaypointList.EnsureVisible(s2)

    def OnDelete(self, event):
        index = self.WaypointList.GetSelection()
        if index != wx.NOT_FOUND:
            Waypoints.waypoints.pop(index)
            self.OrderWaypoints()
            self.CleanReverseBack()
        elif Waypoints.waypoints:
            Waypoints.waypoints.pop(-1)
            self.OrderWaypoints()
            self.CleanReverseBack()

    def OnClear(self, event):
        Waypoints.waypoints.clear()
        self.WaypointList.Set([])
        self.CleanReverseBack()

    def OnReversePath(self, event):
        if not Game.RecWaypoints:
            color = wx.NullColour
            if len(Waypoints.waypoints) > 2:
                if not Waypoints.reverseAdded:
                    Waypoints.reverseAdded = Waypoints.waypoints[1:-1][::-1]
                    Waypoints.waypoints += Waypoints.reverseAdded
                    color = wx.Colour(52, 152, 219)
                else:
                    Waypoints.waypoints = Waypoints.waypoints[:-len(Waypoints.reverseAdded)]
                    Waypoints.reverseAdded = []
                self.OrderWaypoints()
            else:
                Waypoints.reverseAdded = []
            event.GetEventObject().SetForegroundColour(color)
        elif __DEBUG__:
            print("[CaveBot/Waypoints]: no puedes crear el camino de regreso con la capturadora activada.")

    def CleanReverseBack(self):
        self.buttonReversePath.SetForegroundColour(wx.NullColour)
        Waypoints.reverseAdded = []

    def OnNext(self, event):
        filename = self.extraScript.GetValue()
        if not filename:
            if __DEBUG__:
                print("[CaveBot]: el archivo 'data/cavebot/%s.txt' no existe." % filename)
            return
        selection = self.WaypointList.GetSelection()
        if selection == wx.NOT_FOUND:
            if __DEBUG__:
                print("[CaveBot]: no has seleccionado ningun 'waypoint' de la lista.")
            return
        waypoint = Waypoints.getWaypoints()[selection]
        waypoint.next_ways = self.extraScript.GetValue()
        waypoint.type = WAYPOINT_TYPE_NEXT
        waypoint.updateColour()
        self.UpdateWaypoint(waypoint, selection)

    def OnWaypointCursor(self, event):
        beforeWaypoint = Waypoints.getCurrentWaypoint()
        beforeIndex = Waypoints.currentWaypoint
        Waypoints.currentWaypoint = event.GetSelection()
        waypoint = Waypoints.getWaypoints()[Waypoints.currentWaypoint]
        self.UpdateWaypoint(beforeWaypoint, beforeIndex)
        self.UpdateWaypoint(waypoint, Waypoints.currentWaypoint)

    def OnWaypointMotion(self, event):
        seeIndex = self.WaypointList.HitTest(event.GetPosition())
        if seeIndex != wx.NOT_FOUND:
            waypoint = Waypoints.waypoints[seeIndex]
            nodePos = waypoint.getNodePos()
            if nodePos:
                self.WaypointList.SetToolTip(wx.ToolTip("<TEST>"))

    def OnTextLootItemId(self, event):
        value = self.LootItemId.GetValue()
        keyCode = event.GetKeyCode()
        if keyCode in [8, 314, 316] or (len(value) < 5 and keyCode >= 48 and keyCode <= 57):
            event.Skip()
            return
        return False

    def OrderLooting(self):
        posStrList = []
        for index, itemId in enumerate(Looting.getItems()):
            posStrList.append("ID: %d - %s" % (itemId, 'Unknow'))
        self.LootingList.Set(posStrList)

    def OnAddItemId(self, event):
        value = self.LootItemId.GetValue()
        if not value:
            return
        itemId = int(value)
        if itemId > 99 and Looting.addItem(itemId):
            print("ItemId %d add to list." % itemId)
            self.OrderLooting()

    def OnRemItemId(self, event):
        selection = self.LootingList.GetSelection()
        if selection != wx.NOT_FOUND:
            value = self.LootingList.GetString(selection)
            if not value:
                return
            gmatch = re.compile(r'\d{1,5}').search(value)
            itemId = int(gmatch.group())
            if itemId > 99 and Looting.removeItem(itemId):
                print("ItemId %d rem to list." % itemId)
                self.OrderLooting()

    def GetFiles(self):
        files = []
        for file in os.listdir("data/cavebot"):
            result = file.split(".txt")
            if len(result) == 2:
                files.append(result[0])
        return files

#oooooooo__________________________________oo_____oo__________________
#___oo_____ooooo__oo_ooo___oooo____ooooo___oo_________oo_ooo___oooo___
#___oo____oo___oo_ooo___o_oo__oo__oo____o_oooo____oo__ooo___o_oo__oo__
#___oo____oo___oo_oo______oo___o__ooooooo__oo_____oo__oo____o_oo___o__
#___oo____oo___oo_oo_______oooooo_oo_______oo__o__oo__oo____o__oooooo_
#___oo_____oooo_o_oo______o____oo__ooooo____ooo__oooo_oo____o_o____oo_
#__________________________ooooo_______________________________ooooo__

class GuiTargetingMenu(wx.Frame):
    def __init__(self, parent):
        toolWindow = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.STAY_ON_TOP | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"%s BOT - Targeting" % GAME_TITLE, pos=(383, 159), size=(591, 447), style=toolWindow)
        self.SetIcon(parent.icon)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        Panel = wx.Panel(self, wx.ID_ANY)
        Panel.SetFont(wx.Font(MenuProperties.FontSize, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, MenuProperties.Font))
        wx.StaticBox(Panel, wx.ID_ANY, "Targeting", (2, 2), (572, 225))
        wx.StaticBox(Panel, wx.ID_ANY, "Stance Options", (2, 229), (180, 180))
        wx.StaticBox(Panel, wx.ID_ANY, "Monster filter", (402, 229), (170, 180))
        self.monsterList = wx.ListBox(Panel, wx.ID_ANY, (182, 20), (210, 180), [], wx.LB_SINGLE)
        self.monsterList.Bind(wx.EVT_LISTBOX, self.OnChangeSelectionMlist)
        wx.StaticText(Panel, wx.ID_ANY, "Creature Name", (12, 20), (120, 12))
        self.MonsterName =  wx.TextCtrl(Panel, wx.ID_ANY, "", (12, 34), (160, 20))
        self.MonsterName.SetToolTip(wx.ToolTip("Nombre del monstruo\nEjemplo: Rotworm"))
        wx.StaticText(Panel, wx.ID_ANY, "Single", (12, 60), (60, 12))
        self.MonsterSingleSpell =  wx.TextCtrl(Panel, wx.ID_ANY, "F3", (12, 74), (70, 20), style=wx.TE_CENTRE)
        self.MonsterSingleSpell.Bind(wx.EVT_TEXT, self.OnChangeSingleSpell)
        self.MonsterSingleSpell.SetToolTip(wx.ToolTip("Single Spell Hotkey!"))
        wx.StaticText(Panel, wx.ID_ANY, "Expansive", (102, 60), (60, 12))
        self.MonsterPluralSpell =  wx.TextCtrl(Panel, wx.ID_ANY, "F4", (102, 74), (70, 20), style=wx.TE_CENTRE)
        self.MonsterPluralSpell.Bind(wx.EVT_TEXT, self.OnChangePluralSpell)
        self.MonsterPluralSpell.SetToolTip(wx.ToolTip("Expansive Spell Hotkey!"))
        AddMonster = wx.Button(Panel, wx.ID_ANY, "Add", (272, 203), (60, 20))
        AddMonster.Bind(wx.EVT_BUTTON, self.OnAddMonster)
        AddMonster.SetToolTip(wx.ToolTip("Añadir el monstruo presiseñado."))
        DelMonster = wx.Button(Panel, wx.ID_ANY, "Del", (332, 203), (60, 20))
        DelMonster.Bind(wx.EVT_BUTTON, self.OnDeleteMonster)
        DelMonster.SetToolTip(wx.ToolTip("Eliminar el monstruo seleccionado."))
        wx.StaticText(Panel, wx.ID_ANY, "Action", (12, 100), (60, 12))
        self.monsterAction = wx.ComboBox(Panel, wx.ID_ANY, 'No Action', (12, 114), (160, 21), choices=['No Action', 'Attack', 'Follow'], style=wx.CB_SIMPLE|wx.CB_READONLY&~wx.CB_DROPDOWN)
        wx.StaticText(Panel, wx.ID_ANY, "Count", (402, 94), (80, 15))
        self.monsterCount = wx.ComboBox(Panel, wx.ID_ANY, 'Any', (402, 109), (160, 21), choices=['Any', '1', '1+', '2', '2+', '3', '3+', '4', '4+', '5', '5+', '6', '6+', '7', '7+'], style=wx.CB_SIMPLE|wx.CB_READONLY&~wx.CB_DROPDOWN)
        wx.StaticText(Panel, wx.ID_ANY, "Range distance:", (12, 255), (90, 20))
        rangeSelected = wx.ComboBox(Panel, wx.ID_ANY, '2', (122, 249), (50, 21), choices=['2', '3', '4', '5', '6', '7'], style=wx.CB_SIMPLE|wx.CB_READONLY&~wx.CB_DROPDOWN)
        wx.StaticBox(Panel, wx.ID_ANY, "Saving && Loading settings", (192, 229), (200, 180))
        self.CheckBoxRunTarget = wx.CheckBox(Panel, wx.ID_ANY, "Run Targeting", (12, 379), (140, 20))
        self.fileSelected = wx.ListBox(Panel, wx.ID_ANY, (202, 249), (180, 100), self.GetFiles(), wx.LB_SINGLE)
        self.fileSelected.Bind(wx.EVT_LISTBOX, self.OnFileSelected)
        wx.StaticText(Panel, wx.ID_ANY, "Name", (203, 358), (50, 15))
        self.fileName =  wx.TextCtrl(Panel, wx.ID_ANY, "", (262, 354), (120, 20))
        ButtonEdit = wx.Button(Panel, wx.ID_ANY, "Edit", (202, 379), (60, 20))
        ButtonEdit.Bind(wx.EVT_BUTTON, self.OnEdit)
        ButtonSave = wx.Button(Panel, wx.ID_ANY, "Save", (262, 379), (60, 20))
        ButtonSave.Bind(wx.EVT_BUTTON, self.OnSave)
        ButtonLoad = wx.Button(Panel, wx.ID_ANY, "Load", (322, 379), (60, 20))
        ButtonLoad.Bind(wx.EVT_BUTTON, self.OnLoad)

    def OnChangeSingleSpell(self, event):
        self.MonsterSingleSpell.ChangeValue(self.MonsterSingleSpell.GetValue().upper())
        self.MonsterSingleSpell.SetInsertionPointEnd()
    
    def OnChangePluralSpell(self, event):
        self.MonsterPluralSpell.ChangeValue(self.MonsterPluralSpell.GetValue().upper())
        self.MonsterPluralSpell.SetInsertionPointEnd()

    def OnClose(self, event):
        return MenuProperties.MainMenu.OnShowHideTargeting(event)

    def OnFileSelected(self, event):
        selection = self.fileSelected.GetSelection()
        if selection != wx.NOT_FOUND:
            fileName = self.fileSelected.GetString(selection)
            if fileName:
                self.fileName.ChangeValue(fileName)

    def OnEdit(self, event):
        index = self.fileSelected.GetSelection()
        if index != wx.NOT_FOUND:
            fileName = self.fileSelected.GetString(index)
            if fileName:
                if __DEBUG__:
                    print("Targeting %s edit..." % fileName)
                return DataBot.SaveTargetingToFile(fileName)

    def OnSave(self, event):
        fileName = self.fileName.GetValue()
        if fileName:
            if __DEBUG__:
                print("Targeting %s save..." % fileName)
            return DataBot.SaveTargetingToFile(fileName)
        else:
            index = self.fileSelected.GetSelection()
            if index != wx.NOT_FOUND:
                fileName = self.fileSelected.GetString(index)
                if fileName:
                    if __DEBUG__:
                        print("Targeting %s save..." % fileName)
                    return DataBot.SaveTargetingToFile(fileName)
    
    def OnLoad(self, event):
        index = self.fileSelected.GetSelection()
        if index != wx.NOT_FOUND:
            fileName = self.fileSelected.GetString(index)
            if fileName:
                if __DEBUG__:
                    print("Targeting %s load..." % fileName)
                return DataBot.LoadTargetingFromFile(fileName)

    def GetFiles(self):
        files = []
        for file in os.listdir("data/targeting"):
            result = file.split(".txt")
            if len(result) == 2:
                files.append(result[0])
        return files

    def OnAddMonster(self, event):
        name = self.MonsterName.GetValue()
        if name:
            targetMonster = TargetMonster(name)
            targetMonster.setSingleSpell('{%s}' % self.MonsterSingleSpell.GetValue())
            targetMonster.setPluralSpell('{%s}' % self.MonsterPluralSpell.GetValue())
            targetMonster.setCount(self.monsterCount.GetString(self.monsterCount.GetSelection()))
            targetMonster.setAction(self.monsterAction.GetString(self.monsterAction.GetSelection()))
            Targeting.addMonster(targetMonster)
            tmStrList = []
            for tm in Targeting.monsterList:
                tmStrList.append(str(tm))
            self.monsterList.Set(tmStrList)

    def OnDeleteMonster(self, event):
        index = self.monsterList.GetSelection()
        if index != wx.NOT_FOUND:
            Targeting.removeMonsterByIndex(index)
            tmStrList = []
            for tm in Targeting.monsterList:
                tmStrList.append(str(tm))
            self.monsterList.Set(tmStrList)

    def OnChangeSelectionMlist(self, event):
        index = event.GetEventObject().GetSelection()
        if index != wx.NOT_FOUND:
            targetMonster = Targeting.getMonsterByIndex(index)
            self.MonsterName.ChangeValue(targetMonster.getName())
            match = re.compile(r'(\w\d+)').search(targetMonster.getSingleSpell())
            self.MonsterSingleSpell.ChangeValue(match and match.group() or '')
            match = re.compile(r'(\w\d+)').search(targetMonster.getPluralSpell())
            self.MonsterPluralSpell.ChangeValue(match and match.group() or '')
            self.monsterCount.SetStringSelection(targetMonster.getCount())
            self.monsterAction.SetStringSelection(targetMonster.getAction())

#_ooooo___________________oo_____________oo___________
#oo___oo__ooooo__oo_ooo__________ooooo___oo_____oooo__
#_oo_____oo___oo_ooo___o__oo_____o___oo_oooo___oo___o_
#___oo___oo______oo_______oo____oo___oo__oo______oo___
#oo___oo_oo______oo_______oo____oo___oo__oo__o_o___oo_
#_ooooo___ooooo__oo______oooo_o_ooooo_____ooo___oooo__
#_____________________________oooo____________________

class GuiScriptsMenu(wx.Frame):
    def __init__(self, parent):
        toolWindow = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.STAY_ON_TOP | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"%s BOT - Scripts" % GAME_TITLE, size=(400, 200), style=toolWindow)
        self.SetIcon(parent.icon)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        Panel = wx.Panel(self, wx.ID_ANY)
        Panel.SetFont(wx.Font(MenuProperties.FontSize, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, MenuProperties.Font))
        self.scriptList = wx.ListCtrl(Panel, wx.ID_ANY, pos=(8, 5), size=(240, 145), style=wx.LC_SINGLE_SEL|wx.LC_REPORT|wx.LC_NO_HEADER)
        self.scriptList.InsertColumn(0, 'Name', width=120)
        self.scriptList.InsertColumn(1, 'Interval', width=70)
        self.scriptList.InsertColumn(2, 'Status', width=30)
        self.scriptList.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnChangeSelectionScript)
        self.scriptInterval =  wx.TextCtrl(Panel, wx.ID_ANY, "0ms", (260, 5), (51, 23), style=wx.TE_READONLY)
        self.scriptInterval.Bind(wx.EVT_CHAR, self.OnChangeInterval)
        self.reloadButton = wx.Button(Panel, wx.ID_ANY, emoji.emojize(":arrows_counterclockwise: Reload", use_aliases=True, variant="emoji_type"), (312, 4), (65, 25))
        self.reloadButton.Bind(wx.EVT_BUTTON, self.reloadScript)
        self.checkScriptRun = wx.CheckBox(Panel, wx.ID_ANY, "Run Script", (260, 32), (120, 23))
        self.checkScriptRun.Bind(wx.EVT_CHECKBOX, self.OnCheckRunScript)
        self.description = wx.TextCtrl(Panel, wx.ID_ANY, "", (260, 60), (115, 90), style=wx.TE_MULTILINE|wx.TE_NO_VSCROLL|wx.TE_READONLY)
        self.currentScript = None
        self.currentSelectScriptIndex = None
        self.currentSelectScriptName = None

    def reloadScript(self, event):
        if self.currentScript:
            self.currentScript = self.currentScript.reload()
            index = self.currentScript.getIndex()
            self.scriptList.EnsureVisible(index)
            self.scriptList.Select(index, on=1)

    def OnChangeInterval(self, event):
        if not self.currentScript:
            return
        interval = self.currentScript.getInterval()
        keyCode = event.GetKeyCode()
        if keyCode in (wx.WXK_NUMPAD_ADD, wx.WXK_UP): # UP
            self.currentScript.setInterval(interval +100000000)
        elif interval > 100000000 and keyCode in (wx.WXK_NUMPAD_SUBTRACT, wx.WXK_DOWN): # DOWN
            self.currentScript.setInterval(interval -100000000)
        intervalString = "%sms" % int(self.currentScript.getInterval()  / 1000 / 1000)
        self.scriptInterval.SetValue(intervalString)
        self.scriptList.SetItem(self.CreateItem(self.currentSelectScriptIndex, 1, intervalString))

    def CreateItem(self, index, column, text):
        item = wx.ListItem()
        item.SetColumn(column)
        item.SetId(index)
        item.SetText(text)
        return item

    def AddItemToScriptList(self, index, script):
        self.scriptList.InsertItem(self.CreateItem(index, 0, script.getName()))
        self.scriptList.SetItem(self.CreateItem(index, 1, '%sms' % int(script.getInterval() / 1000 / 1000)))
        self.scriptList.SetItem(self.CreateItem(index, 2, (script.getRunning() and MenuProperties.ScriptRunningText or MenuProperties.ScriptPauseText)))
        color = MenuProperties.ScriptOffColour
        if script.getRunning():
            color = MenuProperties.ScriptOnColour
        if script.isLocked():
            color = MenuProperties.ScriptLockedColour
        self.scriptList.SetItemTextColour(index, color)
        self.scriptList.SetItemData(index, index)

    def UpdateScriptList(self):
        self.scriptList.DeleteAllItems()
        index = 0
        for script in Scripts.scriptsList:
            script.index = index
            self.AddItemToScriptList(index, script)
            index += 1

    def OnClose(self, event):
        """En este caso funciona GetParent por que se sabe que esta ventana es hijo de main"""
        self.GetParent().OnShowHideScripts(event)

    def OnChangeSelectionScript(self, event):
        script = Scripts.getScriptByName(event.GetItem().GetText())
        if script:
            self.OnUpdateScript(script)

    def OnUpdateScript(self, script):
        self.currentSelectScriptIndex = script.getIndex()
        self.currentSelectScriptName = script.getName()
        self.currentScript = script
        status = script.getRunning() and 1 or 0
        self.checkScriptRun.SetValue(status)
        self.scriptInterval.SetValue("%sms" % int(script.getInterval()  / 1000 / 1000))
        self.description.SetValue(script.getDescription())
        if not script.isReloadable():
            self.reloadButton.Disable()
        else:
            self.reloadButton.Enable()
        if script.isLocked():
            self.checkScriptRun.Disable()
            self.currentScript = None
            return False
        self.checkScriptRun.Enable()

    def OnCheckRunScript(self, event):
        if not self.currentScript:
            return False
        if self.currentScript.isLocked():
            return False
        status = event.GetEventObject().GetValue() == 1 and True or False
        self.currentScript.setRunning(status)
        self.scriptList.SetItem(self.CreateItem(self.currentSelectScriptIndex, 2, (status and MenuProperties.ScriptRunningText or MenuProperties.ScriptPauseText)))
        self.scriptList.SetItemTextColour(self.currentSelectScriptIndex, (status and MenuProperties.ScriptOnColour or MenuProperties.ScriptOffColour))

#ooooooo_________oo___________________________
#oo______o____o__oo____oo_ooo___ooooo___oooo__
#oooo_____oo_o__oooo___ooo___o_oo___oo_oo___o_
#oo________oo____oo____oo______oo___oo___oo___
#oo_______o_oo___oo__o_oo______oo___oo_o___oo_
#ooooooo_o___oo___ooo__oo_______oooo_o__oooo__
#_____________________________________________

class GuiExtrasMenu(wx.Frame):
    def __init__(self, parent):
        toolWindow = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.STAY_ON_TOP | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"%s BOT - Extras" % GAME_TITLE, size=(400, 200), style=toolWindow)
        self.SetIcon(parent.icon)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        Panel = wx.Panel(self, wx.ID_ANY)
        Panel.SetFont(wx.Font(MenuProperties.FontSize, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, MenuProperties.Font))
        wx.StaticBox(Panel, wx.ID_ANY, "Extras:", (5, 1), (373, 155))
        self.squareToLowHp = wx.CheckBox(Panel, wx.ID_ANY, "Square player lowhp on screen", (20, 15), (300, 25))
        self.showNotifications = wx.CheckBox(Panel, wx.ID_ANY, "Show notification from events", (20, 35), (300, 25))
        self.warningPlayerScreen = wx.CheckBox(Panel, wx.ID_ANY, "Warning/Capture player on screen", (20, 55), (300, 25))
        self.autoloadSettings = wx.CheckBox(Panel, wx.ID_ANY, "Autoload Setting by player client", (20, 75), (300, 25))
        self.autoloadSettings.Bind(wx.EVT_CHECKBOX, self.OnAutoloadSettings)
        self.showFps = wx.CheckBox(Panel, wx.ID_ANY, "Always show LAG and FPS of client", (20, 95), (300, 25))
        #self.showFps.Bind(wx.EVT_CHECKBOX, self.OnShopFps)
        self.teleportToTemple = wx.CheckBox(Panel, wx.ID_ANY, "Teleport to the temple if they watch you a lot.", (20, 115), (300, 25))

    def OnClose(self, event):
        return MenuProperties.MainMenu.OnShowHideExtras(event)

    def OnAutoloadSettings(self, event):
        DataBot.setAutoloadSettings(event.GetEventObject().IsChecked())

#oo____oo_________________ooo____oo__________________
#oo____oo__ooooo___ooooo___oo________oo_ooo___oooo___
#oo____oo_oo____o_oo___oo__oo____oo__ooo___o_oo__oo__
#oooooooo_ooooooo_oo___oo__oo____oo__oo____o_oo___o__
#oo____oo_oo______oo___oo__oo____oo__oo____o__oooooo_
#oo____oo__ooooo___oooo_o_ooooo_oooo_oo____o_o____oo_
#_____________________________________________ooooo__

class GuiHealingMenu(wx.Frame):
    def __init__(self, parent):
        toolWindow = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.STAY_ON_TOP | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"%s BOT - Healing" % GAME_TITLE, size=(390, 250), style=toolWindow)
        self.SetIcon(parent.icon)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        Panel = wx.Panel(self, wx.ID_ANY)
        Panel.SetFont(wx.Font(MenuProperties.FontSize, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, MenuProperties.Font))
        wx.StaticBox(Panel, wx.ID_ANY, "Healing:", (5, 1), (180, 205))
        wx.StaticText(Panel, wx.ID_ANY, "Heal Spell %", (10, 15), (80, 12))
        self.healSpellHotkey = wx.TextCtrl(Panel, wx.ID_ANY, "", (10, 30), (40, 20), style=wx.TE_CENTRE)
        self.healSpellValue = wx.Slider(Panel, wx.ID_ANY, 50, 0, 100, (50, 15), (100, 25), style=wx.SL_VALUE_LABEL)
        wx.StaticText(Panel, wx.ID_ANY, "GH Potion %", (10, 50), (80, 12))
        self.GH_PotionHotkey = wx.TextCtrl(Panel, wx.ID_ANY, "", (10, 65), (40, 20), style=wx.TE_CENTRE)
        self.GH_PotionValue = wx.Slider(Panel, wx.ID_ANY, 50, 0, 100, (50, 50), (100, 25), style=wx.SL_VALUE_LABEL)
        wx.StaticText(Panel, wx.ID_ANY, "GM Potion %", (10, 85), (80, 12))
        self.GM_PotionHotkey = wx.TextCtrl(Panel, wx.ID_ANY, "", (10, 100), (40, 20), style=wx.TE_CENTRE)
        self.GM_PotionValue = wx.Slider(Panel, wx.ID_ANY, 50, 0, 100, (50, 85), (100, 25), style=wx.SL_VALUE_LABEL)
        wx.StaticText(Panel, wx.ID_ANY, "Vocation ID", (10, 120), (80, 12))
        self.VocationHotkey = wx.TextCtrl(Panel, wx.ID_ANY, "", (10, 135), (40, 20), style=wx.TE_CENTRE)
        self.VocationID = wx.Slider(Panel, wx.ID_ANY, 1, 1, 5, (50, 120), (100, 25), style=wx.SL_VALUE_LABEL)
        # Miscellaneous
        wx.StaticBox(Panel, wx.ID_ANY, "Miscellaneous:", (190, 1), (180, 205))
        wx.StaticText(Panel, wx.ID_ANY, "Haste Spell %", (200, 15), (80, 12))
        self.hasteSpellHotkey = wx.TextCtrl(Panel, wx.ID_ANY, "", (200, 30), (40, 20), style=wx.TE_CENTRE)
        self.hasteSpellValue = wx.Slider(Panel, wx.ID_ANY, 50, 0, 100, (250, 15), (100, 25), style=wx.SL_VALUE_LABEL)
        wx.StaticText(Panel, wx.ID_ANY, "Manashield %", (200, 50), (80, 12))
        self.manashieldHotkey = wx.TextCtrl(Panel, wx.ID_ANY, "", (200, 65), (40, 20), style=wx.TE_CENTRE)
        self.manashieldValue = wx.Slider(Panel, wx.ID_ANY, 50, 0, 100, (250, 50), (100, 25), style=wx.SL_VALUE_LABEL)
        wx.StaticText(Panel, wx.ID_ANY, "Buff Spell %", (200, 85), (80, 12))
        self.buffSpellHotkey = wx.TextCtrl(Panel, wx.ID_ANY, "", (200, 100), (40, 20), style=wx.TE_CENTRE)
        self.buffSpellValue = wx.Slider(Panel, wx.ID_ANY, 50, 0, 100, (250, 85), (100, 25), style=wx.SL_VALUE_LABEL)
        self.UpdateHotkeys()

    def OnClose(self, event):
        return MenuProperties.MainMenu.OnShowHideHealing(event)

    def UpdateHotkeys(self):
        heal_spell = SpellHotkey.getByName("HealSpell")
        match = re.compile(r'(\w\d+)').search(heal_spell.getButton())
        self.healSpellHotkey.ChangeValue(match and match.group() or '')
        self.healSpellValue.SetValue(heal_spell.getHppc())

        ghp_hotkey = SpellHotkey.getByName("GreatHealthPotion")
        match = re.compile(r'(\w\d+)').search(ghp_hotkey.getButton())
        self.GH_PotionHotkey.ChangeValue(match and match.group() or '')
        self.GH_PotionValue.SetValue(ghp_hotkey.getHppc())

        gmp_hotkey = SpellHotkey.getByName("GreatManaPotion")
        match = re.compile(r'(\w\d+)').search(gmp_hotkey.getButton())
        self.GM_PotionHotkey.ChangeValue(match and match.group() or '')
        self.GM_PotionValue.SetValue(gmp_hotkey.getMppc())

        vocation_id = SpellHotkey.getByName("VocationID")
        self.VocationHotkey.ChangeValue(vocation_id.getButton())
        self.VocationID.SetValue(vocation_id.getHppc())

        haste_spell = SpellHotkey.getByName("Haste")
        match = re.compile(r'(\w\d+)').search(haste_spell.getButton())
        self.hasteSpellHotkey.ChangeValue(match and match.group() or '')
        self.hasteSpellValue.SetValue(haste_spell.getMppc())

        manashield_spell = SpellHotkey.getByName("Manashield")
        match = re.compile(r'(\w\d+)').search(manashield_spell.getButton())
        self.manashieldHotkey.ChangeValue(match and match.group() or '')
        self.manashieldValue.SetValue(manashield_spell.getHppc())

        buff_spell = SpellHotkey.getByName("BuffSpell")
        match = re.compile(r'(\w\d+)').search(buff_spell.getButton())
        self.buffSpellHotkey.ChangeValue(match and match.group() or '')
        self.buffSpellValue.SetValue(buff_spell.getMppc())

#ooooooooooo                                   o8               
# 888    88 oooo   oooo ooooooooo8 oo oooooo o888oo  oooooooo8  
# 888ooo8    888   888 888oooooo8   888   888 888   888ooooooo  
# 888    oo   888 888  888          888   888 888           888 
#o888ooo8888    888      88oooo888 o888o o888o 888o 88oooooo88  

#ooooooo__ooo___________________________________
#oo____oo__oo____ooooo___o___oo__ooooo__oo_ooo__
#oo____oo__oo___oo___oo__o___oo_oo____o_ooo___o_
#oooooo____oo___oo___oo__o___oo_ooooooo_oo______
#oo________oo___oo___oo___ooooo_oo______oo______
#oo_______ooooo__oooo_o_o____oo__ooooo__oo______
#________________________ooooo__________________

class Events:

    def Player_onChangeExperience(currentExp, lastExp):
        if currentExp > lastExp:
            return Events.Player_addExperience(currentExp - lastExp)
        elif currentExp < lastExp:
            return Events.Player_removeExperience(lastExp - currentExp)

    def Player_addExperience(exp):
        experience = Player.getExperience(None)
        level = Player.getLevel(None)
        currLevelExp = Player.getExpForLevel(level)
        nextLevelExp = Player.getExpForLevel(level + 1)
        if currLevelExp >= nextLevelExp:
            #player has reached max level
            Player.levelPercent = 0
            return
        if nextLevelExp > currLevelExp:
            Player.levelPercent = Player.getPercentLevel(experience - currLevelExp, nextLevelExp - currLevelExp)
        else:
            Player.levelPercent = 0

    def Player_removeExperience(exp):
        experience = Player.getExperience(None)
        level = Player.getLevel(None)
        currLevelExp = Player.getExpForLevel(level)
        nextLevelExp = Player.getExpForLevel(level + 1)
        if nextLevelExp > currLevelExp:
            Player.levelPercent = Player.getPercentLevel(experience - currLevelExp, nextLevelExp - currLevelExp)
        else:
            Player.levelPercent = 0

#     o                            o88   o888  o88                          
#    888   oooo  oooo  oooo   oooo oooo   888  oooo   ooooooo   oo oooooo   
#   8  88   888   888    888o888    888   888   888   ooooo888   888    888 
#  8oooo88  888   888    o88 88o    888   888   888 888    888   888        
#o88o  o888o 888o88 8o o88o   o88o o888o o888o o888o 88ooo88 8o o888o       

def isInArray(array, item):
    if isinstance(array, list):
        for i in array:
            if i != item:
                continue
            return True
    return False

def index_in_list(a_list, index):
    return index < len(a_list)

def checkExpSpeed(player):
    if not player:
        return
    currentExp = player.getExperience()
    currentTime = time.time()
    if Player.lastExps != None:
        Player.expSpeed = (currentExp - Player.lastExps[0][0])/(currentTime - Player.lastExps[0][1])
        onLevelChange(player, player.getLevel(), player.getLevelPercent())
    else:
        Player.lastExps = []
    Player.lastExps.append([currentExp, currentTime])
    if len(player.lastExps) > 30:
        Player.lastExps.pop(1)

def onLevelChange(player, value, percent):
    #setSkillValue('level', comma_value(value))
    #local text = tr('You have %s percent to go', 100 - percent) .. '\n' ..
    #tr('%s of experience left', expToAdvance(localPlayer:getLevel(), localPlayer:getExperience()))
    if Player.expSpeed != None:
        expPerHour = math.floor(Player.expSpeed * 3600)
        if expPerHour > 0:
            nextLevelExp = Player.getExpForLevel(player.getLevel() + 1)
            hoursLeft = (nextLevelExp - player.getExperience()) / expPerHour
            minutesLeft = math.floor((hoursLeft - math.floor(hoursLeft))*60)
            secondsLeft = math.floor((((hoursLeft - math.floor(hoursLeft)) * 60) - minutesLeft)*60)
            hoursLeft = math.floor(hoursLeft)
            wx.CallAfter(MenuProperties.MainMenu.UpdateTimeLeft, (hoursLeft, minutesLeft, secondsLeft))
            wx.CallAfter(MenuProperties.MainMenu.UpdateExpPerHour, expPerHour)

def getTimeFormated():
    localtime = time.localtime(time.time())
    return "%d:%d:%d" % (localtime.tm_hour, localtime.tm_min, localtime.tm_sec)

LOGCONSOLE_MAXLINES = 1000
LOGCONSOLE_LASTINSERT = False
def printConsole(*args):
    if not MenuProperties.MainMenu:
        return
    global LOGCONSOLE_LASTINSERT
    for text in args:
        wx.CallAfter(MenuProperties.MainMenu.logConsole.write, '%s%s >> %s' % ((LOGCONSOLE_LASTINSERT and '\n' or ''), getTimeFormated(), str(text)))
        LOGCONSOLE_LASTINSERT = True

DefaultPrintFunc = print
def print(*args, **kwargs):
    DefaultPrintFunc(*args)
    return printConsole(*args)

def error(message):
    Game.addTelemetryMessage(TelemetryMessage(message))

def sec_to_ns(sec):
    return sec * 1000000000

# Create Workers
g_zed = CreateThread()
g_zed.running = True
g_zed.start()
g_yasuo = CreateThread()
g_yasuo.running = True
g_yasuo.start()
g_k6 = CreateThread()
g_k6.running = True
g_k6.start()
g_sett = CreateThread()
g_sett.running = True
g_sett.start()
print("[Threads]: se han creado 4 hilos para el manejo de los scripts.")
