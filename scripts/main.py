# -*- coding: utf-8 -*-
import threading
import time
import re
import keyboard 

from VariablesCheck import *
from TwitchConnection import *
from TexteToSpeech import *

File = Variables("config.txt")
USERNAME, BANWORDS, DELAY, FORMAT, SHORTCUT, CHAR_MAX = File.GetVariables()

Voice = TTS()

Twitch = Connection(USERNAME)
Twitch.ConnectionTwitchChat()

PingCheck = threading.Thread(target=Twitch.HandlePingVerification)
PingCheck.daemon = True
PingCheck.start()


while True:
    ViewerName, ViewerMessage = Twitch.ProcessMessage() 
    if ViewerName == 0 or ViewerMessage == 0: continue
    Reponse = Twitch.FormatUserMessage(ViewerName, ViewerMessage, FORMAT)
    if len(Reponse) > CHAR_MAX: continue
    for mot in BANWORDS:
        if mot in Reponse: Reponse = Reponse.replace(mot, " ")
    for char in char_speciaux:
        if char.isalnum():
            Reponse = Reponse.replace(char, " ")
            # keep only characters and numbers
            
    Reponse = re.sub(r'[^\w\s]', '', Reponse)
    print(Reponse)
    
    Voice.Say(Reponse)

    time.sleep(float(DELAY))


